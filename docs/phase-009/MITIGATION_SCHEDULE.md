# Phase 009 — Mitigation schedule

This schedule ties each risk family to the phase that can produce real evidence. Mitigation tasks do not make a later phase complete early.

| Window | Risks emphasized | Required mitigation/evidence | Primary owner |
| --- | --- | --- | --- |
| 009–010 | R005, R013, R021, R022, R023 | preproduction consistency, scope/cash/runway disposition, public-name risk, kill thresholds | Product |
| 011–020 | R007, R008, R015, R016, R020 | pinned toolchain, clean build/import, deterministic kernel, save foundation, dependency discipline | Engineering / Art Tools |
| 021–030 | R001, R002, R003, R025 | core-loop prototype, blind-description test, fresh-player comprehension/retry cohort | Design / UX / QA |
| 031–040 | R004, R012, R015, R016 | forecast/combat/fair-loss fixtures, same-seed/speed behavior, causal defeat explanation | Design / Engineering |
| 041–050 | R009, R018 | structural doctrine differences, distinct structure jobs, content-ceiling audit | Design / Product |
| 051–061 | R010, R018 | enemy/boss counter diversity, upgrade/event role audit, run-director pressure | Design / Balance |
| 062–070 | R011, R006 | run pacing, tutorial/post-run behavior, VFX/animation throughput checkpoint | UX / Art / Tools |
| 071–080 | R006, R024 | final-art throughput, asset provenance, audio/text scope, source-string discipline | Art / Audio / Writing |
| 081–090 | R017, R019, R024 | accessibility, controller, resolutions, performance, saves, localization pipeline | UX / Engineering |
| 091–100 | R010, R012, R014, R019, R020, R025 | balance sweeps, automated tests, platform/export, demo QA and fresh-player demo cohort | QA / Engineering / Product |
| 101–110 | R001, R013, R021, R025 | title/store/marketing rights, public feedback synthesis, evidence-based revision, content lock | Product |
| 111–116 | R016, R017, R019, R022, R023, R026 | alpha/beta/RC blockers, localization QA, depot/config, launch rollback/support | Product / QA / Engineering |
| 117–120 | R026 | support load, hotfix learning, postmortem, maintenance/future-roadmap decision | Product / Support |

## Owner obligations

An owner must attach one of:
- test/fixture result;
- playtest/session record;
- profile/export measurement;
- source/license record;
- budget/schedule forecast;
- explicit owner decision.

“Monitoring” without a next evidence gate is not a mitigation.

## Risk closure

Close a risk only when:
1. the trigger has been tested at the appropriate scale;
2. evidence is linked;
3. no known blocker remains;
4. recurrence conditions are defined if the risk can return.

Risks such as scope creep, performance regression, accessibility, title rights, and save safety remain recurrent WATCH items through launch even after one green gate.
