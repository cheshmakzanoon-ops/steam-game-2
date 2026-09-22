#!/usr/bin/env python3
"""Disposable Phase 004 design oracle. Not production game code or a save service.

Use only Python's standard library. Exit non-zero on any failed expectation.
Port the independent fixtures to typed GDScript tests in the scheduled engine phases.
"""
from __future__ import annotations

import argparse
import copy
import itertools
import json
from pathlib import Path
import sys
import subprocess
import tempfile
from typing import Any

ROOT = Path(__file__).resolve().parent
LIMIT = 2**31 - 1
SIZE = 9
KEEP = 40
DIRECTIONS = ((0, -1), (1, 0), (0, 1), (-1, 0))
PHASES = ('Forecast', 'Council', 'Build', 'Route', 'Production', 'Siege', 'Aftermath')
CHECKS = 0


def check(value: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not value:
        raise AssertionError(label)


def integer(value: Any, low: int = 0, high: int = LIMIT) -> int:
    if type(value) is not int or not low <= value <= high:
        raise ValueError(f'Invalid integer: {value!r}')
    return value


def bundle(values: Any) -> list[int]:
    if not isinstance(values, list) or len(values) != 3:
        raise ValueError('A resource bundle must contain exactly three integers.')
    return [integer(v) for v in values]


def cell(x: int, y: int) -> int:
    return integer(y, 0, SIZE-1)*SIZE + integer(x, 0, SIZE-1)


def xy(index: int) -> tuple[int, int]:
    integer(index, 0, SIZE*SIZE-1)
    return index % SIZE, index // SIZE


def neighbor(index: int, direction: int) -> int | None:
    x, y = xy(index)
    dx, dy = DIRECTIONS[integer(direction, 0, 3)]
    return cell(x+dx, y+dy) if 0 <= x+dx < SIZE and 0 <= y+dy < SIZE else None


def rotate(mask: int, turns: int) -> int:
    integer(mask, 0, 15)
    integer(turns, -100, 100)
    turns %= 4
    return ((mask << turns) | (mask >> (4-turns))) & 15


def graph(nodes: list[dict], cuts: list | None = None) -> dict[int, set[int]]:
    masks = {KEEP: 15}
    seen = {KEEP}
    for n in nodes:
        i = integer(n['index'], 0, 80)
        if i in seen or i in (4, 44, 76, 36):
            raise ValueError('Duplicate, reserved entry or Keep overwrite.')
        seen.add(i)
        mask = rotate(n['mask'], n.get('rotation', 0))
        if integer(n.get('health', 1)) > 0:
            masks[i] = mask
    blocked = set()
    for edge in cuts or []:
        if len(edge) != 2 or edge[0] == edge[1]:
            raise ValueError('Invalid cut edge.')
        a, b = (integer(v, 0, 80) for v in edge)
        if a not in masks or b not in masks or b not in [neighbor(a, d) for d in range(4)]:
            raise ValueError('Cut must name living adjacent endpoints.')
        blocked.add(tuple(sorted((a, b))))
    g = {i: set() for i in masks}
    for i, mask in masks.items():
        for d in range(4):
            j = neighbor(i, d)
            if j in masks and mask & (1 << d) and masks[j] & (1 << ((d+2) % 4)):
                if tuple(sorted((i, j))) not in blocked:
                    g[i].add(j)
    return g


def reachable(g: dict[int, set[int]], start: int, remove: int | None = None) -> set[int]:
    if start not in g or start == remove:
        return set()
    seen, todo = {start}, [start]
    while todo:
        for nxt in sorted(g[todo.pop()]):
            if nxt != remove and nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
    return seen


def resonant(g: dict[int, set[int]], start: int, target: int) -> bool:
    if target == start or target not in reachable(g, start):
        return False
    if target in g[start]:
        alternative = {k: set(v) for k, v in g.items()}
        alternative[start].remove(target)
        alternative[target].remove(start)
        return target in reachable(alternative, start)
    return all(target in reachable(g, start, v) for v in g if v not in (start, target))


def exchange(stock: list[int], cost: list[int], output: list[int]) -> list[int] | None:
    stock, cost, output = bundle(stock), bundle(cost), bundle(output)
    if any(s < c for s, c in zip(stock, cost)):
        return None
    return bundle([s-c+o for s, c, o in zip(stock, cost, output)])


def allocate(c: dict) -> dict:
    capacity, stock = integer(c['capacity']), bundle(c['stock'])
    g = graph(c['nodes'], c.get('cuts', []))
    connected = reachable(g, KEEP)
    paid, failed = set(c.get('paid', [])), set(c.get('failed', []))
    rank = {'Crown': 0, 'Charter': 1, 'Dormant': 2}
    for n in c['nodes']:
        integer(n['load'])
        if n['priority'] not in rank:
            raise ValueError('Unknown priority.')
        bundle(n.get('upkeep', [0, 0, 0]))
    powered, used = [], 0
    for n in sorted(c['nodes'], key=lambda n: (rank[n['priority']], n['index'])):
        i, load = n['index'], n['load']
        if i not in connected or n['priority'] == 'Dormant' or i in failed:
            continue
        if used+load > capacity:
            continue
        if i not in paid:
            after = exchange(stock, n.get('upkeep', [0, 0, 0]), [0, 0, 0])
            if after is None:
                failed.add(i)
                continue
            stock = after
            paid.add(i)
        powered.append(i)
        used += load
    return dict(powered=powered, used=used, stock=stock, paid=sorted(paid), failed=sorted(failed))


def production(c: dict) -> tuple[list[int], list[int]]:
    a = allocate(dict(c, capacity=c.get('capacity', 6)))
    stock, failed = a['stock'], []
    by_id = {n['index']: n for n in c['nodes']}
    for i in a['powered']:
        recipe = by_id[i].get('recipe')
        if recipe is not None:
            after = exchange(stock, recipe['cost'], recipe['output'])
            if after is None:
                failed.append(i)
            else:
                stock = after
    return stock, failed


def damage(health: int, maximum: int, armor: int, ward: int, raw: int) -> list[int]:
    integer(maximum, 1)
    integer(health, 0, maximum)
    integer(armor)
    integer(ward)
    integer(raw)
    post_armor = max(0, raw-armor)
    absorbed = min(ward, post_armor)
    return [max(0, health-(post_armor-absorbed)), ward-absorbed]


def repair(c: dict, defaults: dict) -> list | None:
    maximum = integer(c['maximum'], 1)
    health = integer(c['health'], 0, maximum)
    stock = bundle(c['stock'])
    if health in (0, maximum):
        return None
    after = exchange(stock, defaults['repair_cost'], [0, 0, 0])
    return None if after is None else [min(maximum, health+integer(defaults['repair_amount'], 1)), after]


def outcome(watch: int, integrity: int, boss_dead: bool, encounter_clear: bool,
            fatal: bool, doctrine_loss: bool) -> str:
    integer(watch, 1, 15)
    integer(integrity)
    if any(type(v) is not bool for v in (boss_dead, encounter_clear, fatal, doctrine_loss)):
        raise ValueError('Outcome flags must be boolean.')
    if integrity == 0 or fatal or doctrine_loss:
        return 'DEFEAT'
    if watch == 15 and boss_dead and encounter_clear:
        return 'VICTORY'
    return 'ONGOING'


def planning_batch(state: dict, commands: list[dict], revision: int) -> dict:
    """Probe atomic cost/rotation semantics only, not a production command dispatcher."""
    if revision != state['revision']:
        raise ValueError('Stale planning revision.')
    proposed = copy.deepcopy(state)
    for cmd in commands:
        if cmd['type'] == 'spend':
            after = exchange(proposed['stock'], cmd['cost'], [0, 0, 0])
            if after is None:
                raise ValueError('Unaffordable command.')
            proposed['stock'] = after
        elif cmd['type'] == 'rotate':
            proposed['mask'] = rotate(proposed['mask'], cmd['turns'])
        else:
            raise ValueError('Unknown command.')
    proposed['revision'] += 1
    return proposed



def advance(watch: int, phase: str, *, council_done: bool = True,
            sealed: bool = False, post_production_done: bool = True,
            siege_clear: bool = False, settlement_done: bool = False) -> tuple[int, str]:
    """Probe guarded phase boundaries, not a production encounter resolver."""
    integer(watch, 1, 15)
    if phase not in PHASES:
        raise ValueError('Unknown phase.')
    if phase == 'Council' and not council_done:
        raise ValueError('Council choice unresolved.')
    if phase == 'Route' and not sealed:
        raise ValueError('Seal transaction required.')
    if phase == 'Production' and not post_production_done:
        raise ValueError('Declared post-Production exception is unresolved.')
    if phase == 'Siege' and not siege_clear:
        raise ValueError('Hostiles or scheduled waves remain.')
    if phase == 'Aftermath':
        if not settlement_done or watch == 15:
            raise ValueError('Settlement incomplete or final Watch requires run-end handling.')
        return watch+1, 'Forecast'
    return watch, PHASES[PHASES.index(phase)+1]


def rejects(fn: Any, label: str) -> None:
    try:
        fn()
    except (ValueError, KeyError, TypeError):
        check(True, label)
        return
    raise AssertionError(f'Expected rejection: {label}')


def path_oracle(g: dict[int, set[int]], start: int, target: int) -> bool:
    paths = []
    def visit(path: list[int]) -> None:
        if path[-1] == target:
            paths.append(set(path[1:-1]))
        else:
            for nxt in g[path[-1]]:
                if nxt not in path:
                    visit(path+[nxt])
    visit([start])
    return any(not a.intersection(b) for a, b in itertools.combinations(paths, 2))


def run(data: dict) -> tuple[int, int]:
    check(data['rules_version'] == '1.0.0', 'Rules version')
    c = data['constants']
    expected = dict(size=9, keep_index=40, entry_indices=[4,44,76,36],
        directions=[list(d) for d in DIRECTIONS], priority_order=['Crown','Charter','Dormant'],
        resource_order=['Supply','Material','Insight'], capacity=6, watches=15,
        boss_watches=[5,10,15], phases=list(PHASES))
    check(c == expected, 'Constants must match locked v1.0.0 contract')
    check(data['calibration_defaults']['keep_integrity'] == 20, 'Calibration Keep')
    check(data['calibration_defaults']['repair_amount'] == 3, 'Calibration repair amount')
    check(data['calibration_defaults']['repair_cost'] == [1,1,0], 'Calibration repair cost')
    check(data['calibration_defaults']['tick_presentation_ms'] == 100, 'Calibration tick display')
    for i in range(81):
        check(cell(*xy(i)) == i, f'BRD round trip {i}')
        for d in range(4):
            j = neighbor(i, d)
            if j is not None:
                check(neighbor(j, (d+2)%4) == i, f'BRD reciprocity {i}/{d}')
                check(sum(abs(a-b) for a,b in zip(xy(i),xy(j))) == 1, 'No diagonal/wrap')
    check(neighbor(8,1) is None and neighbor(9,3) is None, 'No row wrapping')
    check(len(set(range(81)) - {40,4,44,76,36}) == 76, 'Buildable count')
    for mask in range(16):
        for turns in range(4):
            expected_mask = sum(1 << ((d+turns)%4) for d in range(4) if mask & (1<<d))
            check(rotate(mask,turns) == expected_mask, 'PRT quarter turn')
            check(rotate(rotate(mask,turns),-turns) == mask, 'PRT inverse')
    for bad in (-1,81,True,1.2):
        rejects(lambda bad=bad: xy(bad), 'Invalid board index')
    for bad in (-1,16,True):
        rejects(lambda bad=bad: rotate(bad,1), 'Invalid port mask')
    for bad in ([-1,0,0],[True,0,0],[1,2],[LIMIT+1,0,0]):
        rejects(lambda bad=bad: bundle(bad), 'Invalid bundle')
    rejects(lambda: exchange([LIMIT,0,0],[0,0,0],[1,0,0]), 'Overflow')
    check(exchange([1,1,0],[1,2,0],[0,0,1]) is None, 'Atomic bundle rejection')
    ids = set()
    fixtures = 0
    for group in ('allocation','production','damage','repair','outcomes'):
        check(isinstance(data[group],list) and len(data[group]) > 0, f'Missing {group} fixtures')
        for row in data[group]:
            fixtures += 1
            check(row['id'] not in ids, 'Unique fixture ID')
            ids.add(row['id'])
            before = copy.deepcopy(row)
            if group == 'allocation':
                a = allocate(row)
                check(a['powered'] == row['expected'], row['id'])
                check(a['used'] <= row['capacity'], row['id']+' capacity invariant')
                if 'expected_stock' in row:
                    check(a['stock'] == row['expected_stock'], row['id']+' stock')
                if 'expected_failed' in row:
                    check(a['failed'] == row['expected_failed'], row['id']+' upkeep failure')
            elif group == 'production':
                stock, failed = production(row)
                check(stock == row['expected_stock'], row['id']+' stock')
                check(failed == row['expected_failed'], row['id']+' recipe failure')
            elif group == 'damage':
                check(damage(*row['state']) == row['expected'], row['id'])
            elif group == 'repair':
                check(repair(row,data['calibration_defaults']) == row['expected'], row['id'])
            else:
                check(outcome(*row['state']) == row['expected'], row['id'])
            check(row == before, row['id']+' input not mutated')
    # Every undirected graph on four vertices is compared against explicit simple paths.
    edges = list(itertools.combinations(range(4),2))
    for bits in range(1 << len(edges)):
        g = {i:set() for i in range(4)}
        for j,(a,b) in enumerate(edges):
            if bits & (1<<j):
                g[a].add(b); g[b].add(a)
        for a,b in itertools.combinations(range(4),2):
            check(resonant(g,a,b) == path_oracle(g,a,b), 'NET independent-path oracle')
    # A cycle attached through a stem is not redundant to the Keep.
    stem = {0:{1},1:{0,2,3},2:{1,3},3:{1,2}}
    check(not resonant(stem,0,2), 'NET cycle with single stem')
    base = dict(revision=7, stock=[2,1,0], mask=3)
    original = copy.deepcopy(base)
    changed = planning_batch(base,[dict(type='rotate',turns=1),dict(type='spend',cost=[1,1,0])],7)
    check(changed == dict(revision=8,stock=[1,0,0],mask=6), 'REC successful seal probe')
    rejects(lambda: planning_batch(base,[dict(type='spend',cost=[1,0,0]),dict(type='spend',cost=[9,0,0])],7), 'REC rollback entire batch')
    rejects(lambda: planning_batch(base,[],6), 'REC stale revision')
    rejects(lambda: planning_batch(base,[dict(type='unknown')],7), 'REC unknown command')
    check(base == original, 'REC rejected batch retains original state')
    check(json.loads(json.dumps(base)) == original, 'REC probe serialization round trip')
    for watch in range(1,16):
        check(1+(watch-1)//5 in (1,2,3), 'WCH valid Act')
        check((watch % 5 == 0) == (watch in c['boss_watches']), 'WCH exact boss placement')
    rejects(lambda: outcome(16,20,True,True,False,False), 'No Watch 16')
    rejects(lambda: damage(10,10,0,0,-1), 'Negative damage')
    bad_node = dict(index=4,load=1,mask=15,priority='Charter')
    rejects(lambda: graph([bad_node]), 'Reserved entry')
    bad_node['index'] = 40
    rejects(lambda: graph([bad_node]), 'Keep overwrite')
    bad_node['index'] = 31
    rejects(lambda: graph([bad_node,bad_node]), 'Duplicate anchor')
    rejects(lambda: planning_batch(changed,[],7), 'REC duplicate sealed revision')
    rejects(lambda: planning_batch(base,[dict(type='spend',cost=[1,0,0]),dict(type='rotate',turns='bad')],7), 'REC malformed second command')
    check(base == original, 'REC malformed batch remains atomic')
    for i, phase in enumerate(PHASES[:-1]):
        check(advance(1,phase,sealed=True,siege_clear=True) == (1,PHASES[i+1]), 'WCH ordered advance')
    check(advance(5,'Aftermath',settlement_done=True) == (6,'Forecast'), 'WCH new Act')
    rejects(lambda: advance(1,'Council',council_done=False), 'WCH Council gate')
    rejects(lambda: advance(1,'Route'), 'WCH no unsealed Production')
    rejects(lambda: advance(1,'Production',post_production_done=False), 'WCH Lantern exception gate')
    rejects(lambda: advance(1,'Siege'), 'WCH pending-wave gate')
    rejects(lambda: advance(1,'Aftermath'), 'WCH settlement gate')
    rejects(lambda: advance(15,'Aftermath',settlement_done=True), 'WCH no Watch 16 advance')
    rejects(lambda: advance(1,'unknown'), 'WCH unknown phase')
    check(sum([0,2,4])//2 == 3, 'DMG paid-Material salvage rounding example')
    return CHECKS, fixtures



def negative_tests(data: dict) -> int:
    """Verify the CLI rejects bad expectations/data instead of silently passing."""
    variants: list[tuple[str, str]] = []
    def variant(label: str, mutate: Any) -> None:
        value = copy.deepcopy(data)
        mutate(value)
        variants.append((label, json.dumps(value)))
    variant('overload expectation', lambda d: d['allocation'][1].update(expected=[31,39,41]))
    variant('damage expectation', lambda d: d['damage'][0].update(expected=[10,0]))
    variant('simultaneous victory', lambda d: d['outcomes'][1].update(expected='VICTORY'))
    variant('board size', lambda d: d['constants'].update(size=10))
    variant('empty fixture group', lambda d: d.update(production=[]))
    variant('negative upkeep', lambda d: d['allocation'][11]['nodes'][0].update(upkeep=[-1,0,0]))
    variant('rules version', lambda d: d.update(rules_version='99.0.0'))
    variants.append(('malformed JSON', '{"incomplete":'))
    with tempfile.TemporaryDirectory(prefix='charterwake-phase004-') as tmp:
        for label, content in variants:
            path = Path(tmp)/'invalid.json'
            path.write_text(content, encoding='utf-8')
            result = subprocess.run([sys.executable, str(Path(__file__).resolve()),
                '--fixtures', str(path)], capture_output=True, text=True, timeout=15)
            if result.returncode != 1 or not result.stderr.startswith('FAIL:'):
                raise AssertionError(f'Negative-path test did not reject: {label}')
    return len(variants)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fixtures', type=Path, default=ROOT/'rule_examples.json')
    parser.add_argument('--self-test', action='store_true', help='Also test eight CLI failure cases.')
    args = parser.parse_args()
    try:
        data = json.loads(args.fixtures.read_text(encoding='utf-8'))
        checks, fixtures = run(data)
        negatives = negative_tests(data) if args.self_test else 0
    except (OSError, ValueError, KeyError, TypeError, AssertionError, subprocess.TimeoutExpired) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        return 1
    print(f'PASS: {checks} contract checks; {fixtures} explicit examples; rules 1.0.0')
    if negatives:
        print(f'PASS: {negatives} deliberately invalid CLI cases rejected with exit 1')
    print('Scope: pure design examples only; no Godot/game/save/UI/export acceptance claimed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
