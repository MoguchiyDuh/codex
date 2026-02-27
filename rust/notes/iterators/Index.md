---
tags:
  - rust
  - iterators
  - index
source: iterators/src/
---

# Iterators — Module Index

| Module | Source File | Note |
|---|---|---|
| Basics | `iterators/src/basics.rs` | [[Basics]] |
| Adapters | `iterators/src/adapters.rs` | [[Adapters]] |
| Consumers | `iterators/src/consumers.rs` | [[Consumers]] |
| Custom Iterators | `iterators/src/custom_iterators.rs` | [[Custom Iterators]] |
| Patterns | `iterators/src/patterns.rs` | [[Patterns]] |
| Advanced | `iterators/src/advanced.rs` | [[Advanced]] |

## Quick Reference

### Picking the right iteration method
- Need to read elements → `iter()` (`&T`)
- Need to modify elements in place → `iter_mut()` (`&mut T`)
- Need to consume/move elements → `into_iter()` (`T`)

### Adapter vs Consumer
- **Adapter** — returns a new iterator, lazy, no work done: `map`, `filter`, `take`, `zip`, …
- **Consumer** — drives evaluation, produces a result: `collect`, `fold`, `sum`, `find`, …

### Custom iterator decision tree
- Simple recurrence / stateful closure → `std::iter::from_fn` or `successors` ([[Advanced]])
- Need `rev()` → implement `DoubleEndedIterator` ([[Custom Iterators]])
- Need `len()` → implement `ExactSizeIterator` ([[Custom Iterators]])
- Need safe `None`-after-`None` guarantee → implement `FusedIterator` ([[Custom Iterators]])
