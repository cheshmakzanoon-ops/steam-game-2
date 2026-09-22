# Phase 004 — Core rules lock v1.0.0

**Project:** Charterwake: The Last Relay (provisional working title)
**Rules version:** 1.0.0
**Date:** 2026-09-22
**Scope:** normative preproduction contract, worked examples and disposable verification; not a playable game.

## 1. Authority, versioning and ownership

The controlling source is *STEAM GAME NUMBER 2 — Master Production Prompt and Project Bible*, uploaded as `steam%20game%20number%202(1).md`. The owner-authorized rename changes the title, not the design. Source locations and distinctions between inherited rules and new decisions are in [DECISIONS_AND_QUESTIONS.md](DECISIONS_AND_QUESTIONS.md).

`MUST` is a rule, not a suggestion. This specification closes the baseline ambiguities for Phase 004. It does not claim the later simulation, content, save, input, art or export phases are implemented. The production implementation remains typed GDScript in Godot, with Blender as the authored-visual source. `verify_rules.py` is an offline, disposable mathematical/design probe, not a second shipping engine.

`rule_examples.json` owns the machine-readable constants and worked examples for this version. Narrative numbers here are checked against it where the verifier states coverage. Runtime content will be validated resources in the later content-schema phase, not ad-hoc imports of this probe. Port the examples into the future Godot tests; do not make the production game depend on Python.

A change to ordering, state transitions, geometry, rounding, meaning of an identifier or failure precedence requires a rules-version change, a decision record and updated expected examples. Balance-only changes require a separately versioned content profile. Do not silently reinterpret old saves. Stable content and instance IDs never use the marketing title. Source/reference records from completed earlier phases remain intact.

**Authoritative ownership:** one run session owns the board, resources, RNG state, Watch, phase, content/rules versions, command journal and event log. UI, animation, audio, focus and rendering speed cannot change results. Preview and eventual runtime resolution must call the same implementation; the present probe only checks selected rule examples.

## 2. Board coordinates, Keep and entries — BRD

The standard board is exactly 9 by 9. Coordinates are zero-based: `(0,0)` is northwest; x increases east, y increases south. `index = y * 9 + x`; inverse is `(index % 9, index // 9)`. Valid indices are 0 through 80 inclusive. Reject out-of-range coordinates before array access. There is no wraparound, including between indices 8 and 9.

The Keep occupies `(4,4)`, index 40, in every standard run. It owns four basic ports, is the sole ordinary Command source, consumes no Load itself, and cannot be moved, dismantled, rotated or made Dormant. Its Crown Relay is the same survival objective, not a second hidden health bar.

Baseline entries are the four center-edge cells: north `(4,0)/4`, east `(8,4)/44`, south `(4,8)/76`, west `(0,4)/36`. They are reserved from normal construction. Other perimeter cells are buildable subject to terrain and occupancy, preserving frontier choices. Thus an unmarked board has 76 ordinary buildable cells: 81 minus Keep minus four entries. Enemies sharing an entry are ordered by stable instance ID; an entry is never silently relocated because it is busy.

A baseline structure occupies one cell. Later larger footprints use a unique anchor and an explicit rotated occupied-cell list; all cells must be valid, unreserved and non-overlapping. They do not enlarge the board. Keep, an entry, a blocking terrain mark, a living structure and rubble block ordinary placement. Placement checks every affected cell before mutation. An illegal placement/rotation is a rejected command with no cost, ID allocation or RNG consumption.

A declared enemy route is an ordered cardinal cell sequence from a declared entry toward its objective; no diagonal steps, wrapping or repeated-cell cycles in the baseline. The baseline straight lanes are `4,13,22,31,40`; `44,43,42,41,40`; `76,67,58,49,40`; `36,37,38,39,40`. Routes are not a second map. A living blocking structure in the next route cell stops normal movement before that cell; the enemy attacks the blocker from the adjacent cell under its announced attack rule. The Keep similarly blocks the final step. Exceptional movement/targets must be declared by content and forecast, not secretly chosen after commitment. Rubble blocks construction but not these baseline enemy routes.

Terrain is a small set of visible marks, not a terrain simulator. The minimal verification board has no marks. A later generator must validate legal starts, legal threat routes and at least two reasonable expansion directions. A specialized starting blueprint without required terrain is invalid content, not player defeat.

## 3. Ports, rotation and switches — PRT

Direction order is `N=0, E=1, S=2, W=3`, with vectors `(0,-1),(1,0),(0,1),(-1,0)`. A port mask uses those four bit positions. One clockwise quarter-turn maps each direction `d` to `(d+1)%4`; counterclockwise maps to `(d+3)%4`. Four turns restore the exact state. Rotate footprint offsets, local port positions, switch tabs and directional attack arcs together. The default one-cell cost of rotation or priority editing during planning is zero.

A physical adjacent edge exists only when both living endpoints have facing, compatible, enabled ports. Basic connects to basic; no one-sided connection, diagonal connection or implicit crossing. Specialized compatibility is an explicit symmetric content table; missing types/pairs fail validation instead of silently becoming basic. A zero-port defensive structure is permitted where explicitly declared (for example the bible's non-Iron-Charter wall); it is not an invisible connector.

Store switches as `link_enabled=true/false`; avoid ambiguous electrical uses of the words open/closed. Either endpoint disabling the shared edge disables it for both. Only explicitly switch-capable tabs may be toggled. Local switch settings persist when disconnected and rotate with the structure. A severed link is distinct from a disabled switch: toggling cannot heal it. Edge identity uses persistent endpoint IDs plus local port identity, not the current screen coordinates. Rebuilding a destroyed endpoint creates a new instance and new edge identities; undoing an uncommitted edit restores the old ones.

The Signal Mast is a declared exception: a facing compatible endpoint exactly two cells away may connect across one empty cell, in the configured cardinal direction. The middle cell must contain no structure/rubble or blocking terrain/Hush effect. No longer jumps, implicit branching or chains that ignore occupancy. Other special links require a separately versioned rule and example. The Phase 004 executable probe covers ordinary adjacency; it does not claim a Mast implementation.

## 4. Connectivity, Load, priorities and Resonance — NET

Build an undirected graph of living structures and valid enabled edges. Root reachability starts only at the Keep. Basic connectivity does not require intermediate structures to be powered. In particular, **Dormant structures remain connected, consume no Command and do not operate**, as required by bible section 20.2. An unpaid or overloaded structure also retains its intact physical ports. Destruction, explicit port disabling, a severed edge or a stated disabling effect can break the graph; lack of allocated power alone cannot.

The initial baseline capacity is six Load. Capacity and Load are non-negative integers; connected zero-Load structures may operate at zero capacity. The Keep is not placed into its own allocator. Sort other connected, eligible structures by `(priority_rank, row_major_anchor_index, stable_instance_id)`: Crown first, Charter second; Dormant is excluded from operation. Unique anchors make the last tie-breaker a defensive invariant.

**Allocation algorithm:** scan once in order. If the full effective Load fits, and any required upkeep can be paid, admit the structure and reserve its entire Load. Otherwise record the reason and continue scanning. Never partly power a structure. A rejected large structure does not prevent a later smaller one fitting. Do not reorder the player's priorities to maximize output. Advanced tooltips must expose the tie order and the skipped structure.

Example: with capacity 6, ordered Loads `4,3,2` produce `powered,overloaded,powered`, using 6. With capacity 0, a connected zero-Load Charter relay operates; a one-Load structure does not. A disconnected zero-Load structure is still isolated.

Compute content modifiers at an explicit boundary from the declared snapshot, with published integer caps and rounding. The baseline has no Amplifier/Resonance numerical modifiers. Later Amplifier effects cannot read their own resulting powered state to bootstrap an unbounded allocation loop; those content definitions must supply a non-circular activation/cost rule and pass their own fixtures before introduction. The minimal allocator is completely defined without these later effects.

Keep independent flags and a reason list: physically connected; player Dormant; explicitly disabled; upkeep failure; overloaded; powered; damaged; resonant; predicted disconnection. An isolated Dormant building can have both facts. Do not compress them into a misleading single color.

**Resonance predicate:** there must be two distinct paths to the Keep sharing no internal vertex; the structure and Keep may be shared endpoints. Parallel drawings of the same edge do not count. A cycle attached to the Keep by one vulnerable stem is not sufficient. Compute after topology changes, not per render frame. Resonance alone neither grants capacity nor overrides Load/priority. Exact small family bonuses remain a scheduled Phase 027 content decision, not an unresolved baseline operation rule.

After a link cut/destruction in Siege tick t, mark connectivity/allocation dirty. The published allocation is refreshed at step 2 of tick t+1, unless the run has ended. A destroyed defender cannot act again merely because its old allocation cache said powered. Predicted cuts use the same graph rules.

## 5. Resources, upkeep and Production — ECO

Resource bundles have exactly `Supply, Material, Insight`, in that serialization order. Command is live capacity, never a fourth stockpile or bankable reward. Values, costs, health, armor, damage, cooldown ticks and ordinary outputs are integers. The probe uses a non-negative signed-32-bit resource domain; overflow/negative/unknown-resource input is invalid data and never silently clamped, paid in part or converted to a run loss. Signed modifiers are explicitly typed separately. Rational multipliers apply in declared order, round down once at the published boundary, then clamp to a documented cap; no floating-point outcome dependency.

Every cost is an atomic bundle: either all components are affordable and deducted, or no component changes. Every reward records its cause and unique event/transaction ID. Duplicate replay of an already applied transaction must not pay twice. Free rotation, inspection and planning-priority changes do not advance RNG.

**Upkeep admission:** scan in the same order as Command allocation. Do not charge Dormant, isolated, disabled or non-fitting structures. For an otherwise fitting structure, pay its full upkeep from the current stockpile before admitting it. Failure reserves no Load, spends nothing and marks `upkeep_failed_this_watch`; that latch lasts to the next Watch and does not overwrite the player's selected priority. Successful upkeep is charged at most once per structure per Watch, even if damage causes reallocation. Newly eligible structures may be admitted and charged at the next reallocation; already paid structures are not charged again. Preview must explain both latches. Initial admission uses pre-Production stockpiles, so future production cannot retroactively fund an earlier admission failure.

After admission, resolve powered economic structures once in the same stable order. Each recipe has an atomic input bundle followed by its output bundle. Outputs from an earlier row may fund a later recipe; later rows do not cause an earlier failed recipe to retry. A recipe failure does not remove physical connectivity or refund paid upkeep. No automatic repeat-to-fixed-point loop, same-Watch harvest multiplication or re-entry into Production. Separate one-shot triggered effects require declared IDs, ordering and bounded triggering; a cyclic definition is a validation error.

Worked example: start with no Supply. An earlier producer creates 2 Supply; a later converter spends 1 Supply for 1 Material: final `Supply=1, Material=1`. Reverse the order and the converter first fails, then the producer leaves `Supply=2, Material=0`. Both results are intentional and shown in the ledger.

The ledger records Watch/phase/tick, command/event ID, source instance/content ID, before bundle, cost, output, after bundle and rejection reason. Preview displays these authoritative values rather than separately maintained tooltip numbers.

## 6. Watch state machine and commitment — WCH

Watch numbers are 1 through 15. `act = 1 + (watch-1)//5`; boss Watches are exactly 5, 10 and 15. Required order:

`Forecast -> Council -> Build -> Route -> Production -> Siege -> Aftermath -> next Watch Forecast`.

Forecast reveals the next two real major pressure events (or all remaining when fewer exist); Lantern Synod reveals one additional event. Records include arrival Watch, entry, count, rule, target and modifiers. Revealed threats and RNG choices remain fixed unless an explicitly previewed choice changes them. Do not fabricate a sixteenth Watch or extra threat to fill a UI slot.

Council generates/resolves its scheduled choice exactly once. With no scheduled choice it advances without a dummy modal. Committed rerolls/banishes/offer selections checkpoint their costs and RNG state; planning undo cannot fish for new random offers. Build/Route allow unlimited inspection and reversible eligible edits on a proposed state. Moving focus, waiting, previews or presentation speed consume no RNG and never auto-commit.

**Seal the Charter** submits the proposed command list with its expected base revision. Revalidate every command sequentially on a scratch state. Validate the resulting board, resource, ownership and phase invariants; present nonfatal warnings such as overloaded defenses. On success swap the complete validated state atomically, record the commit ID and invalidate the undo boundary before Production. On any invalid/stale command, reject the whole batch, report the exact command/reason, and retain the original state/resources/RNG. An unacknowledged fatal data error cannot be waved through as a warning. Re-submission of the same sealed command ID cannot run Production twice.

The ordinary plan remains fixed from Production through Siege. Do not offer a free universal economy-to-defense reroute after harvesting. **Lantern Synod's explicit exception** is one optional single switch-edge reconfiguration after Production and before the first Siege tick. It permits no placement, priority rewrite, extra Production or second free switch action. Save its consumed/declined flag; resume at that window only if unresolved.

After Siege, apply pending salvage and persistent aftermath effects once, offer at most one defined recovery choice or skip, and checkpoint before moving to the next Forecast. Ordinary damage already applied during Siege is not applied a second time in Aftermath. Final victory uses the same once-only settlement, then the run-end screen; no next Watch. Any declared fatal effect during settlement retains defeat precedence.

## 7. Combat ordering and targets — CMB

The following adopts the bible's section 20.7 recommendation as the locked baseline. A tick is a logical integer step. The verification profile uses 100 ms at normal presentation speed; this interval is not an arithmetic input. Actual animation calibration belongs to later combat/presentation phases. No direct per-enemy player targeting or reaction-time requirement is introduced.

1. Apply scheduled start-of-tick effects in stable effect-ID order, including declared spawns.
2. Recalculate Command if graph, Load, capacity, eligibility or priority changed.
3. Determine enemy movement intents from the same snapshot.
4. Resolve movement in stable enemy-instance order.
5. Determine defense targets from the post-movement state.
6. Resolve defense attacks in stable structure-index order.
7. Remove defeated enemies and process their on-defeat events once.
8. Determine surviving enemy targets.
9. Resolve surviving enemy attacks and sabotage.
10. Apply destruction, link cuts, deaths and on-damage effects.
11. Apply queued end-of-tick effects and evaluate terminal conditions, then stage/encounter transitions.

The terminal check at step 11 observes all same-tick lethal effects. Intermediate queued victory notifications cannot pre-empt it. Queues use stable IDs/packet sequence, never scene-tree iteration. A killed enemy removed at step 7 cannot attack in step 9. A defender never retargets halfway through its already chosen packet; if an earlier defense killed the same target, its invalid shot does no damage and consumes no cooldown, and it selects again next tick. A valid shot starts its declared positive integer cooldown even if armor absorbs all damage.

Normal baseline targeting: choose legal in-range targets by least remaining route steps to the declared objective, then stable enemy ID. Baseline range is Manhattan distance on the board, inclusive of the declared integer radius; directional attacks additionally use the rotated content arc. Specialized target hierarchies must be declared and previewable. Surviving normal enemies prioritize their next living lane blocker/Keep under their declared range/cooldown, not an arbitrary convenient target. A sabotage packet names a valid edge explicitly. Additional path/range/ward/trait behavior is content work, not permission to introduce hidden randomness.

An encounter finishes only when all scheduled waves are exhausted and no required living hostile/objective remains. A temporary empty board is not a win. Every encounter must have a finite validated resolution guard. Exceeding it is an invalid-content/technical recovery condition, not an invented player defeat or free victory; retain checkpoint/log and report it. Exact guard values and unit balance belong to content profiles.

At 1x, 2x, 4x and allowed instant resolution, execute identical ticks, queues and RNG calls. Speed only changes presentation scheduling. Newly encountered rules default to visible resolution, with the bible's explicit player setting override. Reduced motion alters feedback, not rules. No simulation state is read back from a tween or VFX node.

## 8. Damage, repairs, destruction and salvage — DMG

Keep Integrity is health of the Keep/Crown Relay. A valid live target has `0 < health <= max_health`, non-negative armor and non-negative temporary ward. Ward is a per-target protective quantity, not an economic resource. For a normal integer packet:

`after_armor = max(0, raw_damage - armor)`
`ward_absorbed = min(ward, after_armor)`
`health_damage = after_armor - ward_absorbed`
`new_ward = ward - ward_absorbed`
`new_health = max(0, health - health_damage)`.

Armor applies separately to each packet. Zero damage causes no hit-trigger, negative damage is invalid rather than healing, and overkill never creates negative health. Explicit piercing/healing rules must identify which stage they alter. Example: health 10, armor 2, ward 3, raw damage 7 leaves health 8, ward 0.

Positive health does not automatically reduce output merely because the structure is damaged. A disabled intact structure retains health and can recover; a destroyed one at zero health cannot be repaired or continue operating. Damage-based disable/port-block conditions must be explicit content. The Keep reaching zero is terminal; later repair cannot resurrect the run.

For the **verification balance profile**, Keep maximum Integrity is 20, default armor zero, and one repair restores up to 3 missing health for 1 Supply + 1 Material. Charge the full bundle even for a smaller remaining deficit; preview that fact. Full-health, destroyed, invalid-target and unaffordable repairs fail atomically. Build/Route repair remains reversible until Seal. During Siege, no manual repair; only already declared automatic effects. The same repair can be selected as the one Aftermath recovery action. These newly selected numbers are documented calibration defaults, not claims that the bible specified final balance. Other building maximum health/repair definitions are mandatory validated content fields, not guessed fallback values.

Destroyed non-Keep structures leave nonconducting rubble occupying the footprint until cleared in planning; clearing is free and can be batched/undone before Seal. No implicit rebirth on rotation, switch toggling or reload. Baseline salvage is `floor(actual Material paid for construction and upgrades / 2)`, zero Supply/Insight. Repairs are excluded from that cost basis. Destruction credits salvage once during Aftermath; dismantling credits once in the sealed planning transaction. A rubble-clear action produces no second payout. Free starting structures with zero paid basis give zero salvage. Later doctrine rewards are separately tagged events, not duplicate base refunds.

A severed link can be repaired only while its original living endpoints and compatible geometry exist. The baseline repair spends the same repair bundle and restores that one link, not unrelated HP. Switch toggles never do this for free. A replacement endpoint creates a new link; recovered salvage cannot exceed paid construction, so replacement is not an infinite refund loop.

## 9. Victory, defeat and precedence — END

At every terminal checkpoint collect all reasons, then apply the same precedence:

1. Keep Integrity zero, an explicitly forecast fatal boss objective, or a declared doctrine loss predicate means **DEFEAT**. Record all applicable causes, including a simultaneous final-boss kill.
2. Otherwise, at Watch 15 only, final boss defeated, no remaining required hostiles/waves/objectives and an intact Keep means **VICTORY** (followed by once-only final settlement).
3. Otherwise the run remains **ONGOING**. Finishing Watch 5 or 10 is not a run victory.

A missing boss, unknown doctrine predicate, invalid rules/content version or impossible state is a validation/recovery error, not a silent success and not a punishment for the player. The baseline doctrine-loss set is empty; adding a predicate requires a visible condition and tests. Watch 15 cannot simply roll over to 16 if its required final boss was never defined. Once terminal, no commands can alter the outcome or duplicate rewards.

## 10. Undo, reload, failures and accessible inspection — REC

Planning uses immutable base revision plus an ordered proposed-command list. Undo restores the entire prior proposed board/resource/port/switch/priority state and derived previews, not merely the sprite. Cancel drops all unsealed changes. A new edit after undo discards the redo tail. No undo crosses Council RNG checkpoint, Seal, Production, Siege tick or settled Aftermath. Reversible edits allocate instance IDs only in their transaction; restored proposals do not leak IDs into the active run.

A save records rules/content/schema versions, seed/RNG state, base revision, authoritative board/IDs/health/ports/switches, stockpiles, committed phase/Watch/tick, one-shot event/transaction IDs, pending salvage and upkeep/exception flags. A planning save also records proposed commands so the same preview can be reconstructed. Derived graphs can be rebuilt; scene nodes, frame delta, tooltip text and visual coordinates are not authoritative save fields.

Load into scratch state, validate/migrate before swap, rebuild derived state and compare invariants. Unknown version/missing ID/corruption leaves the current session and last valid checkpoint untouched. Save-service atomic disk replacement, migrations, controller paths and actual UI-scale testing remain later implementation gates; the Phase 004 checks only prove the stated pure examples and serialization round-trip of probe data.

Every supported device issues the same abstract commands. Cell focus uses the same row-major coordinates; at a board boundary an arrow in that direction stays put, never wraps. Inspecting a focused structure exposes port orientation, priority, effective Load, paths and reasons for inactivity. Errors return focus to the offending field/cell; a state revision invalidates stale previews without silently accepting a different decision. Critical states require text/icon/line cues as well as color. No fixed camera angle or printed pattern changes a port, route or target calculation.

## 11. Worked examples and reproducible checks

Run from the repository root:

```sh
python3 docs/phase-004/verify_rules.py
```

On Windows the equivalent launcher is `py -3 docs/phase-004/verify_rules.py` (Python 3.10+ syntax; tested environment recorded in closure). No package installation or network is required.

The JSON contains explicit expected allocation, Production, damage, repair and end-condition cases. The script additionally enumerates all board coordinates/neighbor directions, all 4-bit port masks/quarter-turns, small graph redundancy examples, transaction failure/rollback and serialization checks. It fails non-zero for mismatches and malformed fixture data; it does not rewrite expected outputs to make a run green. [CLOSURE_EVIDENCE.md](CLOSURE_EVIDENCE.md) states executed coverage and limitations.

Illustrative first meaningful choice: a connected seven-Load plan under capacity six can prioritize a one-Load defense instead of a one-Load producer. Both choices have visible costs and fit the same allocator. Phase 004 fixes that arithmetic, not a claim that a playable onboarding scene or fair-loss usability study has passed.

## 12. Closure and next dependency

All eight Phase 004 work items map to BRD, PRT, NET, ECO, WCH, DMG and END above, with REC covering undo/reload/accessibility/failure behavior. There are no unresolved critical questions about the **minimal v1.0.0 rules**. Scheduled content/balance/art work is explicitly listed separately rather than being labeled complete.

Phase 005 is **Scope budget and content ceiling**. It must budget the established product and its actual verification/art/content costs without expanding scope. This rules lock does not authorize skipping the remaining preproduction gates, repository bootstrap, Godot foundation or Blender pipeline phases.
