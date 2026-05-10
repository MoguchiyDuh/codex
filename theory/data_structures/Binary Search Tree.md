---
tags:
  - data-structures
  - trees
  - bst
status: complete
---

# Binary Search Tree

> A binary tree whose in-order traversal is sorted: every key in the left subtree is less than the node's key, every key in the right subtree is greater.

## Invariant

For every node `n`:

- all keys in `n.left` subtree are `< n.key`
- all keys in `n.right` subtree are `> n.key`

This invariant must be preserved by every mutation. Duplicate keys are usually disallowed or stored as a count.

## Operations

| Op                 | Average  | Worst |
| ------------------ | -------- | ----- |
| Search             | O(log n) | O(n)  |
| Insert             | O(log n) | O(n)  |
| Delete             | O(log n) | O(n)  |
| Min / Max          | O(log n) | O(n)  |
| In-order traversal | O(n)     | O(n)  |

The worst case occurs when the tree degenerates into a chain (e.g. inserting already-sorted keys into an unbalanced BST). Self-balancing variants ([[AVL Tree]], [[Red-Black Tree]]) guarantee O(log n).

![[bst.png]]

### Search

Compare key to node; recurse left if smaller, right if larger, stop on equal or null.

### Insert

Search until a null link is reached; attach the new node there. Preserves the invariant by construction.

### Delete

Three cases by number of children of the node being removed:

1. **Leaf** — remove directly.
2. **One child** — replace node with that child.
3. **Two children** — replace node's key with its in-order successor (min of right subtree), then delete that successor (which has at most one child).

## In-order traversal yields sorted output

Visit `left`, emit node, visit `right`. This is the defining property and a useful sanity check during testing.

## Limitations

A plain BST gives no guarantee against degeneration. Production code uses a self-balancing variant. The plain BST is still a valuable conceptual baseline because the balancing schemes are layered on top of these operations.

![[bst_degeneration.png]]

## See also

- [[Trees]]
- [[AVL Tree]]
- [[Red-Black Tree]]
- [[../algorithms/Searching|Searching]]
