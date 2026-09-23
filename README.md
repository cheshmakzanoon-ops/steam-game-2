# Charterwake: The Last Relay

Compact one-board kingdom/base-building strategy roguelite for Steam.

> **Naming status:** Charterwake: The Last Relay is the current WORKING TITLE and remains provisional pending full public-name clearance.

## Production status

**Current gate:** Phase 008 — Production roadmap and dependency graph — COMPLETE

Phases 001–008 now establish the product charter, originality/IP boundary, player experience, core rules, scope budget, canonical vocabulary, consolidated GDD, and capacity-aware 120-phase production roadmap.

## Current authoritative entry points

- [GDD v1.0](docs/phase-007/GDD_V1.md)
- [Phase estimates — all 120 phases](docs/phase-008/PHASE_ESTIMATES.csv)
- [Dependency graph and critical path](docs/phase-008/DEPENDENCY_GRAPH.md)
- [Relative milestone calendar](docs/phase-008/MILESTONE_CALENDAR.md)
- [Contingency and pivot plan](docs/phase-008/CONTINGENCY_AND_PIVOT_PLAN.md)
- [Weekly dashboard template](docs/phase-008/WEEKLY_DASHBOARD_TEMPLATE.md)
- [Roadmap model](docs/phase-008/ROADMAP_MODEL.json)
- [Phase 008 closure evidence](docs/phase-008/CLOSURE_EVIDENCE.md)

## Roadmap headline

- **165 planned pre-launch developer-days**
- **75 protected contingency days**
- **240 productive pre-launch capacity days** in the 15-month model
- **10 planned post-launch developer-days**
- Milestones: Prototype 030, Vertical Slice 040, Demo 100, Alpha 111, Beta 112, RC 114, Launch 116

Agents and automation do not multiply the solo developer capacity.

## Preproduction verification

~~~sh
python3 docs/phase-004/verify_rules.py --self-test
python3 -S docs/phase-005/verify_scope.py --self-test
python3 -S docs/phase-008/verify_roadmap.py --self-test
~~~

These validate preproduction contracts, not later gameplay/runtime acceptance.

The next mandatory gate is **Phase 009 — Risk register and kill criteria**.
