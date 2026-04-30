---
tags:
  - data-structures
  - adt
status: complete
---

# Abstract Data Types

> An ADT defines *what* operations a container supports; a data structure defines *how* they are implemented.

## ADT vs data structure

An **ADT** is a mathematical specification: a set of values plus the operations that act on them, defined by their behaviour and not their representation. A **data structure** is a concrete representation in memory chosen to implement an ADT efficiently.

The same ADT admits many implementations. A `Stack` ADT can be backed by a dynamic array or a singly linked list — the interface is identical, the cost profile differs.

## The two core interfaces

Most introductory data structures fit one of two interfaces.

| Interface | Purpose | Key operations |
|---|---|---|
| Sequence | Maintain items in an extrinsic order (position) | `get(i)`, `set(i,x)`, `insert(i,x)`, `delete(i)` |
| Set / Dictionary | Maintain items keyed by intrinsic value | `find(k)`, `insert(k,v)`, `delete(k)` |

A priority queue is a variant of the set interface where extraction is always of the min/max key.

## Why this distinction matters

Choice of data structure is driven by which operations dominate the workload. An array gives O(1) `get(i)` but O(n) `insert(i,x)`; a linked list reverses that. There is no universally best implementation — only best for a given operation mix.

## Cost model

Every ADT operation has a cost in time and space. Comparison is done asymptotically (see [[../algorithms/Complexity|Complexity]]) and is usually expressed per operation, sometimes amortized over a sequence (e.g. dynamic array push).

## See also

- [[Arrays]]
- [[Linked List]]
- [[../algorithms/Complexity|Complexity]]
