---
tags: [math, discrete, logic, proofs]
status: complete
---

# Logic & Proofs

> Formal reasoning — the language of mathematics and the engine behind every theorem.

---

## Propositional logic

A **proposition** is a declarative sentence that is either true or false. Not a question (`How are you?`), not a command (`Sit down!`), not an open variable ($x + 3 = 5$).

| symbol                | name                      | rule                         |
| --------------------- | ------------------------- | ---------------------------- |
| $\neg p$              | negation · NOT            | T → F, F → T                 |
| $p \wedge q$          | conjunction · AND         | T only if both T             |
| $p \vee q$            | disjunction · OR          | F only if both F (inclusive) |
| $p \Rightarrow q$     | implication · IF p THEN q | F only when p=T, q=F         |
| $p \Leftrightarrow q$ | equivalence · IFF         | T when same truth value      |

### Truth table

| $p$ | $q$ | $p \wedge q$ | $p \vee q$ | $p \Rightarrow q$ | $p \Leftrightarrow q$ |
| --- | --- | ------------ | ---------- | ----------------- | --------------------- |
| T   | T   | T            | T          | T                 | T                     |
| T   | F   | F            | T          | **F**             | F                     |
| F   | T   | F            | T          | T                 | F                     |
| F   | F   | F            | F          | T                 | T                     |

$p \Rightarrow q$ is false **only** when p=T, q=F. A false premise makes any implication vacuously true.

### Converse vs contrapositive

| form           | expression                  | equivalent to $p \Rightarrow q$? |
| -------------- | --------------------------- | -------------------------------- |
| Original       | $p \Rightarrow q$           | —                                |
| Contrapositive | $\neg q \Rightarrow \neg p$ | **yes**                          |
| Converse       | $q \Rightarrow p$           | no                               |
| Inverse        | $\neg p \Rightarrow \neg q$ | no (equivalent to converse)      |

### Tautology · contradiction · contingency

- **Tautology** — always T: $p \vee \neg p$, $(p \Rightarrow q) \Leftrightarrow (\neg q \Rightarrow \neg p)$, $(p \wedge q) \Rightarrow p$
- **Contradiction** — always F: $p \wedge \neg p$
- **Contingency** — depends on values: $p \Rightarrow q$

Two propositions are **logically equivalent** iff their biconditional is a tautology.

### Key equivalences

| equivalence                                                                 | law                 |
| --------------------------------------------------------------------------- | ------------------- |
| $\neg(p \vee q) \Leftrightarrow \neg p \wedge \neg q$                       | De Morgan           |
| $\neg(p \wedge q) \Leftrightarrow \neg p \vee \neg q$                       | De Morgan           |
| $p \Rightarrow q \Leftrightarrow \neg p \vee q$                             | implication rewrite |
| $\neg(\neg p) \Leftrightarrow p$                                            | double negation     |
| $p \vee q \Leftrightarrow q \vee p$                                         | commutative         |
| $p \wedge \top \Leftrightarrow p \quad p \vee \bot \Leftrightarrow p$       | identity            |
| $p \vee \top \Leftrightarrow \top \quad p \wedge \bot \Leftrightarrow \bot$ | domination          |
| $p \vee p \Leftrightarrow p \quad p \wedge p \Leftrightarrow p$             | idempotent          |
| $p \vee (q \wedge r) \Leftrightarrow (p \vee q) \wedge (p \vee r)$          | distributive        |

### Building truth tables

1. n variables → $2^n$ rows (col 1: $n/2$ Ts then $n/2$ Fs, col 2: $n/4$ each, …)
2. Add intermediate columns innermost-first
3. Apply outermost operator last

Example — $(p \Rightarrow q) \wedge (\neg p \Leftrightarrow q)$:

| $p$ | $q$ | $\neg p$ | $p \Rightarrow q$ | $\neg p \Leftrightarrow q$ | result |
| --- | --- | -------- | ----------------- | -------------------------- | ------ |
| T   | T   | F        | T                 | F                          | F      |
| T   | F   | F        | F                 | T                          | F      |
| F   | T   | T        | T                 | T                          | **T**  |
| F   | F   | T        | T                 | F                          | F      |

---

## Predicate logic

Propositional logic can't talk about objects, properties, or groups. Predicate logic adds: **constants**, **variables**, **predicates**, and **quantifiers**.

A **predicate** $P(x)$ returns T or F depending on whether the property holds for x. Not a proposition until all variables are bound.

$P(x, y) = $ "x + 5 > y": $P(3, 7)$ is a proposition (T); $P(3, y)$ is not (y is free).

### Quantifiers

| symbol            | name                           | true when                       | false when                      |
| ----------------- | ------------------------------ | ------------------------------- | ------------------------------- |
| $\forall x\ P(x)$ | universal — "for all x"        | $P(x)$ holds for every x        | at least one x where $P(x) = F$ |
| $\exists x\ P(x)$ | existential — "there exists x" | at least one x where $P(x) = T$ | $P(x) = F$ for all x            |

### Translation patterns

- **$\forall$ uses $\Rightarrow$** inside: $\forall x\ (Student(x) \Rightarrow Smart(x))$
  Using $\wedge$ with $\forall$ is almost always wrong — it asserts everything is a student.
- **$\exists$ uses $\wedge$** inside: $\exists x\ (Student(x) \wedge Smart(x))$
  Using $\Rightarrow$ with $\exists$ would be satisfied trivially by a non-student.

| sentence                  | formula                                                         |
| ------------------------- | --------------------------------------------------------------- |
| All SU students are smart | $\forall x\ (Student(x) \wedge At(x, SU)) \Rightarrow Smart(x)$ |
| Someone at SU is smart    | $\exists x\ (At(x, SU) \wedge Smart(x))$                        |
| Everybody loves Raymond   | $\forall x\ L(x,\ Raymond)$                                     |
| Everybody loves somebody  | $\forall x\ \exists y\ L(x, y)$                                 |
| Someone is loved by all   | $\exists y\ \forall x\ L(x, y)$                                 |
| Nobody loves y            | $\exists y\ \forall x\ \neg L(x, y)$                            |

### Nested quantifiers — order matters

$\forall x\ \exists y\ L(x,y)$ — everybody loves somebody (y can depend on x)

$\exists y\ \forall x\ L(x,y)$ — there's one person everybody loves (one fixed y)

$\forall\forall$ and $\exists\exists$ are order-independent. $\forall\exists$ and $\exists\forall$ are **not**.

### Negation of quantifiers

$$\neg \exists x\ P(x) \Longleftrightarrow \forall x\ \neg P(x)$$
$$\neg \forall x\ P(x) \Longleftrightarrow \exists x\ \neg P(x)$$
$$\neg \forall x\ \exists y\ P(x,y) \Longleftrightarrow \exists x\ \forall y\ \neg P(x,y)$$

Flip each quantifier, negate the predicate.

---

## See also

- [[Sets, Relations, Functions]]
- [[Combinatorics]]
