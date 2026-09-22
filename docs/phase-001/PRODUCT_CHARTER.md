# Phase 001 — Product Charter

**Project:** Signalhold: The Last Relay  
**Phase:** 001 — Research traceability and project charter  
**Status:** APPROVED BASELINE  
**Date:** 2026-09-22  
**Decision owner:** Project owner / repository owner  
**Approval basis:** Direct project-owner instruction to execute Phase 001 and publish it to the repository.  
**Controlling sources:**  
1. *STEAM GAME NUMBER 2 — Master Production Prompt and Project Bible* (authoritative design/production specification).  
2. *Market-Validated 2D Strategy Game Opportunity for a Solo Steam Developer* (market-research source used to derive the concept).

---

## 1. Product decision

Signalhold is a compact one-board kingdom/base-building strategy roguelite in which the player builds a tiny frontier kingdom on a **9×9 charter board** and routes a visible command network through buildings with directional signal ports.

The player never has enough Command to power every desirable structure simultaneously. Planning therefore centers on **what receives authority now**, rather than on repetitive worker control or unit micromanagement. Threats are substantially telegraphed before commitment. Powered economy and defenses then resolve automatically and deterministically enough that the player can understand why a plan succeeded or failed.

### One-sentence positioning

> **A one-board strategy roguelite where every major threat is visible, but your physical command network can never power everything at once.**

### Player-facing promise

A run should make the player feel like a planner, cartographer, and commander who wins by reading the entire board, routing scarce Command intelligently, creating structural synergies, and adapting to forecast pressure—not by clicking faster or gambling on hidden outcomes.

---

## 2. Commercial hypothesis

| Item | Phase 001 baseline |
|---|---|
| Primary storefront | Steam |
| Primary launch OS | Windows |
| Additional verification | Linux and Steam Deck before launch |
| Business model | Premium one-time purchase |
| Launch-price hypothesis | USD $14.99 |
| Target run length | 35–50 minutes |
| Production target | 12–15 months full-time |
| Hard schedule ceiling | 18 months |
| Online dependency | None |
| Multiplayer | Out of launch scope |
| Live service | Out of launch scope |
| Mandatory account | None |
| Public-demo strategy | A polished demo only after the core loop is credible |

The price is a hypothesis, not a promise. It must be revalidated against the market before store publication without changing the game's product pillars merely to match competitors.

---

## 3. Toolchain pin

The project bible requires exact versions to be pinned at project start.

- **Godot:** 4.7.2-stable
- **Blender:** 4.5.14 LTS

Godot 4.7.2 is the stable 4.x production baseline. Blender 4.5.14 LTS keeps this project inside the bible's required Blender 4.x line and an actively supported LTS branch.

Changing either version requires an architecture decision record containing: reason, migration risk, rollback path, export/import compatibility evidence, and validation results.

---

## 4. Audience

### Primary audience

Players of compact strategy and strategy-roguelite games such as **9 Kings, The King is Watching, Thronefall, Into the Breach, Shogun Showdown**, and lighter automation titles who enjoy:

- planning and synergy discovery;
- a readable whole-board state;
- short complete runs;
- deterministic or strongly telegraphed consequences;
- build experimentation;
- meaningful spatial decisions;
- low unit micromanagement.

### Secondary audience

Players from adjacent board-game, tower-defense, automation, city-building, and roguelite communities who want strategic depth without long campaigns, factory-scale sprawl, heavy menu management, or high actions-per-minute execution.

### Explicitly not the target

The launch product is not optimized for players primarily seeking:

- StarCraft-like unit micro;
- a deep individual-citizen simulation;
- traditional collectible-card/deckbuilding play;
- competitive multiplayer;
- an open-world campaign;
- a live-service progression treadmill.

---

## 5. Product pillars and measurable gates

### P1 — One-board readability

**Requirement:** the important strategic state is understandable from the main play view.

**Gate targets:**
- board, threat forecast, three stockpiled resources, Command state, activation state, damage, and immediate choices coexist coherently;
- powered, unpowered, disabled, isolated, resonant, damaged, and predicted-disconnect states are visually distinct;
- no routine strategic decision requires a separate management screen;
- controller/keyboard focus exposes the same authoritative information as pointer interaction.

### P2 — Scarcity of Command, not scarcity of clicks

**Requirement:** difficulty comes from prioritization.

**Gate targets:**
- Command is non-stockpiled and insufficient to power every desirable structure in representative mid-run states;
- routine production and combat resolve automatically after commitment;
- no direct worker dragging or mandatory per-enemy targeting;
- each repeated input must have a strategic purpose rather than exist as upkeep.

### P3 — Transparent consequences

**Requirement:** players can form and inspect a plan before committing.

**Gate targets:**
- the next two major pressure events are forecast during the normal run structure;
- enemy entry, targeting rules, major damage ranges, and special rules are inspectable;
- resource conversion and Command assignment use explicit deterministic ordering;
- losses generate a post-run causal explanation rather than a vague failure message.

### P4 — Structural build diversity

**Requirement:** different builds change how the system is played.

**Gate targets:**
- four launch doctrines change rules, not merely percentages;
- network geometry, priorities, structure families, and upgrades support qualitatively different solutions;
- no difficulty tier is intentionally balanced around one mandatory build;
- run upgrades should alter relationships, shapes, timing, conversion, targeting, or circuit behavior more often than flat stats.

### P5 — Short, complete, replayable runs

**Requirement:** a normal victory targets 35–50 minutes.

**Gate targets:**
- 15 Watches across 3 Acts;
- bosses at Watches 5, 10, and 15;
- no late-run housekeeping section with obvious but slow decisions;
- 1×/2×/4× Siege speed plus safe skipping of already-understood deterministic resolutions.

### P6 — Premium authored presentation

**Requirement:** screenshots read as a deliberately illustrated living strategy map.

**Gate targets:**
- paper-cut / woodcut / screen-print visual language;
- strong silhouettes at gameplay scale;
- restrained functional palette and non-color-only interaction cues;
- Blender source, export settings, generated passes, pivots, and Godot-ready assets remain reproducible.

---

## 6. Anti-pillars and launch exclusions

Do **not** add the following to create an illusion of value:

- direct unit micromanagement;
- real-time or asynchronous multiplayer;
- player accounts or cloud-hosted progression;
- Workshop/UGC browser;
- open world;
- freeform diplomacy;
- individual citizen schedules;
- procedural story generator;
- voice acting;
- physics-driven combat;
- conventional collectible-card deck;
- five launch biomes;
- twenty resources;
- dozens of professions;
- hundreds of buildings;
- permanent universal stat inflation as the main metaprogression model.

Depth must come from interactions among a deliberately limited set of readable systems.

---

## 7. Comparable set and learning boundaries

### Direct commercial/mechanical comparables

- **9 Kings** — validates compact kingdom-grid strategy, adjacency, escalating combinations, and automated resolution.
- **The King is Watching** — validates attention/allocation pressure on a compact kingdom board.
- **Thronefall** — validates low-friction kingdom defense with strong readability.

### Adjacent design comparables

- **Into the Breach** — information clarity and forecastable tactical consequences.
- **Shogun Showdown** — readable sequencing, compact runs, and minimal micromanagement.
- **dotAGE** — planning depth and forecasting, plus a warning about solo-development content scale.
- **Mindustry** — network/logistics + defense appetite, but at a much broader systems scale.
- **Stacklands** and **Backpack Battles** — simple physical/spatial grammars generating systemic combinations.
- **Kingdom Two Crowns** — readable low-micro kingdom pressure and strong authored atmosphere.
- **Drop Duchy** — familiar spatial interaction carrying deeper strategy.
- **Slipways** — compressing strategic decisions into shorter sessions without traditional micro.

### Prohibited copying

Comparables are evidence and design references, not templates. Signalhold must not copy names, layouts, icons, progression structures, resource sets, signature activation shapes, exact mechanics, or marketing language.

The command network must be visibly original: ports, relays, loops, switchgates, Load, priorities, cut points, and physical routing.

---

## 8. Decision ownership and change control

### Decision hierarchy

1. Product pillars and player promise.
2. Approved scope ceiling.
3. Deterministic simulation and player trust.
4. Solo-production feasibility.
5. Presentation quality.
6. Convenience or novelty.

### Owner

The project owner is the final product/scope decision owner. Implementation agents may recommend changes but may not silently approve scope growth.

### Change classes

**Class A — clarification:** wording or implementation detail that does not alter player promise, scope ceiling, content count, schedule, or architecture. Record in normal changelog.

**Class B — bounded design change:** changes a rule or item while remaining within existing ceilings. Requires an ADR or design-decision note plus regression evidence.

**Class C — scope/product change:** adds a mode, platform commitment, online feature, major system, biome, content family, dependency, or extends a ceiling. Requires explicit project-owner approval and an updated risk/schedule assessment before implementation.

### No-silent-widening rule

If a later request conflicts with this charter, the request must explicitly supersede the affected baseline. Absence of discussion is not approval.

---

## 9. Phase 001 exit statement

This charter fixes the audience, commercial hypothesis, core hook, product pillars, anti-pillars, decision ownership, and non-negotiable scope direction required to proceed to Phase 002.

Phase 002 may refine originality/IP boundaries but may not weaken this product contract without the change-control process above.
