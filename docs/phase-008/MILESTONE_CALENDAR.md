# Phase 008 — Relative milestone calendar

**Calendar type:** relative capacity windows, not booked dates.  
**Target:** 12–15 months full-time planning; 18-month safety ceiling.  
**Capacity:** 240 productive pre-launch developer-days; 165 planned phase-days + 75 protected contingency days.

This roadmap deliberately avoids release dates. Re-baseline after evidence gates instead of converting uncertain work into promises.

| Window | Phase band / checkpoint | Planned days | Confidence | Exit evidence |
| --- | --- | ---: | --- | --- |
| M1 | 001–010 preproduction | 8.75 | High | Phase 010 preproduction approval |
| M2 | 011–020 foundation | 12.50 | Medium | boot/build/tests/save/input/UI + Blender/Godot calibration |
| M3 | 021–030 graybox toy | 13.75 | Medium | **Prototype** gate |
| M4 | 031–040 combat core | 15.00 | Medium | **Vertical slice** gate |
| M5 | 041–050 doctrines/structures | 13.75 | Medium | bounded core content |
| M6 | 051–060 enemies/events/bosses | 13.75 | Medium | content envelope + three bosses |
| M7–M8 | 061–070 pacing/progression/feel/VFX/animation | 20.00 | Low–Medium | full-run structure + feel/animation systems |
| M8–M9 | 071–080 final art/audio/text | 15.00 | Low | reproducible final presentation inside caps |
| M9–M10 | 081–090 accessibility/reliability | 13.75 | Medium | accessibility, performance, saves, localization pipeline |
| M10–M11 | 091–100 testing/platform/demo | 13.75 | Medium | **Demo** Phase 100 gate |
| M11–M12 | 101–110 market/feedback/content lock | 8.75 | Low–Medium | feedback decision + content lock |
| M12–M15 | 111–116 release sequence | 16.25 | Low | **Alpha 111 → Beta 112 → RC 114 → Launch 116** |
| M15–M16 | 117–120 post-launch | 10.00 | Low | support/postmortem/final acceptance |

## Named milestones

- **Prototype — Phase 030:** graybox core loop accepted; not a public demo.
- **Vertical Slice — Phase 040:** forecast/combat/fair-loss loop accepted.
- **Demo — Phase 100:** demo boundary, onboarding, compatibility, and QA green.
- **Alpha — Phase 111:** full-run stability phase.
- **Beta — Phase 112:** external beta evidence and triage.
- **Release Candidate — Phase 114:** reproducible candidate; only release-blocking changes.
- **Launch — Phase 116:** depot/pricing/support/rollback/communication gate green.

## Confidence rule

Confidence describes estimate uncertainty, not quality. Low-confidence work receives extra review and reserve protection; it does not get weaker acceptance criteria.

## Re-baseline rule

Re-estimate remaining work after Phases 010, 030, 040, 070, 100, 107, 112, and 114. Preserve actual accepted history. Never rewrite old estimates to make the roadmap appear accurate in hindsight.
