---
tags: [data-structures, graphs, adjacency-list, adjacency-matrix]
status: complete
---

# Graphs

> Concrete in-memory representations for graph-shaped data: how vertices and edges are stored, queried, and updated.

## Graph as a data-structure problem

Mathematically, a graph is just a set of vertices plus a set of edges. In code, that description is too abstract: we need a representation that supports the operations the workload actually performs.

Typical operations are:

- iterate neighbours of a vertex
- test whether an edge exists
- insert or delete vertices and edges
- store per-edge weights or labels
- run traversals and shortest-path routines efficiently

This note owns the storage question. The mathematical structure is developed in [[../math/discrete/Graphs|Graphs]]. Traversal and optimisation algorithms are developed in [[../algorithms/Graph Basics|Graph Basics]] and the graph-algorithm notes that follow it.

## Design axes

Before choosing a representation, pin down the graph's semantics.

| Axis | Variants | Why it matters |
|---|---|---|
| Direction | undirected / directed | affects edge storage and degree bookkeeping |
| Weights | unweighted / weighted | edges may need payloads instead of plain vertex IDs |
| Multiplicity | simple / multigraph | parallel edges may require edge IDs instead of bare neighbours |
| Mutability | static / dynamic | frequent updates favour different layouts than read-mostly workloads |
| Density | sparse / dense | determines whether `O(n + m)` or `O(n^2)` space is acceptable |

Write these decisions down first. A representation that is perfect for one workload can be terrible for another.

## Adjacency list

Per vertex, store a collection of outgoing neighbours. For a weighted graph, store `(neighbour, weight)` pairs instead of plain neighbour IDs.

Space: `O(n + m)`. Iterating neighbours of `v`: `O(deg(v))`. Edge existence check: `O(deg(v))`.

This is the standard representation for sparse graphs, which is the common case in practice.

### Typical layouts

| Layout | Shape | Strength |
|---|---|---|
| Array of vectors/lists | `adj[v]` is a dynamic sequence | simple, common, fast neighbour iteration |
| Hash-set per vertex | `adj[v]` is a set | faster expected `hasEdge(u, v)` |
| Compressed sparse row (CSR) | flat edge array + offsets | compact, cache-friendly, great for static graphs |

Array-of-vectors is the default teaching representation because it matches BFS, DFS, Dijkstra, and topological sort directly.

![[adjacency_list_layout.png]]

## Adjacency matrix

`n × n` matrix where `A[i][j]` records whether edge `i → j` exists, or stores its weight.

Space: `O(n^2)`. Edge existence check: `O(1)`. Iterating neighbours: `O(n)`.

Best for dense graphs or when constant-time edge queries matter more than memory, for example in Floyd-Warshall or small dense relation graphs.

![[adjacency_list_vs_matrix.png]]

## Edge list

Just a flat list of edges such as `(u, v)` or `(u, v, w)`. Space `O(m)`.

An edge list is poor for neighbour queries, but excellent when the computation naturally scans edges globally. Kruskal's algorithm is the standard example.

## Incidence matrix

Less common in programming courses but common in combinatorics and linear-algebra treatments. Rows represent vertices, columns represent edges, and entries record incidence.

It is usually not the best implementation choice for graph algorithms, but it is conceptually useful in proofs and in algebraic treatments.

## Representation tradeoffs

| | Adjacency list | Adjacency matrix |
|---|---|---|
| Space | O(n + m) | O(n^2) |
| `hasEdge(u, v)` | O(deg(u)) | O(1) |
| Neighbours of `u` | O(deg(u)) | O(n) |
| Add edge | O(1) | O(1) |
| Delete edge | O(deg(u)) unless augmented | O(1) |
| Sparse graphs | Preferred | Wasteful |
| Dense graphs | Acceptable | Preferred |

## Representation of edge payloads

Real graphs often need more than connectivity.

| Use case | Edge payload |
|---|---|
| Shortest path | weight / cost |
| Road network | distance, speed limit, road type |
| Dependency graph | label, version constraint |
| Flow network | capacity, current flow |

That means an adjacency-list entry is often a small record rather than just an integer.

## Directed vs undirected storage

For an undirected graph, edge `u - v` is usually stored twice in an adjacency list: once in `adj[u]`, once in `adj[v]`. That makes neighbour iteration symmetric and keeps traversals simple.

For a directed graph, store only the outgoing edge in `adj[u]`. If algorithms frequently need predecessors, maintain a second reverse adjacency list.

## Mutable vs static graphs

The right representation depends heavily on whether the graph changes.

| Workload | Preferred representation | Why |
|---|---|---|
| Static sparse graph | adjacency list or CSR | compact, fast scans |
| Dynamic sparse graph | adjacency list with dynamic containers | cheap inserts |
| Dense graph | adjacency matrix | constant-time edge tests |
| Edge-scan algorithm | edge list | simplest global iteration |

CSR is especially strong when the graph is built once and then queried or traversed many times. Insertions are expensive because the edge arrays must be rebuilt.

![[compressed_sparse_row_layout.png]]

## Common operations

| Op | Algorithm | Cost (adj list) |
|---|---|---|
| Reachability | BFS or DFS | O(n + m) |
| Shortest path (unweighted) | BFS | O(n + m) |
| Shortest path (non-negative weights) | Dijkstra + heap | O((n + m) log n) |
| Topological sort (DAG) | DFS or Kahn | O(n + m) |
| Connected components | DFS / union-find | O(n + m) |
| Cycle detection | DFS | O(n + m) |

See [[../algorithms/Graph Basics|Graph Basics]] and [[../algorithms/Shortest Path|Shortest Path]] for the algorithms.

## Sparse vs dense intuition

For a simple graph on $n$ vertices, the maximum number of edges is $\binom{n}{2}$ undirected or $n(n-1)$ directed without self-loops.

- **Sparse** means $m$ is much closer to $n$ than to $n^2$.
- **Dense** means $m$ is on the order of $n^2$.

This single fact explains the main representation split:

- adjacency lists scale with actual edges present
- adjacency matrices allocate for every possible edge whether it exists or not

## Implicit graphs

Sometimes the best graph representation is no explicit graph at all. In a chess position graph, puzzle state space, or word-ladder problem, neighbours can be generated on demand from a state.

This is still a graph algorithm problem, but the representation is **implicit**: vertices are states, edges are legal moves, and adjacency is computed rather than stored.

## Decision guide

| Situation | Representation |
|---|---|
| Social network, road map, dependency graph | adjacency list |
| Small dense relation matrix | adjacency matrix |
| MST by sorting edges | edge list |
| Static analytics pipeline on huge sparse graph | CSR |
| Puzzle/search state space | implicit graph |

## See also

- [[Trees]]
- [[../math/discrete/Graphs|Graphs]]
- [[Disjoint Set]]
- [[../algorithms/Graph Basics|Graph Basics]]
- [[../algorithms/Shortest Path|Shortest Path]]
- [[Index]]
