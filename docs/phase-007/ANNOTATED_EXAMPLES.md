# Phase 007 — Annotated examples and board diagrams

These examples explain the locked rules. They are not screenshots, final UI, balance proof, or a substitute for later Godot tests.

---

## Example A — Standard board and reserved cells

~~~text
          x → 0 1 2 3 4 5 6 7 8
        +-------------------+
y = 0   | . . . . N . . . . |
y = 1   | . . . . . . . . . |
y = 2   | . . . . . . . . . |
y = 3   | . . . . . . . . . |
y = 4   | W . . . K . . . E |
y = 5   | . . . . . . . . . |
y = 6   | . . . . . . . . . |
y = 7   | . . . . . . . . . |
y = 8   | . . . . S . . . . |
        +-------------------+
~~~

Annotations:
- Keep K is coordinate 4,4 and index 40.
- North, east, south, west entries are indices 4, 44, 76, and 36.
- Ordinary row-major index is y times 9 plus x.
- Entries and Keep reject ordinary placement.
- There is no wrap from index 8 to index 9.

Boundary test: a structure at 8,3 with an east-facing port does not connect to 0,4. Flat-array adjacency does not override board geometry.

---

## Example B — Atomic placement and undo

Starting state:
- Material = 4.
- Proposed one-cell structure costs 2 Material.
- Target 3,4 is empty and legal.

Player places it:
- proposed Material becomes 2;
- network preview recalculates;
- authoritative committed run has not changed yet.

Player rotates it:
- cost does not repeat;
- ports rotate 90 degrees;
- preview changes.

Player undoes rotation:
- previous orientation and preview return.

Player undoes placement:
- proposed structure disappears;
- projected Material returns to 4;
- no persistent instance ID or RNG is consumed.

If the cell had been occupied or reserved, the command would reject with no partial cost.

---

## Example C — Command overload and deterministic skipping

Capacity = 6.

Connected eligible structures in priority and tie order:

~~~text
A: Load 4
B: Load 3
C: Load 2
~~~

Resolution:
1. A fits and powers. Used = 4.
2. B needs 3 but only 2 remain, so B is Unpowered due to Load.
3. C needs 2 and powers. Used = 6.

The allocator does not partially power B and does not secretly reorder B and C.

---

## Example D — Dormant structure still conducts

~~~text
[Keep] —— [Relay A: Dormant] —— [Defense B: Crown]
~~~

If ports and links are intact:
- Relay A remains physically connected;
- A consumes no Command and does not operate;
- B can remain connected through A;
- B's own Load and eligibility determine whether it powers.

Dormant is an operating priority state, not physical disconnection.

---

## Example E — Switch disabled versus severed

~~~text
[Keep] —— [Switchhouse] —— [Archive]
~~~

Case 1: switch edge disabled in planning:
- enabled state is false;
- preview shows Archive isolated;
- player can re-enable before Seal;
- no repair resource is required.

Case 2: link severed by Siege damage:
- damage state is distinct;
- switch toggling cannot heal it;
- repair follows damage and recovery rules.

---

## Example F — Siege disconnection timeline

Before tick t:
- Defense D is powered through one vulnerable link.
- Forecast and preview identify the cut point.

During tick t:
1. combat reaches enemy attack or sabotage;
2. link is severed;
3. destruction or link-cut effects apply;
4. network state becomes dirty.

At the next defined Command-refresh boundary:
- D has no valid path to Keep;
- D becomes Isolated and unpowered;
- later actions use the refreshed authoritative state.

Animation may visually lag but may not keep D authoritative or powered.

Post-run causal chain can report:

> vulnerable link severed → defense isolated → lane lost → Keep exposed.

---

## Example G — Production order changes an outcome transparently

Starting Supply = 0.

Order 1:
1. Producer adds 2 Supply.
2. Converter spends 1 Supply for 1 Material.

Final: Supply 1, Material 1.

Reverse order:
1. Converter cannot pay and fails.
2. Producer adds 2 Supply.

Final: Supply 2, Material 0.

The failed earlier recipe does not retry after later production.

---

## Example H — Annotated full Watch

### Forecast
Player sees an east-entry threat due this Watch and knows its declared target rule.

### Council
No scheduled decision, so the phase advances without a fake modal.

### Build
Player repairs a damaged network anchor, places one structure, rotates it, and sees projected costs.

### Route
Player marks one defense Crown, leaves an economy structure Charter, sets another structure Dormant, previews an exposed cut point, and sees Command allocation.

### Seal the Charter
The entire proposed transaction is revalidated.

If valid:
- it commits atomically;
- undo boundary closes.

If one command is invalid:
- no partial subset commits;
- player returns to editing with the exact failing command identified.

### Production
Powered economy resolves in stable order.

### Siege
Combat runs deterministic ticks; presentation speed only changes viewing speed.

### Aftermath
Damage and salvage settle once, causal losses are explained, the defined recovery choice appears, and the run checkpoints before the next Forecast.

---

## Example I — Simultaneous final boss and Keep death

At the final terminal checkpoint:
- final boss is defeated;
- Keep Integrity also reaches zero.

Result: DEFEAT.

Fatal Keep failure has higher terminal precedence than victory eligibility. The recap records both events.

---

## Example J — Controller and focus equivalence

A controller-focused structure exposes the same decision information as mouse hover:
- port orientation;
- priority;
- effective Load;
- connectivity;
- reason for inactivity;
- predicted Siege behavior.

At the right edge of the board, pressing right keeps focus at the boundary. It does not wrap to the next row.

Input parity is part of strategic fairness, not optional polish.
