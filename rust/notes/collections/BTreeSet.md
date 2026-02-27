---
tags: [rust, collections, btreeset]
source: collections/src/btreeset.rs
---

# BTreeSet\<T\>

`BTreeSet<T>` is an ordered set of unique values backed by `BTreeMap<T, ()>`. `T` must implement `Ord`. All operations are O(log n). Iteration always yields elements in ascending order, and the set supports efficient range queries and min/max access.

## Creation

```rust
use std::collections::BTreeSet;

let mut set: BTreeSet<i32> = BTreeSet::new();

// duplicates are silently dropped; result is sorted
let set = BTreeSet::from([5, 3, 1, 4, 2, 3, 1]);
// => {1, 2, 3, 4, 5}

let set: BTreeSet<i32> = vec![9, 7, 5, 3, 1, 3, 7].into_iter().collect();
```

## Insert, Contains, Get, Take

```rust
let new  = set.insert(3);  // true  — first time
let dup  = set.insert(3);  // false — already present

set.contains(&3);          // bool
let r: Option<&i32> = set.get(&3); // reference to stored value

// take removes and returns the value — useful when you need ownership
let taken: Option<String> = set.take("go");
```

## Remove

```rust
let ok: bool = set.remove(&3);   // true if element existed
```

## Min, Max, Pop

```rust
set.first()      // Option<&T> — minimum element
set.last()       // Option<&T> — maximum element

set.pop_first()  // Option<T> — remove and return minimum
set.pop_last()   // Option<T> — remove and return maximum
```

## Range Queries (BTreeSet-exclusive)

```rust
let nums: BTreeSet<i32> = BTreeSet::from([10, 20, 30, 40, 50]);

nums.range(20..=40).collect::<Vec<_>>()  // [&20, &30, &40]
nums.range(..30).collect::<Vec<_>>()     // [&10, &20]
nums.range(30..).collect::<Vec<_>>()     // [&30, &40, &50]
```

## Set Operations (always sorted output)

```rust
let a = BTreeSet::from([1, 2, 3, 4, 5]);
let b = BTreeSet::from([3, 4, 5, 6, 7]);

let union:    BTreeSet<i32> = a.union(&b).copied().collect();               // {1..7}
let inter:    BTreeSet<i32> = a.intersection(&b).copied().collect();        // {3,4,5}
let diff:     BTreeSet<i32> = a.difference(&b).copied().collect();          // {1,2}
let sym_diff: BTreeSet<i32> = a.symmetric_difference(&b).copied().collect(); // {1,2,6,7}
```

Unlike [[HashSet]], the output collections maintain sorted order automatically.

## Set Relations

```rust
small.is_subset(&a)    // all of small in a?
a.is_superset(&small)  // a contains all of small?
a.is_disjoint(&b)      // no shared elements?
```

## Filtering

```rust
set.retain(|x| x % 2 == 0);  // keep only even elements, in-place
```

## Iteration (always sorted)

```rust
for elem in &set  { }  // ascending order
for elem in set   { }  // consuming, ascending order
set.iter().collect::<Vec<_>>()
```

## HashSet vs BTreeSet

| | [[HashSet]] | BTreeSet |
|---|---|---|
| Operations | O(1) avg | O(log n) |
| Iteration order | arbitrary | ascending |
| Range queries | no | yes |
| Min / max | no | yes |
| Key bound | `Eq + Hash` | `Ord` |

Choose `BTreeSet` when sorted iteration, range queries, or min/max access are needed.

## See Also

- [[HashSet]] — unordered, faster average case
- [[BTreeMap]] — same tree, stores key-value pairs
