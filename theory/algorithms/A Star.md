---
tags:
  - algorithms
  - graphs
  - a-star
  - heuristic-search
  - pathfinding
status: complete
---

# A Star

> Goal-directed shortest path: Dijkstra guided by a heuristic estimate of remaining distance to the target. Optimal when the heuristic is admissible and consistent.

## Why A\*

Dijkstra explores the graph in concentric circles around the source — wasteful when you only need a path to _one_ specific target. A\* biases the search toward the goal using a heuristic $h(v)$ that estimates the remaining cost from $v$ to the target.

Best-first search by itself ($f(v) = h(v)$) is fast but not optimal — it can mistake a low-heuristic vertex for a good one. Dijkstra's $f(v) = g(v)$ (cost-so-far) is optimal but slow. A\* combines them:

$$f(v) = g(v) + h(v)$$

where $g(v)$ is the known cost from source to $v$, and $h(v)$ estimates the cost from $v$ to the goal. Always extract the vertex with smallest $f$.

## Algorithm

```pseudo
a_star(G, s, t, h):
    for each v in V:
        g[v] = ∞
        parent[v] = NIL
    g[s] = 0
    Q = min-priority queue keyed by f-value
    insert(Q, s, key = h(s))
    closed = empty set
    while Q not empty:
        u = extract_min(Q)
        if u == t: return reconstruct(parent, t)
        closed.add(u)
        for each (u, v, w) in adj[u]:
            if v in closed: continue
            tentative = g[u] + w
            if tentative < g[v]:
                g[v] = tentative
                parent[v] = u
                f = tentative + h(v)
                insert(Q, v, key = f)        # or decrease-key if already in Q
    return NO_PATH
```

**Code:** `theory/algorithms/showcase/path_finding/a_star.py`

The structure mirrors Dijkstra; the only change is the priority key.

## Video references

- ![A* Pathfinding (E01: algorithm explanation) - Clear visualization of the A* algorithm mechanics and heuristics.](https://youtu.be/-L-WgKMFuhE)

## Heuristic properties

The heuristic determines whether A\* is correct, optimal, and efficient.

| Property                              | Definition                                                             | Implication                                                                   |
| ------------------------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Admissible**                        | $h(v) \leq h^*(v)$ for all $v$ — never overestimates true cost to goal | A\* finds an optimal path                                                     |
| **Consistent** (monotone)             | $h(u) \leq w(u, v) + h(v)$ for every edge                              | Each vertex extracted has its final $g$-value; no need to reopen closed nodes |
| **Zero heuristic** $h(v) = 0$         | trivially admissible and consistent                                    | A\* degrades to Dijkstra                                                      |
| **Perfect heuristic** $h(v) = h^*(v)$ | knows the answer                                                       | A\* expands only vertices on a shortest path                                  |

Consistency implies admissibility. Most natural heuristics on metric spaces (Euclidean, Manhattan) are consistent.

### Common heuristics

| Domain                           | Heuristic                                             |
| -------------------------------- | ----------------------------------------------------- | --------- | --- | --------- | --- |
| Grid with 4-directional movement | Manhattan distance $                                  | x_1 - x_2 | +   | y_1 - y_2 | $   |
| Grid with 8-directional movement | Chebyshev or octile distance                          |
| Continuous 2D / 3D               | Euclidean distance                                    |
| Road network                     | great-circle distance, scaled by speed limit          |
| Puzzle (15-puzzle, Rubik's)      | sum of tile-displacement distances, pattern databases |

A heuristic is **stronger** when it returns higher (but still admissible) values — closer to $h^*$. Stronger heuristics expand fewer nodes.

## Correctness

**Theorem.** With an admissible heuristic, A\* returns an optimal path if one exists.

**Sketch.** Suppose A* terminates with a suboptimal path. Let $v$ be the first vertex on a true optimal path that is still in the open set when A* extracts the goal $t$. Then $f(v) = g(v) + h(v) \leq g(v) + h^*(v) = $ true optimal cost $< g(t) = f(t)$, contradicting that A\* extracted $t$ before $v$.

With consistency the proof is sharper: $f$ along any path is non-decreasing, and each vertex is finalised on first extraction.

## Complexity

A\* has the same worst-case bounds as Dijkstra — $\Theta((n + m) \log n)$ — but in practice expands far fewer nodes when the heuristic is informative.

| Heuristic quality           | Behaviour                                                         |
| --------------------------- | ----------------------------------------------------------------- |
| $h \equiv 0$                | Dijkstra                                                          |
| Weak (admissible but loose) | between Dijkstra and goal-directed                                |
| Strong (close to $h^*$)     | nearly straight-line search to goal                               |
| Perfect                     | only nodes on the shortest path expanded                          |
| Inadmissible                | fast but no optimality guarantee — useful for "good enough" paths |

The standard textbook bound is the **effective branching factor** $b^*$: A* expands $\Theta((b^*)^d)$ nodes for solution depth $d$. A better heuristic reduces $b^*$.

## Variants

| Variant                         | Idea                                           | Use                             |
| ------------------------------- | ---------------------------------------------- | ------------------------------- |
| **Weighted A\***                | $f = g + \varepsilon h$ with $\varepsilon > 1$ | faster, near-optimal solutions  |
| **IDA\*** (iterative deepening) | DFS with $f$-bound, increase iteratively       | $\Theta(d)$ memory; for puzzles |
| **Bidirectional A\***           | search from $s$ and $t$ simultaneously         | road networks                   |
| **D\* / D\* Lite**              | incremental A\* for changing graphs            | robotics, replanning            |
| **Anytime A\***                 | weighted A\* that improves the bound over time | real-time systems               |
| **Jump-point search**           | grid-specific pruning of equivalent paths      | large open grids in games       |

## A\* vs Dijkstra vs BFS

|                 | BFS              | Dijkstra               | A\*                                   |
| --------------- | ---------------- | ---------------------- | ------------------------------------- |
| Edge weights    | unweighted       | non-negative           | non-negative                          |
| Heuristic       | none             | none                   | required                              |
| Source-to-all?  | yes              | yes                    | typically single-target               |
| Expansion order | hop-count        | $g(v)$                 | $g(v) + h(v)$                         |
| Time            | $\Theta(n + m)$  | $\Theta((n+m) \log n)$ | $\leq$ Dijkstra (heuristic-dependent) |
| Optimality      | yes (unweighted) | yes                    | iff $h$ admissible                    |

## When to use A\*

| Situation                                 | A\* / not                                         |
| ----------------------------------------- | ------------------------------------------------- |
| Pathfinding in games / robotics on a grid | yes — Manhattan or Euclidean heuristic            |
| Route planning on road networks           | yes — great-circle heuristic, often bidirectional |
| Generic graph SSSP                        | no — Dijkstra (no useful heuristic)               |
| Single-pair, no domain structure          | no — same as Dijkstra                             |
| Need all-pairs                            | no — A\* is single-target                         |
| Need optimal under negative weights       | no — A\* requires non-negative                    |

## Caveats

- **Memory.** A* stores all opened nodes; on huge state spaces (puzzles, planning) this dominates. IDA* trades time for memory.
- **Heuristic computation cost.** A heuristic that takes $\Theta(n)$ to evaluate per call destroys the speedup. Real-world heuristics must be $\Theta(1)$ or amortised cheap.
- **Tie-breaking.** When multiple vertices have equal $f$, prefer the one with larger $g$ (closer to goal) — fewer expansions in practice.

## See also

- [[Shortest Path]]
- [[Graph Basics]]
- [[../data_structures/Heap|Heap]]
- [[Greedy Algorithms]]
- [[Index]]
