# Phase 005 — Scope budget and content ceiling

Project: **Charterwake: The Last Relay** (provisional title)  
Baseline: **scope v1.0**, 2026-09-22; core rules remain **1.0.0**  
Entry: `ad04e3cf519c5c839c5a897837c630dc88829dcb`  
Status: **APPROVED PREPRODUCTION BUDGET BASELINE**

## Authority and interpretation

`SCOPE_CEILINGS.json` is the machine-readable budget contract. `scope_budget.xlsx` is the formula-driven review workbook. This document explains counting rules and controls. No runtime content catalog or shipping dependency is introduced.

The authoritative bible supplies 24 non-combat structures, nine combat structures, 15 ordinary enemies, three bosses, four doctrines, about 45 run upgrades, 24 systemic events and six Oaths. Phase 005 freezes the approximately-45 upgrade target as an exact **45-entry ceiling**. Twenty doctrine-exclusive upgrades are INCLUDED, not additional. Unique starting structures use entries inside the structure ceiling. Keep is one of the 24 non-combat structures. Tiers, modes and cosmetic variants cannot conceal extra strategic entries.

The art, text, cue, cash allocation and effort values below are **planning decisions**, not empirical throughput measurements, vendor quotations, legal clearance or spending approvals. Unknown living costs and available cash stay blank, never silently zero.

## 1. Content ceilings and staged subsets

| Category | Toy | MVP | Demo | Launch cap | Counting rule |
| --- | ---: | ---: | ---: | ---: | --- |
| Civilian/network (Keep included) | 6 | 6 | 7 | 24 | All doctrine starting structures count inside this cap. |
| Combat structures | 0 | 2 | 3 | 9 | Crews/emblems, not independently simulated armies. |
| Standard enemies | 0 | 3 | 6 | 15 | One definition per strategically distinct type. |
| Bosses | 0 | 1 | 1 | 3 | Stages do not create additional boss identities. |
| Doctrines | 1 | 1 | 1 | 4 | Shared rules; doctrines do not become separate games. |
| Run upgrades (inclusive) | 0 | 8 | 12 | 45 | Includes twenty doctrine-exclusive upgrades. |
| Systemic events | 0 | 2 | 4 | 24 | Text variants do not count as strategic events. |
| Difficulty Oaths | 0 | 0 | 0 | 6 | Baseline difficulty is not an extra Oath. |
| Principal biomes/themes | 1 | 1 | 1 | 1 | Palette swaps do not authorize new biome content. |
| Principal run modes | 1 | 1 | 1 | 1 | Demo/test harnesses are subsets, not extra modes. |

### Toy — Phase 030 gate

Five planning rounds, six non-combat grayboxes: Keep, Croft, Timber Yard, Archive, Relay Post, Switchhouse. No combat/boss content. Roughly ten-minute non-combat core-loop test; no public-product quality claim.

### Combat MVP — Phase 040 gate

Internal five-Watch first-Act vertical slice: the same six structures plus Watchtower and Barricade; three standard enemy roles, one reduced Mute Colossus test, eight upgrades and two events. One doctrine context. Target 10–20 minutes.

### Public demo — Phase 100 gate

One doctrine (**Iron Charter**), ten total structures including Keep, six standard enemies, one Mute Colossus boss, twelve upgrades, four events and no Oaths. Curated first-Act arc: five Watches, 20–40-minute new-player target. Require two viable build directions, one understandable spectacular synergy, explainable failure, offline saves/settings, input/accessibility parity and safe retry.

### Launch — Phase 116 gate

Standard run stays 15 Watches, three Acts, bosses at 5/10/15, target 35–50 minutes. All 33 structure slots remain governed by the Phase 001 catalog. The demo is an allowlisted subset of the same validated content, never a fork.

## 2. Visual and animation budget

| Visual family | Source-set cap | Color-frame allocation |
| --- | ---: | ---: |
| Structure source sets | 33 | 99 |
| Standard enemy sets | 15 | 45 |
| Boss source sets | 3 | 36 |
| Terrain mark sets | 5 | 5 |
| UI and icon sets | 100 | 100 |
| Network/state sets | 18 | 36 |
| Combat effect sets | 20 | 40 |
| Marketing compositions | 8 | 8 |
| Doctrine emblems | 4 | 4 |
| Board/prop sets | 14 | 16 |

**220 authored visual sets; 389 allocated color-frame slots; hard ceiling 400.** Baseline export accounting reserves up to five required passes per frame. Functional states, non-color warnings, controller focus and accessibility masks are protected.

Blender remains the later source-of-truth asset tool. No final Blender work, render, font import or Godot asset acceptance is claimed here.

## 3. Text and localization

Launch source text ceiling: **12,000 words**. Demo source text ceiling: **4,000 words**. Source English is mandatory. Capacity is reserved for **at most two additional target languages**, chosen later from budget and audience evidence; no locale is promised.

Cuts remove optional lore and verbosity first. Rules, accessibility notices, fair-loss explanations, required tutorials and decisive warnings cannot be cut merely to meet a word count.

## 4. Audio and music

**76 non-music cue identities and 180 variant recordings.** Five adaptive pieces are the target, seven the absolute cap, at most four stems per piece and 24 minutes of unique composition. No voice-acting scope. Critical Keep, boss and network-failure cues retain mix priority at accelerated speed.

## 5. Performance, installation and platform workload

| Metric | Threshold |
| --- | ---: |
| Baseline frame rate | 60 fps minimum |
| Playable fallback | 30 fps minimum |
| Process memory | 1,900 MB decimal maximum |
| Installed launch build | 1,800 MB decimal maximum |
| Resident texture allocation | 512 MB decimal maximum |
| Board graph rebuild | strictly under 1 ms |
| Full combat tick | strictly under 2 ms |
| Scene transition | strictly under 3 seconds |

All are **targets, not measured results**. Launch verification covers Windows 10/11, Linux and Steam Deck; mouse+keyboard, keyboard-only and controller; 16:9, 16:10 and 21:9 layouts where applicable. No macOS/console/mobile commitment is added.

Install allocation totals **1,500 MB**, leaving 300 MB headroom inside the 1,800 MB ceiling.

## 6. External cash envelope — USD planning allowances

External scenario totals including 20% contingency:

- **Lean: $4,320** inside a $5,000 ceiling.
- **Base: $12,600** inside a $15,000 ceiling.
- **Stretch: $18,480** inside a $20,000 ceiling.

These are top-down planning allowances, not purchases, vendor quotes or spending authorization. Personal living runway is separate and remains **UNSET** until supplied.

The 15-month capacity model yields 1,920 productive prelaunch hours, with 1,320 allocated and 600 unallocated (**31.25% reserve**). An unchanged 12-month scenario leaves only **14.06% reserve**, below the 20% target, and is therefore AMBER rather than endorsed.

## 7. Change control and safe phase closure

Use `CUT_LADDER_AND_REVIEW.md` and `MILESTONE_MAP.md`. Every cap has an owner and measurement route. Propose changes in a new revision, compare the delta, rerun validation and retain the prior revision. Invalid proposed data must fail without altering the accepted model.

The next gate after remote closure is **Phase 006 — Working title and brand vocabulary**.