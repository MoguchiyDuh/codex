---
tags: [math, discrete, trees, graph-theory]
status: complete
---

# Trees

> Minimally connected graphs — acyclic structures that thread through every vertex with the fewest possible edges.

This note covers the mathematical theory of trees. The data-structure view (BST, AVL, heap) lives in `theory/data_structures/`. Spanning-tree algorithms (Kruskal, Prim) live in [[../../algorithms/Minimum Spanning Tree|Minimum Spanning Tree]].

## Definition and equivalent characterisations

A **tree** is a connected acyclic undirected graph. For a graph $T$ on $n$ vertices, the following are all equivalent:

| Characterisation | Statement                                                                                   |
| ---------------- | ------------------------------------------------------------------------------------------- |
| (a)              | $T$ is connected and acyclic                                                                |
| (b)              | $T$ is connected and has $n - 1$ edges                                                      |
| (c)              | $T$ is acyclic and has $n - 1$ edges                                                        |
| (d)              | There is a unique path between every pair of vertices                                       |
| (e)              | $T$ is connected, but removing any single edge disconnects it                               |
| (f)              | $T$ is acyclic, but adding any edge between non-adjacent vertices creates exactly one cycle |

Any one of these can be taken as the definition; the others follow as theorems.

**Proof that (a) $\implies$ (b).** By induction on $n$. Base: $n = 1$, one vertex, zero edges, $1 - 1 = 0$. ✓. Inductive step: every tree on $n \geq 2$ vertices has at least one leaf (vertex of degree 1 — proved below). Remove a leaf and its incident edge; the result is still connected and acyclic, hence a tree on $n-1$ vertices, which by hypothesis has $n-2$ edges. Adding the leaf back adds one edge, giving $n-1$ total.

**Lemma (every non-trivial tree has a leaf).** Let $T$ be a tree on $n \geq 2$ vertices. Take a longest path $v_0, v_1, \ldots, v_k$. The endpoint $v_0$ must have degree 1: any other neighbour $u \neq v_1$ would either extend the path (contradicting maximality) or create a cycle (contradicting acyclicity).

![[tree_leaf_lemma.png]]

## Rooted trees

A tree becomes **rooted** by designating one vertex as the **root**. This induces a natural hierarchy:

- **Parent** of $v$: the first vertex on the unique path from $v$ to the root.
- **Children** of $v$: vertices whose parent is $v$.
- **Ancestors / descendants**: transitive closure of the parent / child relation.
- **Depth** of $v$: length of the path from root to $v$.
- **Height** of $T$: maximum depth of any vertex.
- **Subtree** rooted at $v$: $v$ and all its descendants.

![[rooted_tree_anatomy.png]]

A rooted tree in which every internal node has exactly $k$ children is a **$k$-ary tree**. For $k = 2$: a **binary tree**. A binary tree with $n$ internal nodes has exactly $n + 1$ leaves (proved by structural induction in [[Induction]]).

## Spanning trees

A **spanning tree** of a connected graph $G = (V, E)$ is a subgraph that is a tree and includes every vertex of $G$.

**Existence.** Every connected graph has at least one spanning tree.

**Proof.** If $G$ has a cycle, remove one edge of the cycle — connectivity is preserved (the remaining path still connects the endpoints). Repeat until no cycles remain. The result is connected and acyclic: a spanning tree.

The number of spanning trees of $K_n$ (the complete graph on $n$ vertices) is given by Cayley's formula.

## Cayley's formula

The number of labelled spanning trees of $K_n$ is $n^{n-2}$.

| $n$ | $n^{n-2}$ | Trees                                        |
| --- | --------- | -------------------------------------------- |
| 1   | 1         | just the single vertex                       |
| 2   | 1         | the single edge                              |
| 3   | 3         | three distinct trees (one for each "centre") |
| 4   | 16        | 16 labelled trees                            |

**Proof via Prüfer sequences.** There is a bijection between labelled trees on $n$ vertices and sequences of length $n - 2$ from $\{1, \ldots, n\}$ (Prüfer sequences). Since there are $n^{n-2}$ such sequences, there are $n^{n-2}$ labelled trees.

_Encoding:_ Repeat $n - 2$ times: find the leaf with the smallest label, record its neighbour's label, remove the leaf. The recorded sequence is the Prüfer sequence.

_Decoding:_ Reconstruct the tree from the sequence by the reverse: at each step, connect the sequence's current element to the smallest label not yet seen in the remaining sequence or already removed.

The bijection proves the count without explicitly enumerating the trees.

## Minimum spanning trees

For a **weighted** connected graph, a **minimum spanning tree** (MST) is a spanning tree whose total edge weight is minimised.

MSTs arise in network design (minimum cost to connect $n$ nodes), clustering, and approximation algorithms. The key property:

**Cut property.** For any partition of $V$ into two non-empty sets $S$ and $V \setminus S$, the minimum-weight edge crossing the cut belongs to some MST.

**Cycle property.** The maximum-weight edge in any cycle belongs to no MST (assuming distinct weights).

These two properties underpin Kruskal's and Prim's algorithms, developed in [[../../algorithms/Minimum Spanning Tree|Minimum Spanning Tree]].

## Trees in CS

| Use                  | Tree type           | Why                                      |
| -------------------- | ------------------- | ---------------------------------------- |
| Sorted lookup        | BST, AVL, red-black | search in $O(\log n)$ via tree structure |
| Priority queues      | binary heap         | parent ≤ children invariant              |
| Compiler parse trees | parse / AST         | hierarchical grammar derivation          |
| File systems         | directory tree      | one parent per node, rooted              |
| Decision procedures  | decision tree       | branching on conditions                  |
| Huffman coding       | binary tree         | optimal prefix-free code                 |

In all these cases the mathematical properties above — unique paths, $n-1$ edges, leaf existence — are what make the data structures work correctly.

## Video references

- ![Lecture 8: Graph Theory II: Minimum Spanning Trees](https://www.youtube.com/watch?v=GJpt_3ie4WU)

## See also

- [[Graphs]]
- [[Induction]]
- [[Counting]]
- [[../../algorithms/Minimum Spanning Tree|Minimum Spanning Tree]]
- [[../../data_structures/Trees|Trees (data structures)]]
- [[Index]]
