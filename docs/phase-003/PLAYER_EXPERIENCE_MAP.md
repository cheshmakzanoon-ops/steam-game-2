# Phase 003 — Player Experience Map

**Project:** Charterwake: The Last Relay  
**Status:** APPROVED EXPERIENCE BASELINE  
**Date:** 2026-09-22  
**Scope:** Player understanding, decisions, emotion, feedback, recovery and post-run explanation. This document does not replace the Phase 004 core-rules lock.

---

## 1. Player promise

The player should feel like a **planner, cartographer and commander**, not an RTS operator.

The experience succeeds when the player can say:

> I could see the pressure coming. I could not power everything. I made a routing and priority plan, watched it resolve, understood the result, and immediately saw another plan I want to try.

The experience fails when the player instead says:

- I did not know what the game expected me to notice.
- I lost because a rule was hidden.
- I clicked constantly but made few meaningful decisions.
- I cannot tell which choice actually caused the failure.
- The correct play was obvious but tedious.
- I was waiting for random offers rather than shaping a plan.

---

## 2. First-ten-seconds comprehension goal

Within roughly the first ten seconds of an interactive run view, without opening a secondary management screen, a new player should be able to identify:

1. **The Keep** as the central asset that must survive.
2. **The board** as the complete strategic space rather than one viewport into a larger map.
3. **The command network** as visible links connecting structures back toward the Keep.
4. **Scarce Command** as the reason not everything can operate at once.
5. **Powered versus unpowered state** using more than color alone.
6. **The nearest meaningful threat/forecast direction** and where to inspect it.
7. **The next actionable planning area** without being forced into high-speed execution.

The player does **not** need to understand Resonance, doctrine optimization, advanced conversions, boss exceptions or every icon in the first ten seconds.

### First-ten-seconds acceptance test

Show a clean run view to a first-time tester for ten seconds, then hide it and ask:

- What are you protecting?
- What seems limited?
- What connects the buildings?
- Where does danger appear to be coming from?
- Does this look like a game about fast clicking or planning?

A pass does not require exact terminology. It requires the correct mental model.

---

## 3. First useful decision

The first meaningful decision must demonstrate the game's thesis, not a disposable tutorial action.

The player should face a **small, reversible planning tradeoff** in which visible forecast pressure makes two desirable uses of scarce Command compete. The player must be able to:

- inspect what will be powered;
- inspect what will remain unpowered;
- see the relevant forecast;
- make a priority/routing choice;
- preview the consequence;
- undo or revise while still in planning;
- commit only when satisfied.

The first useful decision should teach:

> "I am not deciding whether to click a thing. I am deciding what my kingdom is allowed to do before the threat arrives."

It must not be:

- a forced choice with only one reasonable answer;
- a hidden tutorial quiz;
- a cosmetic placement action;
- a rapid reaction test;
- a long text explanation before interaction.

---

## 4. Run-level experience map

| Run stage | Player should understand | Primary decision | Desired emotion | Required feedback | Failure/recovery expectation |
|---|---|---|---|---|---|
| First look | Board, Keep, network, Command scarcity, visible danger | Where to inspect first | Curiosity, orientation | Clear hierarchy; non-color state cues | No lethal surprise while basic model is still forming |
| Early planning | Power is allocated, not universal | Economy vs defense vs resilience | Productive tension | Preview of powered/unpowered state and consequences | Revision/undo available before commitment |
| First resolution | Plan produces deterministic consequences | Observe rather than micromanage | Anticipation | Concise ledger + readable Siege effects | Result matches preview/rules |
| Early aftermath | Damage/reward has causes | Repair, adapt, invest | Relief + learning | Causal summary; changed board state obvious | Recovery options visible where intended |
| Mid-run expansion | Topology creates combinations and vulnerabilities | Shape a build identity | Discovery, ownership | Synergies and cut points legible | Bad topology remains diagnosable |
| Pre-boss preparation | Future rule can reshape priorities | Commit to a counter-plan | Dread + confidence | Boss rule forecasted early enough to matter | No boss rule arrives as an untelegraphed gotcha |
| Boss resolution | Earlier choices are tested together | Observe plan under stress | High tension, spectacle | Strong but readable audiovisual hierarchy | Defeat chain reconstructable |
| Post-boss reset | Surviving creates a new strategic problem | Rebuild/re-route, not housekeeping | Release + renewed ambition | Damage/reward summarized quickly | Recovery does not become repetitive repair clicking |
| Late-run mastery | Player exploits learned interactions | Push a powerful but vulnerable plan | Mastery, greed, controlled risk | Preview scales to complex board state | Complexity must not hide state |
| Final preparation | Player understands what final test demands | Sacrifice/priority for final plan | Focus, dread | Forecast + whole-board consequence view | No late hidden rule invalidates build |
| Final resolution | Full run thesis is tested | Commitment already made | Spectacle, suspense | Clear decisive chain | Victory/defeat both explain why |
| Post-run | The run becomes a story | Choose retry/new approach | Reflection + desire to retry | Causal recap, build identity, pivotal moments | No vague "you lost" screen |

---

## 5. Emotional vocabulary

### Tension

Comes from **visible competing needs**, not hidden probability. Typical causes:

- insufficient Command for all desired functions;
- forecast pressure arriving from multiple directions;
- a valuable structure sitting behind a vulnerable cut point;
- a strong synergy that increases fragility elsewhere;
- choosing between immediate safety and compounding economy.

### Relief

Comes after a plan survives a meaningful test:

- a threatened lane holds;
- a redundant path prevents isolation;
- a sacrifice prevents wider collapse;
- a boss phase ends and the board becomes writable again.

Relief should create space to think. It should not immediately be replaced by a modal reward stack.

### Mastery

Occurs when the player deliberately predicts a system interaction before the game confirms it.

Examples:

- preserving power through redundant routing;
- intentionally leaving a lower-priority structure dormant;
- exploiting a doctrine rule to reshape a plan;
- predicting which structure will lose Command after damage;
- building a combination that is powerful because of topology, not merely stacked percentages.

### Spectacle

Spectacle is the **payoff of understood systems**. It should amplify a result the player can explain.

Good spectacle:
- a well-routed defense activates in sequence and erases a forecast threat;
- a resilient loop survives a severed link;
- a late-run combination produces an overwhelming but readable resolution.

Bad spectacle:
- visual noise that hides outcomes;
- random effects that appear stronger than the plan;
- long animations after the result is already known;
- presentation that prevents the player from seeing why the strategy worked.

---

## 6. Information hierarchy

At normal play scale, information priority is:

1. immediate threat and fatal risk;
2. Keep integrity / run-ending condition;
3. connectivity and Command allocation;
4. powered/unpowered/isolated/disabled state;
5. forecast consequence;
6. resources and costs;
7. synergy/detail;
8. flavor.

Lower-priority information must not visually compete with higher-priority state.

Tooltips explain. They do not rescue an unreadable board.

---

## 7. Input and accessibility experience

The emotional arc may not depend on pointer hover, fast reaction or color discrimination.

Required experience equivalence:

- pointer, keyboard and controller can reach the same strategic information;
- focus state is explicit;
- forecast and network state remain inspectable with UI scaling;
- powered/unpowered/danger states have shape/line/icon/pattern cues in addition to color;
- planning allows time to inspect before commitment;
- speed controls affect presentation time, not simulation outcome;
- skipping known resolution never removes access to the causal summary.

---

## 8. Undo, reload and recovery experience

Phase 003 does not lock final implementation details, but it locks the player promise:

### Undo

During a reversible planning context, the player must be able to correct an input mistake without losing the strategic state they were reasoning about. Previewed consequences must update with the restored state.

### Reload

Reloading the same saved planning state must not produce a different authoritative strategic state merely because presentation/input timing differs.

### Failure

When a run fails, the game must surface the decisive causal chain at a useful level: threat → board/network condition → lost/disabled operation → breach/objective failure.

### Recovery

Recovery mechanics may create a meaningful tradeoff, but they may not become repetitive maintenance whose correct answer is obvious.

---

## 9. Desired post-run conversation

The product should generate conversations like:

- "I should have kept a second route to that side."
- "I powered the economy one Watch too long and entered the boss underprepared."
- "That doctrine completely changed how I shaped the board."
- "I knew the link was vulnerable and gambled anyway."
- "My loop survived the break and the whole defense stayed online."
- "I want to retry the same idea but change the priority order."

Conversations we should **not** normalize:

- "The game never told me that."
- "There was nothing I could have done."
- "I guess I needed a lucky roll."
- "I lost because the controller could not reach that information."
- "I spent five minutes clicking repairs that were obviously correct."
- "I have no idea why that structure shut off."

---

## 10. Phase 004 handoff constraints

Phase 004 may lock rules only if they preserve this experience baseline.

When two technically valid rule designs exist, prefer the one that:

1. makes cause and effect easier to inspect;
2. creates a real priority/routing decision;
3. reduces repetitive input;
4. keeps the full board readable;
5. allows deterministic explanation;
6. preserves short-run pacing.
