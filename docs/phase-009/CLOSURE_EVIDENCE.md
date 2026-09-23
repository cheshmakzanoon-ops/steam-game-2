# Phase 009 — Closure evidence

**Project:** Charterwake: The Last Relay — provisional working title  
**Phase:** 009 — Risk register and kill criteria  
**Status:** COMPLETE / GREEN for preproduction risk-control baseline  
**Date:** 2026-09-23  
**Entry commit:** `cbb41ef5c62c926bd203270da6666dc205b1b504`  
**Implementation commit:** `6641bd6b4551c531139350461cf171cad852401d`  
**Target branch:** `main`

This closes the Phase 009 risk-control gate. It defines precommitted evidence thresholds and escalation rules; it does **not** claim that future prototypes, performance builds, demos, beta builds, title searches, or commercial results already satisfy them.

## 1. Required deliverables

- `LIVING_RISK_REGISTER.csv` — 26 scored commercial, design, technical, art, schedule, budget, accessibility, localization, research, brand, and operations risks.
- `RISK_SCORING_AND_POLICY.md` — probability / impact / detectability scales, priority bands, statuses, ownership, and review behavior.
- `KILL_CRITERIA.md` — prototype replayability, readability/tutorial, fair-loss, performance, art-throughput, schedule/cash, demo, feedback, beta, and RC thresholds.
- `MITIGATION_SCHEDULE.md` — owner and evidence windows through Phases 009–120.
- `REVIEW_CADENCE.md` — phase, weekly, monthly, formal stop/pivot, and incident reviews.
- `RISK_MODEL.json` — machine-readable thresholds.
- `verify_risks.py` — offline consistency checker.
- package README.

## 2. Bible work-package acceptance

| Required Phase 009 item | Evidence | Result |
| --- | --- | --- |
| Score probability, impact, detectability | CSV + scoring policy | PASS |
| Prototype replayability threshold | KILL_CRITERIA + RISK_MODEL | PASS |
| Readability/tutorial thresholds | KILL_CRITERIA + RISK_MODEL | PASS |
| Performance red lines | KILL_CRITERIA + RISK_MODEL | PASS |
| Content-production throughput target | KILL_CRITERIA | PASS |
| Budget limits | KILL_CRITERIA + Phase 005 references | PASS |
| Mitigation owners | Living register + mitigation schedule | PASS |
| Kill/pivot/scope-reduction triggers | KILL_CRITERIA + review cadence | PASS |

## 3. Risk-scoring baseline

Scoring is 1–5 for:

- probability;
- impact;
- detectability, where a higher number means harder to discover early.

Priority score:

`probability × impact × detectability`

Bands:

- CRITICAL: 60–125
- HIGH: 40–59
- MEDIUM: 20–39
- LOW: 1–19

The implementation register currently contains:

- **5 CRITICAL**
- **7 HIGH**
- **10 MEDIUM**
- **4 LOW**

The five current CRITICAL risks are:

- R002 — Command scarcity becomes busywork/obvious toggling;
- R003 — one-board readability collapses;
- R012 — losses are opaque/unfair;
- R015 — UI/animation becomes authoritative simulation state;
- R016 — save/replay determinism diverges or arrives too late.

Risk score is a prioritization aid. A hard blocker overrides the score.

## 4. Prototype / readability / fairness thresholds

### Phase 030 prototype

Minimum stable-build cohort: **8 fresh players**.

GO baseline:
- 6/8 explain scarce Command + routing/priority thesis;
- 6/8 identify Keep + immediate threat in the first-look exercise;
- 5/8 immediately retry or state a materially different retry plan;
- zero input-path failures that prevent the representative planning decision.

Core-pivot review is forced if the defined thresholds remain materially below baseline after two bounded rework cycles using no more than C2's 10-day reserve.

### Readability/tutorial

Minimum cohort: **10 fresh players**.

Required:
- 8/10 first-look comprehension;
- 8/10 first-Watch completion without facilitator intervention beyond allowed tutorial text;
- 8/10 explain an inactive structure;
- median urgent-state scan ≤2 seconds after onboarding;
- zero critical accessibility/input failures.

### Fair loss

At least 8 representative defeat cases:
- each ≥14/16 on the Phase 003 rubric;
- no zero category;
- ≥7/8 player explanations substantially match the authoritative causal chain.

Any preview/simulation contradiction, hidden decisive boss rule, or save/reload outcome divergence is an immediate blocker.

These are future evidence thresholds, not present playtest results.

## 5. Performance red lines

Phase 005 targets remain the owning pass criteria.

Phase 009 adds escalation/redesign red lines after two focused optimization passes on the defined representative exported build/reference hardware:

- sustained gameplay below 30 fps;
- graph p95 ≥2 ms;
- combat tick p95 ≥4 ms;
- scene transition p95 ≥6 seconds without justified loading mode;
- process memory >2,200 MB;
- installed build >2,000 MB;
- any authoritative outcome change caused by render rate, 1x/2x/4x speed, or skip.

Values between target and red line remain AMBER and do not automatically satisfy the later owning phase.

## 6. Production-throughput red line

At Phase 070:

- GREEN: forecast accepted Phase 071–080 work within 15 planned developer-days;
- AMBER: >15 and ≤20;
- RED: >20 after two pipeline/style iterations, or clean batch regeneration cannot be reproduced.

Response order is simplify style/animation complexity, cut optional decoration under the Phase 005 ladder, then rebaseline. Readability/provenance cannot be traded away to hit throughput.

## 7. Schedule and budget

Schedule:
- ≥20% pre-launch reserve: GREEN;
- >0 and <20%: AMBER + mandatory scope review;
- beyond productive capacity or >18 months after cuts: RED.

External project cash uses the owner-selected Phase 005 scenario:
- >90% committed too early: AMBER;
- projected above selected ceiling: RED until funding/scope disposition.

Personal living-runway numbers remain private/unset unless the owner chooses otherwise. Phase 010 requires an explicit owner disposition for production mode rather than treating missing private data as zero or sufficient.

## 8. Formal stop/pivot reviews

Phase 009 supplies the criteria used at the Phase 008 review points:

- Phase 010 — preproduction go/no-go;
- Phase 030 — core-loop prototype;
- Phase 040 — combat vertical slice;
- Phase 070 — production throughput;
- Phase 100 — demo go/no-go;
- Phase 107 — feedback synthesis;
- Phase 112 — beta shipability;
- Phase 114 — release candidate.

Schedule inconvenience cannot suppress or weaken a review.

## 9. Demo and release blockers

Phase 100 demo minimum includes:
- fresh-player cohort ≥12;
- ≥10/12 complete the intended demo arc without facilitator help for core rules;
- ≥8/12 state a specific different build/routing retry plan;
- fairness/readability/accessibility gates green;
- no P0/P1 crash, save corruption, deterministic replay, or required-input blocker.

Beta/RC hard blockers include:
- reproducible save corruption/migration loss;
- deterministic speed/replay divergence;
- inaccessible required controller/keyboard path;
- unresolved license/provenance blocker;
- known supported-platform crash/data-loss issue;
- Steam-absent/offline failure;
- launch build outside accepted hard target without approved change;
- no final public-title risk disposition.

## 10. Mitigation and review cadence

Every risk has:
- a named owner role;
- an evidence gate;
- mitigation;
- formal review phase.

Reviews occur:
- at every phase closure;
- weekly for CRITICAL/HIGH/BLOCKING/new risks;
- monthly for the full register/scope/cash/reserve picture;
- at all eight formal stop/pivot gates;
- immediately for defined critical incidents such as save corruption, deterministic divergence, rights conflict, required-input blocker, severe cash/scope overrun, or supported-platform critical crash.

A risk closes only with evidence. Stable recurrent risks may remain WATCH through launch.

## 11. Verification evidence

After the implementation commit was moved to `main`, all eight Phase 009 files were fetched back from GitHub and independently parsed.

Committed-content checks passed for:

- exactly 26 ordered risk IDs R001–R026;
- every probability/impact/detectability score in range 1–5;
- every priority score equals probability × impact × detectability;
- every risk band matches the defined score thresholds;
- every row has an owner and evidence gate;
- JSON risk-ID list matches the CSV;
- prototype/readability/fair-loss thresholds;
- Phase 005 performance target values;
- performance red lines;
- 15/20-day art-throughput thresholds;
- exact eight formal review phases;
- prototype/readability/performance/budget sections in the kill-criteria document;
- mitigation owner policy;
- phase/weekly/formal review cadence;
- verifier presence.

The GitHub compare from the Phase 008 closure to the Phase 009 implementation shows one fast-forward commit containing only eight newly added `docs/phase-009/` files.

The package's offline verifier can be run as:

```sh
python3 -S docs/phase-009/verify_risks.py --self-test
```

It checks register/model consistency and contains an impossible-threshold negative test. The closure evidence above reports the independent committed-content validation actually performed in this session rather than pretending a future runtime test exists.

## 12. Prior-gate preservation

No Phase 001–008 file was modified in the implementation commit.

No Godot gameplay runtime, Blender production asset, extra content family, extra mode/biome, online dependency, release date, or external purchase was introduced.

The Phase 001 register remains historical evidence; the Phase 009 register becomes the living operational risk register.

## 13. Known non-blocking future evidence

Still unmeasured until the owning phases:
- fresh-player comprehension/retry behavior;
- fair-loss cohorts;
- runtime CPU/GPU/memory/install measurements;
- art production throughput;
- demo completion/retry behavior;
- market feedback;
- final title clearance;
- beta/RC defect state.

The absence of future measurements is not recorded as a pass.

## 14. Safe entry condition for Phase 010

Phase 010 — Preproduction approval gate — may begin from this green baseline.

It must review Phases 001–009 as a complete case and issue an explicit GO / REVISE / NO-GO decision before repository/engine construction begins.

It must specifically challenge:
1. the core Command-network hook;
2. solo scope/capacity and reserve;
3. Blender-to-Godot feasibility assumptions;
4. offline/no-service dependency;
5. platform/price assumptions;
6. critical unknowns and current CRITICAL risks;
7. public-name disposition appropriate to an internal preproduction project.

**Phase 009 is closed.**
