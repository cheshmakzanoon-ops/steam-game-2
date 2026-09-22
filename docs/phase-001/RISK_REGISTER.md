# Phase 001 — Risk Register

**Status:** ACTIVE  
**Date:** 2026-09-22  
**Owner model:** project owner owns product/scope decisions; implementation owners must attach mitigations and evidence before closing a risk.

Scale: **Likelihood** and **Impact** use Low / Medium / High / Critical.

| ID | Risk | Likelihood | Impact | Trigger / early warning | Mitigation | Owner | Exit evidence |
|---|---|---|---|---|---|---|---|
| R01 | Signalhold is perceived as a clone of The King is Watching or another compact kingdom title | High | Critical | Store GIF/screenshot can be described mainly by reference-game language | Make physical port/relay/switch/Load routing visible from first prototype; Phase 002 originality matrix; unique paper/woodcut language | Product | Originality gate + blind description test |
| R02 | Command scarcity is annoying rather than strategically interesting | Medium | Critical | Players treat power assignment as busywork or obvious toggling | Prototype the network before content production; remove repetitive controls; ensure several viable allocations | Design | Testers voluntarily retry and discuss alternate routing/priorities |
| R03 | One-board readability collapses as systems accumulate | High | Critical | Tooltips/menus become required to know basic activation/threat state | Hard state hierarchy; overlays; restrained palette; resolution/controller tests; remove low-value state | UX | Core state readable at gameplay zoom across target aspect ratios |
| R04 | Random offers overwhelm player agency | Medium | High | Frequent restart fishing or losses blamed on unavailable counters | Forecast threats; rerolls/banishes/weighting; sidegrade pools; seeded balance sweeps | Design/Simulation | Same-seed reproducibility + fair-loss playtest evidence |
| R05 | Scope expands beyond solo-production ceiling | High | Critical | New biome/mode/system/content family appears without removing equivalent work | Enforce APPROVED_SCOPE.md; Class C changes require owner approval + schedule/risk update | Product | Milestone scope audit remains within ceilings |
| R06 | Art pipeline becomes the schedule bottleneck | High | High | Unique manual setup/export work per asset; inconsistent camera/palette | Locked Blender template, modular library, batch exporter, strict silhouette-first process | Art/Tools | Clean batch regeneration from source |
| R07 | Blender version mismatch breaks the bible's reproducible 4.x pipeline | Medium | High | Assets authored in unpinned 5.x environment or incompatible Python/API | Pin Blender 4.5.14 LTS for this repo; reject production assets made with a different version unless ADR-approved | Art/Tools | Version capture in asset manifests and batch logs |
| R08 | Engine upgrades destabilize deterministic behavior or imports | Medium | High | Unplanned upgrade because newer Godot exists | Pin Godot 4.7.2-stable; upgrades need ADR, branch test, rollback and full gate | Engineering | Reproducible clean project on pinned engine |
| R09 | Doctrines become cosmetic percentage variants | Medium | High | Doctrine identity appears only in numeric modifiers | Require one structural rule change per doctrine and doctrine-specific starting behavior | Design | Cross-doctrine playtests produce different routing/build patterns |
| R10 | One dominant build invalidates replayability | Medium | High | High-difficulty runs converge on same structures/priority | Balance harness, doctrine/boss matrix, nerf interactions rather than add filler content | Design | Multiple viable archetypes across representative difficulty |
| R11 | Run length exceeds 50 minutes through housekeeping | Medium | High | Late Watches contain obvious but numerous maintenance clicks | Automate upkeep; speed/skip known resolution; remove redundant actions/content | Design/UX | External median/typical runs remain in target envelope |
| R12 | Losses feel opaque or unfair | Medium | Critical | Player cannot identify decisive chain after defeat | Forecast rules; inspectable calculations; deterministic ledger; post-run causal reconstruction | Design/UX | Blind players can explain why they lost |
| R13 | Market research is overinterpreted as a sales forecast | Medium | High | Planning assumes breakout-comparable revenue or wishlist velocity | Treat market data as demand-shape evidence; use ranges/caveats; refresh before commercial commitments | Product | Commercial decisions cite current primary evidence |
| R14 | Public demo launches before the core is compelling | Medium | High | Festival deadline starts driving feature/polish shortcuts | Demo only after readable board, distinct builds, trailer-worthy synergy and fair loss are demonstrated | Product/QA | Formal demo go/no-go gate |
| R15 | Technical architecture mixes simulation with UI/presentation | Medium | Critical | UI nodes become authoritative state; animations affect outcomes | Typed deterministic simulation separate from input/rendering; validated data resources; tests first | Engineering | Headless deterministic fixtures |
| R16 | Save/replay determinism is designed too late | Medium | Critical | Same seed diverges by speed/input timing; migrations ad hoc | Seeded RNG ownership, explicit ordering, schema versioning, golden fixtures from early systems phases | Engineering | Same-seed/speed reproducibility |
| R17 | Accessibility/controller support becomes late rework | Medium | High | Core interaction assumes hover, tiny targets, or color-only state | Every relevant phase checks focus, controller and non-color cues; scalable UI | UX | Controller-only complete flow + high-contrast/UI-scale checks |
| R18 | Content quantity substitutes for strategic depth | Medium | High | Requests add buildings/enemies because runs feel same | Fix interactions first; only add content inside ceiling when it creates a distinct job/counter | Product/Design | Every retained item has a unique strategic role |
| R19 | Performance/memory grows from oversized rendered assets and effects | Low | Medium | Full-resolution source assets leak into runtime; excessive overlays/VFX | Generate engine-ready assets separately; budgets; downsample; profile representative board states | Engineering/Art | Performance budgets green on target hardware |
| R20 | Dependencies or services create removal/availability risk | Low | High | Plugin/SDK added without rationale/pin/fallback | No new dependency without recorded need, pin, removal path and offline behavior | Engineering | Dependency register and clean offline build |

## Top five risks for the next gates

1. **R01 — clone perception**
2. **R02 — Command mechanic quality**
3. **R03 — board readability**
4. **R05 — scope expansion**
5. **R07/R08 — reproducible toolchain**

Phase 002 should directly reduce R01. Early prototype phases must reduce R02/R03 before high-volume art or content work begins.
