---
tags:
  - data-structures
  - trees
  - avl
  - balanced-bst
status: complete
---

# AVL Tree

> A self-balancing BST in which the heights of the two child subtrees of every node differ by at most one.

## Balance factor

For a node `n`, `bf(n) = height(n.left) − height(n.right)`. The AVL invariant requires `bf(n) ∈ {−1, 0, +1}` for every node. A node with `|bf| ≥ 2` is unbalanced and must be repaired.

This invariant bounds the height at `≈ 1.44 · log₂(n)`, so all BST operations remain O(log n) worst-case.

## Rotations

Rebalancing uses tree rotations — local pointer reorderings that preserve the BST invariant.

| Imbalance case | Fix |
|---|---|
| Left-Left (bf = +2, child bf ≥ 0) | Right rotation on root |
| Right-Right (bf = −2, child bf ≤ 0) | Left rotation on root |
| Left-Right (bf = +2, child bf = −1) | Left rotation on child, then right on root |
| Right-Left (bf = −2, child bf = +1) | Right rotation on child, then left on root |

A single rotation moves one node up and another down; it changes the height of the affected subtree by at most one and runs in O(1).

![[avl_rotations.png]]

## Insert

1. Insert as in a plain BST.
2. Walk back to the root, updating heights.
3. At the first ancestor with `|bf| = 2`, apply the matching rotation. One rotation suffices for insert.

## Delete

1. Delete as in a plain BST.
2. Walk back to the root, updating heights.
3. Rotate at any unbalanced ancestor. Up to O(log n) rotations may be needed (unlike insert).

## Performance

| Op | Cost |
|---|---|
| Search / Insert / Delete | O(log n) worst case |
| Space | O(n) plus 1 height/balance field per node |

AVL trees are more strictly balanced than red-black trees, giving slightly faster lookups but slightly slower mutations due to more rotations on average.

## See also

- [[Binary Search Tree]]
- [[Red-Black Tree]]
- [[Trees]]
