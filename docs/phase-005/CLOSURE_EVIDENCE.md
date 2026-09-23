# Phase 005 — Closure evidence

**Project:** Charterwake: The Last Relay — provisional working title  
**Phase:** 005 — Scope budget and content ceiling  
**Status:** COMPLETE / GREEN for preproduction scope budgeting  
**Date:** 2026-09-22  
**Entry commit:** `ad04e3cf519c5c839c5a897837c630dc88829dcb`  
**Implementation commit:** `35d9b7592411b684bf2ad6255443249676f163e3`  
**Target branch:** `main`

This closes the bible's Phase 005 scope-budget gate. It does not certify production throughput, hardware performance, vendor pricing, living runway, a release date, Godot runtime behavior, Blender throughput or commercial success.

## Required deliverables

- `scope_budget.csv` — diffable spreadsheet containing content, art, text, audio, performance, cash and schedule ceilings.
- `SCOPE_BUDGET.md` — counting rules, staged subsets and budget interpretation.
- `CUT_LADDER_AND_REVIEW.md` — ranked cuts, protected boundaries and monthly review form.
- `MILESTONE_MAP.md` — relative 001–120 phase allocation and major checkpoints.
- `SCOPE_CEILINGS.json` — machine-readable accepted ceiling values.
- `verify_scope.py` — standard-library verification of canonical scope invariants.
- this closure record.

## Work-package acceptance

| Bible item | Evidence | Result |
|---|---|---|
| Structure/enemy/boss/upgrade/event/doctrine/Oath counts | CSV + JSON + SCOPE_BUDGET | PASS |
| Visual deliverable/frame budgets | SCOPE_BUDGET + CSV | PASS |
| Text/localization budget | SCOPE_BUDGET + CSV | PASS |
| Audio cue/music budget | SCOPE_BUDGET + CSV | PASS |
| Performance/install budgets | SCOPE_BUDGET + CSV | PASS AS TARGETS |
| MVP/demo/launch subsets | SCOPE_BUDGET | PASS |
| Ranked cuts | CUT_LADDER_AND_REVIEW | PASS |
| Monthly scope review | CUT_LADDER_AND_REVIEW | PASS |

## Locked ceiling summary

Launch ceiling: 24 non-combat structures including Keep, 9 combat structures, 15 standard enemies, 3 bosses, 4 doctrines, 45 total run upgrades, 24 systemic events, 6 Oaths, 1 principal biome/theme and 1 principal mode.

Demo ceiling: 1 doctrine, 10 total structures, 6 standard enemies, 1 boss, 12 upgrades, 4 events, 5 Watches, 20–40 minute target.

Art ceiling: 220 authored visual sets; 389 allocated color frames inside a hard cap of 400.

Text: 12,000 launch source words; 4,000 demo source words; at most two additional target languages before a future approved change.

Audio: 76 cue identities, 180 variants, five adaptive pieces target, seven cap, 24 unique music minutes cap.

Install target: 1,800 MB decimal maximum; modeled allocation 1,500 MB. Performance values remain future exported-build targets.

## Cash and schedule interpretation

External planning totals including contingency: USD 4,320 lean, 12,600 base, 18,480 stretch. They are allowances, not purchase authorization or vendor quotes.

The 15-month planning model has 1,920 productive prelaunch hours, 1,320 allocated and 600 unallocated, a 31.25% reserve. The unchanged 12-month scenario leaves 14.06% reserve and is AMBER. Personal living runway and available cash remain UNSET and may not be interpreted as zero.

## Executed verification

The published machine-readable contract was reproduced locally with:

```sh
python3 -S docs/phase-005/verify_scope.py --self-test
```

Actual output:

```text
PASS: 66 Phase 005 scope-ceiling checks
PASS: invalid extra-doctrine case rejected
```

The checks include all core content ceilings, demo limits, art/text/audio boundaries, performance/install targets, cash-scenario ceilings, null private runway inputs, schedule accounting, reserve behavior and exact coverage of Phases 001–120.

## Boundary/failure/recovery contract

- Exactly 400 color frames or 12,000 source words is legal; the next unit requires scope disposition.
- Reserve below 20% is AMBER; capacity overrun, quality-gate failure or >18-month forecast is RED.
- Missing living-runway information stays UNSET.
- Negative/fractional/hidden extra content is invalid.
- Recovery preserves the last accepted revision, changes the proposed source, reruns verification and records explicit owner approval before widening scope.

## Earlier gates and implementation boundary

No Phase 001–004 file was modified by the implementation commit. No Godot runtime, Blender production asset, new mode, biome, resource, online feature or platform commitment was introduced.

## Safe entry condition for Phase 006

Phase 006 may begin only from this remotely published Phase 005 baseline and must preserve:

1. Phase 001 product/scope pillars;
2. Phase 002 originality/IP controls;
3. Phase 003 player-experience/fair-loss contracts;
4. Phase 004 core-rules v1.0.0;
5. Phase 005 content, art, text, audio, performance and cash ceilings;
6. Charterwake's provisional-name status.

**Phase 005 is closed.**