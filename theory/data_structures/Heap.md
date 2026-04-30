---
tags:
  - data-structures
  - heap
  - priority-queue
status: complete
---

# Heap

> A complete binary tree obeying a heap-order property: every parent compares ≤ (min-heap) or ≥ (max-heap) to its children. Backs the priority queue ADT.

## Heap-order property

| Variant | Invariant |
|---|---|
| Min-heap | `parent.key ≤ child.key` |
| Max-heap | `parent.key ≥ child.key` |

The root therefore holds the minimum (or maximum). The order is *partial* — siblings have no defined relationship — which is what makes the structure cheaper than a sorted tree.

## Array layout

A complete binary tree maps onto a flat array with no pointers. For 0-based indexing:

| Relation | Index |
|---|---|
| Parent of `i` | `(i − 1) / 2` |
| Left child of `i` | `2i + 1` |
| Right child of `i` | `2i + 2` |

This packing gives excellent cache behaviour and zero per-node memory overhead.

![[heap_array_layout.png]]

## Operations

| Op | Cost |
|---|---|
| `peek` (top) | O(1) |
| `push` | O(log n) |
| `pop` | O(log n) |
| `heapify` (build from array) | O(n) |
| `heap_sort` (sort in place) | O(n log n) |

### Sift up (used by `push`)

Append at the end; while the new element violates heap order with its parent, swap with the parent. At most O(log n) swaps.

### Sift down (used by `pop`)

Replace the root with the last element, shrink size; while the new root violates heap order with the smaller child, swap with that child. At most O(log n) swaps.

![[heap_sift.png]]

### `heapify` runs in O(n)

Calling sift-down on every node from the last internal node down to the root costs O(n), not O(n log n). The bound is tighter because most nodes are near the leaves and sift only a constant number of levels. This is asymptotically better than inserting one by one.

## Priority queue

The heap is the standard implementation of the [[Abstract Data Types|priority queue]] ADT. Used for:

- Dijkstra's algorithm and A* (extract-min frontier)
- Event-driven simulation (next event by timestamp)
- Job schedulers
- Top-k queries (bounded-size heap)

## Variants

- **d-ary heap** — each node has `d` children. Shallower (`log_d n`) so `push` is faster, but `pop` does more comparisons per level. Used to tune cache behaviour.
- **Binomial / Fibonacci heap** — support O(1) merge and decrease-key, useful for advanced graph algorithms; rarely used in practice.

## See also

- [[Trees]]
- [[../algorithms/Sorting|Sorting]]
- [[../algorithms/Shortest Path|Shortest Path]]
