# Phase 009 — Risk scoring and policy

**Status:** LIVING PREPRODUCTION RISK SYSTEM  
**Date:** 2026-09-23

Phase 001 identified the initial risk set. Phase 009 replaces ad-hoc prioritization with a scored, reviewable living register. It does **not** erase Phase 001 history.

## Score scales

Each risk uses three integer scores from 1 to 5.

### Probability

1. Rare under current plan  
2. Unlikely but plausible  
3. Material possibility  
4. Likely without active mitigation  
5. Already occurring / near certain

### Impact

1. Local inconvenience  
2. Bounded rework  
3. Milestone-level quality/schedule damage  
4. Major scope/commercial/release damage  
5. Product viability, player trust, or launch-blocking damage

### Detectability

Higher means harder to discover early.

1. Automatically or immediately visible  
2. Usually visible in ordinary review  
3. Requires targeted fixture/playtest/profile  
4. Often appears late without dedicated evidence  
5. Can remain hidden until public/release conditions

### Priority score

`probability × impact × detectability`.

Bands:

- **CRITICAL:** 60–125
- **HIGH:** 40–59
- **MEDIUM:** 20–39
- **LOW:** 1–19

The score prioritizes attention; it never overrides a hard kill/red-line criterion. A LOW legal or save risk can still block a gate when its hard condition occurs.

## Statuses

Allowed register status:

- OPEN
- MITIGATING
- WATCH
- BLOCKING
- CLOSED
- ACCEPTED_BY_OWNER

“Closed” requires evidence, not optimism. “Accepted by owner” requires an explicit decision and does not permit violating a release blocker, law/license, save-safety contract, accessibility gate, or platform requirement.

## Review behavior

Every review:
1. verify evidence freshness;
2. rescore probability/impact/detectability if evidence changed;
3. record new risks rather than hiding them inside an old row;
4. attach mitigation owner and next evidence gate;
5. escalate any kill/red-line trigger immediately into the relevant stop/pivot review;
6. never reduce a score solely because the schedule is uncomfortable.

## Risk ownership

The project owner owns product, scope, commercial, schedule, budget, and public-name decisions.

Engineering owns deterministic runtime/save/performance/dependency mitigations.

Design/UX owns Command quality, readability, pacing, fair-loss, doctrine/build diversity.

Art/Tools owns Blender pipeline, source reproducibility, art throughput.

QA/research owns fixture quality, external-session evidence, cohort notes, and release-gate reproduction.

One person can hold several roles in a solo project, but the role must still be named so responsibilities do not disappear.
