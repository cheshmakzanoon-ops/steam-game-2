# Phase 001 — Research-to-Feature Traceability

**Status:** BASELINE  
**Date:** 2026-09-22

This document connects market evidence to product decisions so later work can distinguish research-backed intent from accidental implementation.

## 1. Source register

### S1 — Market research

**Title:** *Market-Validated 2D Strategy Game Opportunity for a Solo Steam Developer*

Use for:
- market shape;
- audience;
- demand patterns;
- comparable games;
- anti-RNG and low-micro community themes;
- price hypothesis;
- production-scope rationale.

**Method limitation:** sales estimates are not audited unless publicly disclosed; community discussions are qualitative rather than representative surveys; publisher-backed successes indicate appetite and ceiling, not a guaranteed solo-sales forecast.

### S2 — Authoritative project bible

**Title:** *STEAM GAME NUMBER 2 — Master Production Prompt and Project Bible*

Use for:
- final product definition;
- product pillars;
- anti-pillars;
- core rules;
- content ceilings;
- architecture;
- art direction;
- phase order;
- acceptance requirements.

**Precedence:** S2 controls whenever S1 and S2 differ because the bible is the approved production specification derived from the research.

---

## 2. Traceability matrix

| ID | Research / product evidence | Locked decision | Product requirement | Verification path | Source |
|---|---|---|---|---|---|
| T01 | Strong demand signal for compact kingdom/base strategy with explosive synergies | Compact one-board kingdom/base strategy roguelite | Core strategic state fits one coherent play view | Board/UI readability tests and playtest observation | S1, S2 §§1–2 |
| T02 | Players praise accessible information and dislike menu drilling/micro | One-board readability | Activation, danger, output, damage, intent, resources and Command remain inspectable from play view | Usability gate; controller-only run; screenshot review | S1; S2 Pillar A |
| T03 | Community asks for more depth than ultra-minimal strategy without RTS micro | Low-friction but genuinely deep planning | Decisions center on network routing, priorities and structural combinations | Prototype testers discuss routing/prioritization rather than click speed | S1; S2 §§1,6 |
| T04 | Compact kingdom hits validate a small spatial toy | 9×9 charter board with central Keep | Board geometry stays intentionally constrained | Deterministic board model and edge/rotation fixtures | S1; S2 §§5–6 |
| T05 | Need an instantly explainable signature mechanic | Scarce physical command network | Ports, relays, loops, switches, Load and priorities are the central object | Core-loop graybox gate | S1; S2 §§1,6 |
| T06 | Players reject uncontrolled roguelike RNG and repeated restart fishing | Controlled randomness | Limited rerolls/banishes/weighting; visible future pressure; deterministic threat forecasting | Seed/replay tests; player loss explanation | S1; S2 §§1–2 |
| T07 | Players value fair, inspectable consequences | Transparent threats | Reveal/confirm next two pressure events and relevant rules before commitment | Forecast fixtures and UI acceptance | S1; S2 Pillar C, §5 |
| T08 | Demand exists for build discovery and dramatic synergies | Structural build diversity | Four doctrines change rules; network and upgrade interactions support multiple strategies | Doctrine comparison playtests and balance harness | S1; S2 Pillar D, §8 |
| T09 | Short strategy sessions are commercially legible | 35–50 minute normal victory | 15 Watches / 3 Acts / bosses at 5,10,15 | Timed external playtests and telemetry-free local session logs | S1; S2 Pillar E, §5 |
| T10 | Generic medieval pixel art is crowded | Paper-cut / woodcut / screen-print identity | Blender-authored layered paper reliefs rendered through locked orthographic pipeline | Silhouette, palette, export-manifest and in-engine capture review | S1; S2 §§1,9 |
| T11 | $15 tier clusters around relevant comparables | USD $14.99 launch-price hypothesis | Premium one-time purchase; no monetization systems in gameplay | Revalidate before store publication | S1, S2 header |
| T12 | Solo production collapses when content quantity becomes the value proposition | Strict content ceiling | Small system set; no hundreds of buildings/resources/professions | Scope audit at every milestone | S1; S2 §§3,8 |
| T13 | Content breadth must come from interactions, not separate subgames | Shared central rules | Doctrines share base systems and alter rules within them | Doctrine implementation review | S2 §8 |
| T14 | Automation/defense appeal does not require direct unit micro | Mostly automatic resolution | Production/Siege resolve after planning; no mandatory per-unit orders | Input-count review and combat tests | S1; S2 Pillar B, §5 |
| T15 | Offline premium scope protects solo feasibility | No online dependency | Core game functions without internet/account/server | Clean offline launch and run | S1; S2 operating instructions |
| T16 | Recent comparable successes are not reliable median-sales forecasts | No sales guarantee in scope | Market evidence informs product shape, not revenue promises | Commercial docs must label hypotheses and uncertainty | S1 limitations |
| T17 | Clone perception is the principal differentiation risk | Original network architecture and visual language | No gaze-rectangle imitation, copied layout, names, resources or progression | Phase 002 originality/IP gate | S1; S2 §3 |
| T18 | A weak public demo can waste a major discovery opportunity | Demo follows mature core | Public demo is treated as product, not disposable prototype | Later demo acceptance gate | S1, S2 production plan |
| T19 | Premium presentation improves differentiation | Authored, reproducible visual pipeline | Blender source of truth; Godot runtime source of truth | Batch regeneration and asset-manifest tests | S2 operating instructions, §9 |
| T20 | Market gap combines clarity + agency + replayability | Fair-loss standard | Player should be able to explain the decisive failure chain | Post-run explanation and blind playtest interviews | S1; S2 §§1,5 |

---

## 3. Comparable learning matrix

| Comparable | Learn from | Do not copy |
|---|---|---|
| 9 Kings | Compact kingdom grid, escalating synergies, autobattle payoff | Exact drafting/content/progression, names, layouts or art |
| The King is Watching | Scarcity/activation tension and readable small kingdom | Gaze-shaped activation, layout, resources, progression or pixel look |
| Thronefall | Low-friction defense and readable strategic choices | Exact economy/defense structure or visual identity |
| Into the Breach | Transparent intent and consequences | Grid combat rules or unit systems |
| Shogun Showdown | Information clarity, sequencing, short replayable structure | Lane/action-tile rules or visual treatment |
| dotAGE | Forecasting and long-range planning | Content-volume ambition; worker/profession simulation |
| Mindustry | Network/logistics + defense appetite | Factory-belt sprawl or RTS scope |
| Stacklands | Simple spatial grammar generating emergent combinations | Card-stack village structure |
| Backpack Battles | Spatial synergy discovery and build expression | Inventory-grid combat loop |
| Kingdom Two Crowns | Readable atmosphere and low-micro pressure | Side-scrolling kingdom structure |
| Drop Duchy | Familiar physical grammar carrying strategy | Falling-block/card hybrid mechanics |
| Slipways | Strategic compression and minimal micro | Galaxy-network theme/rules |

---

## 4. Evidence confidence rules

1. Publicly disclosed sales/wishlist milestones outrank model-based estimates.
2. Review counts indicate engagement but are not equivalent to unit sales.
3. Reddit, Steam forum, and itch.io comments identify recurring themes; they are not population estimates.
4. Publisher-supported breakout performance must not be treated as a guaranteed solo baseline.
5. X/Twitter evidence in the original research is sparse and must not be padded with invented sentiment.
6. If a market claim becomes important to pricing, launch timing, or platform strategy later, refresh it against current primary sources before acting.

---

## 5. Traceability maintenance rule

Any feature proposed after Phase 001 must map to at least one of:

- a product pillar;
- a documented player problem;
- a required platform/accessibility/quality constraint;
- a later explicit bible phase.

If it maps to none, it is presumed scope creep until approved through change control.
