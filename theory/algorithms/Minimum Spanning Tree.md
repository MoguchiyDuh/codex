---
tags:
  - algorithms
  - graphs
  - mst
  - kruskal
  - prim
status: complete
---

# Minimum Spanning Tree

> A subset of edges that connects all vertices of a weighted undirected graph with minimum total weight, forming a tree.

## Definition

Given a connected undirected graph $G = (V, E)$ with edge weights $w$, a **spanning tree** is a subgraph that:

- includes every vertex,
- is connected,
- contains no cycles — equivalently, has exactly $n - 1$ edges.

A **minimum spanning tree (MST)** is a spanning tree of minimum total edge weight. If edge weights are distinct, the MST is unique.

Applications: network design (laying cable, water pipes, road networks), cluster analysis (building dendrograms), approximation algorithms (TSP 2-approximation), image segmentation.

## The cut property

The reason both standard MST algorithms work is a single structural fact.

**Cut property.** For any partition (cut) of $V$ into two non-empty sets $S$ and $V \setminus S$, the lightest edge crossing the cut is in some MST.

**Proof.** Suppose an MST $T$ does not contain the lightest crossing edge $e$. Adding $e$ to $T$ creates a unique cycle, which must contain another edge $f$ crossing the cut (since $e$ does). Since $f \neq e$ and $e$ is lightest, $w(e) \leq w(f)$. Replacing $f$ with $e$ produces a spanning tree of cost $\leq T$ — also an MST.

This is an exchange argument — the MST setting where greedy is provably correct. See [[Greedy Algorithms]].

A symmetric **cycle property** says: for any cycle in $G$, the heaviest edge on it is _not_ in any MST.

## Kruskal's algorithm

Process edges in increasing weight order; add each edge if it does not form a cycle with previously chosen edges. Cycle check via [[../data_structures/Disjoint Set|union-find]].

```pseudo
kruskal(G):
    A = empty set
    for each v in V: make_set(v)
    sort edges of E by weight ascending
    for each edge (u, v, w) in sorted order:
        if find(u) ≠ find(v):
            A = A ∪ {(u, v)}
            union(u, v)
    return A
```

**Code:** `theory/algorithms/showcase/mst/kruskal.py`

| Property       | Value                                        |
| -------------- | -------------------------------------------- |
| Time           | $\Theta(m \log m)$ for sort, dominated by it |
| Space          | $\Theta(n + m)$                              |
| Implementation | sort + union-find                            |

The cut at each step: when considering edge $(u, v)$, the cut separates $\{u\}\text{'s component}$ from the rest. The current edge is the lightest _unconsidered_ edge crossing that cut; the cut property says it's safe to add (if it isn't already internal to one side, in which case it would close a cycle).

## Prim's algorithm

Grow an MST one vertex at a time from an arbitrary start. Maintain the set $S$ of vertices already in the tree; repeatedly add the lightest edge with one endpoint in $S$ and one outside.

```pseudo
prim(G, s):
    for each v in V:
        key[v] = ∞
        parent[v] = NIL
    key[s] = 0
    Q = min-priority queue of V keyed by key
    while Q not empty:
        u = extract_min(Q)
        for each (u, v, w) in adj[u]:
            if v in Q and w < key[v]:
                parent[v] = u
                key[v] = w
                decrease_key(Q, v)
    return {(parent[v], v) : v ≠ s}
```

**Code:** `theory/algorithms/showcase/mst/prim.py`

The cut at each step is between $S$ and $V \setminus S$. Extracting min finds the lightest crossing edge — safe to add by the cut property.

| Priority queue | Total time               |
| -------------- | ------------------------ |
| Array          | $\Theta(n^2)$            |
| Binary heap    | $\Theta((n + m) \log n)$ |
| Fibonacci heap | $\Theta(m + n \log n)$   |

Prim's is structurally identical to [[Shortest Path|Dijkstra]] but with `key[v] = w(u, v)` instead of `key[v] = dist[u] + w(u, v)`.

## Comparing the two

|                       | Kruskal                                                    | Prim                                            |
| --------------------- | ---------------------------------------------------------- | ----------------------------------------------- |
| Strategy              | edge-centric: pick smallest edge that doesn't form a cycle | vertex-centric: grow connected tree from a root |
| Data structure        | union-find                                                 | priority queue                                  |
| Time (sparse)         | $\Theta(m \log m)$                                         | $\Theta((n+m) \log n)$                          |
| Time (dense)          | $\Theta(m \log m) = \Theta(n^2 \log n)$                    | $\Theta(n^2)$ with array                        |
| Best for              | sparse graphs, distributed processing                      | dense graphs                                    |
| Pre-sorted edges?     | $\Theta(m \alpha(n))$ — almost linear                      | not applicable                                  |
| Edges given as stream | natural fit                                                | needs the full graph upfront                    |

For sparse graphs Kruskal is simpler and competitive. For dense graphs Prim with an array beats Kruskal because the sort dominates Kruskal's running time.

## Borůvka's algorithm

The oldest MST algorithm (1926). In each phase, every component finds its lightest outgoing edge in parallel; merge along those edges. Number of components halves each phase.

| Property    | Value                           |
| ----------- | ------------------------------- |
| Time        | $\Theta(m \log n)$              |
| Phases      | $O(\log n)$                     |
| Suitability | parallelism, distributed graphs |

Modern hybrid algorithms (e.g. Borůvka + Prim) achieve $\Theta(m \alpha(n))$ but are intricate.

## Edge cases

- **Disconnected graph.** No spanning tree exists. Kruskal terminates with multiple trees — a **minimum spanning forest**, often the desired output.
- **Equal-weight edges.** Multiple MSTs possible. All are equally valid.
- **Negative weights.** No issue — MST cares only about ordering, not signs.
- **Self-loops.** Ignored (they cannot be in a tree).
- **Parallel edges.** Only the lightest matters.

## Applications

| Domain          | Use of MST                                                                  |
| --------------- | --------------------------------------------------------------------------- |
| Network design  | minimum cost wiring / piping connecting all sites                           |
| Clustering      | single-linkage clustering = MST followed by removing $k - 1$ heaviest edges |
| Approximation   | TSP 2-approximation = DFS of MST + shortcut                                 |
| Computer vision | image segmentation via Felzenszwalb-Huttenlocher                            |
| Phylogenetics   | building evolutionary trees from genetic distance                           |

## Video references

- ![Kruskal's algorithm in 2 minutes - Step by step instructions showing how to run Kruskal's algorithm on a graph.](https://youtu.be/71UQH7Pr9kU)
- ![Prim's algorithm in 2 minutes - Step by step instructions showing how to run Prim's algorithm on a graph.](https://youtu.be/cplfcGZmX7I)

## See also

- [[Greedy Algorithms]]
- [[Graph Basics]]
- [[../data_structures/Disjoint Set|Disjoint Set]]
- [[../data_structures/Heap|Heap]]
- [[Shortest Path]]
- [[Approximation Algorithms]]
- [[Index]]
