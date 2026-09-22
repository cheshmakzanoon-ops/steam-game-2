# Phase 003 — Representative Player Stories and Design Requirements

**Project:** Charterwake: The Last Relay  
**Status:** APPROVED PLAYER-STORY SET  
**Date:** 2026-09-22

These are behavior stories, not personas based on demographic assumptions. Each story describes a successful product experience and converts it into testable design requirements.

---

# Story 1 — "I understood the game before I knew the vocabulary"

## Story

A first-time player enters Watch 1. They immediately identify the Keep, see a small connected settlement, notice that some structures are active while others are not, and see pressure approaching from an edge.

They do not yet know the formal meaning of every icon. They do understand that **the network carries scarce authority and they must choose what matters now**.

They inspect two plausible priorities, preview the result, revise once, then commit. During resolution, they watch the plan behave as expected.

Their reaction is not "I finished the tutorial." It is:

> "Oh, I can't run everything. I have to decide what stays online."

## Design requirements

**PS1-R1** — First-run main view exposes Keep, board boundary, network, Command state and forecast without opening a management screen.  
**PS1-R2** — Powered/unpowered state uses redundant visual cues.  
**PS1-R3** — First meaningful choice contains at least two defensible options.  
**PS1-R4** — Planning choice is reversible before commitment.  
**PS1-R5** — First resolution is short enough that cause/effect remains in working memory.  
**PS1-R6** — Tutorial text cannot block interaction until a long reading sequence is complete.  
**PS1-R7** — Keyboard/controller focus exposes the same information needed to make the first choice.

### Validation

A new tester can describe the core scarcity in their own words after Watch 1.

---

# Story 2 — "I lost and immediately knew the retry"

## Story

A player builds a strong-looking branch toward one threatened side. They see that one connection is a vulnerable cut point but spend scarce Command elsewhere rather than adding resilience.

During Siege, the link is severed under a rule that was forecast. Two downstream structures become isolated. The lane collapses.

The player loses later, but the post-run explanation traces the failure back to the cut point rather than only reporting the final hit.

Their reaction:

> "I gambled on one route. Next time I either keep redundancy or lower that side's priority before the break."

## Design requirements

**PS2-R1** — Vulnerable disconnection points are inspectable before commitment.  
**PS2-R2** — Link damage/recalculation uses the same authoritative graph rule in preview, simulation and recap.  
**PS2-R3** — Isolation transition is visually obvious without pausing to read a log.  
**PS2-R4** — Post-run recap distinguishes root cause from final damage.  
**PS2-R5** — Same saved state/seed cannot produce a different topology result at different presentation speeds.  
**PS2-R6** — A defeat caused by network failure identifies at least one actionable earlier decision.

### Validation

After defeat, the tester's explanation matches the recorded authoritative causal chain.

---

# Story 3 — "My build did something spectacular because I understood it"

## Story

By Act III, a player has deliberately shaped a network around a doctrine and several complementary structures. The build is powerful, but it is not a pile of opaque percentage bonuses.

The player knows why the combination works. They forecast a large assault, shift priorities, preserve the key route and commit.

The Siege produces the run's biggest visual payoff. The player can still track what activated and why.

Their reaction:

> "I built that. I knew the chain was going to fire."

## Design requirements

**PS3-R1** — Late-run synergy feedback identifies participating structures/circuits rather than only emitting large numbers.  
**PS3-R2** — Spectacle layers must not obscure critical network or threat state.  
**PS3-R3** — Build-defining upgrades favor relationships, topology, timing, targeting or conversion over flat-stat accumulation.  
**PS3-R4** — Mature builds remain inspectable at normal gameplay scale.  
**PS3-R5** — At least one Act III beat allows an understood powerful build to visibly pay off before final compression.  
**PS3-R6** — Speed-up/skip produces the same authoritative outcome and retains a causal summary.

### Validation

The tester can explain the combination before or immediately after it resolves.

---

# Story 4 — "I could play the strategy, not fight the interface"

## Story

A player completes planning with a controller at a larger UI scale. They do not rely on hover. They can move focus through board cells and relevant UI, inspect threat details, tell powered from unpowered without color alone, and confirm the same decision a pointer user could.

When pressure rises, difficulty comes from tradeoffs—not from racing the focus cursor.

Their reaction:

> "I had time to think. I wasn't missing information because of the input method."

## Design requirements

**PS4-R1** — All required strategic inspection is reachable without hover.  
**PS4-R2** — Focus order is explicit, bounded and recoverable.  
**PS4-R3** — Critical states use icon/shape/line/pattern in addition to color.  
**PS4-R4** — UI scaling does not hide the forecast, Command state or commitment controls.  
**PS4-R5** — Planning has no reaction-speed requirement.  
**PS4-R6** — A controller-only path can complete every phase transition in a run.  
**PS4-R7** — Losing due to an inaccessible focus path is a blocker defect.

### Validation

Controller-only and keyboard-only testers can complete the same representative planning fixtures as pointer users.

---

# Story 5 — "The run ended, but I have a story and another plan"

## Story

An experienced player reaches the final boss after a 40-ish-minute run. They have survived one boss cleanly, barely recovered from another, and deliberately accepted risk to keep an aggressive build alive.

The final forecast is clear. They make a painful sacrifice in priorities. They either win spectacularly or lose for a reason the recap can explain.

The run-end screen does not bury them in account progression or generic XP. It emphasizes what their build became, where the decisive turn occurred, and what new sideways possibility exists.

Their reaction:

> "That run became its own story. I want another one with a different doctrine."

## Design requirements

**PS5-R1** — The 15-Watch curve contains tension, release, mastery and spectacle rather than constant escalation.  
**PS5-R2** — Bosses occur at Watches 5/10/15 and test previously taught concepts.  
**PS5-R3** — Normal victory remains targeted at 35–50 minutes.  
**PS5-R4** — Post-boss recovery is strategic, not housekeeping.  
**PS5-R5** — Post-run screen surfaces build identity, decisive chain and actionable reflection.  
**PS5-R6** — Meta-progression emphasizes sideways possibilities rather than universal stat compensation.  
**PS5-R7** — Retry/new-run flow is fast enough that story panels do not become friction.

### Validation

Immediately after a run, the tester can recount at least one pivotal decision and state a different plan they want to try.

---

# Cross-story design requirements

These requirements are mandatory consequences of all five stories:

**XR1 — One authoritative calculation.** Gameplay, preview, tooltip/log and recap may not independently reimplement the same rule.  
**XR2 — Information before commitment.** Major consequences are inspectable while the decision is still reversible.  
**XR3 — No presentation authority.** Animation/UI state may not determine simulation outcome.  
**XR4 — No mandatory micro.** Repeated actions require strategic meaning or should be automated.  
**XR5 — Retryable failure.** Defeat should reveal a new plan, not demand grind before fairness.  
**XR6 — Accessibility parity.** Required information/actions must remain available across supported input modes and non-color cues.  
**XR7 — Scope discipline.** If a story cannot be satisfied without adding a new major subsystem beyond the Phase 001 ceiling, redesign the interaction before expanding scope.  
**XR8 — Originality.** All player-facing solutions still pass Phase 002 originality and licensing gates.

---

# Desired post-run conversation test

A successful external playtest should naturally produce at least one statement in these categories:

- **routing reflection:** "I should have connected that differently";
- **priority reflection:** "I powered the wrong thing at the wrong time";
- **forecast reflection:** "I saw it coming but prepared for the wrong consequence";
- **build identity:** "My doctrine/build wanted me to...";
- **retry intent:** "Next run I want to try...".

If conversation instead centers on hidden rules, lucky rolls, interface friction or unexplained shutdowns, the experience baseline is not met.
