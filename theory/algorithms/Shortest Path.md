---
tags:
  - algorithms
  - graphs
  - shortest-path
  - dijkstra
  - bellman-ford
status: complete
---

# Shortest Path

> Find a minimum-weight path from a source vertex to every other vertex in a weighted graph. The single-source shortest path (SSSP) problem.

## Problem variants

| Variant | Goal |
|---|---|
| Single-source shortest path | shortest paths from one source $s$ to all vertices |
| Single-pair | shortest path between two specific vertices |
| Single-destination | shortest paths from all vertices to one destination |
| All-pairs | shortest paths between every pair (see [[All-Pairs Shortest Path]]) |

In practice nobody solves "single-pair" specially — early-terminating an SSSP algorithm at the destination is asymptotically the same.

## Edge weights

| Weight type | Algorithm | Time |
|---|---|---|
| Unweighted (or all equal) | BFS | $\Theta(n + m)$ |
| Non-negative | Dijkstra | $\Theta((n + m) \log n)$ with binary heap |
| Arbitrary (negative allowed, no negative cycles) | Bellman-Ford | $\Theta(nm)$ |
| DAG, any weights | DAG-shortest-path (topological + relaxation) | $\Theta(n + m)$ |
| Goal-directed with admissible heuristic | A* | depends on heuristic; never worse than Dijkstra |

A negative cycle reachable from $s$ makes shortest paths undefined — you can drive the cost arbitrarily low by looping. Bellman-Ford detects this.

## Relaxation

Every shortest-path algorithm here is built on a single primitive: **edge relaxation**.

```pseudo
relax(u, v, w):
    if dist[u] + w(u, v) < dist[v]:
        dist[v] = dist[u] + w(u, v)
        parent[v] = u
```

The current best-known distance to $v$ is improved if going through $u$ is shorter. After enough relaxations, `dist[v]` equals the true shortest-path cost. Algorithms differ in *which order* they relax edges and *when they stop*.

The triangle inequality $\delta(s, v) \leq \delta(s, u) + w(u, v)$ guarantees relaxation never overshoots — `dist[v]` is always an upper bound on the true distance.

## Dijkstra's algorithm

Greedy SSSP for non-negative weights. Maintain a set $S$ of vertices whose final shortest distance is known; repeatedly extract the unvisited vertex with smallest tentative distance, add it to $S$, and relax its outgoing edges.

```pseudo
dijkstra(G, s):
    for each v in V:
        dist[v] = ∞
        parent[v] = NIL
    dist[s] = 0
    Q = min-priority queue keyed by dist, containing all vertices
    while Q not empty:
        u = extract_min(Q)
        for each (u, v) in adj[u]:
            if dist[u] + w(u, v) < dist[v]:
                dist[v] = dist[u] + w(u, v)
                parent[v] = u
                decrease_key(Q, v)
```

**Code:** `theory/algorithms/showcase/path_finding/dijkstra.py`

### Complexity

| Priority queue | Total time |
|---|---|
| Array (linear scan for min) | $\Theta(n^2)$ — best for dense graphs |
| Binary heap | $\Theta((n + m) \log n)$ |
| Fibonacci heap | $\Theta(m + n \log n)$ — theoretical, rarely faster in practice |

For sparse graphs ($m = O(n)$), the binary heap version dominates.

### Why non-negative weights are required

Dijkstra's correctness relies on the invariant: when a vertex $u$ is extracted from the queue, `dist[u]` equals the true shortest distance. Proof: any shorter path to $u$ would have to pass through some unvisited vertex $v$ with `dist[v] < dist[u]`; but then $v$ would have been extracted first.

This argument fails with negative edges — a "later" detour through a negative edge could improve a vertex's distance after we've finalised it. Dijkstra silently produces wrong answers; it does not error out.

## Bellman-Ford

Handles arbitrary edge weights. Relax every edge, $n - 1$ times.

```pseudo
bellman_ford(G, s):
    for each v in V:
        dist[v] = ∞
        parent[v] = NIL
    dist[s] = 0
    for i = 1 to n - 1:
        for each edge (u, v, w) in E:
            relax(u, v, w)
    # negative-cycle check
    for each edge (u, v, w) in E:
        if dist[u] + w < dist[v]:
            error "negative cycle reachable from s"
```

**Code:** `theory/algorithms/showcase/path_finding/bellman_ford.py`


### Complexity

| Property | Value |
|---|---|
| Time | $\Theta(nm)$ |
| Space | $\Theta(n)$ |
| Detects negative cycle | yes |

### Why $n - 1$ passes suffice

A simple path has at most $n - 1$ edges. Lemma: after the $k$-th pass, `dist[v]` is at most the cost of any shortest path from $s$ to $v$ using at most $k$ edges. After $n - 1$ passes, all simple shortest paths are captured. A further pass that still relaxes any edge proves the existence of a negative cycle.

### Optimisations

- **SPFA** (Shortest Path Faster Algorithm): a queue-based variant that only relaxes edges from vertices whose distance just improved. Average performance much better than $\Theta(nm)$ on real graphs, but worst case is still $\Theta(nm)$.
- **Early termination**: if a full pass relaxes nothing, the answer is final — terminate.

## DAG shortest path

If the graph is a DAG, topologically sort the vertices and relax edges in that order. One linear pass.

```pseudo
dag_shortest_path(G, s):
    L = topological_sort(G)
    for each v in V: dist[v] = ∞
    dist[s] = 0
    for each u in L (in topological order):
        for each (u, v) in adj[u]:
            relax(u, v, w(u, v))
```

| Property | Value |
|---|---|
| Time | $\Theta(n + m)$ |
| Weights | any (negative allowed, no cycles to worry about) |

Faster than Dijkstra and Bellman-Ford because the topological order eliminates the priority queue and the multi-pass relaxation. Used in PERT charts, longest path in DAG (negate weights), and DAG-shaped DP problems.

## Algorithm selection

| Situation | Algorithm | Reason |
|---|---|---|
| Unweighted graph | BFS | $\Theta(n + m)$, no heap needed |
| Weighted, non-negative | Dijkstra | optimal greedy, $\Theta((n+m)\log n)$ |
| Weighted, possibly negative, no negative cycles | Bellman-Ford | only correct option |
| DAG, any weights | DAG-shortest-path | linear time |
| Single-pair with heuristic | A* | best when domain knowledge available |
| All pairs, dense, small $n$ | Floyd-Warshall | $\Theta(n^3)$ — see [[All-Pairs Shortest Path]] |
| All pairs, sparse | Johnson's | $\Theta(n m \log n)$ — see [[All-Pairs Shortest Path]] |

## Path reconstruction

Each algorithm above maintains a `parent` array. To extract the shortest $s \to v$ path:

```pseudo
path(v):
    if v == NIL: return []
    if v == s: return [s]
    return path(parent[v]) + [v]
```

If `parent[v] == NIL` and `v != s`, then $v$ is unreachable.

## Practical notes

- **Dijkstra implementations** in production usually use a binary heap with lazy deletion: instead of `decrease_key`, push a duplicate entry and skip outdated ones on extraction. Simpler code, same asymptotic cost.
- **Sparse vs dense.** For dense graphs the array-based Dijkstra ($\Theta(n^2)$) actually beats the heap version because $m = \Theta(n^2)$ makes the heap factor cost more than save.
- **Bidirectional Dijkstra** runs the algorithm forward from $s$ and backward from $t$ simultaneously, terminating when frontiers meet. Often $\sqrt{}$ smaller search than one-way Dijkstra in practice.

## Video references

- ![Dijkstra's algorithm in 3 minutes - Step by step instructions showing how to run Dijkstra's algorithm on a graph.](https://youtu.be/_lHSawdgXpI)
- ![Bellman-Ford in 4 minutes — Theory](https://www.youtube.com/watch?v=9PHkk0UavIM)
- ![Bellman-Ford in 5 minutes — Step by step example](https://www.youtube.com/watch?v=obWXjtg0L64)

## See also

- [[Graph Basics]]
- [[A Star]]
- [[All-Pairs Shortest Path]]
- [[Minimum Spanning Tree]]
- [[../data_structures/Heap|Heap]]
- [[Index]]
