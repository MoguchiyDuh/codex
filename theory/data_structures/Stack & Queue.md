---
tags:
  - data-structures
  - stack
  - queue
  - deque
status: complete
---

# Stack & Queue

> Two restricted-access sequence ADTs: a stack is LIFO, a queue is FIFO. Both support O(1) insert and remove at their designated ends.

![[stack_vs_queue.png]]

## Stack (LIFO)

A stack exposes `push`, `pop`, and `peek`. The last element pushed is the first popped. Used for function call frames, expression evaluation, backtracking, undo histories, depth-first traversal.

### Implementations

| Backing | `push` | `pop` | Notes |
|---|---|---|---|
| Dynamic array | O(1) amortized | O(1) | Best cache behaviour; preferred |
| Singly linked list | O(1) | O(1) | No resize cost; pointer overhead |

Operate on the *back* of a dynamic array (last index) — operating on the front would be O(n) per operation.

## Queue (FIFO)

A queue exposes `enqueue` (back) and `dequeue` (front). First in, first out. Used for BFS, scheduling, producer–consumer pipelines, request buffering.

### Implementations

| Backing | `enqueue` | `dequeue` | Notes |
|---|---|---|---|
| Singly linked list (head + tail) | O(1) | O(1) | Simple |
| Circular buffer (ring) | O(1) | O(1) | Fixed capacity, cache friendly |
| Two stacks | O(1) amortized | O(1) amortized | Used for persistent/functional queues |

A naive dynamic-array queue with `dequeue` at index 0 is O(n) per dequeue — use a ring buffer instead.

### Circular buffer

Two indices `head` and `tail` walk forward modulo capacity. When they meet, the buffer is empty (or full — disambiguate with a separate count or by reserving one slot).

![[circular_buffer.png]]

## Deque (double-ended queue)

Supports O(1) insert and remove at both ends. Implemented as a doubly linked list or a circular buffer. Generalises both stack and queue.

## See also

- [[Arrays]]
- [[Linked List]]
- [[../algorithms/Graph Basics|Graph Basics]]
