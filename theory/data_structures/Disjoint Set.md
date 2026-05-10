---
tags:
  - data-structures
  - union-find
  - disjoint-set
status: complete
---

# Disjoint Set

> A data structure tracking a partition of `n` elements into disjoint subsets, supporting `find` (which set is `x` in?) and `union` (merge two sets) in near-constant amortized time. Also called union-find.

## Operations

| Op            | Meaning                                        |
| ------------- | ---------------------------------------------- |
| `make_set(x)` | Create a singleton set containing `x`          |
| `find(x)`     | Return a canonical representative of `x`'s set |
| `union(x, y)` | Merge the sets containing `x` and `y`          |

Two elements are in the same set iff `find(x) == find(y)`.

## Representation

Each element stores a parent pointer; following parents leads to the **root**, which is the representative. A set is a tree where every node points (directly or transitively) to the root.

```
parent[x] = x   means x is a root (its own representative)
```

Naive `find` walks parent pointers; naive `union` makes one root the parent of the other. Without optimisations these can degenerate to O(n) per operation if trees become tall.

![[union_find_trees.png]]

## Optimisations

Two cheap heuristics together bring amortized cost down to nearly O(1):

### Union by rank (or size)

Attach the shorter tree under the taller one (rank = upper bound on height) — or attach the smaller tree under the larger. Bounds tree height at O(log n) on its own.

### Path compression

During `find(x)`, point every visited node directly at the root. Subsequent `find`s on the same path are O(1).

![[path_compression.png]]

### Combined complexity

With both optimisations, a sequence of `m` operations on `n` elements runs in `O(m · α(n))`, where `α` is the inverse Ackermann function — effectively constant for any input size encountered in practice (`α(n) ≤ 4` for `n` up to the number of atoms in the universe).

## Uses

- **Kruskal's MST** — detect whether adding an edge would create a cycle.
- **Connected components** in an undirected graph as edges are added.
- **Cycle detection** in incremental graphs.
- **Equivalence classes** in unification (compilers, type inference).
- **Dynamic connectivity** under unions only (not deletions).

## Limitations

Supports only union, not split. Removing an element or splitting a set requires a different structure (e.g. link-cut trees).

## See also

- [[Graphs]]
- [[../algorithms/Graph Basics|Graph Basics]]
- [[../algorithms/Shortest Path|Shortest Path]]
