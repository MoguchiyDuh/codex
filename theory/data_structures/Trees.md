---
tags: [theory, data-structures, trees, bst]
status: stub
---

# Trees

> Hierarchical data structure — nodes connected by edges, no cycles.

## Terminology

### Node, root, leaf, parent, child, sibling

### Height, depth, level

### Subtree

## Binary tree

### Properties: at most 2 children

### Full, complete, perfect binary tree

## Binary Search Tree (BST)

### Invariant: left < node < right

### Search, insert, delete — O(log n) average, O(n) worst

### Inorder traversal gives sorted output

## Balanced trees (concept)

### Why balance matters (degenerate case → O(n))

### AVL tree — height difference ≤ 1

### Red-black tree — used in most standard libraries

## Tree traversal

### Inorder (left → node → right)

### Preorder (node → left → right)

### Postorder (left → right → node)

### Level-order (BFS)

## See also

- [[Heap]]
- [[Graphs]]
- [[../algorithms/Graph Basics|Graph Basics]]
- [[../algorithms/Searching|Searching]]
