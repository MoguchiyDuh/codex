---
tags: [math, discrete, logic, proofs]
status: complete
---

# Logic & Proofs

> Formal reasoning — the language mathematics is written in and the engine behind every theorem.

## Propositions

A **proposition** is a declarative sentence with a definite truth value. Not a question, not a command, not a formula with free variables.

| Proposition? | Example                            | Why                                                   |
| ------------ | ---------------------------------- | ----------------------------------------------------- |
| Yes          | "17 is prime"                      | determinate truth value                               |
| Yes          | "There are infinitely many primes" | determinate (true)                                    |
| No           | "What time is it?"                 | question                                              |
| No           | "$x + 1 = 2$"                      | depends on $x$ — not a proposition until $x$ is fixed |

Propositions are the atoms from which all mathematical arguments are built.

## Logical connectives

New propositions are formed by combining simpler ones with connectives.

| Symbol         | Name          | Read as                  | False when             |
| -------------- | ------------- | ------------------------ | ---------------------- |
| $\neg p$       | negation      | "not $p$"                | $p$ is true            |
| $p \wedge q$   | conjunction   | "$p$ and $q$"            | either is false        |
| $p \vee q$     | disjunction   | "$p$ or $q$"             | both are false         |
| $p \implies q$ | implication   | "if $p$ then $q$"        | $p$ true and $q$ false |
| $p \iff q$     | biconditional | "$p$ if and only if $q$" | they differ            |

The implication $p \implies q$ is the most important and most misread. It is **false only when the hypothesis $p$ is true and the conclusion $q$ is false.** A false hypothesis makes the implication vacuously true — "if $0 = 1$ then pigs fly" is a true statement.

### Truth table

| $p$ | $q$ | $\neg p$ | $p \wedge q$ | $p \vee q$ | $p \implies q$ | $p \iff q$ |
| --- | --- | -------- | ------------ | ---------- | -------------- | ---------- |
| T   | T   | F        | T            | T          | T              | T          |
| T   | F   | F        | F            | T          | **F**          | F          |
| F   | T   | T        | F            | T          | T              | F          |
| F   | F   | T        | F            | F          | T              | T          |

### Tautologies and contradictions

A **tautology** is true for every assignment of truth values. A **contradiction** is false for every assignment.

| Example                                        | Type                               |
| ---------------------------------------------- | ---------------------------------- |
| $p \vee \neg p$                                | tautology (law of excluded middle) |
| $p \wedge \neg p$                              | contradiction                      |
| $p \implies p$                                 | tautology                          |
| $(p \implies q) \iff (\neg q \implies \neg p)$ | tautology                          |

Two propositions are **logically equivalent** ($\equiv$) when their biconditional is a tautology — they have identical truth tables.

### Key equivalences

| Name                | Equivalence                                                 |
| ------------------- | ----------------------------------------------------------- |
| De Morgan           | $\neg(p \wedge q) \equiv \neg p \vee \neg q$                |
| De Morgan           | $\neg(p \vee q) \equiv \neg p \wedge \neg q$                |
| Implication rewrite | $p \implies q \equiv \neg p \vee q$                         |
| Contrapositive      | $p \implies q \equiv \neg q \implies \neg p$                |
| Double negation     | $\neg\neg p \equiv p$                                       |
| Distributive        | $p \wedge (q \vee r) \equiv (p \wedge q) \vee (p \wedge r)$ |

The contrapositive equivalence is not just notation — it is a proof technique: proving $\neg q \implies \neg p$ is logically identical to proving $p \implies q$.

## Predicates and quantifiers

A **predicate** is a proposition-valued function: $P(x)$ has no truth value until $x$ is assigned. Quantifiers bind the variable and produce a proposition.

$$\forall x \in S,\; P(x) \qquad \exists x \in S,\; P(x)$$

$\forall x \in S,\; P(x)$ is true iff $P(x)$ holds for every element of $S$. $\exists x \in S,\; P(x)$ is true iff at least one element of $S$ satisfies $P$.

### Negating quantifiers

Negation flips the quantifier and negates the predicate — a direct consequence of De Morgan applied to an infinite conjunction or disjunction.

$$\neg\bigl(\forall x,\; P(x)\bigr) \equiv \exists x,\; \neg P(x)$$
$$\neg\bigl(\exists x,\; P(x)\bigr) \equiv \forall x,\; \neg P(x)$$

**Example.** The negation of "every student passed" is "some student did not pass" — not "no student passed."

### Nested quantifiers

Order matters when quantifiers are mixed.

$$\forall x\, \exists y,\; y > x \quad \text{(for every number there is a larger one — true in } \mathbb{Z}\text{)}$$
$$\exists y\, \forall x,\; y > x \quad \text{(some number is larger than all — false in } \mathbb{Z}\text{)}$$

Swapping $\forall$ and $\exists$ generally changes the meaning.

![[quantifier_scope.png]]

## Proof techniques

A **proof** is a sequence of steps, each justified by a definition, axiom, or previously proved fact, establishing that a proposition is true.

### Direct proof

Assume the hypothesis; derive the conclusion by a chain of implications.

**Claim.** If $n$ is odd then $n^2$ is odd.

**Proof.** Suppose $n$ is odd. Then $n = 2k + 1$ for some integer $k$. So
$$n^2 = (2k+1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1,$$
which is odd.

### Proof by contrapositive

Prove $\neg q \implies \neg p$ instead of $p \implies q$. Logically identical, often simpler when $q$ being false gives a more tractable assumption.

**Claim.** If $n^2$ is even then $n$ is even.

**Proof.** Contrapositive: if $n$ is odd then $n^2$ is odd. Shown above.

### Proof by contradiction

Assume the negation of the claim; derive a contradiction. Conclude the claim must be true.

**Claim.** $\sqrt{2}$ is irrational.

**Proof.** Suppose $\sqrt{2} = p/q$ with $p, q \in \mathbb{Z}$, $q \neq 0$, and the fraction in lowest terms (so $p$ and $q$ are not both even). Then $2 = p^2/q^2$, so $p^2 = 2q^2$, making $p^2$ even, hence $p$ even (by the claim above). Write $p = 2m$. Then $4m^2 = 2q^2$, so $q^2 = 2m^2$, making $q$ even. But then $p$ and $q$ are both even — contradicting lowest terms.

This is one of the most famous proofs in mathematics. The contradiction arose from the structure of the assumption itself, not from any external fact.

### Proof by cases

Partition the hypothesis space into exhaustive, mutually exclusive cases and prove each separately.

**Claim.** For any integer $n$, $n^2 + n$ is even.

**Proof.** Either $n$ is even or $n$ is odd.

- **Case 1:** $n = 2k$. Then $n^2 + n = 4k^2 + 2k = 2(2k^2 + k)$, even.
- **Case 2:** $n = 2k + 1$. Then $n^2 + n = (2k+1)^2 + (2k+1) = 4k^2 + 4k + 1 + 2k + 1 = 4k^2 + 6k + 2 = 2(2k^2 + 3k + 1)$, even.

Both cases give an even result.

### Proof by counterexample

To disprove $\forall x,\; P(x)$, exhibit a single $x$ for which $P(x)$ is false.

**Claim (false).** Every prime is odd.

**Counterexample.** $2$ is prime and even.

One counterexample is sufficient and necessary to disprove a universal claim.

## Well-ordering principle

Every non-empty subset of $\mathbb{N}$ has a least element. This is equivalent to induction (see [[Induction]]) and is itself a powerful proof tool.

**Proof that $\sqrt{2}$ is irrational (well-ordering version).** Suppose rational: $\sqrt{2} = p/q$ with $p, q \in \mathbb{N}^+$. Consider the set $S = \{q \in \mathbb{N}^+ \mid \sqrt{2} = p/q \text{ for some } p \in \mathbb{N}^+\}$. If $\sqrt{2}$ is rational, $S$ is non-empty, so by well-ordering it has a minimum $q_0$, with corresponding $p_0$. Then $\sqrt{2} = p_0/q_0$ implies $p_0 = \sqrt{2}\, q_0$, and one can show $p_0 - q_0$ and $q_0({\sqrt{2}-1})$ yield a smaller valid denominator — contradicting minimality of $q_0$.

The well-ordering principle is the starting assumption that grounds all of discrete mathematics.

## Common proof mistakes

| Mistake                         | Example                                                               |
| ------------------------------- | --------------------------------------------------------------------- |
| Assuming what you want to prove | "Suppose $\sqrt{2} = p/q$... therefore $\sqrt{2}$ is rational"        |
| Arguing from examples           | "I checked $n = 1, 2, 3$, so it holds for all $n$"                    |
| Invalid quantifier swap         | Treating $\exists x\, \forall y$ as $\forall y\, \exists x$           |
| Vacuous truth ignored           | Concluding a universal is false because a case has a false hypothesis |
| Incomplete cases                | Splitting into cases that do not cover all possibilities              |

## Video references

- ![Lecture 1: Introduction and Proofs](https://www.youtube.com/watch?v=L3LMbpZIKhQ)

## See also

- [[Induction]]
- [[Sets]]
- [[../algebra/Index|Algebra]]
- [[Index]]
