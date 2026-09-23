# Charterwake: The Last Relay

Compact one-board kingdom/base-building strategy roguelite for Steam.

> **Naming status:** Charterwake: The Last Relay is the current WORKING TITLE and remains provisional pending full public-name clearance.

## Production status

**Current gate:** Phase 007 — Game design document baseline — COMPLETE

Phases 001–007 now establish the product charter, originality/IP boundary, player-experience contract, exact core-rule semantics, scope budget, canonical vocabulary, and consolidated GDD/change-control baseline.

## Authoritative design entry points

- [GDD v1.0](docs/phase-007/GDD_V1.md)
- [Annotated examples and board diagrams](docs/phase-007/ANNOTATED_EXAMPLES.md)
- [Design change-request template](docs/phase-007/CHANGE_REQUEST_TEMPLATE.md)
- [Phase 007 design review sign-off](docs/phase-007/DESIGN_REVIEW_SIGNOFF.md)
- [Phase 007 closure evidence](docs/phase-007/CLOSURE_EVIDENCE.md)

## Source contracts

- [Phase 001 — Product charter](docs/phase-001/PRODUCT_CHARTER.md)
- [Phase 002 — Originality and IP safety](docs/phase-002/ORIGINALITY_BRIEF.md)
- [Phase 003 — Player experience](docs/phase-003/PLAYER_EXPERIENCE_MAP.md)
- [Phase 004 — Core Rules v1.0.0](docs/phase-004/CORE_RULES_V1.md)
- [Phase 005 — Scope and budget contract](docs/phase-005/SCOPE_BUDGET.md)
- [Phase 006 — Brand vocabulary](docs/phase-006/BRAND_VOCABULARY_GUIDE.md)

## Preproduction verification

~~~sh
python3 docs/phase-004/verify_rules.py --self-test
python3 -S docs/phase-005/verify_scope.py --self-test
~~~

These commands validate design and scope fixtures. They do not claim later gameplay-runtime acceptance.

## Locked project identity

- **Working title:** Charterwake: The Last Relay — provisional
- **Genre:** compact one-board kingdom/base-building strategy roguelite
- **Core promise:** You can see every major threat coming, but your command network can never power everything at once.
- **Run:** 15 Watches across three Acts; normal victory target 35–50 minutes
- **Business model:** premium one-time purchase
- **Primary launch target:** Steam for Windows; Linux and Steam Deck verification before launch
- **Launch ceiling:** one principal mode, one principal biome/theme, four doctrines, three bosses

The next mandatory gate is **Phase 008 — Production roadmap and dependency graph**.
