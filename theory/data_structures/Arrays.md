---
tags:
  - data-structures
  - array
  - dynamic-array
status: complete
---

# Arrays

> Contiguous block of memory holding fixed-size elements, indexed in O(1) by offset arithmetic.

## Static array

A static array reserves a fixed number of slots at allocation time. Address of element `i` is `base + i * sizeof(elem)`, so random access is O(1). Size cannot change.

| Operation | Cost |
|---|---|
| `get(i)` / `set(i, x)` | O(1) |
| `insert(i, x)` / `delete(i)` | O(n) (shift) |
| `append` | O(1) only if room remains |

Cache locality is excellent: sequential traversal is the fastest access pattern on modern hardware.

## Dynamic array

A dynamic array (C++ `vector`, Rust `Vec`, Python `list`, Java `ArrayList`) wraps a static array and grows it on demand.

### Growth strategy

When capacity is exhausted, allocate a larger buffer and copy existing elements. Growth factor is typically 2× (doubling) or 1.5×. A constant-factor multiplicative growth is required for amortized O(1) append; additive growth gives O(n) per append.

### Amortized analysis

A single resize costs O(n), but it happens only every n appends. Total cost of n appends is bounded by `n + n/2 + n/4 + ... ≤ 2n`, giving O(1) amortized cost per append.

![[dynamic_array_growth.png]]

### Shrink policy

Implementations often *do not* shrink on delete, or shrink only when load drops below 1/4 to avoid oscillation when size hovers near a capacity threshold.

## Multi-dimensional arrays

A 2D array can be stored in **row-major** (C, C++, Python NumPy default) or **column-major** (Fortran, MATLAB) order. Element `(i, j)` of an `R × C` row-major array sits at offset `i * C + j`. Access pattern should match storage order for cache efficiency.

## Tradeoffs vs linked list

| | Array | Linked list |
|---|---|---|
| Random access | O(1) | O(n) |
| Insert/delete at end | O(1) amortized | O(1) |
| Insert/delete at front | O(n) | O(1) |
| Memory overhead | Low (just data) | Per-node pointer overhead |
| Cache behaviour | Excellent | Poor (scattered nodes) |

## See also

- [[Linked List]]
- [[Abstract Data Types]]
- [[../algorithms/Complexity|Complexity]]
