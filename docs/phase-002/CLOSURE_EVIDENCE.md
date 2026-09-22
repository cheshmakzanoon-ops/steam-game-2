# Phase 002 — Closure Evidence

**Phase:** 002 — Originality boundary and IP safety  
**Status:** COMPLETE / GREEN  
**Closure date:** 2026-09-22  
**Entry baseline:** Phase 001 closure at 6c9ca0d7d45ba9c6cad50e22d8de0639e9775977  
**Phase 002 implementation commit:** 9755bf2e884eebd6c658c8f2751619a8531f48a7  
**Branch:** main

## 1. Bible deliverables

All required Phase 002 deliverables are present:

- Originality brief — ORIGINALITY_BRIEF.md
- IP checklist — IP_CHECKLIST.md
- Licensing register template — LICENSING_REGISTER.csv
- Naming-validation plan — NAMING_VALIDATION_PLAN.md

Additional work-package evidence:

- Third-party licensing rules — THIRD_PARTY_LICENSING_POLICY.md
- Original abstract visual reference board — visual_reference_board.svg
- Visual-board rationale/guardrails — VISUAL_REFERENCE_BOARD.md
- Mandatory milestone originality review — ORIGINALITY_REVIEW_GATE.md
- Root README updated to the Phase 002 gate and working-title warning

## 2. Work-package closure

| Required work | Evidence | Result |
|---|---|---|
| Map every major reference mechanic to an original alternative | ORIGINALITY_BRIEF.md reference-to-original matrix | PASS |
| Ban copied names, layouts, icons and progression | ORIGINALITY_BRIEF.md banned imitation zones + IP_CHECKLIST.md | PASS |
| Define command-network distinction | ORIGINALITY_BRIEF.md command-network section | PASS |
| Define undo, reload and failure behavior around network authority | ORIGINALITY_BRIEF.md contracts | PASS |
| Create visual reference board from broad historical/material sources | visual_reference_board.svg + VISUAL_REFERENCE_BOARD.md | PASS |
| Write trademark/naming procedure | NAMING_VALIDATION_PLAN.md | PASS |
| Define third-party licensing rules | THIRD_PARTY_LICENSING_POLICY.md + CSV register | PASS |
| Add originality review gate to milestones | ORIGINALITY_REVIEW_GATE.md | PASS |
| Record prohibited lookalike marketing claims | ORIGINALITY_BRIEF.md public-marketing rules | PASS |

## 3. Material IP finding

A preliminary public screen performed during Phase 002 found an existing UK application for the word SIGNALHOLD:

- application: UK00004235663;
- filed: 2025-07-17;
- journal publication: 2025-08-01;
- listed classes: 9, 41, 42;
- software-related goods/services are present.

This Phase does **not** determine infringement, registrability or legal clearance.

The production consequence is explicit: **Signalhold: The Last Relay remains a working title only.**

The naming plan marks the title RED / PROVISIONAL and blocks title-dependent public/store investment until fuller clearance and owner disposition, with qualified legal advice where warranted.

Official UK journal record:
https://www.ipo.gov.uk/t-tmj/tm-journals/2025-031/UK00004235663.html

## 4. Current official search resources verified

The naming procedure records current official search entry points for:

- CIPO Canadian Trademarks Database;
- USPTO Trademark Search;
- UK IPO trade-mark search;
- EUIPO / TMview;
- WIPO Global Brand Database.

The procedure requires both official-register searches and common-law/market searches. A zero-result quick search is never treated as legal clearance.

## 5. Repository verification

After the implementation commit, every required Phase 002 file was fetched back from main.

Automated content checks performed against the committed GitHub files returned PASS for:

- all required files non-empty;
- README Phase 002 status;
- reference-to-original mapping present;
- command-network distinction present;
- prohibited marketing claims present;
- UK naming-risk record present;
- RED / PROVISIONAL title status present;
- third-party prohibited-license rules present;
- licensing-register schema present;
- milestone originality gate present;
- SVG begins/ends as an SVG document;
- SVG contains no external raster/image href reference.

No build/gameplay command was run because Phase 002 explicitly does not authorize production gameplay merely for visible progress and the repository still has no game project.

## 6. Acceptance-gate review

### Clean reproducibility — PASS

All Phase 002 production controls are plain-text/SVG/CSV artifacts under version control. A clean checkout reproduces the Phase output without an undocumented local dependency.

### Deliverable proof — PASS

The four named deliverables exist and the eight work-package requirements have concrete repository evidence.

### Normal/boundary/failure behavior — PASS FOR PHASE SCOPE

- normal path: original project-authored or clearly licensed work enters production through the register/checklists;
- boundary path: ambiguous licenses, similar marks and reference-adjacent designs enter REVIEW/AMBER status rather than being silently accepted;
- failure path: RED naming/IP issues and failed originality checks block public use or later milestone closure until corrected/disposed.

### Prior baseline remains green — PASS

Phase 001 documents remain intact. No gameplay code, saves, imports, engine assets, plugins, dependencies, controller paths or export configuration were modified because none exist yet.

## 7. Known non-blocking issue

The working title has an unresolved trademark-risk signal. This does not prevent internal preproduction from continuing because the project architecture is required to remain rename-safe. It **does** block treating the current title as legally/publicly cleared.

## 8. Safe entry condition for Phase 003

Phase 003 may begin from this main baseline if it:

1. preserves the Phase 001 product pillars and scope ceiling;
2. obeys Phase 002 originality/IP gates;
3. treats Signalhold as a provisional internal title;
4. adds no copied reference-game vocabulary/layout/art;
5. registers any new third-party production dependency;
6. produces the Phase 003 player-experience map, emotional pacing chart, fair-loss rubric and player-story set;
7. closes green before Phase 004 is claimed.

**Phase 002 is closed.**
