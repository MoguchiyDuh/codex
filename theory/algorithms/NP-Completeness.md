---
tags:
  - algorithms
  - np-completeness
  - complexity-theory
status: complete
---

# NP-Completeness

> A theoretical framework for classifying problems by computational hardness. NP-complete problems are the hardest in NP — solving any one of them in polynomial time would solve all of them.

## Decision problems

The theory works on **decision problems** — those with yes/no answers. Optimisation problems convert to decision problems with a threshold: "is there a solution of cost $\leq k$?"

A problem is encoded as a language $L \subseteq \{0, 1\}^*$: the set of input strings whose answer is "yes".

## The classes P and NP

| Class     | Definition                                                                                              |
| --------- | ------------------------------------------------------------------------------------------------------- |
| **P**     | Decision problems solvable in polynomial time                                                           |
| **NP**    | Decision problems whose "yes" answers are _verifiable_ in polynomial time given a certificate (witness) |
| **co-NP** | Decision problems whose "no" answers are verifiable in polynomial time                                  |
| **EXP**   | Solvable in exponential time                                                                            |

NP stands for _non-deterministic polynomial_ — equivalent definition: solvable in polynomial time on a non-deterministic Turing machine that can branch arbitrarily on each step.

**Key facts (proven):**

- $\text{P} \subseteq \text{NP}$ — anything solvable can be verified.
- $\text{P} \subseteq \text{co-NP}$.
- $\text{NP} \subseteq \text{EXP}$.

**Open (the central question):**

$$\text{P} \stackrel{?}{=} \text{NP}$$

Most computer scientists believe $\text{P} \neq \text{NP}$, but no proof exists. A proof either way wins a Clay Millennium Prize.

![[complexity_class_hierarchy.png]]

## Polynomial-time reductions

A reduction $A \leq_p B$ from problem $A$ to problem $B$ is a polynomial-time function $f$ that maps every instance $x$ of $A$ to an instance $f(x)$ of $B$ such that

$$x \in A \iff f(x) \in B$$

If $A \leq_p B$ and $B \in \text{P}$, then $A \in \text{P}$.

Reductions transfer hardness: if you can reduce a known-hard problem to a new problem, the new problem is at least as hard.

![[reduction_diagram.png]]

## NP-hard and NP-complete

| Class           | Definition                                                                            |
| --------------- | ------------------------------------------------------------------------------------- |
| **NP-hard**     | Problems $H$ such that every $L \in \text{NP}$ has $L \leq_p H$. (Need not be in NP.) |
| **NP-complete** | NP-hard problems that are also in NP                                                  |

NP-complete problems are the "hardest in NP" — every NP problem reduces to them. Consequence: if any NP-complete problem is in P, then $\text{P} = \text{NP}$.

To prove a new problem $X$ is NP-complete:

1. Show $X \in \text{NP}$ (give a polynomial-time verifier).
2. Pick a known NP-complete problem $Y$ and show $Y \leq_p X$.

The "first" NP-complete problem was **SAT** — the **Cook-Levin theorem** (1971) proves it directly from the definition of NP, by encoding any non-deterministic polynomial-time computation as a Boolean formula.

## Classic NP-complete problems

These are the problems most often used as the source of new reductions.

| Problem                     | Question                                                           |
| --------------------------- | ------------------------------------------------------------------ |
| **SAT**                     | Is a given Boolean formula satisfiable?                            |
| **3-SAT**                   | SAT restricted to clauses of $\leq 3$ literals                     |
| **CLIQUE**                  | Does graph $G$ contain a clique of size $k$?                       |
| **VERTEX-COVER**            | Does graph $G$ have a vertex cover of size $\leq k$?               |
| **INDEPENDENT-SET**         | Does graph $G$ have an independent set of size $\geq k$?           |
| **HAMILTONIAN-CYCLE**       | Does graph $G$ have a cycle visiting every vertex exactly once?    |
| **TSP (decision)**          | Is there a tour of cost $\leq k$?                                  |
| **SUBSET-SUM**              | Does a subset of $\{a_1, \dots, a_n\}$ sum to $T$?                 |
| **PARTITION**               | Can $\{a_1, \dots, a_n\}$ be split into two equal-sum subsets?     |
| **0/1 KNAPSACK (decision)** | Is there a packing of value $\geq k$?                              |
| **GRAPH-COLORING**          | Can $G$ be coloured with $k$ colours? (NP-complete for $k \geq 3$) |
| **SET-COVER**               | Cover a universe with $\leq k$ sets from a collection?             |

These cluster into families: logic (SAT variants), graph (clique, vertex-cover, etc.), arithmetic (subset-sum, knapsack), and they all reduce to each other.

The classic chain of reductions in CLRS:

$$\text{SAT} \leq_p \text{3-SAT} \leq_p \text{CLIQUE} \leq_p \text{VERTEX-COVER} \leq_p \text{HAMILTONIAN-CYCLE} \leq_p \text{TSP}$$

## Reduction examples

### 3-SAT $\leq_p$ CLIQUE

Given a 3-SAT formula with $m$ clauses, build a graph: one vertex per literal occurrence in each clause. Connect two vertices iff (a) they are in different clauses and (b) they are not negations of each other. The formula is satisfiable iff the graph has a clique of size $m$ — pick one literal per clause, all consistent (no contradictions because no negation edges).

### VERTEX-COVER $\leq_p$ INDEPENDENT-SET

$S$ is a vertex cover of $G$ iff $V \setminus S$ is an independent set. So $G$ has a vertex cover of size $\leq k$ iff $G$ has an independent set of size $\geq n - k$. The reduction is just complementation of the size parameter.

### SUBSET-SUM $\leq_p$ PARTITION

Given an instance of SUBSET-SUM with target $T$ and total sum $S$, add one element of value $|S - 2T|$. Check parity. The new set partitions into two equal-sum halves iff the original has a subset summing to $T$.

These show how mechanical the reductions can be — once a few are in hand, new ones come in pairs.

## Practical implications

A problem being NP-complete does not mean "no algorithm exists" — only that no _efficient_ (polynomial-time) algorithm is known.

| Strategy                         | Approach                                                                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------ |
| **Approximation algorithms**     | settle for provably-near-optimal solutions in polynomial time — see [[Approximation Algorithms]] |
| **Heuristics**                   | local search, simulated annealing, genetic algorithms — no guarantee but often work              |
| **Restrict the input**           | many NP-complete problems become polynomial on planar graphs, trees, bounded-treewidth graphs    |
| **Parameterised algorithms**     | exponential in some parameter $k$, polynomial in $n$ — useful when $k$ is small (FPT theory)     |
| **Pseudo-polynomial algorithms** | polynomial in numeric value (knapsack: $\Theta(nW)$) — fine for small numbers                    |
| **SAT solvers and ILP solvers**  | exponential worst case but extremely effective on real-world instances                           |
| **Branch and bound**             | exhaustive search with smart pruning — see [[Backtracking]]                                      |

## Beyond NP

| Class       | Loosely                                                                                 |
| ----------- | --------------------------------------------------------------------------------------- |
| **PSPACE**  | Polynomial _space_ (any time). Contains NP and co-NP.                                   |
| **EXPTIME** | Exponential time. Properly contains P.                                                  |
| **NEXP**    | Non-deterministic exponential time                                                      |
| **#P**      | Counting versions of NP problems (e.g. count satisfying assignments)                    |
| **PH**      | Polynomial hierarchy — generalises NP, co-NP, etc., levelled by quantifier alternations |

These richer hierarchies classify problems beyond NP, used in cryptography, formal verification, and game theory.

## Related concepts

- **Decidability** — does an algorithm exist at all? Halting problem is undecidable; NP-completeness is _within_ the decidable.
- **Reducibility** — many-one reductions, Turing reductions, log-space reductions. Each gives a different NP-complete world.
- **Average-case complexity** — some NP-complete problems are easy on average; cryptography needs the harder ones.

## See also

- [[Complexity]]
- [[Approximation Algorithms]]
- [[Backtracking]]
- [[Network Flow]]
- [[Index]]
