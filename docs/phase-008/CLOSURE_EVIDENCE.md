# Phase 008 — Closure evidence

**Project:** Charterwake: The Last Relay — provisional working title  
**Phase:** 008 — Production roadmap and dependency graph  
**Status:** COMPLETE / GREEN for preproduction production-planning baseline  
**Date:** 2026-09-22  
**Entry commit:** `0910d58e44f4fec9255c30cb230ae586f0d4d1f4`  
**Implementation commit:** `13ad18ababcd7c508c24b865fbad4059bcfe4240`  
**Target branch:** `main`

This closes the Phase 008 planning gate. It does not claim future phases are implemented, that any public date is booked, that the 15-month target is guaranteed, or that contingency is spare feature capacity.

## 1. Required deliverables

- `DEPENDENCY_GRAPH.md` — hard acceptance path, critical-path interpretation, cross-system spine, and parallel-safe preparation lanes.
- `MILESTONE_CALENDAR.md` — relative prototype, vertical-slice, demo, alpha, beta, release-candidate, launch, and post-launch windows.
- `CONTINGENCY_AND_PIVOT_PLAN.md` — protected contingency blocks, consumption rules, stop/pivot reviews, and recovery behavior.
- `WEEKLY_DASHBOARD_TEMPLATE.md` — accepted-work burndown and weekly production review.
- `PHASE_ESTIMATES.csv` — all 120 phases with developer-day estimate, confidence, hard predecessor, relative window, milestone/review flags, status, and acceptance weight.
- `ROADMAP_MODEL.json` — machine-readable staffing/capacity/contingency/milestone constants.
- `verify_roadmap.py` — offline roadmap invariant checker.
- Phase package README.

## 2. Bible work-package acceptance

| Required Phase 008 item | Evidence | Result |
| --- | --- | --- |
| Estimate each phase in developer-days | PHASE_ESTIMATES.csv, 120 rows | PASS |
| Identify critical path | DEPENDENCY_GRAPH.md | PASS |
| Mark parallel-safe art/audio/writing | DEPENDENCY_GRAPH.md | PASS |
| Prototype / vertical slice / demo / alpha / beta / launch milestones | MILESTONE_CALENDAR.md | PASS |
| Include contingency blocks | CONTINGENCY_AND_PIVOT_PLAN.md + ROADMAP_MODEL.json | PASS |
| Define stop-or-pivot reviews | CONTINGENCY_AND_PIVOT_PLAN.md | PASS |
| Set review cadence | dashboard + milestone/re-baseline rules | PASS |
| Burndown based on accepted work, not hours | WEEKLY_DASHBOARD_TEMPLATE.md | PASS |

## 3. Staffing and capacity baseline

The model retains the Phase 005 solo-production assumption:

- one solo generalist owner;
- 40 nominal hours/week;
- 80% project focus;
- 32 effective project hours/week;
- agents/automation do not multiply developer capacity;
- bounded optional specialists remain inside the Phase 005 external-cash scenarios.

Pre-launch capacity:
- 240 productive developer-days in the 15-month model;
- 165 planned phase-days;
- 75 unallocated contingency days;
- 31.25% reserve.

Post-launch Phase 117–120 planning allocation: 10 developer-days.

## 4. Phase-estimate coverage

`PHASE_ESTIMATES.csv` contains exactly Phase 001 through Phase 120, once each.

Each row records:
- phase ID/title;
- estimate in developer-days;
- estimate confidence;
- exact hard predecessor;
- launch-critical vs post-launch classification;
- relative month window;
- workstream;
- named milestone if any;
- stop/pivot review if any;
- accepted/planned baseline status;
- Acceptance Weight Points.

Planned pre-launch total: **165 developer-days**.  
Post-launch total: **10 developer-days**.

Estimates are planning weights, not promises or recorded actuals. Completed Phase 001–008 retain estimates for baseline comparison; the project must not fabricate historical time spent.

## 5. Critical path and safe parallelism

The bible's phase gates create a sequential **acceptance critical path** through Phase 116.

Parallel-safe preparation is intentionally narrower:
- art references/inventory can prepare early, while final art waits on pipeline and art-bible gates;
- audio provenance/cue planning can prepare early, while final cue production waits for implemented events;
- writing outlines/terminology can prepare early, while final tutorials/events/store copy wait for owning mechanics;
- QA fixture design can prepare early, while execution waits for implementation;
- marketing research can prepare early, while title-dependent/public assets wait for clearance and gameplay evidence.

No preparatory work is allowed to masquerade as completion of a future phase.

## 6. Named milestones

The baseline reserves:

- Phase 030 — **Prototype**
- Phase 040 — **Vertical Slice**
- Phase 100 — **Demo**
- Phase 111 — **Alpha**
- Phase 112 — **Beta**
- Phase 114 — **Release Candidate**
- Phase 116 — **Launch**
- Phase 120 — Final project acceptance

These are relative gates, not calendar-date commitments.

## 7. Contingency

The accepted 75-day reserve is split into protected planning blocks:

- C1 foundation recovery: 8 days;
- C2 prototype/vertical-slice rework: 10 days;
- C3 content/art/throughput rework: 20 days;
- C4 reliability/demo recovery: 15 days;
- C5 release reserve: 22 days.

Total: **75 days**.

Unused reserve remains unused. C5 cannot be silently spent on optional early content. Reserve erosion triggers the Phase 005 scope process rather than hidden overtime or lower quality.

## 8. Stop-or-pivot reviews

Formal roadmap review points are fixed at:

- Phase 010 — preproduction go/no-go;
- Phase 030 — core-loop prototype;
- Phase 040 — combat vertical slice;
- Phase 070 — production throughput;
- Phase 100 — demo go/no-go;
- Phase 107 — feedback synthesis;
- Phase 112 — beta shipability;
- Phase 114 — release-candidate go/no-go.

Phase 009 owns detailed risk scoring and kill thresholds. Phase 008 only fixes where those decisions must occur and the allowable decision classes.

## 9. Accepted-work burndown

The dashboard uses **Acceptance Weight Points (AWP)**:

- four AWP per planned developer-day;
- total program: 700 AWP;
- pre-launch through Phase 116: 660 AWP;
- accepted baseline through Phase 008: 29 AWP.

Points burn **only when a phase closure is merged to main**. Hours spent, agents run, commits made, files created, or subjective percent-complete claims earn zero partial burndown credit.

This deliberately measures accepted outcomes rather than activity.

## 10. Verification evidence

Before publication, the generated roadmap model was checked with the Phase 008 verifier:

```text
PASS: 388 Phase 008 roadmap checks; 120 phases; 165 prelaunch planned days; 75 contingency days
PASS: invalid reserve case rejected
```

After publication, every Phase 008 file was fetched back from GitHub and the committed CSV/JSON were independently checked for:

- exactly 120 rows;
- Phase 001–120 sequence;
- exact predecessor chain;
- 165 pre-launch planned days;
- 10 post-launch days;
- 700 AWP total;
- 75 contingency days;
- 240 productive pre-launch capacity days;
- no agent capacity multiplier;
- prototype/vertical-slice/demo/alpha/beta/launch milestones;
- parallel-safe preparation section;
- stop/pivot review section;
- accepted-work burndown rule.

All checks passed.

The GitHub compare from the Phase 007 closure to the Phase 008 implementation showed one fast-forward commit containing only eight newly added `docs/phase-008/` files.

## 11. Prior-gate preservation

No Phase 001–007 file was changed in the implementation commit.

No gameplay runtime, Godot scene, Blender production asset, public-release date, new content family, platform, online feature, or external dependency was introduced.

The roadmap schedules accepted scope; it does not widen it.

## 12. Known non-blocking limitations

- Developer-day estimates remain uncertain until implementation throughput exists.
- Relative month windows are not booked dates.
- Phase 009 has not yet supplied detailed probability/impact/kill thresholds.
- Personal living runway remains private/unset in Phase 005.
- Final public-title clearance remains open.
- Runtime performance, art throughput, balance, and public demand remain future evidence gates.

## 13. Safe entry condition for Phase 009

Phase 009 — Risk register and kill criteria — may begin from this green baseline.

It must:
1. score risks by probability, impact, and detectability;
2. define prototype replayability/readability/tutorial thresholds;
3. define performance red lines and production-throughput targets;
4. preserve Phase 005 budget limits;
5. assign mitigation owners;
6. set formal kill/pivot/scope-reduction triggers at the Phase 008 review points;
7. avoid converting planning assumptions into invented evidence.

**Phase 008 is closed.**
