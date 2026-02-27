---
tags: [c, data-structures]
status: stub
source: linked_list.c
---

# Linked List

> A C implementation of singly and doubly linked lists — dynamic chains of heap-allocated nodes connected by pointers.

## Node structure

### Singly linked

```c
typedef struct Node {
    int value;
    struct Node *next;
} Node;
```

### Doubly linked

```c
typedef struct DNode {
    int value;
    struct DNode *prev;
    struct DNode *next;
} DNode;
```

## Singly linked list

### Push front — O(1)

### Push back — O(n) without tail pointer, O(1) with

### Delete by value — requires `prev` pointer

### Traversal

### Reverse in-place

## Doubly linked list

### Push and delete — O(1) with direct node pointer

### Sentinel nodes — dummy head and tail simplify edge cases

## Memory management

### Every `node_new` needs a matching `node_free`

### `list_free` — walk the chain, free each node

### Classic bug: save `next` before freeing the current node

```c
Node *curr = head;
while (curr != NULL) {
    Node *next = curr->next;   // save before free
    free(curr);
    curr = next;
}
```

## Common bugs

| Bug                       | Cause                                    |
| ------------------------- | ---------------------------------------- |
| Losing the head pointer   | Advancing head without saving it first   |
| Use-after-free            | Freeing a node before reading its `next` |
| Forgetting to update tail | Push-back with a stale tail pointer      |
| Off-by-one in delete      | Not handling head removal separately     |

## Tasks

1. **Singly linked list** — implement `push_front`, `push_back`, `delete_value`, `print_list`, `list_free` in `src/linked_list.c`.
2. **Reverse** — implement `list_reverse` in-place without allocating new nodes.
3. **Cycle detection** — implement Floyd's slow/fast pointer algorithm. Write a helper that deliberately creates a cycle to test it.
4. **Doubly linked list** — extend with `DNode`. Implement `push_front`, `push_back`, `delete_node` (given a pointer directly to the node), forward and backward traversal.
5. **Merge sorted lists** — given two sorted singly linked lists, merge them into one sorted list without allocating new nodes.

## See also

- [[../../theory/data_structures/Linked List]]
- [[Heap Memory]]
- [[Stack & Queue]]
