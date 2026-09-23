# Phase 007 — Closure evidence

**Project:** Charterwake: The Last Relay — provisional working title  
**Phase:** 007 — Game design document baseline  
**Status:** COMPLETE / GREEN for the preproduction GDD baseline  
**GDD version:** 1.0  
**Date:** 2026-09-22  
**Entry commit:** 050d4cb78e9ea9110ecd1fc4c7c8441c998fc591  
**Implementation commit:** 682cb25be86eee73a28bbdcd5a7eeb081e029001  
**Target branch:** main

This closes the Phase 007 documentation gate. It does not claim that later Godot gameplay, Blender production assets, final balance, measured performance, Steam integration, public-title clearance, or launch QA are complete.

## 1. Deliverables

- GDD_V1.md — consolidated authoritative design baseline.
- ANNOTATED_EXAMPLES.md — ten worked player-visible rule examples and board diagrams.
- CHANGE_REQUEST_TEMPLATE.md — required change-control workflow.
- DESIGN_REVIEW_SIGNOFF.md — cross-phase design review and sign-off record.
- CLOSURE_EVIDENCE.md — this evidence packet.
- README.md — project index updated to Phase 007 complete.

## 2. Bible work-package acceptance

| Required Phase 007 item | Repository evidence | Result |
| --- | --- | --- |
| Organize mechanics into player-visible rules | GDD sections 5 through 18 | PASS |
| Include annotated turn examples | Annotated Examples B through J | PASS |
| Include board diagrams | GDD section 6 and Example A | PASS |
| Placement/disconnection edge cases | GDD section 24 and Examples B, E, F | PASS |
| Define launch content categories | GDD section 17 | PASS |
| UX/accessibility requirements | GDD section 18 | PASS |
| Change history | GDD section 27 | PASS |
| Link systems to owning phases | GDD section 25 | PASS |

## 3. Committed-content verification

After the implementation commit was moved to main, every Phase 007 deliverable was fetched back from GitHub.

Checks passed for:
- GDD v1.0 heading and status;
- canonical run/player-visible rules section;
- board diagram;
- placement/disconnection edge-case section;
- launch-content category section;
- accessibility section;
- change history;
- system ownership map;
- exactly ten numbered annotated examples;
- change-template acceptance-test section;
- PASS/GREEN design-review result.

The fetched Git blob identities for the implementation files are:

- GDD_V1.md: 924642b8dc357e6b929458721c7e4eb2999ee544
- ANNOTATED_EXAMPLES.md: 8036d51bc1fcf7dd7aacb41689a04b70e00a5d51
- CHANGE_REQUEST_TEMPLATE.md: fee5ce07e27c12f32b55b387392de2d5ee385588
- DESIGN_REVIEW_SIGNOFF.md: dcb3b2e1309b09129350fb8e2a5a727a355e68ea

## 4. Consolidation review

The GDD does not silently replace the source contracts.

Source precedence is explicit:
1. master project bible;
2. approved superseding change record;
3. Phase 004 Core Rules for exact rule semantics;
4. Phase 005 scope contract for ceilings;
5. Phase 006 lexicon for player-facing naming;
6. GDD as consolidated working reference.

If two documents diverge, the divergence is a defect to resolve through the change process rather than an excuse to choose the convenient interpretation.

## 5. Normal, boundary, failure, and recovery evidence

### Normal path

Annotated Example H traces one complete Watch from Forecast through Aftermath, including atomic Seal, deterministic Production, deterministic Siege, and checkpointing.

### Boundary paths

Examples cover:
- 9x9 board edges with no array-row wrapping;
- whole-Load allocation with a skipped non-fitting structure;
- Dormant physical conduction;
- disabled switch versus severed link;
- controller focus at a board boundary;
- simultaneous final-boss and Keep death.

### Failure paths

The GDD requires atomic rejection for illegal placement, invalid Seal transactions, impossible content, invalid terminal configuration, and inaccessible strategic information.

### Recovery paths

The design preserves whole-state planning undo, validated save/reload ownership, title-independent stable IDs, explicit design rollback, and the Phase 007 change request's rollback section.

These are design-contract examples, not claims that the later runtime tests already exist.

## 6. Cross-phase preservation

### Phase 001 — PASS

The one-board product, scarce Command, transparent consequences, 35–50 minute run target, premium business model, and solo scope ceiling remain intact.

### Phase 002 — PASS

The physical command network remains the product differentiator. No copied gaze mechanic, competitor UI, copied terminology, or unlicensed asset is introduced. Charterwake remains provisional.

### Phase 003 — PASS

The GDD preserves first-look comprehension, meaningful planning tradeoffs, saw-toothed Watch pacing, fair-loss standards, input parity, and causal post-run explanation.

### Phase 004 — PASS

Exact board, port, allocation, resource, Watch, combat, damage, terminal, undo, and reload summaries remain aligned with Core Rules v1.0.0. The GDD explicitly defers exact semantics to that rules document.

### Phase 005 — PASS

No content, visual, text, audio, cash, install, mode, biome, or platform ceiling is widened.

### Phase 006 — PASS

Canonical Charterwake title/subtitle usage, Act names, Watch naming, priorities, resource names, doctrines, enemy families, and provisional-name status remain consistent.

## 7. Change-control rule

Future contributors must use CHANGE_REQUEST_TEMPLATE.md for a behavior or scope change.

Implementation code does not approve a design change by itself.

An accepted change must identify its player problem, prior source, impact, alternatives, normal/boundary/failure/recovery evidence, rollback, required document updates, and explicit decision owner.

## 8. Production boundary

No production Godot scene, GDScript system, Blender asset, final font, final logo, audio file, Steam configuration, or new third-party dependency was added by Phase 007.

No later phase is claimed complete merely because the GDD describes it.

## 9. Known non-blocking later work

Still intentionally unresolved by their later owner phases:
- final Charterwake public-name clearance;
- exact six Oath mechanics;
- detailed remaining enemy and content definitions;
- full balance values;
- Resonance family bonuses;
- measured runtime performance;
- final visual/audio assets;
- empirical player testing;
- localization language selection;
- final public pricing.

## 10. Safe entry condition for Phase 008

Phase 008 — Production roadmap and dependency graph — may begin from this green baseline.

It must:
1. schedule the accepted work rather than create new scope;
2. identify the true dependency graph and critical path;
3. mark genuinely parallel-safe work;
4. budget contingency;
5. establish stop-or-pivot reviews;
6. create milestone and weekly tracking based on accepted outputs rather than hours alone;
7. preserve every Phase 001–007 gate.

**Phase 007 is closed.**
