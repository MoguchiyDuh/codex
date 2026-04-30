---
tags: [algorithms, graphs, bfs, dfs, topological-sort]
status: complete
---

# Graph Basics

> Traversal and structural algorithms — the foundation every other graph algorithm sits on.

## Preliminaries

This note assumes the graph-theoretic vocabulary from [[../math/discrete/Graphs|Graphs]] and the storage tradeoffs from [[../data_structures/Graphs|Graphs]]. Its job is different: given a graph representation, what can we compute from it efficiently?

Graph algorithms usually assume an adjacency-list representation, because neighbour iteration is the primitive operation both BFS and DFS perform on every visited vertex.

## Representations and cost model

A graph $G = (V, E)$ with $|V| = n$ and $|E| = m$ admits multiple storage layouts. The traversals below are analysed for adjacency lists; on an adjacency matrix, neighbour scans cost $\Theta(n)$ per vertex instead of $\Theta(\deg(u))$.

| | Adjacency list | Adjacency matrix |
|---|---|---|
| Space | $\Theta(n + m)$ | $\Theta(n^2)$ |
| `hasEdge(u, v)` | $\Theta(\deg(u))$ | $\Theta(1)$ |
| Iterate neighbours of $u$ | $\Theta(\deg(u))$ | $\Theta(n)$ |
| Best for | sparse graphs (the usual case) | dense graphs / Floyd-Warshall |

The traversal algorithms below assume an adjacency-list representation; their costs change to $\Theta(n^2)$ on a matrix.

## Breadth-First Search (BFS)

Explore the graph in layers from a source $s$: first $s$, then all neighbours of $s$, then all neighbours of neighbours, and so on. Uses a FIFO queue.

```pseudo
BFS(G, s):
    for each u in V:
        dist[u] = ∞
        parent[u] = NIL
    dist[s] = 0
    Q = empty queue
    enqueue(Q, s)
    while Q not empty:
        u = dequeue(Q)
        for each v in adj[u]:
            if dist[v] == ∞:
                dist[v] = dist[u] + 1
                parent[v] = u
                enqueue(Q, v)
```

**Code:** `theory/algorithms/showcase/path_finding/bfs.py`

| Property | Value |
|---|---|
| Time | $\Theta(n + m)$ |
| Space | $\Theta(n)$ for queue + bookkeeping |
| Output | distance and parent for every reachable vertex |

### What BFS computes

| Task | Why BFS works |
|---|---|
| Reachability from $s$ | discovers exactly the vertices in $s$'s component |
| Shortest path in unweighted graphs | first discovery happens at minimum hop-count |
| Bipartiteness check | alternating layers define a 2-colouring iff no same-layer conflict appears |
| Connected components | rerun from each unvisited vertex |

### Why BFS solves shortest path on unweighted graphs

Loop invariant: when BFS dequeues a vertex $u$ for processing, all vertices at distance $< \text{dist}[u]$ from $s$ are already discovered, and all vertices at distance $\text{dist}[u]$ are either discovered or in the queue. The queue's FIFO order guarantees layers are processed in order. Adds $1$ to each newly discovered vertex's distance — exactly the unweighted shortest path.

This breaks for weighted graphs because hop-count $\neq$ path cost. See [[Shortest Path]].

## Depth-First Search (DFS)

Explore as deep as possible from each vertex before backtracking. Implemented recursively (call stack) or iteratively (explicit stack).

```pseudo
DFS(G):
    for each u in V:
        color[u] = WHITE
        parent[u] = NIL
    time = 0
    for each u in V:
        if color[u] == WHITE:
            DFS_visit(u)

DFS_visit(u):
    color[u] = GRAY
    time = time + 1
    discover[u] = time
    for each v in adj[u]:
        if color[v] == WHITE:
            parent[v] = u
            DFS_visit(v)
    color[u] = BLACK
    time = time + 1
    finish[u] = time
```

**Code:** `theory/algorithms/showcase/path_finding/dfs.py`

| Property | Value |
|---|---|
| Time | $\Theta(n + m)$ |
| Space | $\Theta(n)$ stack depth (in worst case = depth of DFS tree) |
| Output | discover/finish times, DFS forest (parent edges) |

The discover and finish times bracket each subtree: $u$ is an ancestor of $v$ in the DFS forest iff $[\text{discover}_u, \text{finish}_u]$ contains $[\text{discover}_v, \text{finish}_v]$. This **parenthesisation theorem** underpins many DFS-based algorithms.

## DFS edge classification (directed graphs)

Each edge $(u, v)$ falls into one of four classes based on the colour of $v$ when the edge is examined.

| Class | Condition | Meaning |
|---|---|---|
| **Tree edge** | $v$ is WHITE | $v$ first discovered via this edge |
| **Back edge** | $v$ is GRAY | $v$ is an ancestor — indicates a cycle |
| **Forward edge** | $v$ is BLACK and $\text{discover}[u] < \text{discover}[v]$ | descendant in DFS tree, not via tree edge |
| **Cross edge** | $v$ is BLACK and $\text{discover}[u] > \text{discover}[v]$ | between distinct subtrees |

Undirected DFS produces only tree and back edges.

### What edge classification gives you

| Consequence | Reason |
|---|---|
| Cycle detection | a back edge points to an ancestor |
| Topological sort | DAGs are exactly digraphs with no DFS back edge |
| Strongly connected components | DFS finishing order exposes SCC structure |

## Topological sort

A linearisation of a DAG: a permutation of $V$ such that every edge $(u, v)$ has $u$ appearing before $v$. Models dependency resolution — build systems, course prerequisites, task scheduling.

### DFS-based

Run DFS. When a vertex finishes (turns BLACK), prepend it to a list. The list is a topological order.

**Why.** Finish time orders descendants before ancestors. Prepending reverses to ancestors-before-descendants, which respects all edges of a DAG.

### Kahn's algorithm (BFS-based)

Maintain in-degree for each vertex. Repeatedly extract a vertex with in-degree $0$, append it to the output, decrement in-degrees of its successors. Stops when the queue is empty.

```pseudo
kahn(G):
    compute in_degree[v] for all v
    Q = queue of all v with in_degree[v] == 0
    output = []
    while Q not empty:
        u = dequeue(Q)
        output.append(u)
        for each v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                enqueue(Q, v)
    if length(output) < n: error "graph has a cycle"
    return output
```

**Code:** `theory/algorithms/showcase/path_finding/topological_sort.py`

| Method | Time | Detects cycle |
|---|---|---|
| DFS-based | $\Theta(n + m)$ | yes (back edge) |
| Kahn's | $\Theta(n + m)$ | yes (output length $< n$) |

Both run in linear time. DFS-based gives a single deterministic order; Kahn's can yield any valid topological order depending on tie-breaking — useful for parallel scheduling (vertices with in-degree $0$ can run concurrently).

![[topological_sort.png]]

## Connected components

### Undirected

Run BFS or DFS from each unvisited vertex; each launch discovers one component. $\Theta(n + m)$ total.

Alternative: [[../data_structures/Disjoint Set|Disjoint Set]] processes edges incrementally — useful when components merge dynamically.

### Strongly connected components (directed)

A subset $C \subseteq V$ is strongly connected if every pair $u, v \in C$ has paths $u \to v$ and $v \to u$. The SCCs partition $V$; the condensation graph (one node per SCC) is a DAG.

Two algorithms in $\Theta(n + m)$:

| Algorithm | Idea |
|---|---|
| **Kosaraju** | DFS on $G$ recording finish times → DFS on $G^T$ in decreasing-finish order, each tree is an SCC |
| **Tarjan** | single DFS using a stack and lowlink values; SCC pops when a root is finished |

Kosaraju is conceptually simpler; Tarjan does the same work in one pass and is usually faster in practice.

The SCC condensation graph is always a DAG. This lets you collapse cyclic subsystems into single meta-vertices and then reason about dependencies between them.

![[scc_condensation_dag.png]]

## Cycle detection

| Graph | Algorithm |
|---|---|
| Directed | DFS — cycle iff back edge found |
| Undirected | DFS — cycle iff back edge to non-parent (track parent to ignore the edge you came in on) |
| Either | union-find — for each edge $(u, v)$, cycle iff `find(u) == find(v)` |

For undirected graphs union-find is the standard approach inside MST algorithms (see [[Minimum Spanning Tree]]).

## Traversal as a design pattern

Most graph algorithms are not built from scratch. They are refinements of a traversal pattern:

| Pattern | Replace queue/stack with | Example |
|---|---|---|
| Layered exploration | queue | BFS |
| Depth exploration | stack / recursion | DFS |
| Best frontier first | priority queue | Dijkstra, A* |
| Repeated edge relaxation | full edge scans | Bellman-Ford |

That is why traversal belongs before weighted shortest paths, MST, and flow. It provides the control structure those later algorithms modify.

## Summary

| Algorithm | Time | Use |
|---|---|---|
| BFS | $\Theta(n + m)$ | unweighted shortest path, layers, bipartite, components |
| DFS | $\Theta(n + m)$ | structure (tree, edges), cycles, topological, SCC |
| Kahn's topological sort | $\Theta(n + m)$ | scheduling, dependency resolution |
| Kosaraju / Tarjan SCC | $\Theta(n + m)$ | condensation graph, web crawling, dataflow |

These four are the foundation. Every weighted-graph algorithm — shortest path, MST, flow — modifies BFS or DFS with priority orderings or auxiliary data structures.

## Video references

- ![Breadth-first search in 4 minutes](https://www.youtube.com/watch?v=HZ5YTanv5QE)
- ![Depth-first search in 4 minutes](https://www.youtube.com/watch?v=Urx87-NMm6c)

## See also

- [[../math/discrete/Graphs|Graphs]]
- [[../data_structures/Graphs|Graphs]]
- [[../data_structures/Disjoint Set|Disjoint Set]]
- [[Shortest Path]]
- [[Minimum Spanning Tree]]
- [[Index]]
