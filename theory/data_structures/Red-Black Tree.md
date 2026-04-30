---
tags:
  - data-structures
  - trees
  - red-black
  - balanced-bst
status: complete
---

# Red-Black Tree

> A self-balancing BST in which each node carries a colour (red or black) and a set of colour invariants bounds the height to O(log n).

## Invariants

1. Every node is red or black.
2. The root is black.
3. Every leaf (a `NIL` sentinel) is black.
4. A red node's children are both black (no two reds in a row).
5. Every path from a node to its descendant leaves contains the same number of black nodes (the *black-height*).

These rules together guarantee `height ≤ 2 · log₂(n + 1)`.

![[red_black_tree_example.png]]

## How balancing works

Insert and delete proceed as in a plain BST, then a fix-up phase restores the invariants by **recolouring** nodes and applying **rotations** (same primitive as in [[AVL Tree]]). The fix-up walks up from the modified node and terminates either when the invariants hold or after a constant number of rotations (≤ 2 for insert, ≤ 3 for delete).

## Performance

| Op | Cost |
|---|---|
| Search / Insert / Delete | O(log n) worst case |
| Rotations per mutation | O(1) amortized |
| Space | O(n) plus 1 colour bit per node |

## AVL vs red-black

| | AVL | Red-Black |
|---|---|---|
| Height bound | ≈ 1.44 log n | ≤ 2 log n |
| Lookup speed | Faster (tighter) | Slightly slower |
| Insert/delete | More rotations | Fewer rotations |
| Typical use | Read-heavy workloads | General-purpose libraries |

## Where you'll see it

- C++ `std::map`, `std::set`
- Java `TreeMap`, `TreeSet`
- Linux kernel — completely fair scheduler runqueue, virtual memory area tree, epoll
- The `nginx` timer tree

It is the default ordered-map implementation in most language standard libraries because its bounded mutation cost is more important than AVL's slightly faster lookups for typical workloads.

## See also

- [[Binary Search Tree]]
- [[AVL Tree]]
- [[Trees]]
