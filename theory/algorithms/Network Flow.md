---
tags:
  - algorithms
  - graphs
  - max-flow
  - min-cut
  - ford-fulkerson
status: complete
---

# Network Flow

> Send the maximum amount of "flow" from a source $s$ to a sink $t$ through a directed graph with capacity-limited edges.

## Flow networks

A **flow network** is a directed graph $G = (V, E)$ with:

- Two designated vertices: source $s$ and sink $t$.
- A non-negative **capacity** $c(u, v) \geq 0$ on each edge (or $0$ if no edge).

A **flow** is an assignment $f: E \to \mathbb{R}_{\geq 0}$ satisfying two constraints:

| Constraint | Statement |
|---|---|
| Capacity | $0 \leq f(u, v) \leq c(u, v)$ for every edge |
| Conservation | for every $v \neq s, t$: total flow in equals total flow out |

The **value** of a flow is the net flow leaving the source: $|f| = \sum_v f(s, v) - \sum_v f(v, s)$.

The **maximum-flow problem** asks for a flow with the largest value.

## Min-cut

A **cut** is a partition $(S, T)$ with $s \in S$ and $t \in T$. Its **capacity** is the sum of capacities on edges from $S$ to $T$ (only forward direction).

The **min-cut problem** asks for a cut of minimum capacity — the bottleneck separating $s$ from $t$.

## Max-flow min-cut theorem

The central result of network flow:

$$\max_{f}\, |f| \;=\; \min_{(S, T)} c(S, T)$$

The maximum value of a flow equals the minimum capacity of an $s$–$t$ cut. Three equivalent statements:

| Statement | Direction |
|---|---|
| $f$ is a max flow | iff |
| there exists no augmenting path in the residual graph | iff |
| $|f|$ equals the capacity of some cut |

This is what makes flow algorithms work: we increase $|f|$ until no augmenting path remains, at which point the flow is provably optimal.

## Residual graph

Given a flow $f$, the **residual graph** $G_f$ has, for every original edge $(u, v)$:

- A forward residual edge $(u, v)$ with capacity $c(u, v) - f(u, v)$ — remaining room.
- A backward residual edge $(v, u)$ with capacity $f(u, v)$ — flow that could be cancelled.

An **augmenting path** is a path from $s$ to $t$ in $G_f$ using only positive-residual-capacity edges. Pushing additional flow along it (limited by the smallest residual capacity on the path — the bottleneck) increases $|f|$.

The backward edges are essential: they let later augmentations "undo" earlier suboptimal choices.

## Ford-Fulkerson

The general method: repeatedly find an augmenting path and push flow along it.

```pseudo
ford_fulkerson(G, s, t):
    initialise f(u, v) = 0 for all edges
    while there exists an augmenting path P in residual G_f:
        b = min residual capacity on P
        for each edge (u, v) in P:
            f(u, v) += b
            f(v, u) -= b      # update via residual
    return f
```

**Code:** `theory/algorithms/showcase/max_flow.py`

The method's complexity depends on **how** augmenting paths are found.


### Naive Ford-Fulkerson (DFS to find paths)

If capacities are integers, each augmentation increases $|f|$ by at least $1$. Total iterations $\leq |f^*|$, each costing $\Theta(m)$.

| Property | Value |
|---|---|
| Time | $\Theta(m \cdot |f^*|)$ |
| Issue | for irrational capacities may not terminate; for large $|f^*|$ very slow |

The pathological example: a four-vertex graph where bad path choices ping-pong $|f^*|$ times even when $|f^*|$ is huge.

### Edmonds-Karp

Always pick the **shortest** augmenting path (BFS in the residual graph).

| Property | Value |
|---|---|
| Time | $\Theta(n m^2)$ |
| Termination | always, regardless of capacities |

The bound holds even for irrational capacities. Proof uses the fact that the shortest path length monotonically increases, so each edge can be "saturated" at most $\Theta(n)$ times.

### Dinic's algorithm

Use BFS to build a layered graph, then push **blocking flows** through it. More efficient in practice and theoretically.

| Property | Value |
|---|---|
| Time | $\Theta(n^2 m)$ |
| Time (unit capacities) | $\Theta(m \sqrt{n})$ — used for bipartite matching |

Dinic's is the standard choice in competitive programming and most production max-flow code.

### Push-relabel

A different paradigm that doesn't use augmenting paths. Maintains a *preflow* (allows excess at vertices) and pushes flow downhill via vertex labels (heights).

| Property | Value |
|---|---|
| Time (generic) | $\Theta(n^2 m)$ |
| Time (highest-label) | $\Theta(n^2 \sqrt{m})$ |

Asymptotically the fastest in dense graphs.

## Algorithm summary

| Algorithm | Time | Notes |
|---|---|---|
| Ford-Fulkerson (DFS) | $\Theta(m |f^*|)$ | only safe for integer capacities |
| **Edmonds-Karp** | $\Theta(nm^2)$ | shortest augmenting path via BFS |
| **Dinic's** | $\Theta(n^2 m)$ | layered + blocking flow; standard in practice |
| Push-relabel | $\Theta(n^2 \sqrt{m})$ | preflow paradigm |
| Orlin's | $\Theta(nm)$ | strongly polynomial — theoretical |

## Applications

Max-flow is the underlying solver for many seemingly unrelated problems via reductions.

| Problem | Reduction |
|---|---|
| **Bipartite matching** | source → left side → right side → sink, all unit capacity. Max matching = max flow |
| **Edge-disjoint paths** | unit capacities; max flow = max disjoint $s$–$t$ paths (Menger's theorem) |
| **Vertex-disjoint paths** | split each vertex into two; edge between them has unit capacity |
| **Image segmentation** | foreground/background separation as min-cut |
| **Project selection** | max-weight closure problem reduces to min-cut |
| **Baseball elimination** | construct a flow network where saturation = team eliminated |

## Min-cost flow

Add a per-unit cost to each edge; find a flow of given value with minimum total cost. Solved by successive-shortest-paths or cycle-canceling, both polynomial.

Applications: transportation problems, assignment with weights, traffic engineering.

## Practical notes

- **Capacities are always non-negative.** Negative would make the problem ill-defined.
- **Multiple sources/sinks**: add a super-source connecting to all sources with infinite capacity; symmetric for sinks.
- **Vertex capacities**: split each vertex into two connected by an edge of the desired capacity.
- **Undirected edges**: replace with two directed edges, each of the same capacity.

The transformation tricks above let max-flow solve a wide variety of constraint problems with a single solver.

## Video references

- ![Ford-Fulkerson in 5 minutes](https://www.youtube.com/watch?v=Tl90tNtKvxs)

## See also

- [[Graph Basics]]
- [[Shortest Path]]
- [[Greedy Algorithms]]
- [[Approximation Algorithms]]
- [[NP-Completeness]]
- [[Index]]
