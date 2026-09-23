# Phase 008 — Dependency graph and critical path

**Project:** Charterwake: The Last Relay  
**Status:** APPROVED ROADMAP BASELINE  
**Entry baseline:** Phase 007 closure at `0910d58e44f4fec9255c30cb230ae586f0d4d1f4`  
**Planning rule:** dependencies describe acceptance order; they do not claim future work is complete.

## Staffing assumption

The baseline assumes one solo generalist owner. Phase 005 models 40 nominal hours/week at 80% project focus, or 32 effective project hours/week. Agents, automation, and short-lived helpers can reduce friction but **do not multiply accepted developer-day capacity**. Optional external specialist work is bounded by the Phase 005 cash envelope and never owns the product decision.

## Hard acceptance graph

The bible requires each phase's prerequisite gates to be green, merged, documented, and reproducible. Therefore the acceptance path to launch is sequential through Phase 116, followed by post-launch Phases 117–120.

~~~mermaid
flowchart LR
  P001[001 Charter] --> P010[010 Preproduction gate]
  P010 --> P020[020 Foundation calibrated]
  P020 --> P030[030 Prototype]
  P030 --> P040[040 Vertical slice]
  P040 --> P050[050 Core structures]
  P050 --> P060[060 Boss content]
  P060 --> P070[070 Animation system]
  P070 --> P080[080 Music / narrative]
  P080 --> P090[090 Reliability]
  P090 --> P100[100 Demo gate]
  P100 --> P110[110 Content/presentation lock]
  P110 --> P111[111 Alpha]
  P111 --> P112[112 Beta]
  P112 --> P114[114 Release candidate]
  P114 --> P116[116 Launch]
  P116 --> P120[120 Final acceptance]
~~~

The diagram is compressed only for readability. `PHASE_ESTIMATES.csv` records the exact hard predecessor for every phase.

## Critical-path interpretation

- Every Phase 001–116 gate is acceptance-critical to launch.
- Phases 117–120 remain sequential after launch.
- A blocked gate blocks later acceptance even if unrelated-looking assets already exist.
- Preparatory work may start early only when reversible, clearly marked as preparation, and not treated as a completed future phase.

## Parallel-safe preparation lanes

“Parallel” means safe overlap during blocked/waiting time or bounded specialist assistance. It does not multiply one developer into multiple FTEs.

| Lane | Earliest safe preparation | Safe early work | Must wait for owning gate |
| --- | --- | --- | --- |
| Art | accepted brand/GDD | reference boards, silhouette questions, asset inventory, provenance research | final source assets wait for Phase 019/020 pipeline and Phase 071 art-bible lock |
| Audio | rights controls + GDD event vocabulary | recording plan, library provenance, cue taxonomy | final production waits for implemented events and Phase 079/080 |
| Writing | Phase 006 lexicon + Phase 007 GDD | optional codex outlines, terminology/localization notes | final tutorials/events/store copy wait for owning mechanics/content lock |
| QA/test design | relevant rule accepted | fixture plans, expected invariants, hardware matrix | execution/sign-off waits for implementation/export |
| Marketing research | naming risk + scope accepted | audience research and shot-list hypotheses | public title-dependent assets wait for clearance and gameplay evidence |

## Explicitly not parallel-safe

- later runtime systems before deterministic kernel/schema foundations;
- final art before pipeline calibration and art-bible lock;
- public demo/store commitments before demo acceptance;
- localization production before source strings/content stabilize;
- release configuration before release-candidate quality gates.

## Cross-system dependency spine

1. Rules/GDD → deterministic kernel.
2. Kernel → schema/save/input/UI.
3. Blender authoring template → import calibration.
4. Board → network → economy.
5. Economy → threat/combat.
6. Combat core → doctrines/structures/content.
7. Content → progression/onboarding/post-run.
8. Playable content → feel/VFX/animation/final art/audio.
9. Feature-complete presentation → accessibility/performance/save/reliability.
10. Stable platform build → Steam/demo.
11. Demo evidence → marketing/feedback/revision/content lock.
12. Content lock → alpha/beta/localization/RC/launch.

A new dependency edge requires a Phase 007 design change record and roadmap update.
