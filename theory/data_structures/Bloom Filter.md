---
tags:
  - data-structures
  - bloom-filter
  - probabilistic
status: complete
---

# Bloom Filter

> A space-efficient probabilistic set that can answer "is `x` in the set?" with no false negatives and a tunable false-positive rate.

## Structure

- A bit array of `m` bits, all zero initially.
- `k` independent hash functions `h₁ … h_k`, each mapping a key to `[0, m)`.

### Insert

Compute `h₁(x) … h_k(x)`. Set those `k` bits to 1.

### Query

Compute the same `k` bits. If any is 0, `x` is **definitely not** in the set. If all are 1, `x` is **probably** in the set.

False positives are possible (different keys' bits coincidentally all set); false negatives are impossible.

![[bloom_filter_bits.png]]

## False positive rate

After inserting `n` items into a filter of `m` bits with `k` hashes:

```
p ≈ (1 − e^(−kn/m))^k
```

Optimal `k = (m/n) · ln 2`. With this `k`, achieving a target false-positive rate `p` needs roughly `m ≈ −n · ln(p) / (ln 2)²` bits — about 9.6 bits per item for `p = 1%`, 14.4 for 0.1%.

## What you give up

- **No deletion.** Clearing bits would create false negatives because bits are shared across keys. Variants like _counting Bloom filters_ allow deletion at the cost of more space (counters instead of bits).
- **No iteration.** The filter stores no keys, only bits.
- **No exact answer.** Only "definitely not" or "probably yes".

## When to use

Use a Bloom filter as a cheap front-line check before an expensive lookup, when:

- the set is large,
- false positives are tolerable (the expensive check filters them out),
- false negatives are not.

Examples:

- Database engines (LevelDB, RocksDB, Cassandra) skip SSTable disk reads when the filter says the key is absent.
- Web caches and CDNs check whether a URL has been seen.
- Browsers historically used Bloom filters for malicious-URL lists.
- Dedup pipelines pre-filter likely duplicates.

## Variants

| Variant               | Property                                         |
| --------------------- | ------------------------------------------------ |
| Counting Bloom filter | Supports deletion via small per-cell counters    |
| Scalable Bloom filter | Grows by chaining filters as data arrives        |
| Cuckoo filter         | Supports deletion, often better space efficiency |

## See also

- [[Hash Tables]]
- [[../algorithms/Searching|Searching]]
