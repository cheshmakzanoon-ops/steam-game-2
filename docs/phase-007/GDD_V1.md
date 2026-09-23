# Charterwake: The Last Relay — Game Design Document v1.0

**Phase:** 007 — Game design document baseline  
**Status:** AUTHORITATIVE CONSOLIDATED PREPRODUCTION BASELINE  
**Date:** 2026-09-22  
**Working title status:** Charterwake: The Last Relay remains provisional / AMBER  
**Core-rules version:** 1.0.0  
**Scope-budget baseline:** Phase 005  

---

## 0. How to use this GDD

This GDD consolidates the accepted product, originality, player-experience, rules, scope, and naming decisions from Phases 001–006. It is the normal design entry point for contributors, but it does not erase the source contracts and it does not imply that later implementation phases are complete.

### Source precedence

1. The project bible remains the controlling product specification.
2. Explicitly approved later change records may supersede an earlier baseline.
3. Phase 004 Core Rules v1.0.0 owns exact mechanical ordering, geometry, state transition, and failure precedence.
4. Phase 005 owns content, art, text, audio, performance, cash, and schedule ceilings.
5. Phase 006 owns canonical player-facing vocabulary and provisional branding.
6. This GDD organizes those decisions into one coherent reference.

If a summary here conflicts with an accepted source document, treat that as a documentation defect. Do not silently reinterpret the source.

Changes to a locked rule, player promise, scope ceiling, content category, naming rule, accessibility requirement, or platform commitment require the Phase 007 change-request process.

---

# 1. Product definition

## 1.1 High concept

Charterwake: The Last Relay is a compact one-board kingdom/base-building strategy roguelite in which every major threat is visible, but the kingdom's physical command network can never power everything at once.

The player is not rewarded for clicking quickly. The core skill is deciding what receives authority, where the network should run, which vulnerabilities are acceptable, and when economy must yield to survival.

## 1.2 Product format

- Premium one-time-purchase PC game.
- Primary launch target: Steam for Windows.
- Linux and Steam Deck verified before launch.
- Offline core game; no mandatory account or server.
- One principal launch mode.
- One principal launch biome/theme.
- Standard victory target: 35–50 minutes.
- Fifteen Watches across three Acts.

## 1.3 Core promise

> You can see every major threat coming, but your command network can never power everything at once.

The desired player response after a run is:

> I saw the pressure, made a plan, understand why it worked or failed, and already know what I want to route differently next time.

---

# 2. Product pillars

## P1 — One-board readability

The entire strategic state must remain understandable from the main play view. Tooltips expand detail; they do not rescue an unreadable board.

The player must be able to inspect connection state, powered state, Command and Load, damage, target intent, forecast, resources, and circuit vulnerability.

## P2 — Scarcity of Command, not scarcity of clicks

The hard choice is what receives authority. Routine production, upkeep, and combat resolve automatically after commitment.

Do not build worker dragging, per-enemy targeting, repeated upkeep confirmation, reaction-speed gates during planning, or repetitive repair clicks when the answer is obvious.

## P3 — Transparent consequences

Threat routes, timing, target rules, special rules, costs, Load, and deterministic ordering must be inspectable before commitment. Unknown information is labeled unknown rather than represented with false precision.

## P4 — Structural build diversity

Network geometry, doctrines, priorities, and upgrades create qualitatively different plans. Doctrines change rules rather than merely percentages.

## P5 — Short, complete, replayable runs

A run has a beginning, escalation, climax, and post-run explanation. No late-game housekeeping phase exists merely to inflate duration.

## P6 — Premium authored presentation

The visual language is deliberately illustrated: paper-cut, woodcut, screen-print, ink, and parchment, with restrained but precise animation, sound, and feedback.

---

# 3. Anti-pillars and launch exclusions

Do not add to the launch baseline without formal scope change:

- direct unit micromanagement;
- real-time or asynchronous multiplayer;
- mandatory accounts;
- cloud-hosted progression;
- live-service systems;
- Workshop or UGC browser;
- open world;
- freeform diplomacy;
- individual-citizen schedules;
- procedural story generator;
- voice-acting production;
- physics-driven combat;
- conventional collectible-card deck;
- multiple principal launch modes;
- multiple principal launch biomes;
- console launch commitment;
- hundreds of buildings, professions, or resources;
- permanent universal-stat grind used to compensate for weak balance.

Depth must come from interactions among a deliberately bounded system set.

---

# 4. Player fantasy, setting, and tone

The player is the Warden of the last operational signal-fortress in the Ashen March.

The old kingdom coordinated itself through illuminated charter lines drawn into enchanted maps. The Hush has severed those lines and turned abandoned forces, siege engines, and oath-bound pressure against the frontier.

The Keep contains the final working Crown Relay.

The player should feel like a planner, cartographer, and civic commander repairing a damaged system under visible pressure.

Tone:
- grave, not hopeless;
- practical, not melodramatic;
- tactile and civic rather than generic heroic fantasy;
- dry humor through civic compromises and building behavior;
- story supports decisions and never delays retry.

---

# 5. Canonical run structure

## 5.1 Acts and Watches

A standard run has fifteen Watches:

- Act I — First Lines: Watches 01–05
- Act II — Frayed Charter: Watches 06–10
- Act III — Last Relay: Watches 11–15

Boss assaults conclude Watches 05, 10, and 15.

## 5.2 Watch phases

Every normal Watch follows:

1. Forecast
2. Council
3. Build
4. Route
5. Production
6. Siege
7. Aftermath

### Forecast

Reveal or confirm upcoming pressure, including at minimum the next two major threats, entry location, target logic, and special rule.

### Council

Resolve a scheduled research, event, contract, or doctrine decision. If nothing is scheduled, do not show a dummy modal.

### Build

Place, rotate, upgrade, repair, dismantle, or reserve structures using projected resources.

### Route

Enable or disable supported switch edges, set Crown, Charter, or Dormant priorities, inspect Command allocation, and preview network consequences.

### Production

Resolve powered economy in deterministic order and emit a concise ledger.

### Siege

Enemies and defenses resolve automatically in deterministic ticks.

### Aftermath

Apply salvage and persistent results once, explain causal damage, offer only the defined limited recovery action, then checkpoint.

## 5.3 Commitment

Planning is indefinitely pausable.

Build and Route edits remain proposed until Seal the Charter. Seal revalidates the complete command transaction. If any command is invalid or stale, reject the whole batch without partial mutation.

After successful Seal:
- undo does not cross into Production;
- presentation speed cannot change results;
- the plan remains fixed through ordinary Production and Siege except for explicitly declared doctrine exceptions.

## 5.4 Speed

Siege presentation supports 1x, 2x, and 4x. Familiar resolved content may later support an instant deterministic summary. Simulation ticks and final outcomes remain identical.

---

# 6. Board model

## 6.1 Coordinates

The standard board is exactly 9 by 9.

- Origin: northwest coordinate 0,0.
- x increases east.
- y increases south.
- Row-major index equals y times 9 plus x.
- Valid indices are 0 through 80.
- No wraparound.

The Keep is fixed at coordinate 4,4, index 40.

Reserved enemy-entry cells:
- north: 4,0, index 4;
- east: 8,4, index 44;
- south: 4,8, index 76;
- west: 0,4, index 36.

An otherwise unmarked board therefore exposes 76 ordinary buildable cells.

## 6.2 Board diagram

~~~text
          x → 0 1 2 3 4 5 6 7 8
        +-------------------+
y = 0   | . . . . N . . . . |
y = 1   | . . . . . . . . . |
y = 2   | . . . . . . . . . |
y = 3   | . . . . . . . . . |
y = 4   | W . . . K . . . E |
y = 5   | . . . . . . . . . |
y = 6   | . . . . . . . . . |
y = 7   | . . . . . . . . . |
y = 8   | . . . . S . . . . |
        +-------------------+

K = Keep / Crown Relay
N E S W = reserved baseline enemy entries
. = ordinarily buildable subject to terrain and occupancy
~~~

This is a rule diagram, not final UI or art.

## 6.3 Placement

Baseline structures occupy one cell. Any later larger footprint must declare an anchor and rotated occupied-cell list.

Every affected cell must be:
- in range;
- not the Keep;
- not an enemy-entry cell;
- not blocked by terrain or rubble;
- not occupied by a living structure.

An invalid placement or rotation spends nothing, consumes no RNG, allocates no persistent instance ID, and mutates nothing.

---

# 7. Ports, links, and rotation

Each structure can expose one to four cardinal ports: North, East, South, and West.

Basic ports connect only to facing compatible ports on adjacent cells. No diagonal or one-sided implicit connection exists.

Rotation:
- occurs in 90-degree quarter-turns;
- rotates ports, directional attacks, switch tabs, and footprint offsets together;
- updates previews immediately.

Switch state and physical damage are different concepts:
- a disabled switch edge is intentionally unavailable;
- a severed link is physically damaged;
- toggling a switch cannot heal a severed link.

Special links, such as Signal Mast reach across one empty cell, must be explicit rule or content exceptions and visually unmistakable.

---

# 8. Connectivity, Command, and priorities

## 8.1 Physical graph

The command network is an undirected graph of living structures connected by valid enabled links.

Connectivity starts from the Keep.

A structure can remain physically connected even when it is Dormant, unpowered due to capacity, or unable to pay upkeep. Power state alone never breaks physical network continuity.

## 8.2 Command and Load

Initial baseline Command capacity is 6 Load.

Command is live operational bandwidth, not a stockpiled currency.

Every operating structure has an integer effective Load. A structure receives its entire Load or receives none; partial power is forbidden.

## 8.3 Priorities

Player-controlled tiers:

1. Crown
2. Charter
3. Dormant

Dormant structures remain physically connected, consume no Command, and do not operate.

Within a tier, stable row-major anchor index is the default tie-breaker, followed by stable instance ID as a defensive tie-break.

## 8.4 Allocation

Scan eligible connected non-Dormant structures in deterministic order.

- If full Load fits and required upkeep can be paid, power it.
- Otherwise record why it was rejected and continue.
- Do not reorder to maximize hidden output.
- A large rejected structure does not prevent a later smaller structure from fitting.

The preview tells the player which structures will be unpowered and why.

---

# 9. Switches, circuits, cut points, and Resonance

Switchhouse-supported edges may be enabled or disabled during planning and previewed before commitment.

A cut point is a vulnerable topology point whose loss disconnects downstream structures.

Resonance means a structure has two internally vertex-disjoint valid paths back to the Keep. It represents redundancy, not generic bonus stacking.

Rules:
- two drawings of the same edge do not count as redundancy;
- one cycle hanging from a single vulnerable stem is not Resonant;
- Resonance recalculates after topology changes, not every frame;
- exact family bonuses belong to later implementation and balance phases;
- Resonance never overrides connectivity or Load rules.

If a link breaks during Siege tick t, graph and Command recalculation occurs at the defined next tick boundary. Presentation cannot delay or accelerate the authoritative state.

---

# 10. Economy

Exactly three stockpiled resources:
- Supply
- Material
- Insight

Plus non-stockpiled Command.

Resource values are integers.

## 10.1 Transactions

Costs are atomic bundles: pay all or pay nothing.

No negative stockpiles.

Every transaction has an inspectable cause and unique identity so replay or save recovery cannot duplicate rewards.

## 10.2 Upkeep

Where content has upkeep:
- payment is automatic;
- resolved in deterministic allocation order;
- previewed;
- no repetitive payment clicks;
- failure spends nothing and prevents operation for the defined Watch latch.

## 10.3 Production

Powered economy resolves once, in deterministic order.

Earlier outputs may fund later recipes. Later outputs do not cause an earlier failed recipe to retry.

No automatic fixed-point loops.

The ledger shows source, cost, output, before and after bundle, and failure reason.

---

# 11. Threats and forecasting

The forecast is a player-trust contract.

At minimum it answers:
1. when the threat arrives;
2. where it enters;
3. what it tries to damage;
4. what makes it different.

Once revealed, a threat does not randomly change unless a clearly stated player or event rule changes it. If changed, show before and after.

Boss-defining rules must be previewed early enough to influence the player's build and, where appropriate, demonstrated safely before the boss.

---

# 12. Combat and Siege

Combat resolves in explicit deterministic ticks.

Baseline order:

1. scheduled start-of-tick effects;
2. refresh Command if relevant state changed;
3. determine enemy movement intents;
4. resolve movement in stable order;
5. determine defense targets;
6. resolve defense attacks in stable structure order;
7. remove defeated enemies and on-defeat effects;
8. determine surviving enemy targets;
9. resolve enemy attacks and sabotage;
10. apply destruction, link cuts, and on-damage effects;
11. evaluate terminal, stage, and end-of-tick effects.

Scene-tree or render order never becomes simulation order.

A killed enemy does not attack later in the same tick.

Target selection and tie rules must be deterministic and inspectable.

---

# 13. Damage, repair, and terminal outcomes

Health or integrity, armor, wards, and damage use integer deterministic rules owned by Phase 004 and later combat content.

The player must distinguish damaged, disabled, destroyed, rubble, and severed-link states.

Repair is a planning action with explicit resource cost and timing. It is never hidden automatic debt.

## 13.1 Victory

Victory occurs only when:
- Watch 15 final boss requirements are complete;
- required hostiles and objectives are resolved;
- Keep remains intact;
- no higher-precedence defeat condition exists.

## 13.2 Defeat

Defeat takes precedence when:
- Keep Integrity reaches zero;
- a clearly forecast fatal boss objective resolves;
- a declared doctrine-specific loss predicate resolves.

If final boss death and Keep death happen in the same terminal checkpoint, defeat takes precedence and both causes are recorded.

---

# 14. Fair-loss and post-run explanation

A difficult loss is acceptable only if:
- threat was legible;
- player had actionable agency;
- relevant state was inspectable;
- rules resolved consistently;
- randomness stayed within communicated control;
- causal chain is reconstructable;
- input or accessibility did not cause failure;
- no retroactive gotcha appeared after the last meaningful decision.

Post-run explanation identifies root cause, not merely the final damage packet.

Desired player reflections include:
- I should have routed differently.
- I powered economy one Watch too long.
- I saw the vulnerable cut point and gambled.
- I want to retry this doctrine with different priorities.

---

# 15. Doctrines

Launch doctrines:

1. Iron Charter — fortification, armor, stable circuits.
2. Verdant Compact — adaptive economy, harvest timing, fatigue.
3. Lantern Synod — Insight, forecasting, Resonance, limited after-Production reroute.
4. Free Marches — salvage, edge control, militia abstraction, deliberate risk.

Doctrines share the central simulation. They do not become four separate games.

Each launch doctrine budget includes:
- unique starting building inside the existing structure cap;
- one active ability;
- five doctrine-exclusive upgrades;
- weighted content choices;
- tutorial note;
- visible board identity.

---

# 16. Difficulty and metaprogression

Difficulty uses six Oaths. Phase 006 reserves display names; Phase 062 owns exact mechanical definitions.

Difficulty adds rules and pressure patterns, not merely health inflation.

Metaprogression primarily unlocks doctrines, sidegrade structures, mutators, inks or cosmetics, lore, and challenge options.

Avoid universal permanent damage, health, or income grind used to make early difficulty intentionally unfair.

---

# 17. Launch content categories and ceilings

## 17.1 Civilian and network structures — 24 total including Keep

Keep, Croft, Granary, Timber Yard, Quarry Office, Workshop, Foundry, Archive, Observatory, Market Hall, Salvage Hall, Infirmary, Relay Post, Signal Mast, Switchhouse, Amplifier, Charter Vault, Bell Tower, Survey Office, Contractor Lodge, Waterwheel, Kiln, Scriptorium, Muster Court.

## 17.2 Combat structures — 9

Watchtower, Ballista Nest, Bombard Platform, Ward Spire, Pike Yard, Ranger Lodge, Barricade, Bastion Wall, Field Shrine.

## 17.3 Enemies

- 15 standard enemies total.
- Three families: Raider, Hush, Siege.
- Every enemy differs by behavior, targeting, timing, geometry, or counterplay, not merely health.

## 17.4 Bosses — 3

- The Mute Colossus
- The Pale Cartographer
- The Crownless Choir

Boss names remain working content names until writing review, but boss count is capped at three.

## 17.5 Other launch categories

- four doctrines;
- 45 total run upgrades, including doctrine-exclusive upgrades;
- 24 systemic events;
- six Oaths;
- one principal biome or theme;
- one principal run mode;
- a small bounded terrain-mark vocabulary rather than a terrain simulator.

Any increase is a scope change, not ordinary implementation.

---

# 18. UX and information design

## 18.1 Main-view hierarchy

Highest visual priority:
1. immediate fatal threat;
2. selected cell or committed action;
3. Keep and run-ending state;
4. network or Command warning;
5. unresolved commitment warning.

Secondary priority:
- resources;
- Load and capacity;
- projected production;
- phase progress.

Tertiary:
- formula breakdown;
- history;
- codex links.

## 18.2 Preview before commitment

Before Seal, preview states:
- powered structures;
- unpowered structures and reasons;
- expected production;
- incoming groups;
- likely routes;
- defenses that can engage;
- exposed cut points;
- unresolved warnings.

The preview explains the system. It does not recommend an optimal strategy.

## 18.3 Undo and reload

Planning undo restores the complete proposed state, not only visuals.

Undo does not cross committed Council RNG, Seal, Production, Siege tick, or settled Aftermath boundaries.

Reload reconstructs authoritative simulation state from versioned data; UI, animation, and frame delta are never authoritative save fields.

## 18.4 Input parity

Mouse and keyboard, keyboard-only, and controller expose equivalent strategic information.

Controller focus exposes anything otherwise available through hover.

Board focus at an edge stays at the boundary rather than wrapping unexpectedly.

## 18.5 Accessibility

Launch requirements include:
- key rebinding;
- controller remapping where the platform permits;
- scalable UI;
- readable fonts;
- high-contrast mode;
- color-independent state icons;
- reduced motion;
- reduced flashes;
- adjustable shake;
- separate volume categories;
- pause during planning;
- adjustable Siege speed;
- inspection without time pressure.

Critical warnings use at least two signals among text, icon, shape, sound, and color.

---

# 19. Art direction

The world resembles a strategic map made from dyed paper, printed charcoal ink, thin card, thread, sealing wax, and tarnished fasteners.

Forms are chunky; silhouette readability outranks micro-detail.

## 19.1 Functional palette

- substrate: warm parchment and ash gray;
- Command: desaturated gold and warm white;
- Supply: muted green;
- Material: rust orange;
- Insight: blue-violet;
- immediate danger: vermilion;
- Hush: cold near-black with pale cyan edge.

Color is never the only state cue.

## 19.2 Pipeline responsibility

Blender is source of truth for authored visual geometry, paper layers, masks, sprite renders, and hero scenes.

Godot is source of truth for gameplay composition, UI, shaders, VFX timing, audio behavior, and runtime assembly.

Generated files remain reproducible from source.

Phase 005 ceiling:
- 220 authored visual sets;
- 400 hard color-frame cap;
- 389 currently allocated.

---

# 20. Audio direction

Audio reinforces tactility and state.

Use:
- card, paper, thread, wax, wood, and soft-metal UI sounds;
- recognizable Command-network success and failure cues;
- distinct defense-family sounds;
- prioritized Keep, boss, and network-failure warnings.

At 4x speed, audio cannot become an unreadable wall of impacts.

Phase 005 ceiling:
- 76 non-music cue identities;
- 180 variants;
- five adaptive pieces target;
- seven-piece cap;
- 24 minutes unique music cap;
- no launch voice-acting scope.

---

# 21. Technical design principles

Production code is typed GDScript in the pinned Godot 4.x baseline.

Core requirements:
- deterministic simulation separate from presentation and input;
- explicit validated commands;
- structured simulation result events;
- one run session owns authoritative run state;
- seeded randomness owned by the run;
- integer replay-critical arithmetic;
- validated content resources;
- stable string IDs;
- versioned save schema and migrations;
- no universal arbitrary GameManager;
- offline operation.

Blender remains the authored asset source.

Python verification scripts in early phases are disposable design probes, not shipping runtime dependencies.

---

# 22. Performance and platform budgets

Targets, not current measurements:

- 60 fps baseline at 1920 by 1080 on modest reference hardware;
- 30 fps playable fallback;
- process memory at or below 1,900 MB decimal;
- installed launch build at or below 1,800 MB decimal;
- texture residency at or below 512 MB;
- graph rebuild strictly under 1 ms;
- worst normal combat tick strictly under 2 ms;
- scene transition strictly under 3 seconds or approved progress treatment.

Later exported-build phases record exact test hardware and percentile or maximum behavior.

---

# 23. Demo and commercial shape

Business model: premium one-time purchase.

Working price hypothesis: USD 14.99; revalidate before store publication.

Public-demo ceiling:
- one doctrine;
- ten total structures including Keep;
- six standard enemies;
- one boss;
- twelve upgrades;
- four events;
- five-Watch complete arc;
- 20–40 minute new-player target;
- two viable build directions;
- one understandable spectacular synergy;
- fair explainable failure.

The demo is an allowlisted subset of the real game, not a separate fork.

---

# 24. Placement and disconnection edge cases

These are mandatory examples, not optional polish.

## Placement

- out-of-bounds footprint: reject atomically;
- Keep cell: reject;
- reserved entry: reject;
- occupied cell: reject;
- blocking terrain or rubble: reject;
- illegal rotation: reject without spending or RNG;
- no row wrap;
- all rotated footprint cells validate before mutation.

## Links

- one-sided ports do not connect;
- diagonal ports do not connect;
- disabled switch is not severed damage;
- disconnected switch state remains saved;
- rebuilt endpoint gets new edge identity;
- toggling cannot heal a severed link.

## Allocation

- Dormant structure remains physical conductor;
- unpowered overload structure remains physical conductor;
- large non-fitting structure can be skipped while a later smaller one powers;
- zero-Load connected structure may operate at zero capacity if otherwise eligible.

## Siege disconnection

- break occurs during authoritative combat order;
- topology becomes dirty;
- next defined Command-recalculation boundary publishes new power state;
- destroyed unit or structure cannot act from stale cached state;
- preview and recap use the same graph semantics.

## Terminal

- same-tick Keep death outranks final-boss death;
- missing or invalid boss definition is technical/content error, not free victory;
- terminal run cannot accept further gameplay commands.

---

# 25. System ownership map

| System | Owning phase or range |
| --- | --- |
| Market/product charter | 001 |
| Originality/IP | 002 |
| Player promise/pacing/fair loss | 003 |
| Core rule semantics | 004 |
| Scope/content/cash ceilings | 005 |
| Brand/naming vocabulary | 006 |
| Consolidated GDD/change process | 007 |
| Roadmap/dependency graph | 008 |
| Kill criteria/risk | 009 |
| Preproduction approval | 010 |
| Repository/engine bootstrap | 011 |
| CI/build skeleton | 012 |
| Coding standard | 013 |
| Deterministic simulation kernel | 014 |
| Content schema | 015 |
| Saves/versioning/migration | 016 |
| Input abstraction | 017 |
| UI design-system foundation | 018 |
| Blender template/export | 019 |
| Godot asset calibration | 020 |
| Board coordinates | 021 |
| Board view/camera | 022 |
| Placement/rotation | 023 |
| Port graph | 024 |
| Command allocation | 025 |
| Switchhouse/circuits | 026 |
| Resonance/redundancy | 027 |
| Resource ledger | 028 |
| Production resolver | 029 |
| Core-loop graybox gate | 030 |
| Threat forecast | 031 |
| Enemy lanes/paths | 032 |
| Combat tick | 033 |
| Defense targeting | 034 |
| Enemy attacks/sabotage | 035 |
| Health/repair/destruction | 036 |
| Siege presentation bridge | 037 |
| Aftermath/recovery | 038 |
| Research/rerolls/banishes | 039 |
| Combat vertical slice | 040 |
| Doctrine framework/content | 041–045 |
| Civilian/network/combat structures | 046–050 |
| Upgrades/events | 051–054 |
| Standard enemy families | 055–057 |
| Elites/mutators/bosses/run director | 058–061 |
| Oaths/metaprogression/codex/tutorial/post-run | 062–067 |
| Game feel/VFX/animation | 068–070 |
| Final art production | 071–078 |
| SFX/music/narrative | 079–080 |
| Accessibility/input/resolution audits | 081–084 |
| Performance/save/settings/localization/reliability | 085–090 |
| Balance/debug/automated testing/platform | 091–095 |
| Steamworks/demo | 096–100 |
| Store/marketing/public playtest | 101–107 |
| Post-demo revisions/content lock/polish | 108–110 |
| Alpha/beta/localization/RC/launch | 111–116 |
| Support/post-launch/final acceptance | 117–120 |

A phase number identifies responsibility. It does not imply that system is implemented today.

---

# 26. GDD change control

No contributor may silently edit a locked design and call the new behavior an implementation detail.

Use CHANGE_REQUEST_TEMPLATE.md.

A change request identifies:
- player problem;
- source text or rule being superseded;
- scope impact;
- rules and save impact;
- content IDs affected;
- UX and accessibility impact;
- originality/IP impact;
- performance and install impact;
- test/evidence plan;
- rollback;
- approval.

Accepted changes update the owning source, this GDD, expected examples and tests, change history, and version where required.

---

# 27. Change history

| GDD version | Date | Phase | Change |
| --- | --- | --- | --- |
| 1.0 | 2026-09-22 | 007 | Initial consolidated baseline from accepted Phases 001–006; no new gameplay system or scope expansion. |

Future rows reference an approved change-request ID and commit.

---

# 28. Intentional later decisions

These are owned by later phases and do not block GDD v1.0:

- exact balance values for all content;
- exact individual names and behaviors for every enemy;
- exact six Oath mechanics;
- exact Resonance bonuses by family;
- final asset silhouettes and animations;
- final font;
- final public-title clearance;
- measured performance on reference hardware;
- empirical difficulty and balance tuning;
- localization language selection;
- final store pricing.

They may not be filled ad hoc outside their owning phase.

---

# 29. Phase 007 acceptance

This GDD is complete when:
- player-visible mechanics are organized and traceable;
- annotated examples and board diagrams exist;
- placement and disconnection edge cases are explicit;
- launch content categories and ceilings are included;
- UX and accessibility requirements are included;
- system ownership phases are linked;
- a change-request process exists;
- design review reports no critical contradiction with Phases 001–006.

See ANNOTATED_EXAMPLES.md and DESIGN_REVIEW_SIGNOFF.md.
