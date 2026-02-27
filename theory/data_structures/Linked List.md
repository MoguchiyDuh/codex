---
tags: [theory, data-structures, linked-list]
status: stub
---

# Linked List

> Nodes connected by pointers — dynamic size, O(1) insert/delete, O(n) access.

## Node structure

## Singly linked list

### Traversal

### Insert at head / tail / middle

### Delete a node

## Doubly linked list

### Advantages over singly

### Insert and delete

## Circular linked list

## Tradeoffs vs array

| | Array | Linked List |
|---|---|---|
| Access by index | O(1) | O(n) |
| Insert at head | O(n) | O(1) |
| Insert at tail | O(1) amortized | O(1) with tail ptr |
| Memory | Contiguous (cache-friendly) | Scattered (pointer overhead) |

## Common bugs

### Off-by-one when traversing

### Losing the head pointer

### Forgetting to update tail

## See also

- [[Stack & Queue]]
- [[../algorithms/Complexity|Complexity]]
