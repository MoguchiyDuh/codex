---
tags: [c, data-structures]
status: stub
source: stack.c
---

# Stack & Queue

> Stack (LIFO) and queue (FIFO) as concrete C implementations — array-backed for cache efficiency, linked-list-backed for dynamic size.

## Stack — array-backed

```c
typedef struct {
    int *data;
    int  top;
    int  cap;
} Stack;
```

### `push` — write at `top`, increment

### `pop` — decrement `top`, return value

### `peek` — read `data[top - 1]` without removing

### Overflow: fixed-cap vs growable

## Stack — linked-list-backed

### Push and pop at the head — O(1)

### No overflow (bounded only by heap)

## Queue — ring buffer

```c
typedef struct {
    int *data;
    int  head;
    int  tail;
    int  len;
    int  cap;
} Queue;
```

### `enqueue` — write at `tail`, advance with `% cap`

### `dequeue` — read at `head`, advance with `% cap`

### Full vs empty distinction — use `len` or leave one slot empty

## Queue — linked-list-backed

### Enqueue at tail, dequeue at head — O(1) with both head and tail pointers

## Tasks

1. **Array stack** — implement a fixed-capacity int stack with `push`, `pop`, `peek`, `is_empty`, `is_full` in `src/stack.c`.
2. **Growable stack** — extend the array stack to double capacity on overflow using `realloc`.
3. **Balanced brackets** — use a char stack to check whether a string has balanced `()`, `[]`, `{}`. Return the index of the first mismatch or -1.
4. **Ring buffer queue** — implement a fixed-capacity queue using a ring buffer. Test that enqueue wraps around correctly.
5. **Queue with two stacks** — implement a queue using two stacks. Analyze the amortized O(1) complexity.

## See also

- [[../../theory/data_structures/Stack & Queue]]
- [[Linked List]]
- [[Heap Memory]]
