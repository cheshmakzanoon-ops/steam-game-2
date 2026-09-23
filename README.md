# Charterwake: The Last Relay

Compact one-board kingdom/base-building strategy roguelite for Steam.

> **Naming status:** Charterwake: The Last Relay remains a provisional working title pending full public-name clearance.

## Production status

**Current gate:** Phase 010 — Preproduction approval gate — COMPLETE  
**Decision:** **GO — Phase 011 technical foundation only**

Product-definition/preproduction Phases 001–010 are complete. The baseline is frozen for the bible-required **preproduction-v1** tag.

## Phase 010 decision package

- [Preproduction gate report](docs/phase-010/PREPRODUCTION_GATE_REPORT.md)
- [Skeptical player challenge](docs/phase-010/SKEPTICAL_PLAYER_REVIEW.md)
- [Blender→Godot feasibility report](docs/phase-010/BLENDER_GODOT_FEASIBILITY.md)
- [Critical unknown disposition](docs/phase-010/CRITICAL_UNKNOWNS.md)
- [Frozen baseline manifest](docs/phase-010/PREPRODUCTION_BASELINE_MANIFEST.json)
- [Phase 010 closure evidence](docs/phase-010/CLOSURE_EVIDENCE.md)

## What GO means

Authorized next work:
- Phase 011 clean repository/bootstrap and empty bootable Godot foundation.

Not yet claimed:
- core-loop fun/replayability;
- public-title clearance;
- external spending approval;
- personal full-time runway commitment;
- Blender↔Godot clean round-trip;
- runtime performance;
- demo/market/launch readiness.

## Locked planning headline

- 15 Watches / three Acts
- 35–50 minute normal run target
- one principal launch mode and one principal biome/theme
- 165 planned pre-launch developer-days
- 75 protected contingency days
- 18-month safety ceiling
- offline core game
- $14.99 remains a working price hypothesis

## Preproduction contract verification

~~~sh
python3 docs/phase-004/verify_rules.py --self-test
python3 -S docs/phase-005/verify_scope.py --self-test
python3 -S docs/phase-008/verify_roadmap.py --self-test
python3 -S docs/phase-009/verify_risks.py --self-test
python3 -S docs/phase-010/verify_preproduction.py --self-test
~~~

The next mandatory gate is **Phase 011 — Repository bootstrap**.
