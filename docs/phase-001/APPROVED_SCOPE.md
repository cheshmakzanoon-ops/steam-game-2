# Phase 001 — Approved Scope Statement

**Project:** Signalhold: The Last Relay  
**Status:** APPROVED BASELINE  
**Date:** 2026-09-22

This is the launch-scope ceiling. A number described as a target may be reduced when quality improves by shipping less. It may not be silently increased.

---

## 1. Product envelope

- Compact one-board kingdom/base-building strategy roguelite.
- Premium Steam release.
- Windows is the primary launch platform.
- Linux and Steam Deck are verification targets before launch.
- Normal victory target: **35–50 minutes**.
- Production target: **12–15 months full-time**.
- Hard safety ceiling: **18 months**.
- No required internet connection.
- No mandatory player account.
- No live-service dependency.

---

## 2. Core run ceiling

- **Board:** 9×9 charter board.
- **Keep:** occupies the center tile.
- **Run:** 15 Watches.
- **Acts:** 3.
- **Boss Watches:** 5, 10, 15.
- **Planning:** indefinitely pausable.
- **Siege speeds:** 1×, 2×, 4×.
- **Primary run mode at launch:** one principal mode; variants/difficulty are modifiers, not separate campaign-sized modes.
- **Primary visual world:** one principal launch biome/theme; do not multiply biome-specific production burden.

---

## 3. Economy ceiling

Exactly three stockpiled core resources:

1. **Supply**
2. **Material**
3. **Insight**

Plus one non-stockpiled operational resource:

4. **Command**

Do not add resource categories merely to create complexity. Costs should remain small, integer, inspectable, and deterministic in order of resolution.

---

## 4. Launch doctrine ceiling

Exactly **four launch doctrines**:

1. Iron Charter
2. Verdant Compact
3. Lantern Synod
4. Free Marches

Each doctrine must change at least one structural rule and remain built on the shared core simulation.

Each doctrine may include:
- one unique starting building;
- one active ability with clear cooldown;
- five doctrine-exclusive upgrades;
- weighted content choices;
- tutorial note;
- visible board identity.

Do not turn doctrines into four separate games.

---

## 5. Structure ceiling

### Non-combat structures

**Target: 24**

Keep, Croft, Granary, Timber Yard, Quarry Office, Workshop, Foundry, Archive, Observatory, Market Hall, Salvage Hall, Infirmary, Relay Post, Signal Mast, Switchhouse, Amplifier, Charter Vault, Bell Tower, Survey Office, Contractor Lodge, Waterwheel, Kiln, Scriptorium, Muster Court.

Names may change, but every retained structure must own a distinct strategic job.

### Combat structures

**Target: 9**

Watchtower, Ballista Nest, Bombard Platform, Ward Spire, Pike Yard, Ranger Lodge, Barricade, Bastion Wall, Field Shrine.

At least:
- three solve positioning problems;
- three solve enemy-trait problems;
- three create network/economy tradeoffs.

A structure may satisfy more than one category when its role stays readable.

---

## 6. Enemy/content ceiling

- **15 standard enemies**
- **3 bosses**
- **~45 run upgrades**
- **24 systemic events**
- **6 difficulty Oaths**

Enemy families at launch:
- Raider
- Hush
- Siege

Boss working concepts:
- The Mute Colossus
- The Pale Cartographer
- The Crownless Choir

Every enemy needs a distinct silhouette, arrival icon, route behavior, target rule, and meaningful counter. Do not add enemies that differ only by health/damage.

---

## 7. Core network scope

The launch simulation includes:

- cardinal structure ports;
- rotation;
- automatic compatible-adjacent links;
- Keep-originated Command;
- Load costs;
- explicit priority ranks: Crown, Charter, Dormant;
- deterministic tie-breaking;
- Switchhouse edge disabling;
- Relay behavior;
- Resonance from redundant vertex-disjoint paths;
- link/structure damage;
- next-tick command recalculation;
- preview of vulnerable cut points;
- inspectable connected/powered/unpowered/disabled/isolated/resonant states.

This is **not** a general-purpose electrical/network-flow simulator.

---

## 8. Art/presentation scope

### Style

Paper-cut + woodcut + screen-print / ink-and-parchment hybrid.

### Production rule

- Blender is source of truth for authored geometry, paper layers, rendered sprites, masks, and hero marketing scenes.
- Godot is source of truth for runtime assembly, gameplay composition, shaders, UI, VFX timing, audio behavior, and animation state.
- Generated artifacts are reproducible from source.
- Final sprites use a locked orthographic camera/palette/export pipeline.
- Visual states must remain readable without relying on color alone.

### Toolchain

- Godot 4.7.2-stable
- Blender 4.5.14 LTS

---

## 9. Launch exclusions

The following are out of scope unless a later explicit owner-approved scope change supersedes this document:

- direct unit micromanagement;
- real-time multiplayer;
- asynchronous matchmaking;
- player accounts;
- cloud-hosted progression;
- live service;
- server-authoritative gameplay;
- Workshop/UGC browser;
- open world;
- freeform diplomacy;
- individual citizen schedules;
- procedural story generator;
- voice acting;
- physics-driven combat;
- conventional collectible-card deck;
- multiple campaign-sized launch modes;
- five launch biomes;
- console launch commitment;
- sophisticated freeform pathfinding as a core requirement;
- twenty resources;
- dozens of professions;
- hundreds of buildings;
- permanent universal stat grinding as balance compensation.

---

## 10. Scope substitution rule

If new content is judged essential after a ceiling is reached, something of comparable production/maintenance cost must be removed or the change must be approved as a **Class C scope change** with a revised schedule and risk assessment.

"Nice to have" is not a reason to exceed a ceiling.

---

## 11. Approval and change policy

This scope is adopted as the Phase 001 implementation baseline under the project owner's instruction to complete and publish Phase 001.

Any later request that changes:
- a content ceiling;
- a platform commitment;
- the business model;
- the core hook;
- the primary mode/biome count;
- an online feature;
- the toolchain;
- or the production safety ceiling

must explicitly supersede this baseline and record the consequences before implementation.
