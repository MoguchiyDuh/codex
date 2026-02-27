---
tags: [rust, collections, hashmap]
source: collections/src/hashmaps.rs
---

# HashMap\<K, V\>

`HashMap<K, V>` is an unordered key-value store backed by a hash table. Average O(1) insert, lookup, and remove. Keys must implement `Eq + Hash`. Rust's default hasher is SipHash 1-3, which is DoS-resistant but slower than non-cryptographic hashers like `ahash` — swap it via `HashMap<K, V, S>` if throughput matters.

Iteration order is arbitrary and changes between runs.

## Creation

```rust
use std::collections::HashMap;

let mut map: HashMap<String, i32> = HashMap::new();

// from array of tuples
let map = HashMap::from([("red", 1), ("blue", 2)]);

// from two iterators zipped together
let keys   = vec!["a", "b", "c"];
let values = vec![1, 2, 3];
let map: HashMap<&str, i32> = keys.into_iter().zip(values).collect();

let map: HashMap<i32, i32> = HashMap::with_capacity(10);
```

## Insert and Access

`insert` returns `Option<V>` — `None` if the key was new, `Some(old_val)` if it replaced an existing entry.

```rust
let old = map.insert("key", 100); // None (new)
let old = map.insert("key", 200); // Some(100) (replaced)

// get returns Option<&V>; direct index panics on missing key
let v: Option<&i32> = map.get("key");
let v: &i32         = &map["key"];       // panics if absent

// returns (key_ref, value_ref)
let pair = map.get_key_value("key");
```

## Entry API

The entry API lets you insert-or-modify in a single lookup, avoiding the double-hash of a get-then-insert.

```rust
// insert default if absent; returns &mut V either way
let count = map.entry("word").or_insert(0);
*count += 1;

// lazy default — closure only called when key is missing
map.entry("key").or_insert_with(|| expensive_default());

// insert T::default() if missing
map.entry("key").or_default();

// modify existing value, then insert if still absent
map.entry("a").and_modify(|v| *v += 1).or_insert(0);
```

Classic word-count pattern:

```rust
let mut counts: HashMap<&str, i32> = HashMap::new();
for word in text.split_whitespace() {
    *counts.entry(word).or_insert(0) += 1;
}
```

## Removing

```rust
let val:  Option<i32>         = map.remove("key");        // returns value
let pair: Option<(&str, i32)> = map.remove_entry("key");  // returns (k, v)
```

Both return `None` if the key was absent.

## Iteration

Order is non-deterministic.

```rust
for (k, v) in &map     { }   // borrows
for k in map.keys()    { }
for v in map.values()  { }

for v in map.values_mut() { *v *= 10; }  // mutable values

for (k, v) in map { }  // consuming, map is moved
```

## Filtering and Merging

```rust
// retain: keep entries where predicate returns true
map.retain(|_k, &mut v| v > 20);

// merge (overwrite on conflict)
for (k, v) in other { map.insert(k, v); }

// merge without overwriting existing keys
for (k, v) in other { map.entry(k).or_insert(v); }
```

## Common Patterns

```rust
// grouping values by key
let mut grouped: HashMap<&str, Vec<i32>> = HashMap::new();
for (key, val) in items {
    grouped.entry(key).or_insert_with(Vec::new).push(val);
}

// swap keys and values (only safe when values are unique)
let swapped: HashMap<i32, &str> = original.iter().map(|(k, v)| (*v, *k)).collect();
```

## Capacity

```rust
map.reserve(20);       // ensure room for 20 MORE entries
map.shrink_to_fit();   // release excess memory
map.len();
map.is_empty();
map.clear();
```

## Performance Notes

- Average O(1) for get/insert/remove; worst case O(n) on hash collision.
- `with_capacity` avoids rehashing when the final size is known.
- For ordered iteration or range queries use [[BTreeMap]] instead.

## See Also

- [[HashSet]] — same hashing, stores keys only
- [[BTreeMap]] — sorted, O(log n), supports range queries
