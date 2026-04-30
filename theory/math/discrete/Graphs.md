---
tags: [math, discrete, graphs, graph-theory]
status: complete
---

# Graphs

> The mathematics of pairwise relationships — definitions, theorems, and structural properties that underpin every graph algorithm.

This note covers the mathematical side only. Storage representations live in [[../../data_structures/Graphs|Graphs (data structures)]]; traversal and algorithm complexity live in [[../../algorithms/Graph Basics|Graph Basics]].

## Definitions

A **graph** $G = (V, E)$ consists of a set of **vertices** $V$ and a set of **edges** $E \subseteq \binom{V}{2}$, where each edge is a 2-element subset $\{u, v\}$ of $V$.

- **Simple graph**: no self-loops ($\{v,v\}$), no parallel edges. Default assumption.
- **Directed graph** (digraph): edges are ordered pairs $(u,v)$; direction matters.
- **Multigraph**: parallel edges allowed.
- **Weighted graph**: each edge carries a real-valued weight.

| Parameter | Symbol | Meaning |
|---|---|---|
| Number of vertices | $n = \|V\|$ | order of the graph |
| Number of edges | $m = \|E\|$ | size of the graph |
| Degree of $v$ | $\deg(v)$ | number of edges incident to $v$ |

For a directed graph, distinguish **in-degree** $\deg^-(v)$ and **out-degree** $\deg^+(v)$.

## Handshaking lemma

$$\sum_{v \in V} \deg(v) = 2m.$$

**Proof.** Each edge $\{u,v\}$ contributes exactly $1$ to $\deg(u)$ and $1$ to $\deg(v)$, so it contributes $2$ to the total degree sum. Summing over all $m$ edges gives $2m$.

**Corollary.** Every graph has an even number of odd-degree vertices.

**Proof.** Split $V$ into even-degree vertices $V_e$ and odd-degree vertices $V_o$. Then $\sum_{v \in V_e} \deg(v) + \sum_{v \in V_o} \deg(v) = 2m$. The first sum is even; $2m$ is even; so the second sum is even. A sum of odd numbers is even iff the count of terms is even.

This corollary is the reason you cannot draw a map with exactly three odd-degree landmasses sharing borders — it would require an odd number of odd-degree vertices.

## Paths, walks, and cycles

A **walk** of length $k$ is a sequence $v_0, v_1, \ldots, v_k$ where $\{v_i, v_{i+1}\} \in E$ for each $i$.

- **Path**: a walk with no repeated vertices.
- **Cycle**: a walk with $v_0 = v_k$ and no other repeated vertices, length $\geq 3$ (undirected) or $\geq 2$ (directed with distinct edges).
- **Simple**: "simple path" and "simple cycle" are common synonyms for path and cycle.

A graph with no cycles is **acyclic**. An acyclic connected undirected graph is a tree (see [[Trees]]).

## Connectivity

**Connected graph**: there is a path between every pair of vertices. Otherwise the graph has multiple **connected components** — maximal connected subgraphs.

**For directed graphs:**

- **Weakly connected**: the underlying undirected graph (ignoring edge direction) is connected.
- **Strongly connected**: there is a directed path from $u$ to $v$ and from $v$ to $u$ for every pair $(u,v)$. The **strongly connected components** (SCCs) are the maximal strongly-connected subgraphs; they partition $V$. Their condensation is always a DAG.

![[graph_connectivity.png]]

## Bipartite graphs

$G = (V, E)$ is **bipartite** if $V$ can be partitioned into two sets $L$ and $R$ such that every edge goes between $L$ and $R$ — no edge has both endpoints in the same part.

**Characterisation.** $G$ is bipartite if and only if it contains no odd-length cycle.

**Proof sketch.** ($\Rightarrow$) In a bipartite graph, any walk alternates between $L$ and $R$, so it takes an even number of steps to return to the start — no odd cycle. ($\Leftarrow$) If no odd cycle exists, 2-colour the graph by BFS layers: vertices at even depth get colour $L$, odd depth get colour $R$. An edge between two vertices of the same colour would create an odd cycle — contradiction.

Bipartiteness is detected by BFS in $O(n + m)$ (see [[../../algorithms/Graph Basics|Graph Basics]]).

## Euler tours

An **Eulerian path** visits every edge exactly once. An **Eulerian circuit** is an Eulerian path that starts and ends at the same vertex.

**Theorem (Euler 1736).** A connected graph has an Eulerian circuit if and only if every vertex has even degree.

**Proof sketch.** ($\Rightarrow$) Any circuit entering a vertex must also leave it, consuming edges in pairs — every vertex has even degree. ($\Leftarrow$) Start a walk from any vertex, always moving along an unvisited edge, never revisiting an edge. Because every vertex has even degree, whenever the walk enters a vertex it can always leave (until all edges incident to the start are exhausted). The walk must return to the start. If unused edges remain, there is a vertex on the current circuit with unused edges; splice in a sub-circuit from there. Repeating this merging process covers all edges.

**Corollary.** A connected graph has an Eulerian path (not necessarily a circuit) iff it has exactly zero or two odd-degree vertices.

The original problem Euler solved: the seven bridges of Königsberg. Each landmass had odd degree — no Eulerian circuit existed.

![[euler_tour.png]]

## Planar graphs

A graph is **planar** if it can be drawn in the plane with no edge crossings.

**Euler's formula.** For any connected planar graph with $n$ vertices, $m$ edges, and $f$ faces (including the outer infinite face):

$$n - m + f = 2.$$

**Proof by induction on $m$.** Base: a tree has $n$ vertices, $n-1$ edges, $1$ face: $n - (n-1) + 1 = 2$. ✓. Inductive step: take any edge $e$ on a cycle. Removing $e$ merges two faces into one, reducing $m$ by $1$ and $f$ by $1$, leaving $n - m + f$ unchanged.

**Corollary.** For a simple planar graph ($n \geq 3$): $m \leq 3n - 6$.

**Proof.** Each face is bounded by $\geq 3$ edges; each edge borders $\leq 2$ faces, so $3f \leq 2m$. Combined with $n - m + f = 2$: $f = 2 - n + m$, so $3(2 - n + m) \leq 2m$, giving $m \leq 3n - 6$.

$K_5$ ($5$ vertices, $10$ edges): $3 \cdot 5 - 6 = 9 < 10$ — not planar. Similarly $K_{3,3}$ is not planar. By Kuratowski's theorem, these are the only obstructions: a graph is planar iff it contains no subdivision of $K_5$ or $K_{3,3}$.

## Graph colouring

A **proper $k$-colouring** assigns one of $k$ colours to each vertex so that no two adjacent vertices share a colour. The **chromatic number** $\chi(G)$ is the minimum $k$ for which a proper colouring exists.

| Graph | $\chi$ |
|---|---|
| Empty graph ($m=0$) | $1$ |
| Any bipartite graph | $\leq 2$ (and $= 2$ if any edge exists) |
| Odd cycle $C_{2k+1}$ | $3$ |
| Complete graph $K_n$ | $n$ |
| Planar graph | $\leq 4$ (four colour theorem) |

**Greedy colouring bound.** $\chi(G) \leq \Delta(G) + 1$, where $\Delta(G)$ is the maximum degree. Proof: colour vertices one by one; each vertex has at most $\Delta$ neighbours already coloured, so at least one of $\Delta + 1$ colours is always available.

**CS application.** Register allocation in compilers is a graph colouring problem: vertices are variables, edges connect variables live at the same time, colours are registers. Minimising the number of registers used is equivalent to finding $\chi(G)$ — NP-hard in general, so compilers use greedy heuristics.

## Matching

A **matching** $M \subseteq E$ is a set of edges no two of which share a vertex. A **perfect matching** covers every vertex.

**Hall's theorem.** A bipartite graph $G = (L \cup R, E)$ has a matching that covers all of $L$ iff for every $S \subseteq L$, the neighbourhood $N(S)$ satisfies $|N(S)| \geq |S|$.

The condition "$|N(S)| \geq |S|$ for all $S$" is **Hall's condition**. Intuitively: no subset of $L$ is "too demanding" for $R$ to supply.

Matchings formalise assignment problems: workers to jobs, medical students to hospitals (the stable matching problem in 6.042J), tasks to machines.

## See also

- [[Trees]]
- [[Relations]]
- [[Counting]]
- [[../../data_structures/Graphs|Graphs (data structures)]]
- [[../../algorithms/Graph Basics|Graph Basics]]
- [[Index]]
