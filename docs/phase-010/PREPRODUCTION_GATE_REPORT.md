# Phase 010 — Preproduction approval gate report

**Project:** Charterwake: The Last Relay  
**Decision date:** 2026-09-23  
**Entry baseline:** Phase 009 closure at \`4e601bec5e3bba2a901bbf64b215bb45fe75b9a0\`  
**Decision:** **GO — Phase 011 technical foundation only**  
**Public-title status:** provisional / AMBER  
**Full-time 12–15 month execution commitment:** NOT YET ASSERTED  
**External spending authorization:** DEFERRED unless separately approved by the project owner

This is the final product-definition/preproduction gate before technical repository/bootstrap work. The decision is intentionally narrower than “the game will succeed” or “ship in 15 months.” It authorizes the next controlled technical-foundation phase because the design case is coherent, bounded, original enough to prototype, and governed by explicit kill criteria.

It does **not** waive the future empirical gates for fun, readability, fairness, performance, art throughput, market response, title clearance, or launch readiness.

## 1. Structured review of Phases 001–009

| Phase | Question | Evidence reviewed | Decision |
| ---: | --- | --- | --- |
| 001 | Is there a coherent product and commercial hypothesis? | product charter, traceability, scope, risk baseline | PASS |
| 002 | Is the concept structurally/originally bounded and rights-aware? | originality brief, IP/licensing controls, naming plan | PASS WITH TITLE PROVISIONAL |
| 003 | Is the intended player experience explicit enough to judge later? | experience map, 15-Watch pacing, fair-loss rubric, player stories | PASS |
| 004 | Are minimal core rules frozen before implementation? | Core Rules v1.0.0 + worked examples/verifier | PASS |
| 005 | Does the proposed product fit a solo scope envelope? | content/art/text/audio/performance/cash ceilings and cut ladder | PASS WITH PRIVATE-RUNWAY/SPEND CONDITIONS |
| 006 | Is player-facing vocabulary coherent and rename-safe? | brand guide, lexicon, logo brief, public-name risk note | PASS AS PROVISIONAL |
| 007 | Is there a consolidated GDD/change-control baseline? | GDD v1.0, examples, change template, design sign-off | PASS |
| 008 | Is the 120-phase plan capacity-aware rather than date fiction? | phase estimates, dependency graph, contingency, dashboard | PASS |
| 009 | Are material failure conditions precommitted? | 26-risk register, kill criteria, mitigation, review cadence | PASS |

No contradiction was found that requires a new mode, biome, resource family, online service, or content expansion to proceed into technical foundation.

## 2. Product case

The product remains:

- compact one-board kingdom/base-building strategy roguelite;
- 9×9 board with Keep at center;
- physical Command network as the main strategic differentiator;
- visible pressure + limited Command as the central tension;
- 15 Watches / three Acts / bosses at 5, 10, 15;
- 35–50 minute normal run target;
- premium one-time purchase;
- offline-first core game;
- one principal launch mode and one principal biome/theme.

The product is approved for **prototype/foundation investment**, not yet for public commercial commitment.

## 3. Skeptical hook review

The detailed challenge is in \`SKEPTICAL_PLAYER_REVIEW.md\`.

Preproduction conclusion:

- the core hook is distinguishable from a moving-gaze/activation-zone game because power follows a player-built physical port graph, Load capacity, priorities, switches, and redundancy;
- the rules explicitly prevent the network from becoming a hidden electrical-engineering simulation;
- low-micro intent is enforceable because planning is paused/reversible and Production/Siege resolve automatically;
- controlled randomness and visible threat forecasting preserve agency;
- fair-loss/post-run requirements make defeat causally inspectable.

The critical unknown remains empirical: **does this produce compelling repeat play?** Phase 009 deliberately keeps that as a future Phase 030 kill/pivot test instead of fabricating a preproduction answer.

## 4. Scope against solo capacity

Accepted Phase 005/008 model:

- 240 productive pre-launch developer-days in the 15-month model;
- 165 planned pre-launch phase-days;
- 75 protected contingency days;
- 31.25% unallocated reserve;
- 18-month safety ceiling;
- 10 planned post-launch developer-days.

The 12-month scenario is not the baseline because it falls below the 20% reserve target.

**Decision:** scope is acceptable for technical foundation **only while Phase 005 ceilings and Phase 008 reserve rules remain binding**.

### Private runway boundary

No personal living-runway amount is stored or inferred.

The project may continue through low-cash technical foundation and evidence gates. Before assuming a full-time 12–15 month production commitment, the project owner must privately make a runway/production-mode decision.

Missing private runway data is not “zero,” “enough,” or a blocker to creating the Phase 011 foundation.

### External spending

No external specialist scenario is selected by this Phase 010 report. External spending remains deferred until the project owner explicitly chooses/approves it. This satisfies the risk gate without inventing authorization.

## 5. Blender → Godot feasibility decision

See \`BLENDER_GODOT_FEASIBILITY.md\`.

Preproduction architecture decision: **FEASIBLE WITH EXECUTION PROOF DEFERRED TO OWNED PHASES**.

The intended path is:

\`\`\`text
Blender authored source
    ↓ reproducible export
glTF 2.0 / GLB + explicitly managed texture/mask outputs
    ↓ Godot importer
Godot scene/resources
    ↓ runtime composition
2D/2.5D fixed orthographic gameplay presentation
\`\`\`

Official Godot documentation recommends glTF 2.0 and supports Blender through the glTF import path. Blender 4.5 LTS includes a glTF 2.0 exporter.

This execution environment did not expose Blender or Godot binaries, so no fake local round-trip is claimed. Phase 011 owns the initial Godot project/version manifest; Phases 019–020 own actual Blender-template/export/import calibration and clean regeneration.

That limitation is acceptable for Phase 010 because the bible permits a report/fixture/command and explicitly reserves production pipeline implementation for later phases.

## 6. Offline / online dependency decision

**PASS — no mandatory online dependency exists in the accepted product.**

Current repository inspection before Phase 010 found only the root README and documentation tree; no Godot project, package manifest, SDK, service client, backend, account system, telemetry package, or online runtime dependency exists yet.

Design baseline explicitly excludes:
- mandatory accounts;
- live service;
- multiplayer;
- cloud-hosted progression;
- server-authoritative gameplay.

Future Steamworks integration must degrade safely when Steam is absent wherever the bible requires offline behavior.

Any new online dependency is a scope/architecture change and must pass the Phase 007 change request plus Phase 009 dependency/offline risk gate.

## 7. Platform and price assumption decision

### Platform

Retain:
- primary launch target: Steam for Windows;
- Linux and Steam Deck verification before launch;
- no macOS/console/mobile commitment.

This is an **assumption baseline**, not platform certification. Actual export/platform acceptance belongs to later phases.

### Price

Retain **USD $14.99 as a working launch-price hypothesis**, not entitlement or a locked store price.

Price must be revalidated using current market evidence and finished-product quality before store publication. No revenue forecast is derived from the hypothesis.

## 8. Critical unknown disposition

See \`CRITICAL_UNKNOWNS.md\`.

**Critical preproduction decision unknowns blocking Phase 011: zero.**

Important empirical risks remain open by design:

- whether Command routing is compelling rather than busywork;
- whether the board remains readable in a playable build;
- whether losses remain fair in actual combat;
- whether deterministic/save architecture works in Godot;
- whether final art throughput meets the roadmap;
- whether the public title clears;
- whether market response supports launch scope.

Each has an owning phase, threshold, and stop/pivot trigger. These are not “closed” by pretending evidence exists.

## 9. Conditions attached to GO

Phase 011 is authorized only under these conditions:

1. Keep Charterwake provisional and stable IDs title-independent.
2. Do not add production gameplay beyond Phase 011's empty bootable foundation.
3. Do not add online/runtime service dependency without approved change control.
4. Preserve typed deterministic-simulation architecture.
5. Pin actual Godot/Blender versions in Phase 011/019 records and verify what is truly installed.
6. No external spending is authorized by this report.
7. Do not represent the 12–15 month plan as a promise until owner runway/production mode is privately reviewed.
8. Preserve Phase 005 scope ceilings and Phase 009 kill criteria.
9. Do not preempt Phase 030/040 empirical hook/fairness gates with more content.

Violation of a condition reopens the gate.

## 10. Sign-off record

**Decision owner:** project owner.  
**Recorded authorization:** the project owner explicitly instructed ChatGPT on 2026-09-23 to implement Phase 010 and commit/push it to this repository.  
**Recorded decision prepared under that instruction:** **GO — Phase 011 technical foundation only, with the conditions above.**

This is a project decision record. It is not a fabricated handwritten signature, legal opinion, financing approval, or trademark clearance.

## 11. Next gate

**Phase 011 — Repository bootstrap.**

Phase 011 must create the actual bootable empty Godot project, clean repository conventions, version manifest, licensing/notices foundation, and clean-clone verification. It must not jump directly to gameplay production.
