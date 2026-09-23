# Phase 010 — Closure evidence

**Project:** Charterwake: The Last Relay — provisional working title  
**Phase:** 010 — Preproduction approval gate  
**Status:** COMPLETE / GREEN FOR PHASE 011 FOUNDATION ENTRY  
**Decision:** GO — PHASE 011 TECHNICAL FOUNDATION ONLY  
**Date:** 2026-09-23  
**Entry commit:** 4e601bec5e3bba2a901bbf64b215bb45fe75b9a0  
**Implementation commit:** b500e3019f0e15ae88e762fddff311aa10eecc77  
**Target branch:** main  
**Frozen-baseline tag requested by bible:** preproduction-v1

This closes product-definition/preproduction Phases 001–010. It does not approve public launch, public-title clearance, full production spending, a guaranteed 12–15 month schedule, or any future empirical gate.

## 1. Required deliverables

- PREPRODUCTION_GATE_REPORT.md — structured Phase 001–009 design/business review and explicit decision.
- SKEPTICAL_PLAYER_REVIEW.md — 14 adversarial player/product questions.
- BLENDER_GODOT_FEASIBILITY.md — architecture feasibility report and later execution-proof requirements.
- CRITICAL_UNKNOWNS.md — explicit blocker vs future-evidence disposition.
- PREPRODUCTION_BASELINE_MANIFEST.json — frozen Phase 001–009 closure blob identities and locked baseline constants.
- verify_preproduction.py — standard-library consistency checker.
- this closure evidence.
- root README updated to Phase 010.

## 2. Bible work-package acceptance

| Required Phase 010 item | Evidence | Result |
| --- | --- | --- |
| Structured design review | PREPRODUCTION_GATE_REPORT §1 | PASS |
| Challenge hook with skeptical questions | SKEPTICAL_PLAYER_REVIEW | PASS |
| Verify scope against solo capacity | PREPRODUCTION_GATE_REPORT §4 | PASS WITH CONDITIONS |
| Verify Blender→Godot approach | BLENDER_GODOT_FEASIBILITY | PASS FOR APPROACH / EXECUTION DEFERRED |
| Confirm no online dependency | PREPRODUCTION_GATE_REPORT §6 | PASS |
| Confirm platform and price assumptions | PREPRODUCTION_GATE_REPORT §7 | PASS AS ASSUMPTIONS |
| Close critical unknowns | CRITICAL_UNKNOWNS | PASS FOR PHASE 011 ENTRY |
| Explicit go/no-go/revise decision | PREPRODUCTION_GATE_REPORT | GO — FOUNDATION ONLY |

## 3. Explicit gate decision

**GO — Phase 011 technical foundation only.**

This means:
- create the clean repository/bootstrap/empty Godot project next;
- do not skip to production gameplay;
- preserve deterministic/offline architecture;
- keep scope and kill criteria binding.

This does not mean:
- the core loop is already proven fun;
- the title is cleared;
- the owner has committed personal runway;
- external cash is approved;
- Blender/Godot asset transfer has already passed a clean-machine round trip;
- market demand or launch price is proven.

## 4. Structured-review result

Phases 001–009 were reviewed together and found internally coherent enough for foundation investment.

The baseline preserves:
- one-board readability;
- physical Command-network differentiation;
- scarce Command over click scarcity;
- controlled randomness and visible forecasting;
- deterministic simulation;
- fair-loss explanation;
- 35–50 minute normal run target;
- one principal mode and biome/theme;
- bounded launch content;
- offline operation;
- solo-production scope;
- explicit stop/pivot criteria.

No Phase 010 solution widened scope to make the case look stronger.

## 5. Solo-capacity decision

Accepted planning baseline remains:
- 165 planned pre-launch developer-days;
- 75 protected contingency days;
- 240 productive pre-launch capacity days in the 15-month model;
- 18-month safety ceiling.

The 12-month model is not endorsed as the baseline because its reserve falls below the Phase 005 target.

Personal runway remains private/unset in repository data. Phase 010 does not infer it is zero or adequate.

Full-time 12–15 month execution must not be treated as a personal financial commitment until the project owner privately reviews runway/production mode.

No external spending is authorized by Phase 010.

## 6. Blender→Godot feasibility evidence

Official documentation review supports glTF 2.0 / GLB as the intended Blender→Godot interchange architecture. Godot documents glTF 2.0 as recommended and supports Blender through its glTF import path; Blender 4.5 LTS documents glTF 2.0 export.

The Phase 010 runtime environment did not expose Blender or Godot executables. Therefore **no local round-trip execution is claimed**.

Actual clean export/import proof remains mandatory at:
- Phase 011 for the actual Godot project/version manifest;
- Phase 019 for Blender template/exporter;
- Phase 020 for Godot import/calibration.

Failure there reopens the assumption.

## 7. Offline/dependency evidence

Repository-tree inspection at Phase 010 entry found only README/documentation/preproduction verification scripts and no project/package/runtime dependency manifest.

Accepted design explicitly rejects mandatory:
- account service;
- live service;
- multiplayer;
- server-authoritative gameplay;
- cloud-hosted progression.

Future Steam/platform integration cannot become authoritative simulation/save infrastructure.

## 8. Platform and price disposition

Retained assumptions:
- primary launch target: Steam for Windows;
- Linux and Steam Deck verification before launch;
- no macOS/console/mobile commitment;
- USD $14.99 remains a price **hypothesis**, to be revalidated before store publication.

No revenue forecast is inferred.

## 9. Critical-unknown disposition

Critical preproduction decision unknowns that block Phase 011: **zero**.

Open empirical/commercial items remain intentionally assigned to later gates:
- core-loop replayability — Phase 030;
- combat/fair loss — Phase 040;
- art throughput — Phase 070;
- performance — Phase 085/086;
- demo response — Phase 100/107;
- title clearance — before public lock;
- beta/RC readiness — Phase 112/114.

This is disciplined deferral, not a false pass.

## 10. Normal, boundary, failure, and recovery evidence

### Normal

Phases 001–009 green → structured review → conditions recorded → GO to Phase 011.

### Boundary

- public title still provisional;
- no private runway number;
- no external spending decision;
- no local Blender/Godot binaries in this execution environment.

Each has an explicit disposition that does not require inventing data.

### Failure

Phase 010 would be REVISE/NO-GO for foundation if the product required unbounded scope, mandatory online infrastructure, unrecoverable rights conflict affecting architecture, or a roadmap beyond the 18-month safety ceiling after cuts.

### Recovery

Preserve the last green baseline, correct the failed assumption or scope, update the owning source/change record, rerun Phase 009/010 review, and create a new baseline/tag rather than rewriting preproduction-v1 history.

## 11. Committed-content verification

After Phase 010 implementation was moved to main, every Phase 010 file was fetched back from GitHub and independently checked.

PASS conditions included:
- explicit GO-to-Phase-011-only decision;
- all nine prior-phase closure blob identities present;
- at least twelve skeptical questions (actual: fourteen);
- Blender/Godot feasibility document references glTF and owned later proof phases;
- critical blockers for Phase 011 stated as zero without closing empirical risks;
- no external-spend authorization;
- title remains provisional;
- mandatory-online dependency false;
- full-time schedule commitment false;
- verifier present.

The compare from the Phase 009 closure to Phase 010 implementation is a single fast-forward commit containing only newly added docs/phase-010 files.

## 12. Frozen baseline and tag

PREPRODUCTION_BASELINE_MANIFEST.json freezes the accepted Phase 001–009 closure blob identities and key product/scope conditions.

The bible requires the final Phase 010 baseline to be tagged:

**preproduction-v1**

The tag must point to the Phase 010 closure commit so the closure evidence itself is part of the frozen baseline. The tag is an immutable historical baseline; future revisions must use a new tag rather than force-moving it.

## 13. Safe entry condition for Phase 011

Phase 011 may begin only from the Phase 010 closure/tagged baseline.

It must:
1. create the actual empty Godot project;
2. pin actual tool versions in a version manifest;
3. create clean repository structure and ignore/attributes rules;
4. add license and third-party notices foundation;
5. preserve line-ending rules;
6. verify clean clone/open behavior;
7. add no production gameplay merely for visible progress;
8. preserve offline/deterministic architecture and all Phase 001–010 gates.

**Phase 010 is closed, subject to remote creation/verification of the required preproduction-v1 tag on this closure commit.**
