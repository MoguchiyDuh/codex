---
tags:
  - algorithms
  - graphs
  - shortest-path
  - floyd-warshall
  - johnson
status: complete
---

# All-Pairs Shortest Path

> Compute the shortest-path distance between every pair of vertices in a weighted graph.

## When to bother

Running [[Shortest Path|Dijkstra]] from every source gives $\Theta(n (n + m) \log n) = \Theta(n m \log n)$ on sparse graphs, $\Theta(n^3 \log n)$ on dense. The two specialised algorithms below trade flexibility for speed:

| Algorithm                      | Time                      | Space         | Negative weights        | Best for                       |
| ------------------------------ | ------------------------- | ------------- | ----------------------- | ------------------------------ |
| **Floyd-Warshall**             | $\Theta(n^3)$             | $\Theta(n^2)$ | yes (no negative cycle) | dense graphs, all-pairs needed |
| **Johnson's**                  | $\Theta(nm \log n + n^2)$ | $\Theta(n^2)$ | yes (no negative cycle) | sparse graphs                  |
| Dijkstra from every source     | $\Theta(n(n+m)\log n)$    | $\Theta(n^2)$ | no                      | non-negative weights, sparse   |
| Bellman-Ford from every source | $\Theta(n^2 m)$           | $\Theta(n^2)$ | yes                     | rarely competitive             |

## Floyd-Warshall

Dynamic programming over intermediate vertices. Let $d_{ij}^{(k)}$ be the shortest distance from $i$ to $j$ using only vertices $\{1, \dots, k\}$ as intermediate stops.

**Recurrence.**

$$d_{ij}^{(k)} = \min\left( d_{ij}^{(k-1)},\;\; d_{ik}^{(k-1)} + d_{kj}^{(k-1)} \right)$$

For each potential intermediate $k$, either it doesn't help (first term) or going $i \to k \to j$ is shorter (second term). Base: $d_{ij}^{(0)} = w(i, j)$ if edge exists, $\infty$ otherwise, $0$ on diagonal.

```pseudo
floyd_warshall(W):           # W is the n×n weight matrix
    D = copy of W
    for k = 1 to n:
        for i = 1 to n:
            for j = 1 to n:
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    next[i][j] = next[i][k]   # for path reconstruction
    return D
```

**Code:** `theory/algorithms/showcase/path_finding/floyd_warshall.py`

The two-dimensional table is updated in place — each iteration of $k$ uses values from the previous $k$, but the algorithm is correct over a single matrix because the entries that matter are not overwritten before they're read (proof in CLRS Ch. 23).

| Property                 | Value                            |
| ------------------------ | -------------------------------- |
| Time                     | $\Theta(n^3)$                    |
| Space                    | $\Theta(n^2)$                    |
| Negative weights         | allowed                          |
| Negative cycle detection | yes — `D[i][i] < 0` for some $i$ |
| Implementation           | three nested loops, very tight   |

### Why the loop order matters

The outer loop must be $k$. Permuting to $i, j, k$ would compute distances using only direct edges — incorrect. The $k$-as-outer loop ensures: when computing $d_{ij}^{(k)}$, both $d_{ik}^{(k-1)}$ and $d_{kj}^{(k-1)}$ are already finalised.

### Path reconstruction

Maintain a successor matrix `next[i][j]` — when relaxing through $k$, set `next[i][j] = next[i][k]`. To reconstruct the path: follow `next` pointers from $i$ until reaching $j$.

### Variants

- **Transitive closure** (reachability) — same algorithm with boolean OR/AND instead of $\min$/$+$. Computes whether $i$ can reach $j$ for every pair in $\Theta(n^3)$.
- **Min-cost cycle** — $\min_i d_{ii}$ after a Floyd-Warshall pass.
- **Widest-path / max-bottleneck** — replace $+$ with $\min$ and $\min$ with $\max$. Same structure, different semiring.

## Johnson's algorithm

For sparse graphs, $n^3$ is too much. Johnson's combines Bellman-Ford reweighting with $n$ runs of Dijkstra to get $\Theta(nm \log n + n^2)$.

### Reweighting trick

Negative edges block Dijkstra. Johnson's transforms the graph so all edges become non-negative without changing which paths are shortest.

1. Add a new vertex $q$ with zero-weight edges $q \to v$ for every $v$.
2. Run Bellman-Ford from $q$ to compute $h(v)$ = shortest distance from $q$ to $v$. (Detects negative cycles here.)
3. Reweight each edge: $w'(u, v) = w(u, v) + h(u) - h(v)$.
4. Run Dijkstra from each vertex on the reweighted graph.
5. Recover original distances: $\delta(u, v) = \delta'(u, v) - h(u) + h(v)$.

The triangle inequality $h(v) \leq h(u) + w(u, v)$ ensures all $w' \geq 0$. Path costs change by a constant ($h(s) - h(t)$) so shortest paths are preserved.

```pseudo
johnson(G):
    add vertex q with edges q→v of weight 0
    h = bellman_ford(G, q)         # error if negative cycle
    for each edge (u, v, w):
        w'(u, v) = w + h[u] - h[v]
    remove q
    for each u in V:
        d_u = dijkstra(G', u)
        for each v in V:
            δ(u, v) = d_u[v] - h[u] + h[v]
    return δ
```

| Property                 | Value                                                             |
| ------------------------ | ----------------------------------------------------------------- |
| Time                     | $\Theta(nm \log n + n^2)$ — Bellman-Ford once, Dijkstra $n$ times |
| Space                    | $\Theta(n^2)$                                                     |
| Negative weights         | allowed                                                           |
| Negative cycle detection | yes (during Bellman-Ford)                                         |

For dense graphs ($m \to n^2$), Johnson's becomes $\Theta(n^3 \log n)$ — slower than Floyd-Warshall by a log factor. The crossover is roughly when $m / \log n < n^2 / \log n$, which means Johnson's wins on truly sparse graphs.

## When to choose what

| Graph                         | Edge weights             | Choice                                                                           |
| ----------------------------- | ------------------------ | -------------------------------------------------------------------------------- |
| Dense (large $m$)             | any                      | Floyd-Warshall                                                                   |
| Sparse, non-negative          | non-negative             | $n$ × Dijkstra                                                                   |
| Sparse, negative possible     | negative ok              | Johnson's                                                                        |
| Very small $n$ (say $n < 50$) | any                      | Floyd-Warshall regardless of density — tight inner loop wins on constant factors |
| Single source only            | non-negative or negative | Dijkstra or Bellman-Ford alone — see [[Shortest Path]]                           |

## Practical notes

- **Floyd-Warshall's inner loop is exceptionally cache-friendly** for $n$ up to a few thousand. The constant factor is small.
- **Sparse graph in adjacency-list form** must first be expanded to a matrix for Floyd-Warshall, costing $\Theta(n^2)$ space — a memory blowup if $n$ is large.
- **Many problems disguise as APSP**: most-similar-pair in metric spaces, network reliability, transitive closure.

## Video references

- ![Floyd–Warshall algorithm in 4 minutes](https://www.youtube.com/watch?v=4OQeCuLYj-4)

## See also

- [[Shortest Path]]
- [[Graph Basics]]
- [[Dynamic Programming]]
- [[Index]]
