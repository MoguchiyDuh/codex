---
tags: [theory, data-structures, hash-table, hash-map]
status: stub
---

# Hash Tables

> Key-value store with O(1) average lookup — backed by an array and a hash function.

## Hash function

### Properties: deterministic, uniform distribution, fast

### Polynomial rolling hash (djb2, FNV)

## Collision resolution

### Separate chaining (linked lists per bucket)

### Open addressing: linear probing, quadratic probing, double hashing

## Load factor

### α = n / capacity

### When to resize (typically α > 0.7)

### Resizing cost — O(n) amortized

## Operations — O(1) average, O(n) worst

## Worst case and hash DoS attacks

## See also

- [[../algorithms/Searching|Searching]]
- [[../algorithms/Complexity|Complexity]]
