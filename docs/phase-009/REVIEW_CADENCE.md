# Phase 009 — Risk review cadence

## Every phase closure

Before calling a phase green:

1. Ask whether the phase created a new risk.
2. Recheck risks whose evidence gate is the current phase.
3. Record any score/status change.
4. Check all hard kill/red-line criteria relevant to the phase.
5. Link accepted evidence in closure notes.
6. Do not close the phase if a BLOCKING risk contradicts its acceptance gate.

## Weekly during active production

Use the Phase 008 dashboard.

Review:
- all CRITICAL and HIGH risks;
- any BLOCKING risk;
- new risks since last review;
- schedule reserve use;
- scope-change requests;
- dependency/toolchain changes;
- upcoming evidence gates.

Weekly review can leave stable MEDIUM/LOW rows unchanged if their next evidence gate is still valid.

## Monthly

Perform full register review:

- every open risk;
- score freshness;
- Phase 005 ceilings and cash scenario;
- Phase 008 contingency consumption;
- actual versus forecast developer-days;
- art/text/audio/install exposure;
- public-name and license status;
- personal living-runway status only as a private owner disposition, never repository amount unless the owner explicitly wants that.

Monthly outcomes:
- KEEP;
- MITIGATE;
- CUT;
- REBASELINE;
- ESCALATE TO STOP/PIVOT REVIEW.

## Formal stop/pivot reviews

Use the Phase 008 review points with Phase 009 criteria:

- Phase 010 preproduction;
- Phase 030 prototype;
- Phase 040 vertical slice;
- Phase 070 throughput;
- Phase 100 demo;
- Phase 107 feedback synthesis;
- Phase 112 beta shipability;
- Phase 114 release candidate.

The review records:
- relevant risks and scores;
- hard criteria results;
- contingency remaining;
- alternatives;
- chosen action;
- owner decision;
- resulting baseline commit.

## Incident review

Immediately run an out-of-cycle risk review when any of these occurs:
- save corruption/data loss;
- deterministic outcome divergence;
- rights/license conflict;
- unsupported online dependency becomes mandatory;
- severe accessibility/input blocker;
- material scope/cash overrun;
- critical crash on supported platform;
- security/privacy issue from a new dependency or service.

The outcome is fix/cut/rollback/pivot/stop. Schedule pressure cannot suppress the review.

## Register history

Do not rewrite old evidence. If a score changes, record the new score and evidence in the next accepted revision/commit. Git history is the audit trail.
