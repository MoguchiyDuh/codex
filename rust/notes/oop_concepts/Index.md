---
tags:
  - rust
  - oop_concepts
  - index
source: oop_concepts/src/
---

# OOP Concepts — Index

| Module | Source | Note |
|---|---|---|
| `structs` | `src/structs.rs` | [[Structs]] |
| `enums` | `src/enums.rs` | [[Enums]] |
| `traits` | `src/traits.rs` | [[Traits]] |
| `generics` | `src/generics.rs` | [[Generics]] |
| `std_traits` | `src/std_traits.rs` | [[Std Traits]] |

## Dependency map

```
Structs  ──┐
Enums    ──┼──▶  Traits  ──▶  Generics  ──▶  Std Traits
           │         ▲              ▲
           └─────────┴──────────────┘
```

- [[Traits]] depends on concrete types from [[Structs]] and [[Enums]].
- [[Generics]] extends [[Traits]] with bounds, associated types, const generics, and `PhantomData`.
- [[Std Traits]] is the catalogue of traits from `std` that generics and types interact with most.
