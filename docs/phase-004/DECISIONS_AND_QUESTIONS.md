# Phase 004 — Decisions, source traceability and unresolved questions

**Rules version:** 1.0.0
**Date:** 2026-09-22
**Open critical baseline questions:** 0
**Authority:** implementation of the owner's requested Phase 004; not a claim of external playtest approval or legal clearance.

## Source identification

The authoritative upload is `steam%20game%20number%202(1).md`, 459,471 bytes, 5,985 lines. Its SHA-256 is:

`89f805584dea2b90fac1fc7144d35ce0feb376f6d8c75e8037a265f190787f9d`

This is the later *Master Production Prompt and Project Bible*, not the older alternative outline with different content counts. Existing Phase 001–003 documents and the authorized Charterwake rename also apply. The master is identified by its immutable byte hash so a future agent cannot silently use the wrong revision.

| Source ID | Exact source location | Consequence for this phase |
|---|---|---|
| S04 | Phase 004, source lines 631–672 | Freeze minimal rules, give examples, close critical questions; no production gameplay merely for visible progress. |
| S05 | Section 5, source lines 95–109 | 9x9, central Keep, 15 Watches, three Acts, bosses at 5/10/15, seven stages, automatic Siege, terminal conditions. |
| S06 | Section 6, source lines 113–121 | Undirected ports; initial capacity six; Crown/Charter/Dormant; row-major tie order; independent-path Resonance; next-tick reallocation. |
| S07 | Section 7, source lines 125–136 | Supply/Material/Insight plus non-stockpiled Command; integer transactions; automatic upkeep; no negative stockpiles. |
| S10 | Sections 10–11, source lines 288–386 | Explicit commands, atomic rejection, independent simulation, versioned data, reproducible RNG; no UI authority. |
| S12 | Section 12, source lines 390–408 | Focus/hover parity, consequence preview, destructive-action undo and redundant visual cues. |
| S20 | Sections 20.1–20.8, source lines 5666–5742 | Seal transaction, Dormant still connected, quarter-turn ports, fixed forecasts, detailed combat order and speed invariance. |
| S21 | Section 21.4, source lines 5859–5887 | Zero-Load relays, one-cell Mast gap, persistent switch state, bounded Amplifier behavior, limited Vault exception. |
| S27 | Phase 027, source lines 1620–1661 | Exact Resonance family bonuses are scheduled here, not fabricated as implemented in Phase 004. |
| S33 | Phases 033–038, source lines 1879–2136 | Later combat, damage, rubble, salvage, repair and aftermath implementations require their own tests. |

Where a source gives an illustrative value or a recommendation rather than a complete rule, the chosen v1.0.0 decision is explicitly identified below. Nothing in the table increases the launch content ceiling or grants an online dependency.

## Resolved critical ambiguities

| ID | Question | Locked resolution | Provenance / evidence |
|---|---|---|---|
| Q01 | What do coordinates and board-index ties mean? | Zero-based northwest origin; x east, y south; index=9*y+x; no wrapping. | S06 + new coordinate convention; exhaustive coordinate checks. |
| Q02 | Which cells are reserved? | Keep 40, four midpoint entries 4/44/76/36; other perimeter cells remain eligible. | S05 + new bounded entry selection; 76-cell count check. |
| Q03 | Can a user move, rotate, dismantle or disable the Keep? | No. Four basic ports, sole normal Command source, zero own Load. | S05/S06 + explicit objective protection; invalid Keep-overwrite example. |
| Q04 | How do rotations affect connectivity? | Clockwise quarter-turns rotate ports, footprint offsets, local switches and attack arcs together. | S20; all masks/quarter-turns checked for port math. Full footprint/arc rendering remains later work. |
| Q05 | Does Dormant stop transmission? | No. Physical connections remain; no operation or Command consumption. | Explicit S20 rule; A04. |
| Q06 | Does overloaded/unpaid status stop basic connectivity? | No. Destruction, severing or declared disabling changes topology, not power alone. | New disambiguation consistent with S06/S20; A05/A12. |
| Q07 | What happens when a priority entry cannot fit? | Reject its full Load, explain why, continue scanning; never partial allocation or optimizer reordering. | New deterministic packing decision; A02/A03. |
| Q08 | What happens to zero-Load structures? | They still require connectivity/eligibility, but may operate at zero capacity. | S21 + Phase 025 edge-case requirement; A06/A07. |
| Q09 | How are switch and severed states distinguished? | Boolean link_enabled is separate from damage. Toggles cannot heal; local switch state survives isolation. | S20/S21 + explicit representation; A08 checks cut connectivity only. |
| Q10 | What counts as Resonance? | Two distinct internally vertex-disjoint paths to Keep; no bonus from a cycle behind one stem. | S06/S20; exhaustive small-graph comparison to independent path enumeration. |
| Q11 | When does a cut change allocation? | Cut at tick t marks dirty; refresh before actions at step 2 of tick t+1. Destroyed actors cannot act. | S06/S20. Pure examples check graph effects; a live tick scheduler is not claimed. |
| Q12 | How does the Mast cross a gap? | Exactly one empty cell in a declared cardinal direction, compatible facing endpoint; no occupied/blocked midpoint. | S21 plus explicit obstruction rule; contract only, no Mast implementation claim. |
| Q13 | How do costs avoid partial payment? | Validate all three components before commit; overflow/negative input rejects without mutation. | S07/S10; bundle and failed-batch checks. |
| Q14 | What funds upkeep, and can reallocation charge twice? | Admission scan pays once per instance per Watch; failed upkeep latches until next Watch; no payment for non-fitting/isolated/Dormant structures. | S07 + new timing decision; A12–A17/P03. |
| Q15 | Can Production loop or retroactively fund earlier recipes? | Ordered one-pass recipes; earlier output may fund later input; no backward retry or implicit fixed-point evaluation. | S07 and Phase 029 + new exact ordering; P01–P04. |
| Q16 | Can a player power all economy, then freely reroute for defense? | No ordinary post-Production reroute. Preserve Lantern Synod's one explicit optional switch-edge exception only. | S05 and section 8 doctrine rule; guarded exception-window check, no doctrine runtime claim. |
| Q17 | When are proposed edits irreversible? | Seal validates a whole scratch transaction against expected revision, then swaps once. Failure retains original state and identifies bad command. | S10/S20; successful, unaffordable, malformed and stale-batch probes. |
| Q18 | Does undo reset random offers? | No. Council offers/rerolls have their own committed RNG/cost checkpoint. | S10/S20 + explicit boundary; contract only, RNG service remains Phase 014. |
| Q19 | What is the combat order? | Adopt section 20.7's eleven steps; killed enemies are removed before enemy attacks; terminal checks observe end-of-tick effects. | S20. No replacement simultaneous free-for-all combat loop. |
| Q20 | What is basic defense targeting? | Legal in-range enemies: shortest remaining route to objective, then stable ID; Manhattan baseline range and declared rotated arcs. | New deterministic baseline compatible with Phase 034; content-specific variants must be explicit. |
| Q21 | Which mitigation applies first? | Per-packet armor, then ward, then clamped health. No negative-damage healing. | New precise mitigation order within S33; D01–D05. |
| Q22 | What is repair/destruction behavior? | Positive-health repair only; zero-health destruction leaves nonconducting build-blocking rubble. Keep cannot be resurrected. | S33 + precise baseline; R01–R05, destruction-graph check. |
| Q23 | How do refunds avoid duplication? | Half actual paid construction/upgrade Material, rounded down, once per instance; no repair-cost refund or second rubble payout. | New bounded salvage baseline within S33. Numeric example only; no persistent reward journal implementation claim. |
| Q24 | Who wins simultaneous final-boss/Keep deaths? | Defeat takes precedence; collect all causes. | S05 + explicit terminal precedence; E02–E04. |
| Q25 | Does an empty board end an encounter? | Only if required hostile/objective and scheduled-wave sets are exhausted. Never auto-Watch-16. | S05/S20 + explicit guard; E05–E08 and gated stage checks. |
| Q26 | What happens on corrupted/unknown-version input? | Fail validation on scratch state; retain live state/checkpoint. A technical error is not a player loss. | S10/S11; malformed/versioned fixture rejection, not a claim about a disk save service. |
| Q27 | Can presentation speed change outcomes? | No. Integer ticks/RNG/packet order are identical; only visual scheduling varies. | S20. Runtime four-speed equivalence remains a future combat test. |
| Q28 | Which material version should future phases implement? | v1.0.0 with fixture profile plus required content-specific values; marketing name is not an ID. | S10, existing rename decision and this version lock. |

Each Q01–Q28 is RESOLVED for the minimal baseline. New requirements discovered later must be logged and versioned, not retroactively described as having been tested here.

## Explicitly selected calibration values

The bible does not prescribe final Keep health or universal repair costs. For reproducible design examples this phase selects Keep Integrity 20, repair amount 3, repair cost 1 Supply + 1 Material, normal presentation interval 100 ms, base salvage one half of actual paid Material. These are **new calibration decisions**, not quotations, measured balance conclusions or extra economic resources.

Starting resources, building health/costs, unit stats and encounter schedules are required fields in their later content definitions. There is no unspecified silent fallback in the minimal contract: a missing required field is invalid content. Changing calibration requires a versioned content profile and new expected examples, not changing the meaning of the core rules.

## Scheduled non-critical work — not completed by this phase

| ID | Work | Owning gate | Why it does not leave the minimal contract undefined |
|---|---|---|---|
| L01 | Final balance, doctrine starting sets, unit ranges/damage and encounter guard limits | Relevant content/doctrine/balance phases | Required parameters have typed validity/ordering contracts. The verification profile is explicit; it is not a launch catalog. |
| L02 | Exact family Resonance/Amplifier/Vault bonuses and interaction budgets | Phase 027 and relevant structure phases | Base allocation has no such numerical modifier. Later effects must obey caps, snapshots, no recursion and versioned examples. |
| L03 | Godot runtime services, InputMap, controller navigation, save migrations, actual speeds and exports | Phases 011–018 and 021–038 | Those implementation gates were not skipped. Pure design checks do not close them. |
| L04 | Blender camera/template, sprite geometry, masks and motion/readability tests | Phases 019–020 and art phases | No new final visual asset was produced. The rules define what presentation must communicate. |
| L05 | Empirical run length, fair-loss score and player enjoyment | Playable/prototype and balance gates | A document or arithmetic test cannot establish those outcomes. Phase 003 standards remain obligations. |
| L06 | Shipping-name clearance | Existing Phase 002 naming process | Charterwake remains provisional. No store publication or trademark claim is made. |

## Tools and dependency record

Python standard-library checks are used only because this phase permits small examples/disposable verification to settle design questions. Tested on Python 3.13.5; the script uses Python 3.10+ syntax. There is no pip package, plugin, server, network requirement, shipped Python runtime or change to the repository's existing Godot/Blender pins. Removal path: port these JSON expectations to the later Godot test harness, retain the versioned design evidence, and remove the disposable script when no longer useful.

No Godot/Blender execution is claimed. This phase has no question requiring a production scene or final authored geometry. Actual engine-version/import validation belongs to the repository-bootstrap/pipeline gates. Existing pins are preserved as recorded, not independently advertised here as current releases.

## Originality and scope review

PASS for this phase's new material: the central object remains a physical command graph; no gaze rectangle, copied UI, copied asset, new currency, multiplayer, extra mode or extra biome is added. No third-party asset or library is imported, so the licensing register is unchanged. The only new folder is the phase-specific evidence folder required by the existing repository convention.
