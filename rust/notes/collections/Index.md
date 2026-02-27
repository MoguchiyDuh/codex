---
tags: [rust, collections, index]
source: collections/src/
---

# Collections — Index

All notes in this section correspond to modules in the `collections` crate.

| Module | Source file | Note |
|--------|-------------|------|
| `Vec<T>` | `vectors.rs` | [[Vec]] |
| `HashMap<K, V>` | `hashmaps.rs` | [[HashMap]] |
| `HashSet<T>` | `hashsets.rs` | [[HashSet]] |
| `BTreeMap<K, V>` | `btreemap.rs` | [[BTreeMap]] |
| `BTreeSet<T>` | `btreeset.rs` | [[BTreeSet]] |
| `VecDeque<T>` | `deques.rs` | [[VecDeque]] |
| `BinaryHeap<T>` | `binary_heap.rs` | [[BinaryHeap]] |

## Quick Decision Guide

```
Need key-value?
  Yes → ordered / range queries?
          Yes → BTreeMap
          No  → HashMap
  No → unique values only?
         Yes → ordered / range queries?
                 Yes → BTreeSet
                 No  → HashSet
         No → push/pop front AND back?
                Yes → VecDeque
                No  → always need min or max?
                        Yes → BinaryHeap
                        No  → Vec
```
