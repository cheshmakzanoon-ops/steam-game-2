# Phase 004 — Closure evidence

**Project:** Charterwake: The Last Relay — provisional working title  
**Phase:** 004 — Core rules lock  
**Status:** COMPLETE / GREEN for the preproduction specification and verified examples  
**Rules version:** 1.0.0  
**Date:** 2026-09-22  
**Entry commit:** `cdd3acdc289b467b4db0b7159e75ac9e7b7eae7d`  
**Implementation commit:** `814b2639e90cdf3ec2ba6d78596a85ba00618883`  
**Target branch:** `main`

This closes the bible's rules-lock deliverable. It does not certify a playable game, an engine build, final art, player enjoyment, controller usability or launch readiness.

## Deliverables and changelog

- `CORE_RULES_V1.md`: versioned board, port, graph, allocation, economy, Watch, combat, damage, terminal-state and recovery contracts with worked examples.
- `DECISIONS_AND_QUESTIONS.md`: source identity and traceability; 28 resolved baseline questions; explicitly separated calibration decisions and later-phase obligations.
- `rule_examples.json`: shared verification constants and 40 explicit expected-result fixtures.
- `verify_rules.py`: disposable offline standard-library design verifier, including negative-path CLI self-tests. It is not a shipping runtime.
- `CLOSURE_EVIDENCE.md`: this record.
- Root `README.md`: Phase 004 status, navigation, verification command and next gate; earlier-phase links retained.

No existing Phase 001–003 file was included in the change set. No game mode, biome, resource, online service, plugin, external library or production asset was added.

## Bible work-package acceptance

| Required item | Concrete specification | Executed evidence or explicit boundary |
|---|---|---|
| Nine-by-nine coordinates | BRD and REC | All 81 coordinate round trips; neighbor reciprocity; no diagonal/row wrap; invalid indices rejected. |
| Keep placement and edge entries | BRD | Center index 40 and four reserved entries; 76 ordinary buildable cells; duplicate/reserved placement rejection. |
| Port compatibility and rotation | PRT | All 16 basic port masks at all four quarter-turns and inverse rotations; graph fixtures. Specialized ports/Mast are specified, not implemented. |
| Connectivity and priority assignment | NET | Crown/Charter order, whole-Load admission, no-fit continuation, Dormant conduction, isolation, zero Load, cut/destruction and small-graph Resonance cases. |
| Three resources and Command | ECO | Atomic bundles, invalid/overflow rejection, upkeep once per Watch, failure latch, forward Production chains and no backward retries. |
| Watch sequencing | WCH and CMB | Exact seven-stage sequence, all 15 Watches/Acts/boss positions, Seal requirement, Council/exception/encounter/settlement guards and no Watch 16. |
| Damage, repair and Keep Integrity | DMG | Armor then ward then health; zero/exact-lethal/overkill cases; repair rejection, affordability and partial healing. Persistent salvage/rubble lifecycle remains a later implementation obligation. |
| Run victory and failure | END | Final victory, simultaneous defeat precedence, fatal boss/doctrine flags, non-final bosses, pending waves and early Keep defeat. |

REC specifies whole-state undo, reload validation, revision checks and equal information access for keyboard/controller. Executed probes cover cost/rotation transaction atomicity and JSON data round trips, not a production save service or physical input devices.

## Source and decision review

The authoritative master is the later `steam%20game%20number%202(1).md`, 459,471 bytes. Its SHA-256 is:

`89f805584dea2b90fac1fc7144d35ce0feb376f6d8c75e8037a265f190787f9d`

The source traceability document identifies the controlling phase and detailed gameplay sections, including section 20.2's Dormant conduction rule and section 20.7's ordered combat tick. The authorized Charterwake rename is preserved.

All Q01–Q28 are resolved for the minimal v1.0.0 contract. **Open critical baseline questions: zero.** This does not mean all future content has been designed. L01–L06 explicitly retain later balance, content modifiers, Godot implementation, Blender pipeline, empirical playtesting and naming obligations.

Keep Integrity 20, repair 3 for 1 Supply plus 1 Material, 100 ms normal presentation interval and half-paid-Material salvage are newly chosen verification/calibration values. They are not represented as bible-prescribed final balance or measured playtest results.

## Reproduction and actual results

From the repository root, with Python 3.10+ syntax support:

```sh
python3 docs/phase-004/verify_rules.py --self-test
```

Windows launcher equivalent:

```powershell
py -3 docs/phase-004/verify_rules.py --self-test
```

Tested interpreter: **Python 3.13.5**. No package installation, credentials or network access is needed. Actual successful output:

```text
PASS: 1404 contract checks; 40 explicit examples; rules 1.0.0
PASS: 8 deliberately invalid CLI cases rejected with exit 1
Scope: pure design examples only; no Godot/game/save/UI/export acceptance claimed.
```

The count includes enumerated assertions, not 1,404 independent gameplay scenarios. In addition to the 40 explicit fixtures, Resonance is compared with a separate simple-path enumeration oracle across every undirected graph on four vertices and each vertex pair. The attached-cycle/single-stem case is checked separately.

The eight negative CLI tests deliberately change an allocation expectation, damage expectation, simultaneous-victory expectation, board size, fixture-group completeness, upkeep sign, rules version and JSON syntax. Each must return exit code 1 with a failure report; an accidental pass fails the self-test. Expected results are never automatically regenerated from the implementation.

The Python source also parses successfully with `ast.parse`. The default verification command was run twice from a fresh temporary directory containing copied Phase 004 artifacts, with both exit codes zero and byte-identical output. This is clean-directory reproduction, not a claim that a Git clone or Godot import was executed. Direct Git clone access was unavailable because host resolution failed; repository publication uses the connected GitHub Git-data API.

## Tested artifact identities

These are Git blob hashes of the exact local files used in verification and uploaded for the implementation commit:

| Artifact | Git blob SHA |
|---|---|
| `README.md` | `5e1abf7762d5708528fc3cff9295dc2d04003cfd` |
| `CORE_RULES_V1.md` | `8acc28b54bffbe35aadb722c057970be146474d4` |
| `DECISIONS_AND_QUESTIONS.md` | `9fde09d09e7ad3babe34fdc75998fe6ae1c70976` |
| `rule_examples.json` | `f61656fc13b8a2480cc74cc72191382b1cc8b53b` |
| `verify_rules.py` | `236de87d6577c4785b8faf9d91286ae6058b1c4f` |

Entry baseline subtree hashes retained for publication verification:

- Phase 001: `07784c278b761e46afc016fc2ddbf74059a16476`.
- Phase 002: `0ec92de08fd5884e07f0711ff34255f5b2aee4ca`.
- Phase 003: `bf021b1bc1939728817ab5aebaad4f726ad9f53c`.

The implementation commit is followed by the commit introducing this closure file. The intended publication is one non-forced fast-forward of `main` to the closure commit, after rereading the remote head. The final remote head and file presence must be fetched back before reporting successful delivery. The closing commit can be located with `git log -1 -- docs/phase-004/CLOSURE_EVIDENCE.md`; this document does not contain an impossible self-referential commit hash.

## Scope, tool use and limitations

The bible permits small data examples and disposable verification to settle preproduction questions. Python was used for those arithmetic/graph/transaction checks only. Production gameplay remains typed GDScript/Godot, and authored visual production remains Blender. Port these expected fixtures to later Godot tests; do not add Python to the shipping game.

No Godot or Blender execution is claimed. No new production scene, final geometry, sprite, font or other third-party asset was necessary for this rules-lock phase. Existing toolchain records were left unchanged and are not independently claimed here to be current or verified releases.

Still untested and not certified: actual 1x/2x/4x/skip runtime equivalence, content-specific combat behavior, durable save recovery, controller/focus paths, UI scaling, animation readability, performance budgets, full-run pacing and fair-loss playtests. Their rules are specified; their scheduled implementation and empirical gates remain open. The new material preserves the physical command-network identity and Phase 001 scope ceiling. Charterwake remains a provisional name.

## Safe next gate

**Phase 005 — Scope budget and content ceiling.** Budget the already established systems, content, assets, text, audio, platforms and verification workload; provide its required scope spreadsheet, count ceilings, cut ladder, budget envelope and milestone map. Do not silently expand the game or skip remaining preproduction, Godot bootstrap or Blender pipeline gates.
