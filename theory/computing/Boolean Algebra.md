---
tags:
  - computing/digital-logic
  - boolean-algebra
related:
  - "[[Karnaugh Maps (K-Maps)]]"
  - "[[Data Representation]]"
  - "[[00 - Computing MOC]]"
---

## Definition
**Boolean algebra** is a branch of algebra that deals with binary variables and logical operations. It forms the foundation of digital circuit design and computer logic.

---
## Basic Concepts

### Binary Variables
- Can only have two values: **0** (false) or **1** (true)
- Represented by letters: A, B, C, X, Y, Z, etc.

---
## Fundamental Operations #gates

### Order of operations:
1. NOT
2. AND
3. OR

<img src="Pictures/logic-gates.jpeg" width=500 height="auto" style="display: block; margin: auto">

#### AND (Conjunction)
- Symbol: `·`, `∧`, `&` or (often omitted)  
- Truth Table:

| A   | B   | A∧B |
| --- | --- | --- |
| 0   | 0   | 0   |
| 0   | 1   | 0   |
| 1   | 0   | 0   |
| 1   | 1   | 1   |

#### OR (Disjunction)
- Symbol: `+`, `∨`, `|`
- Truth Table:

| A   | B   | A∨B |
| --- | --- | --- |
| 0   | 0   | 0   |
| 0   | 1   | 1   |
| 1   | 0   | 1   |
| 1   | 1   | 1   |

#### NOT (Negation)
- Symbol: `¯`, `¬` , `~`
- Truth Table:

| A   | ¬A  |
| --- | --- |
| 0   | 1   |
| 1   | 0   |

---
## Derived Operations #adv_gates

### NAND (NOT AND)
- Symbol: `↑`
- A NAND B = ¬(A∧B)
- Universal gate (can build any Boolean function)
- Truth Table:

| A   | B   | A↑B |
| --- | --- | --- |
| 0   | 0   | 1   |
| 0   | 1   | 1   |
| 1   | 0   | 1   |
| 1   | 1   | 0   |


### NOR (NOT OR)  
- Symbol: `↓`
- A NOR B = ¬(A∨B)
- Universal gate
- Truth Table:

| A | B | A↓B |
|---|---|-----|
| 0 | 0 |  1  |
| 0 | 1 |  0  |
| 1 | 0 |  0  |
| 1 | 1 |  0  |

### XOR (Exclusive OR)
- Symbol: `⊕`
- A XOR B = A∧¬B ∨ ¬A∧B
- Output 1 when inputs differ
- Truth Table:

| A | B | A⊕B |
|---|---|-----|
| 0 | 0 |  0  |
| 0 | 1 |  1  |
| 1 | 0 |  1  |
| 1 | 1 |  0  |

### XNOR (Exclusive NOR)
- Symbol: `≡`
- A XNOR B = A∧B ∨ ¬A∧¬B
- Output 1 when inputs are same
- Truth Table:

| A | B | A≡B  |
|---|---|------|
| 0 | 0 |  1   |
| 0 | 1 |  0   |
| 1 | 0 |  0   |
| 1 | 1 |  1   |

## Basic Laws and Identities #bin_identities

### Commutative Laws
- $A \lor B = B \lor A$
- $A \land B = B \land A$

### Associative Laws  
- $A \lor (B \lor C) = (A \lor B) \lor C$
- $A \land (B \land C) = (A \land B) \land C$

### Distributive Laws
- $A \land (B \lor C) = (A \land B) \lor (A \land C)$
- $A \lor (B \land C) = (A \lor B) \land (A \lor C)$

**Special case: Absorption Law**
- $A \lor (A \land B) = (A \lor A) \land (A \lor B) = A$

### Identity Laws
- $A \lor 0 = A$
- $A \land 1 = A$

### Null Laws
- $A \lor 1 = 1$
- $A \land 0 = 0$

### Idempotent Laws
- $A \lor A = A$
- $A \land A = A$

### Complement Laws
- $A \lor \lnot A = 1$
- $A \land \lnot A = 0$

### Involution Law
- $\lnot(\lnot A) = A$

## De Morgan's Theorems #de_morgans_theorems

### First Theorem
### $\boxed{\lnot(A \lor B) = \lnot A \land \lnot B}$

### Second Theorem  
### $\boxed{\lnot (A \land B) = \lnot A \lor \lnot B}$

### Generalized Form
- $\lnot(A \lor B \lor C \lor ...) = \lnot A \land \lnot B \land \lnot C \land ...$
- $\lnot(A \land B \land C \land ...) = \lnot A \lor \lnot B \lor \lnot C \lor ...$

### ALL GATES USING NAND
#TODO

---

## See Also
- [[Karnaugh Maps (K-Maps)]] - Simplifying Boolean expressions
- [[Data Representation]] - Binary number systems
- [[00 - Computing MOC]] - Computing topics overview