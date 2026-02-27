---
tags: [rust, collections, hashset]
source: collections/src/hashsets.rs
---

# HashSet\<T\>

`HashSet<T>` is an unordered collection of unique values backed by a hash table (`HashMap<T, ()>` internally). Average O(1) insert, lookup, and remove. `T` must implement `Eq + Hash`. Iteration order is arbitrary.

## Creation

```rust
use std::collections::HashSet;

let mut set: HashSet<i32> = HashSet::new();
let set = HashSet::from([1, 2, 3, 4, 5]);
let set: HashSet<i32> = (0..5).collect();
let set: HashSet<i32> = HashSet::with_capacity(10);
```

## Insert and Membership

`insert` returns `true` if the element was new, `false` if it already existed (the set is unchanged).

```rust
let inserted = set.insert("hello");  // true — new
let inserted = set.insert("hello");  // false — duplicate ignored

let has = set.contains(&20);         // bool
let elem: Option<&T> = set.get(&20); // reference to stored value if present
```

## Removing

```rust
let removed = set.remove(&3);   // bool — true if element existed
let taken: Option<i32> = set.take(&2); // removes and returns the value (useful for owned types)
```

## Set Operations

All operations return iterators; collect them into a new `HashSet` when you need to own the result.

```rust
let a: HashSet<i32> = HashSet::from([1, 2, 3, 4]);
let b: HashSet<i32> = HashSet::from([3, 4, 5, 6]);

let union:    HashSet<i32> = a.union(&b).copied().collect();        // {1,2,3,4,5,6}
let inter:    HashSet<i32> = a.intersection(&b).copied().collect(); // {3,4}
let diff:     HashSet<i32> = a.difference(&b).copied().collect();   // {1,2}  (a − b)
let sym_diff: HashSet<i32> = a.symmetric_difference(&b).copied().collect(); // {1,2,5,6}
```

## Set Relations

```rust
set_x.is_subset(&set_y)    // all of x in y?
set_y.is_superset(&set_x)  // y contains all of x?
set_x.is_disjoint(&set_y)  // no shared elements?
```

## Filtering and Extending

```rust
// retain: keep elements matching predicate, in-place
set.retain(|&x| x % 2 == 0);

// extend: add elements, duplicates silently ignored
set.extend([3, 4, 5]);
set.extend(other_set);
```

## Replacing

`replace` inserts the value if absent (returns `None`) or replaces the stored value with the argument and returns the old one (`Some(old)`). Useful when the new value is equal under `Eq` but differs in data not compared by the hash.

```rust
let old: Option<i32> = set.replace(2); // Some(2) — existed
let old: Option<i32> = set.replace(99); // None — new
```

## Common Patterns

```rust
// de-duplicate a Vec
let unique: HashSet<i32> = vec.into_iter().collect();

// common elements between two lists
let s1: HashSet<i32> = list1.into_iter().collect();
let s2: HashSet<i32> = list2.into_iter().collect();
let common: HashSet<i32> = s1.intersection(&s2).copied().collect();

// check uniqueness
let all_unique = numbers.len() == numbers.iter().copied().collect::<HashSet<_>>().len();
```

## Capacity

```rust
set.reserve(20);       // room for 20 MORE elements
set.shrink_to_fit();
set.len();
set.is_empty();
set.clear();
```

## See Also

- [[HashMap]] — same backing structure, stores key-value pairs
- [[BTreeSet]] — sorted unique values, O(log n), supports range queries
