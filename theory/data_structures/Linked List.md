---
tags:
  - data-structures
  - linked-list
status: complete
---

# Linked List

> Sequence of nodes where each node stores data and a pointer to the next; access is sequential, structural edits are local.

## Node structure

A node holds a value plus one or two pointers. The list itself is identified by a pointer to the head (and often a tail). An empty list has `head = null`.

## Variants

| Variant | Pointers per node | Notes |
|---|---|---|
| Singly linked | `next` | Forward traversal only |
| Doubly linked | `next`, `prev` | Bidirectional, O(1) delete given a node |
| Circular | tail's `next` points to head | No null terminator; useful for round-robin |

A **sentinel** (dummy head/tail node) removes the need to special-case the empty list and the first/last position during insert and delete.

![[linked_list_variants.png]]

## Operations

| Operation | Singly | Doubly |
|---|---|---|
| `prepend` / `pop_front` | O(1) | O(1) |
| `append` (with tail pointer) | O(1) | O(1) |
| `pop_back` | O(n) | O(1) |
| Insert/delete given node ref | O(n) (need prev) | O(1) |
| Search by value | O(n) | O(n) |
| Random access by index | O(n) | O(n) |

## When to use

Choose a linked list when:

- the workload is dominated by insert/delete at known positions,
- the size varies wildly and reallocation cost is unacceptable,
- nodes are owned by other structures (intrusive lists in kernels).

Avoid it when random access, iteration speed, or memory compactness matter — a [[Arrays|dynamic array]] is almost always faster in practice due to cache locality.

## Common pitfalls

- Losing the head pointer during reversal — keep three pointers (`prev`, `curr`, `next`).
- Forgetting to update both `next` and `prev` on a doubly linked edit.
- Cycles introduced by buggy edits — detected with Floyd's tortoise-and-hare.

## See also

- [[Arrays]]
- [[Stack & Queue]]
- [[Abstract Data Types]]
