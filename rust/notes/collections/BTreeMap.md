---
tags: [rust, collections, btreemap]
source: collections/src/btreemap.rs
---

# BTreeMap\<K, V\>

`BTreeMap<K, V>` is an ordered key-value map backed by a B-tree. Keys must implement `Ord`. All operations are O(log n). The critical difference from [[HashMap]]: iteration always happens in ascending key order, and the map supports efficient range queries.

## Creation

```rust
use std::collections::BTreeMap;

let mut map: BTreeMap<String, i32> = BTreeMap::new();

// keys are inserted in any order; output is always sorted
let map = BTreeMap::from([(3, "three"), (1, "one"), (2, "two")]);
// => {1: "one", 2: "two", 3: "three"}

let squares: BTreeMap<i32, i32> = (0..5).map(|i| (i, i * i)).collect();
```

No `with_capacity` — B-trees don't benefit from pre-allocation the way hash tables do.

## Insert, Get, Remove

```rust
map.insert(String::from("apple"), 5);  // returns Option<V> (old value)

let v: Option<&i32>          = map.get("apple");
let pair: Option<(&K, &V)>   = map.get_key_value("apple");
let v: &i32                  = &map["apple"];  // panics if key absent

map.contains_key("apple");

let old: Option<i32>          = map.remove("key");
let pair: Option<(String, i32)> = map.remove_entry("key");
```

## Entry API

Identical semantics to [[HashMap]]'s entry API.

```rust
*map.entry(String::from("apple")).or_insert(0) += 10;

map.entry(String::from("fig")).or_insert_with(|| 42 * 2);
map.entry(String::from("grape")).or_default();  // inserts T::default()

// modify if present, no-op if absent
map.entry(String::from("cherry")).and_modify(|v| *v *= 10);
```

## Range Queries (BTreeMap-exclusive)

`range` returns an iterator over `(&K, &V)` pairs within the given bounds. Any Rust range expression works.

```rust
// inclusive range
for (k, v) in map.range(20..=40) { }

// exclusive upper bound
for (k, v) in map.range(..30) { }

// from key onwards
for (k, v) in map.range(30..) { }

// mutable range
for (_k, v) in map.range_mut(2..=4) { *v += 100; }
```

This is the main reason to choose `BTreeMap` over `HashMap`.

## Min and Max Keys

```rust
map.first_key_value()   // Option<(&K, &V)> — smallest key
map.last_key_value()    // Option<(&K, &V)> — largest key

map.pop_first()         // Option<(K, V)> — remove and return minimum
map.pop_last()          // Option<(K, V)> — remove and return maximum
```

## Splitting

```rust
let mut left: BTreeMap<i32, i32> = (1..=10).map(|i| (i, i * 100)).collect();
let right = left.split_off(&6);
// left  => keys 1..5
// right => keys 6..10
```

## Iteration (always sorted)

```rust
for (k, v) in &map           { }   // borrows, ascending key order
for k in map.keys()          { }
for v in map.values()        { }
for v in map.values_mut()    { *v *= 2; }
for (k, v) in map            { }   // consuming
```

## Filtering

```rust
map.retain(|k, _v| k % 2 == 0);  // keep only even keys
```

## HashMap vs BTreeMap

| | [[HashMap]] | BTreeMap |
|---|---|---|
| Lookup / insert | O(1) avg | O(log n) |
| Iteration order | arbitrary | ascending |
| Range queries | no | yes |
| Min / max | no | yes |
| Key bound | `Eq + Hash` | `Ord` |

Use `BTreeMap` when iteration order matters, you need `range()`, or you need `first`/`last`/`pop_first`/`pop_last`.

## See Also

- [[HashMap]] — unordered, faster average case
- [[BTreeSet]] — same tree, stores keys only
