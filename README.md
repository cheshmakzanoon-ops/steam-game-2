# Charterwake: The Last Relay

Compact one-board kingdom/base-building strategy roguelite for Steam.

> **Naming status:** Charterwake: The Last Relay remains a provisional working title pending full public-name clearance.

## Production status

**Current gate:** Phase 009 — Risk register and kill criteria — COMPLETE

Phases 001–009 now establish the product/design case, originality boundary, player-experience contract, exact core rules, scope budget, brand vocabulary, GDD, production roadmap, and formal risk/kill criteria.

## Current authoritative entry points

- [GDD v1.0](docs/phase-007/GDD_V1.md)
- [Phase 008 roadmap](docs/phase-008/DEPENDENCY_GRAPH.md)
- [Living risk register](docs/phase-009/LIVING_RISK_REGISTER.csv)
- [Risk scoring policy](docs/phase-009/RISK_SCORING_AND_POLICY.md)
- [Kill / pivot criteria](docs/phase-009/KILL_CRITERIA.md)
- [Mitigation schedule](docs/phase-009/MITIGATION_SCHEDULE.md)
- [Risk review cadence](docs/phase-009/REVIEW_CADENCE.md)
- [Machine-readable risk model](docs/phase-009/RISK_MODEL.json)
- [Phase 009 closure evidence](docs/phase-009/CLOSURE_EVIDENCE.md)

## Risk-control headline

- **26 scored living risks**
- **5 critical / 7 high / 10 medium / 4 low**
- Formal stop/pivot reviews: Phases **010, 030, 040, 070, 100, 107, 112, 114**
- Prototype evidence threshold: **8 fresh players**
- Demo evidence threshold: **12 fresh players**
- Phase 005 20% reserve and 18-month safety ceiling remain binding

## Preproduction verification

~~~sh
python3 docs/phase-004/verify_rules.py --self-test
python3 -S docs/phase-005/verify_scope.py --self-test
python3 -S docs/phase-008/verify_roadmap.py --self-test
python3 -S docs/phase-009/verify_risks.py --self-test
~~~

These commands validate preproduction contracts and fixtures, not future gameplay/runtime quality.

The next mandatory gate is **Phase 010 — Preproduction approval gate**.
