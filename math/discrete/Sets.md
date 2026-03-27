---
tags:
  - math
  - discrete
  - sets
status: complete
---

# Sets, Relations, Functions

> The vocabulary of mathematics — how collections, pairings, and mappings are defined.

---

## Sets

A **set** is an unordered collection with no duplicates. Order and duplicates don't matter: $\{1,2,3\} = \{3,1,2\} = \{1,1,2,3\}$.

Two ways to specify:

- **Roster**: $\{1, 2, 3\}$
- **Set-builder**: $\{x \in \mathbb{N} \mid x < 4\}$

### Membership & relations

| symbol          | meaning                                                         |
| --------------- | --------------------------------------------------------------- |
| $x \in A$       | x is an element of A                                            |
| $A \subseteq B$ | subset — every element of A is in B (A can equal B)             |
| $A \subset B$   | proper subset — $A \subseteq B$ and $A \neq B$                  |
| $A = B$         | same elements: $\forall x\ (x \in A) \Leftrightarrow (x \in B)$ |
| \|$A$\|         | cardinality — number of distinct elements                       |

Trap: $\{1,2,3,4\} \neq \{1,2,2,4\}$ — the second set is missing 3.

### Standard number sets

| symbol       | name          | elements                                     |
| ------------ | ------------- | -------------------------------------------- | --------- | ------------------------------------- |
| $\mathbb{N}$ | naturals      | $\{1, 2, 3, \ldots\}$                        |
| $\mathbb{Z}$ | integers      | $\{\ldots, -2, -1, 0, 1, 2, \ldots\}$        |
| $\mathbb{Q}$ | rationals     | $\{p/q \mid p,q \in \mathbb{Z},\ q \neq 0\}$ |
| $\mathbb{R}$ | reals         | includes irrationals ($\pi$, $\sqrt{2}$, …)  |
| $\emptyset$  | empty set     | $\emptyset = 0$; $\emptyset \subseteq$ every set |
| $U$          | universal set | all objects under consideration              |

### Operations

| op           | symbol     | meaning                             |
| ------------ | ---------- | ----------------------------------- |
| Union        | $A \cup B$ | in A **or** B                       |
| Intersection | $A \cap B$ | in A **and** B                      |
| Difference   | $A - B$    | in A, **not** B; $A - B \neq B - A$ |
| Complement   | $\bar{A}$  | in U but not A                      |
| Sym. diff    | $A \oplus B$ | in A or B, **not both**; $(A - B) \cup (B - A)$ |

**Disjoint**: $A \cap B = \emptyset$ — no elements in common.

**Exhaustive** (cover $U$): $A \cup B = U$ — every element appears in at least one set.

**Partition**: disjoint **and** exhaustive — $A \cap B = \emptyset$ and $A \cup B = U$. Every element lands in exactly one part.

Inclusion-exclusion: $|A \cup B| = |A| + |B| - |A \cap B|$

### Power set $\mathcal{P}(S)$

All subsets of S, including $\emptyset$ and S itself.

$|S| = n \Rightarrow |\mathcal{P}(S)| = 2^n$ — each element is either in or out. See [[Combinatorics]] for why: $\binom{n}{0} + \binom{n}{1} + \cdots + \binom{n}{n} = 2^n$.

$$\mathcal{P}(\emptyset) = \{\emptyset\} \quad |\mathcal{P}| = 1$$
$$\mathcal{P}(\{1\}) = \{\emptyset, \{1\}\} \quad |\mathcal{P}| = 2$$
$$\mathcal{P}(\{1,2\}) = \{\emptyset, \{1\}, \{2\}, \{1,2\}\} \quad |\mathcal{P}| = 4$$

### Cartesian product $A \times B$

All ordered pairs $(a, b)$ where $a \in A$, $b \in B$.

$|A \times B| = |A| \times |B|$. Order matters: $A \times B \neq B \times A$ (unless $A = B$).

### Set identities

Mirror of logical equivalences — $\cup \leftrightarrow$ OR, $\cap \leftrightarrow$ AND, complement $\leftrightarrow$ NOT.

| identity                                                                                      | law               |
| --------------------------------------------------------------------------------------------- | ----------------- |
| $A \cup \emptyset = A \quad A \cap U = A$                                                     | identity          |
| $A \cup U = U \quad A \cap \emptyset = \emptyset$                                             | domination        |
| $A \cup A = A \quad A \cap A = A$                                                             | idempotent        |
| $A \cup B = B \cup A \quad A \cap B = B \cap A$                                               | commutative       |
| $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$                                              | distributive      |
| $\overline{A \cup B} = \bar{A} \cap \bar{B} \quad \overline{A \cap B} = \bar{A} \cup \bar{B}$ | De Morgan         |
| $A \cup (A \cap B) = A \quad A \cap (A \cup B) = A$                                           | absorption        |
| $A \cup \bar{A} = U \quad A \cap \bar{A} = \emptyset$                                         | complement        |
| $\overline{\bar{A}} = A$                                                                      | double complement |

### Subset proofs

**$\emptyset \subseteq S$** — vacuously true: $x \in \emptyset$ is always false, so $(x \in \emptyset) \Rightarrow (x \in S)$ holds for all x.

**$A \subseteq B$** — take arbitrary $x \in A$, derive $x \in B$ via $\forall x\ (x \in A) \Rightarrow (x \in B)$.

**$A = B$** — prove $A \subseteq B$ then $B \subseteq A$. Two separate subset proofs.

$$A = B \Longleftrightarrow (A \subseteq B) \wedge (B \subseteq A)$$

---

## See also

- [[Logic & Proofs]]
- [[Combinatorics]]
- [[Graph Theory]]
