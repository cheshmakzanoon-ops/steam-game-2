# Phase 003 — Fair-Loss Rubric

**Project:** Charterwake: The Last Relay  
**Status:** MANDATORY PLAYER-TRUST STANDARD  
**Date:** 2026-09-22

A difficult game may defeat the player often. Charterwake may not confuse opacity with difficulty.

A loss is fair only when the player had enough information and agency to form a plan, the rules resolved consistently, and the decisive causal chain can be understood afterward.

---

## 1. Hard fair-loss requirements

A loss must satisfy **all** of the following unless the player deliberately accepted a clearly labeled unknown-risk event:

### F1 — Threat legibility

The decisive major threat, target rule, arrival direction/timing and relevant special rule were visible early enough to affect planning.

### F2 — Actionable agency

At least one materially different player decision existed before the decisive failure. "You should have clicked faster" does not count.

### F3 — State legibility

The player could inspect which structures were connected, powered, unpowered, disabled or isolated before commitment.

### F4 — Rule consistency

The simulation resolved according to the same authoritative rules shown in previews/tooltips/logs. Presentation timing did not change the outcome.

### F5 — Controlled randomness

No hidden random roll erased a reasonable plan in a way the player could neither price in nor respond to. Allowed variability must stay inside communicated bounds.

### F6 — Causal explanation

After the loss, the game can identify a useful chain such as:

**forecast threat → vulnerable link / priority / resource choice → operation lost → breach/objective failure → Keep defeat**

### F7 — Input fairness

The loss was not caused by inability to access information/action with controller, keyboard, UI scale, focus navigation or color perception.

### F8 — No retroactive gotcha

A critical boss or system rule was not introduced after the player made the last meaningful decision that could address it.

---

## 2. Fairness scorecard

For testing, score each category **0 / 1 / 2**:

- **0 = fail / unavailable**
- **1 = technically present but unclear or too late**
- **2 = clear, timely and actionable**

| Category | 0 | 1 | 2 |
|---|---|---|---|
| Forecast | Decisive threat hidden | Shown but too late/unclear | Clear before relevant planning |
| Agency | No meaningful alternative | Alternative existed but was obscure | Multiple understandable choices |
| Network state | Failure state hidden | Inspectable with friction | Obvious + inspectable |
| Consequence preview | Contradicted outcome | Partial/ambiguous | Matches authoritative resolution |
| Randomness | Hidden decisive RNG | Bounds unclear | Controlled/communicated |
| Causality | "You died" only | Partial clue | Decisive chain reconstructed |
| Input/accessibility | Access failure caused loss | Friction materially contributed | Equivalent access path |
| Recovery signal | No idea what to change | Generic advice | Player can name a different plan |

### Pass threshold

- No category may score **0** for a shipping-quality loss path.
- Total target: **14/16 or better**.
- A score below target requires a specific issue, owner and retest.

The total score never overrides a hard failure. A hidden boss rule is unfair even if every other category scores 2.

---

## 3. Normal loss case

A normal fair defeat should look like:

1. threat is forecast;
2. player inspects the board;
3. player knowingly prioritizes one need over another;
4. resolution follows shown rules;
5. damage compounds;
6. a lane/network/Keep condition fails;
7. post-run recap identifies the chain;
8. player can state what they would try differently.

Desired response:

> "I see why that failed."

---

## 4. Boundary cases

### Overloaded Command

Fair if:
- capacity/load and allocation order are visible;
- the affected structures are previewed;
- ties resolve deterministically;
- player can revise priorities before commitment.

Unfair if:
- a structure silently powers off;
- allocation order changes without explanation.

### Link severing

Fair if:
- vulnerable cut point is inspectable;
- damage behavior is known;
- recalculation follows the same graph rules.

Unfair if:
- links fail decoratively without authoritative feedback;
- presentation suggests a connection that simulation does not recognize.

### Resource shortage

Fair if:
- costs/conversions/order are inspectable;
- inability to pay is previewed;
- the game never creates hidden negative debt.

Unfair if:
- an automatic expenditure steals a resource without visible ordering.

### Boss rule

Fair if:
- rule is previewed before it can invalidate a plan;
- a safe/reduced earlier demonstration is used where required by the bible.

Unfair if:
- the boss reveals a build-invalidating immunity only after the player is locked in.

### Random offers

Fair if:
- randomness shapes options but agency tools exist as designed;
- a run is not effectively dead because one mandatory answer failed to appear.

Unfair if:
- repeated restart fishing is the rational response.

---

## 5. Recovery standard

A damaged but surviving run should present **meaningful recovery decisions**, not chores.

Good recovery:
- repair one critical point vs invest in a new route;
- accept lower economy to restore resilience;
- preserve a damaged structure because its topology remains valuable.

Bad recovery:
- click every damaged building one by one when all repairs are obviously correct;
- repeat the same maintenance action after every Watch;
- force the player through modal confirmations with no tradeoff.

---

## 6. Post-run explanation requirements

The final recap should eventually be able to surface:

- decisive Watch;
- decisive threat;
- relevant board/network state;
- Command/prioritization consequence;
- important resource shortfall if causal;
- first unrecovered breach/collapse;
- final run-ending event.

The recap must distinguish **root cause** from **last hit**.

"The boss dealt 6 damage" is not enough if the meaningful cause was that a cut point disabled two defenses three steps earlier.

---

## 7. Player-test questions

Immediately after defeat, ask without leading:

1. Why do you think you lost?
2. When did the run start going wrong?
3. What information did you wish you had earlier?
4. What would you change if you replayed the same situation?
5. Did anything happen that contradicted your expectation?
6. Was anything difficult to inspect or reach with your input method?

### Pass behavior

The player's explanation substantially matches the authoritative cause and names at least one actionable alternative.

### Red flag

The tester invents a false explanation because the real cause was invisible.

---

## 8. Defect severity

### BLOCKER

- hidden rule causes run loss;
- preview contradicts authoritative outcome;
- same saved/seeded state resolves differently due to presentation speed/timing;
- controller/focus path cannot reach a required decision;
- save/reload changes authoritative network outcome.

### HIGH

- causal recap points to the wrong root cause;
- state is technically inspectable but routinely missed;
- boss forecast is too late to matter;
- allowed random range is materially misleading.

### MEDIUM

- explanation exists but is cumbersome;
- post-run wording overemphasizes last hit;
- a non-critical state cue lacks redundancy.

Fair-loss defects are player-trust defects, not balance polish.
