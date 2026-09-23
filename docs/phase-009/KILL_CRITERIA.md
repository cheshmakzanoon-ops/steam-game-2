# Phase 009 — Kill, pivot, and scope-reduction criteria

**Status:** PRECOMMITTED DECISION THRESHOLDS  
**Date:** 2026-09-23

These thresholds define evidence that forces a review. They are not claims that current or future builds already pass.

A **RED trigger** means later acceptance stops until the project chooses and documents one of: fix, cut, pivot, delay, or stop. It cannot be waived by weakening the measurement after seeing the result.

---

## 1. Phase 010 — Preproduction go/no-go

### GO requirements

- Phases 001–009 green and reproducible.
- No unresolved contradiction among charter, Core Rules, scope ceilings, GDD, roadmap, and risk model.
- No mandatory online/runtime service introduced.
- Phase 005 model still shows at least 20% unallocated pre-launch reserve.
- External project-cost scenario is explicitly chosen or all external spending remains deferred.
- Personal living runway may remain private, but the owner must make an explicit **runway reviewed / production mode chosen** decision before assuming full-time 12–15 month execution.
- Charterwake may remain provisional if the project remains internal and rename-safe.

### REVISE / NO-GO

- Any critical contradiction cannot be resolved without widening scope beyond the approved ceiling.
- The roadmap forecast exceeds the 18-month safety ceiling after applying the cut ladder.
- Required offline operation becomes impossible.
- Rights/license risk makes the planned product unshippable and no rename/replacement path exists.

---

## 2. Phase 030 — Core-loop prototype replayability

Use **one stable prototype build** and a minimum of **8 fresh players** who have not been coached on the answer.

### GO threshold

At least:

- **6/8** correctly explain in their own words that Command is scarce and that routing/priorities decide what operates.
- **6/8** identify the Keep and the immediate threatened direction after the Phase 003 ten-second view test.
- **5/8** either voluntarily choose another attempt immediately or can state a materially different routing/priority plan they want to try.
- No participant is unable to complete the representative planning fixture because required information is inaccessible by the input path being tested.

### PIVOT CORE trigger

After **two bounded rework cycles** using no more than the Phase 008 C2 prototype/vertical-slice reserve:

- fewer than 5/8 understand the Command-routing thesis, **or**
- fewer than 4/8 express concrete retry intent, **or**
- 3 or more of 8 independently describe the central decision as obvious repetitive toggling rather than planning.

Result: stop content expansion and redesign the core interaction before proceeding.

### STOP trigger

If no scoped core-pivot hypothesis can preserve the one-board / scarce-Command product promise inside the existing 18-month and content ceilings, bring the project to a formal stop decision rather than building more content around an unproven hook.

---

## 3. Readability and tutorial thresholds

Fresh-player cohort minimum: **10** on the same representative build/configuration.

Before the public demo gate:

- **8/10** identify Keep, scarce Command, powered/unpowered distinction, and imminent threat without facilitator explanation after the defined first-look exercise.
- **8/10** complete the first Watch without facilitator intervention beyond allowed tutorial text.
- **8/10** can state why at least one inactive structure is inactive.
- Median time to identify the highest-priority urgent board problem in a prepared scan fixture is **≤2 seconds** after onboarding.
- **0** critical failures where controller/keyboard focus or color dependence prevents the required decision.

### RED

Two consecutive measured cohorts below any 8/10 comprehension threshold after targeted UX revision, or any unresolved critical accessibility blocker at the owning gate.

Action: simplify information/state presentation before adding content. Do not add longer tutorial prose as the first fix for an unreadable board.

---

## 4. Fair-loss threshold

Before Phase 040 closes and again before demo acceptance:

- at least **8 representative defeat fixtures/sessions** scored using the Phase 003 rubric;
- every shipping-quality case scores **≥14/16**;
- no category scores zero;
- player-stated root cause substantially matches the authoritative event chain in at least **7/8** cases.

Any preview/simulation contradiction, hidden decisive boss rule, or save/reload outcome divergence is an immediate blocker independent of aggregate score.

---

## 5. Performance red lines

Phase 005 **targets remain the pass criteria**:
- 60 fps baseline;
- 30 fps playable fallback;
- process memory ≤1,900 MB decimal;
- install ≤1,800 MB;
- texture residency ≤512 MB;
- graph rebuild <1 ms;
- normal full combat tick <2 ms;
- scene transition <3 s.

Phase 009 adds **red lines** for redesign/escalation. On the defined reference/minimum hardware and representative exported build, after two focused optimization passes:

- sustained gameplay cannot hold **30 fps** → RED;
- graph-rebuild p95 **≥2 ms** → RED;
- combat-tick p95 **≥4 ms** → RED;
- scene-transition p95 **≥6 s** without a justified loading mode → RED;
- process memory **>2,200 MB** or installed build **>2,000 MB** → RED;
- deterministic outcome changes with render rate, 1x/2x/4x speed, or skip → BLOCKER.

A value between target and red line is AMBER and still cannot pass the final owning gate until the Phase 005 target is met or formally changed with evidence.

---

## 6. Art/content production throughput

At the Phase 070 throughput review, use actual accepted-source throughput from the calibrated Blender/Godot pipeline.

### GREEN

Forecast Phases 071–080 inside the accepted **15 planned developer-days** while preserving the Phase 005 art/audio/text ceilings and reproducible-source requirements.

### AMBER

Forecast is **>15 and ≤20 developer-days**. Use style simplification, shared modular components, and C3 contingency only with explicit review.

### RED / SCOPE REDUCTION

After two pipeline/style iterations, forecast remains **>20 developer-days** for the accepted Phase 071–080 work, or clean batch regeneration cannot be reproduced.

Action order:
1. simplify material/animation complexity;
2. reduce optional decorative variants/marketing compositions;
3. use Phase 005 cut ladder;
4. only then rebaseline schedule/budget.

Do not lower readability, provenance, or functional state coverage to hit throughput.

---

## 7. Budget and schedule limits

### Schedule

- ≥20% pre-launch reserve: GREEN.
- >0% and <20% reserve: AMBER; mandatory scope review.
- forecast beyond 100% productive capacity or beyond **18 months after cuts**: RED.
- C5 release reserve may not fund optional early content.

### External project cash

Use the explicitly selected Phase 005 scenario.

- projected external cost inside chosen ceiling: GREEN;
- >90% of chosen ceiling before the associated work is substantially contracted/completed: AMBER;
- projected cost above the chosen ceiling: RED until funding or scope disposition.

No contract is signed on the assumption that missing personal living-runway data equals zero.

---

## 8. Phase 100 — Demo go/no-go

Do not publish a demo merely to meet an event date.

Minimum evidence:
- Phase 003/040 fairness/readability thresholds green;
- demo is the accepted one-doctrine bounded subset;
- no P0/P1 crash, save-corruption, input-accessibility, or deterministic-replay blocker;
- representative controller/keyboard flows complete;
- target performance/install envelope green for demo configuration;
- fresh-player cohort minimum **12**, with at least **10/12** able to complete the intended demo arc without facilitator intervention for core rules;
- at least **8/12** can state a specific different build/routing plan they would try in another run.

If not met: HOLD. Missing a festival window is preferable to burning the project's public discovery opportunity with an unrepresentative build.

---

## 9. Phase 107 — Market/feedback pivot review

Community/playtest signals are qualitative, not population forecasts.

PIVOT/CUT review if:
- repeated external feedback primarily describes the product by a reference game's signature mechanic despite originality work;
- players understand rules but do not express differentiated build/routing stories;
- demo feedback repeatedly identifies the same non-content core friction and adding more content does not address it;
- current full-launch forecast no longer fits scope/cash/schedule ceilings.

Do not use wishlists, review-count heuristics, or publisher-backed breakout comparisons as guaranteed unit-sales thresholds.

---

## 10. Release/beta/RC hard blockers

At Phases 112/114, any of these blocks progression:
- reproducible save corruption or migration loss;
- deterministic replay/speed divergence;
- required controller or keyboard path inaccessible;
- unresolved license/provenance blocker;
- known crash/data-loss issue on supported launch platform;
- required Steam-absent/offline flow fails;
- launch build exceeds accepted hard target with no approved change;
- final public title lacks owner risk disposition.

A blocker is not downgraded because the release date is inconvenient.
