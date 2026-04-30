---
tags:
  - data-structures
  - trees
status: complete
---

# Trees

> A connected acyclic graph with a designated root; each non-root node has exactly one parent.

## Terminology

| Term | Meaning |
|---|---|
| Root | Node with no parent |
| Leaf | Node with no children |
| Parent / child | Adjacent node above / below |
| Sibling | Shares a parent |
| Ancestor / descendant | On the path to / from the root |
| Subtree | A node and all its descendants |
| Depth | Edges from root to node |
| Height | Edges on longest path from node to a leaf |
| Level | Set of nodes at equal depth |

A tree with `n` nodes has exactly `n - 1` edges.

![[tree_terminology.png]]

## Binary tree

A binary tree restricts each node to at most two children, conventionally `left` and `right`.

| Shape | Definition |
|---|---|
| Full | Every node has 0 or 2 children |
| Complete | All levels full except possibly the last, filled left to right |
| Perfect | Full and all leaves at the same depth |
| Balanced | Height is O(log n) |
| Degenerate | Effectively a linked list, height O(n) |

A complete binary tree with `n` nodes has height `⌊log₂ n⌋` and admits a tight array layout (used by [[Heap]]).

## Traversals

Order in which nodes are visited.

| Traversal | Order | Use |
|---|---|---|
| Inorder | left → node → right | Yields sorted output for a BST |
| Preorder | node → left → right | Serialise tree shape |
| Postorder | left → right → node | Free children before parent |
| Level-order (BFS) | by increasing depth | Shortest-path on unweighted tree |

The first three are naturally recursive; level-order uses a queue.

![[tree_traversals.png]]

## Why balance matters

Most tree operations cost O(height). For a balanced tree height is O(log n) and operations are fast; for a degenerate tree height is O(n) and the structure offers no advantage over a linked list. Self-balancing variants (AVL, red-black, B-tree) enforce a height bound on every mutation.

## Specialisations

- [[Binary Search Tree]] — ordered keys, supports lookup/insert/delete by key.
- [[AVL Tree]] — strictly balanced BST.
- [[Red-Black Tree]] — loosely balanced BST, used in standard libraries.
- [[B-Tree]] — high-fanout tree for disk and database indexes.
- [[Heap]] — partial-order tree backing a priority queue.

## See also

- [[Graphs]]
- [[../algorithms/Searching|Searching]]
