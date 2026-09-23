# Phase 007 — Design change request template

Copy this file for every proposed change that alters an accepted design baseline. Do not overwrite the template.

## Change identity

- Change ID: CR-YYYY-NNN
- Title:
- Requester:
- Date:
- Status: PROPOSED / REVIEW / APPROVED / REJECTED / REVERTED
- Owning phase or system:
- Target version:

## 1. Player problem and evidence

What player problem is being solved?

Evidence:
- playtest, session, or fixture:
- bug or issue:
- measured result:
- source link or commit:

Do not justify a change with “more content,” “more realistic,” or “looks better” alone.

## 2. Current accepted behavior

Quote or link the exact accepted source:
- GDD section:
- Core Rules section:
- scope ceiling:
- content ID:
- UX or accessibility requirement:

## 3. Proposed behavior

Describe the new rule in player-visible terms.

Include:
- trigger;
- authoritative state inputs;
- deterministic ordering;
- output;
- failure or rejection behavior;
- preview and tooltip effects;
- undo and reload implications.

## 4. Change classification

- Clarification — no behavior or scope change
- Bounded design change — behavior changes inside existing ceilings
- Rules change — Core Rules version impact
- Scope change — content, time, cash, platform, or asset ceiling impact
- Public-name or brand change
- Save, schema, or migration change

## 5. Impact analysis

### Product pillars

For each P1–P6: improves, neutral, or harms, with explanation.

### Scope

Before → after:
- systems;
- structures;
- enemies or bosses;
- upgrades, events, or Oaths;
- visual sets and frames;
- source words;
- audio;
- labor hours;
- external cash;
- install and memory.

If no measured estimate exists, state UNKNOWN. Never write zero by default.

### Technical

- deterministic simulation;
- content schema;
- save version and migration;
- RNG and replay;
- performance;
- offline behavior;
- dependencies or plugins.

### UX and accessibility

- mouse and keyboard;
- keyboard-only;
- controller;
- UI scaling;
- non-color cues;
- reduced motion or flashes;
- tutorial or codex changes.

### Originality and IP

- closest reference mechanic;
- structural difference;
- new names, assets, or licenses;
- public-name or trademark effect.

## 6. Alternatives considered

At least:
1. no change;
2. smallest alternative;
3. proposed option.

Explain why the proposed option is worth its cost.

## 7. Acceptance tests and evidence

List exact:
- normal case;
- boundary case;
- failure case;
- recovery or rollback case;
- deterministic fixture;
- save or migration fixture if relevant;
- accessibility or input path;
- performance budget proof if relevant.

Never weaken an existing assertion merely to make the change pass.

## 8. Rollback

How can the change be safely reverted?

Specify:
- code and data rollback;
- save compatibility;
- content IDs;
- generated assets;
- marketing or public communication if applicable.

## 9. Required document updates

Check every affected artifact:
- GDD;
- Core Rules;
- scope model or budget;
- brand lexicon;
- architecture ADR;
- content manifests;
- save schema or migration;
- tests and fixtures;
- localization;
- store and marketing copy;
- closure evidence.

## 10. Decision

- Decision: APPROVE / REJECT / NEEDS EVIDENCE
- Decision owner:
- Date:
- Conditions:
- Approved commit or PR:
- Rules or GDD version after acceptance:

A proposal is not accepted merely because implementation code exists.
