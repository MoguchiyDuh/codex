---
tags: [math, discrete, sets]
status: complete
---

# Sets

> The primitive building block of all mathematics — an unordered collection of distinct objects.

## Notation and basic definitions

A **set** is an unordered collection of distinct objects called **elements** or **members**. Membership is written $x \in A$; non-membership $x \notin A$.

Sets are specified three ways:

| Style       | Example                                          | Use                           |
| ----------- | ------------------------------------------------ | ----------------------------- |
| Roster      | $\{1, 2, 3\}$                                    | small finite sets             |
| Set-builder | $\{x \in \mathbb{Z} \mid x > 0\}$                | infinite or rule-defined sets |
| Named       | $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$ | standard number sets          |

By convention $\mathbb{N} = \{0, 1, 2, \ldots\}$ in 6.042J (0 is included). The **empty set** $\emptyset = \{\}$ has no elements.

## Set relations

**Subset.** $A \subseteq B$ if every element of $A$ is also in $B$: $\forall x,\; x \in A \implies x \in B$.

**Proper subset.** $A \subsetneq B$ if $A \subseteq B$ and $A \neq B$.

**Equality.** $A = B$ iff $A \subseteq B$ and $B \subseteq A$. This double-inclusion pattern is the standard proof strategy for set equality.

**Example.** Prove $\{x \in \mathbb{Z} \mid x^2 \leq 4\} = \{-2, -1, 0, 1, 2\}$.

Both directions: every integer with $x^2 \leq 4$ is in $\{-2,-1,0,1,2\}$ (check: $(\pm 3)^2 = 9 > 4$), and every element of $\{-2,-1,0,1,2\}$ satisfies $x^2 \leq 4$.

## Set operations

| Operation         | Symbol                  | Definition                                               |
| ----------------- | ----------------------- | -------------------------------------------------------- |
| Union             | $A \cup B$              | $\{x \mid x \in A \text{ or } x \in B\}$                 |
| Intersection      | $A \cap B$              | $\{x \mid x \in A \text{ and } x \in B\}$                |
| Difference        | $A \setminus B$         | $\{x \mid x \in A \text{ and } x \notin B\}$             |
| Complement        | $\overline{A}$ or $A^c$ | $\{x \in U \mid x \notin A\}$ (relative to universe $U$) |
| Symmetric diff.   | $A \triangle B$         | $(A \setminus B) \cup (B \setminus A)$                   |
| Cartesian product | $A \times B$            | $\{(a, b) \mid a \in A,\; b \in B\}$                     |

![[set_venn_operations.png]]

### Algebraic laws

| Law          | Expression                                                                                                           |
| ------------ | -------------------------------------------------------------------------------------------------------------------- |
| Commutative  | $A \cup B = B \cup A$, $\quad A \cap B = B \cap A$                                                                   |
| Associative  | $(A \cup B) \cup C = A \cup (B \cup C)$                                                                              |
| Distributive | $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$                                                                     |
| De Morgan    | $\overline{A \cup B} = \overline{A} \cap \overline{B}$, $\quad \overline{A \cap B} = \overline{A} \cup \overline{B}$ |
| Identity     | $A \cup \emptyset = A$, $\quad A \cap U = A$                                                                         |
| Complement   | $A \cup \overline{A} = U$, $\quad A \cap \overline{A} = \emptyset$                                                   |

These mirror the logical equivalences in [[Logic & Proofs]] — union corresponds to $\vee$, intersection to $\wedge$, complement to $\neg$.

## Power set and cardinality

The **power set** $\mathcal{P}(A)$ is the set of all subsets of $A$.

$$\mathcal{P}(\{1,2\}) = \{\emptyset,\, \{1\},\, \{2\},\, \{1,2\}\}$$

For a finite set with $|A| = n$, $|\mathcal{P}(A)| = 2^n$. This is proved by counting: each element is either included or excluded — $2$ choices per element, $n$ elements.

The **cardinality** $|A|$ of a finite set is its number of elements. For infinite sets, cardinality is formalised via bijections (see below and [[Functions]]).

## Russell's paradox

Naive set theory — "any property defines a set" — is inconsistent. Let $R = \{S \mid S \notin S\}$. Then:

- If $R \in R$: the definition requires $R \notin R$ — contradiction.
- If $R \notin R$: the definition requires $R \in R$ — contradiction.

The resolution (ZFC set theory) restricts set-formation: sets can only be built from existing sets using explicit operations. In practice, we always work within a fixed universe and use set-builder notation only over an existing set — $\{x \in A \mid P(x)\}$, never the unrestricted $\{x \mid P(x)\}$.

## Infinite sets and cardinality

Two sets have the same cardinality if there exists a **bijection** between them (a perfect one-to-one correspondence — see [[Functions]]).

**Countably infinite.** A set is countably infinite if it has the same cardinality as $\mathbb{N}$, i.e. its elements can be listed $a_0, a_1, a_2, \ldots$

| Set                            | Countable? | Why                               |
| ------------------------------ | ---------- | --------------------------------- |
| $\mathbb{Z}$                   | Yes        | List: $0, 1, -1, 2, -2, \ldots$   |
| $\mathbb{Q}$                   | Yes        | Diagonal enumeration of fractions |
| $\mathbb{N} \times \mathbb{N}$ | Yes        | Diagonal enumeration              |
| $\mathbb{R}$                   | No         | Cantor's diagonal argument        |

**Cantor's theorem.** For any set $A$, $|\mathcal{P}(A)| > |A|$. In particular $|\mathcal{P}(\mathbb{N})| > |\mathbb{N}|$, and $|\mathbb{R}| = |\mathcal{P}(\mathbb{N})|$.

**Proof sketch.** Suppose $f : A \to \mathcal{P}(A)$ is a bijection. Define $D = \{x \in A \mid x \notin f(x)\}$. Since $f$ is surjective, $D = f(d)$ for some $d$. Then $d \in D \iff d \notin f(d) = D$ — contradiction. So no surjection from $A$ onto $\mathcal{P}(A)$ exists, meaning $|\mathcal{P}(A)| > |A|$.

This argument is the same diagonal construction Cantor used to show $\mathbb{R}$ is uncountable — and is the same idea behind Turing's proof that the halting problem is undecidable.

## See also

- [[Logic & Proofs]]
- [[Relations]]
- [[Functions]]
- [[Index]]
