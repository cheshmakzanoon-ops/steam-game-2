# Phase 008 — Contingency, stop, and pivot plan

Phase 005 reserves **75 unallocated pre-launch developer-days**. These are not feature slots and do not authorize scope expansion.

## Contingency blocks

| ID | Window | Days | Intended use |
| --- | --- | ---: | --- |
| C1 | M2–M3 | 8 | foundation/import/build/save/toolchain recovery |
| C2 | M3–M5 | 10 | prototype and vertical-slice rework |
| C3 | M6–M9 | 20 | content/art/animation throughput uncertainty |
| C4 | M9–M12 | 15 | accessibility/reliability/platform/demo recovery |
| C5 | M12–M15 | 22 | beta/RC/localization/platform/launch blockers |
| **Total** | | **75** | exact Phase 005 reserve |

Unused contingency stays unused.

## Consumption rules

1. Record cause, evidence, owner, days authorized, and protected gate.
2. Prefer fixing/cutting the cause before consuming later reserve.
3. C5 cannot fund optional early content without approved scope/roadmap change.
4. If forecast erodes the Phase 005 reserve threshold, trigger scope review.
5. A cut does not authorize a different unbudgeted feature.

## Stop-or-pivot reviews

Phase 009 owns detailed kill thresholds. Phase 008 fixes the review points and available decisions.

| Phase | Review | Question | Allowed result |
| ---: | --- | --- | --- |
| 010 | Preproduction go/no-go | Are product/rules/scope/name/roadmap/risk gates coherent enough for foundation investment? | GO / REWORK / CUT / STOP |
| 030 | Core-loop prototype | Do players understand and want to retry the Command-routing toy? | GO / REWORK / PIVOT CORE / STOP |
| 040 | Combat vertical slice | Does preparation lead to readable, fair, satisfying consequence? | GO / CUT / REWORK / PIVOT |
| 070 | Production throughput | Can target presentation be produced inside frame/time ceilings? | GO / SIMPLIFY STYLE / CUT / REBASELINE |
| 100 | Demo go/no-go | Is the demo stable, accessible, representative, and commercially credible? | PUBLISH / HOLD / CUT / SKIP EVENT WINDOW |
| 107 | Feedback synthesis | Does external evidence support the current direction? | CONTINUE / TARGETED REVISION / CUT / PIVOT |
| 112 | Beta shipability | Are remaining defects tractable inside release reserve? | PROCEED / DELAY / CUT / REOPEN BLOCKER |
| 114 | Release candidate | Is there a reproducible candidate with no release blocker? | ACCEPT / REJECT |

A review never waives the next phase's acceptance gate.

## Recovery behavior

When the plan goes red:
- preserve the last green commit and reproducible sources;
- identify the first failed assumption;
- use the Phase 005 cut ladder before widening budget or schedule;
- rerun affected acceptance evidence;
- re-estimate remaining days and reserve;
- record owner decision and new baseline commit.

Do not use sunk cost as a reason to continue a failed direction.
