---
tags: [math, discrete, relations, equivalence, order]
status: complete
---

# Relations

> A relation formalises "how elements of a set are connected" — the mathematical basis for equality, ordering, and equivalence.

## Definition

A **binary relation** $R$ on a set $A$ is a subset of the Cartesian product $A \times A$. We write $a \mathrel{R} b$ (or $(a, b) \in R$) to mean the pair $(a, b)$ belongs to $R$.

**Examples on $\mathbb{Z}$:**

| Relation             | $a \mathrel{R} b$ means | Subset of $\mathbb{Z} \times \mathbb{Z}$? |
| -------------------- | ----------------------- | ----------------------------------------- |
| $\leq$               | $a$ is at most $b$      | Yes                                       |
| $\mid$ (divides)     | $a$ divides $b$         | Yes                                       |
| $\equiv_m$ (mod $m$) | $m \mid (a - b)$        | Yes                                       |
| $=$                  | $a$ equals $b$          | Yes (diagonal)                            |

A relation can also be **heterogeneous** — a subset of $A \times B$ for two different sets — but for equivalences and orders we restrict to $A \times A$.

## Properties of relations

| Property          | Definition                                                        | Intuition                       |
| ----------------- | ----------------------------------------------------------------- | ------------------------------- |
| **Reflexive**     | $\forall a,\; a \mathrel{R} a$                                    | every element relates to itself |
| **Irreflexive**   | $\forall a,\; a \not\mathrel{R} a$                                | no element relates to itself    |
| **Symmetric**     | $a \mathrel{R} b \implies b \mathrel{R} a$                        | the relation is undirected      |
| **Antisymmetric** | $a \mathrel{R} b \wedge b \mathrel{R} a \implies a = b$           | direction is consistent         |
| **Transitive**    | $a \mathrel{R} b \wedge b \mathrel{R} c \implies a \mathrel{R} c$ | chains collapse                 |

**Which properties does each standard relation satisfy?**

| Relation               | Refl. | Sym. | Antisym. | Trans. |
| ---------------------- | ----- | ---- | -------- | ------ |
| $=$                    | ✓     | ✓    | ✓        | ✓      |
| $\leq$ on $\mathbb{Z}$ | ✓     | —    | ✓        | ✓      |
| $<$ on $\mathbb{Z}$    | —     | —    | ✓        | ✓      |
| $\mid$ on $\mathbb{N}$ | ✓     | —    | ✓        | ✓      |
| $\equiv_m$             | ✓     | ✓    | —        | ✓      |
| "is a sibling of"      | —     | ✓    | —        | —      |

## Equivalence relations

A relation that is reflexive, symmetric, and transitive is an **equivalence relation**.

The canonical example is congruence mod $m$: $a \equiv b \pmod{m}$ is reflexive ($m \mid 0$), symmetric ($m \mid (a-b) \implies m \mid (b-a)$), and transitive ($m \mid (a-b)$ and $m \mid (b-c)$ implies $m \mid (a-c)$).

### Equivalence classes and partitions

The **equivalence class** of $a$ under $R$ is

$$[a]_R = \{x \in A \mid x \mathrel{R} a\}.$$

Two equivalence classes are either identical or disjoint — they never partially overlap.

**Theorem.** An equivalence relation $R$ on $A$ partitions $A$ into disjoint equivalence classes whose union is all of $A$. Conversely, every partition of $A$ defines an equivalence relation.

**Proof.** (_Classes are disjoint or identical._) Suppose $[a] \cap [b] \neq \emptyset$; let $c \in [a] \cap [b]$, so $c \mathrel{R} a$ and $c \mathrel{R} b$. By symmetry $a \mathrel{R} c$, and by transitivity $a \mathrel{R} b$. Then for any $x \in [a]$: $x \mathrel{R} a$ and $a \mathrel{R} b$ gives $x \mathrel{R} b$, so $x \in [b]$. Hence $[a] \subseteq [b]$; symmetrically $[b] \subseteq [a]$, so $[a] = [b]$.

![[equivalence_partition.png]]

**Example.** Congruence mod $3$ partitions $\mathbb{Z}$ into three classes: $[0] = \{\ldots,-3,0,3,6,\ldots\}$, $[1] = \{\ldots,-2,1,4,7,\ldots\}$, $[2] = \{\ldots,-1,2,5,8,\ldots\}$. Modular arithmetic operates on these classes — addition and multiplication are well-defined on $\mathbb{Z}_3 = \{[0],[1],[2]\}$.

## Partial orders

A relation that is reflexive, antisymmetric, and transitive is a **partial order**. The pair $(A, R)$ is a **partially ordered set** (poset).

The word "partial" means not every pair of elements need be comparable — some pairs may have no ordering relation between them.

**Examples:**

| Poset                         | Relation     | Incomparable elements?               |
| ----------------------------- | ------------ | ------------------------------------ |
| $(\mathbb{Z}, \leq)$          | $\leq$       | None — this is a total order         |
| $(\mathcal{P}(S), \subseteq)$ | subset       | $\{1\}$ and $\{2\}$ are incomparable |
| $(\mathbb{N}^+, \mid)$        | divisibility | $2$ and $3$ are incomparable         |

### Hasse diagrams

A poset on a finite set is drawn as a **Hasse diagram**: elements are nodes, an edge goes up from $a$ to $b$ if $a \mathrel{R} b$ and no element lies strictly between them (no transitively implied edges are drawn).

![[hasse_diagram.png]]

### Total orders

A partial order where every pair is comparable — $\forall a, b,\; a \mathrel{R} b \text{ or } b \mathrel{R} a$ — is a **total order** (or linear order). Examples: $(\mathbb{Z}, \leq)$, lexicographic order on strings.

Sorting algorithms produce total orders. Database indexes exploit total orders for binary search.

### Minimum, maximum, minimal, maximal

| Term        | Definition                                                         |
| ----------- | ------------------------------------------------------------------ |
| **Minimum** | $m \in A$ with $m \mathrel{R} a$ for all $a$ (unique if it exists) |
| **Maximum** | $m \in A$ with $a \mathrel{R} m$ for all $a$ (unique if it exists) |
| **Minimal** | $m$ with no $a \neq m$ satisfying $a \mathrel{R} m$                |
| **Maximal** | $m$ with no $a \neq m$ satisfying $m \mathrel{R} a$                |

In a total order, minimal = minimum and maximal = maximum. In a partial order they can differ: $(\mathcal{P}(\{1,2\}), \subsetneq)$ has two maximal elements ($\{1\}$ and $\{2\}$) but no maximum.

## Closures

Given a relation $R$, its **transitive closure** $R^+$ is the smallest transitive relation containing $R$: $a \mathrel{R^+} b$ iff there is a path $a \mathrel{R} c_1 \mathrel{R} \cdots \mathrel{R} b$ of any length $\geq 1$.

The **reflexive-transitive closure** $R^*$ additionally includes all pairs $(a, a)$.

In CS, the transitive closure of a graph's edge relation gives reachability — the foundation of dependency analysis, type-checking, and compiler dataflow. See [[Graphs]].

## Video references

- ![Lecture 11: Relations, Partial Orders, and Scheduling](https://www.youtube.com/watch?v=1nScXLQAQ9A)

## See also

- [[Sets]]
- [[Functions]]
- [[Number Theory]]
- [[Graphs]]
- [[Index]]
