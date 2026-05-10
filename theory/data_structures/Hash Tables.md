---
tags:
  - data-structures
  - hash-table
  - hash-map
status: complete
---

# Hash Tables

> A key-value store offering O(1) average-time lookup, insert, and delete by mapping each key to an array index through a hash function.

## How it works

A hash function `h: K → [0, m)` maps a key to a bucket index in a backing array of capacity `m`. To look up a key, hash it and inspect the corresponding bucket. Different keys may hash to the same bucket — a **collision** — and the table must have a strategy to resolve them.

## Hash function properties

A good hash function for table use:

- **Deterministic** — same key always hashes to the same value.
- **Uniform** — keys spread evenly across `[0, m)`.
- **Fast** — typically O(1) in key size for fixed-size keys.
- **Avalanche** — small change in input flips many output bits, preventing clustering.

Cryptographic strength (preimage resistance) is _not_ required for correctness, but is needed to defend against adversarial inputs (see DoS below).

Common non-cryptographic hashes: FNV-1a, MurmurHash, xxHash, SipHash (used by Rust and Python's default string hash for DoS resistance).

## Collision resolution

### Separate chaining

Each bucket holds a linked list (or small array) of entries that hash to it. Insert appends; lookup scans the chain. Simple, tolerates load factors above 1.

![[hash_collision_chaining.png]]

### Open addressing

All entries live directly in the array. On collision, probe a deterministic sequence of alternative slots until an empty one (for insert) or the key (for lookup) is found.

![[hash_open_addressing.png]]

| Probe sequence    | Formula                     | Issue                                        |
| ----------------- | --------------------------- | -------------------------------------------- |
| Linear probing    | `(h(k) + i) mod m`          | Primary clustering: long runs degrade lookup |
| Quadratic probing | `(h(k) + c₁i + c₂i²) mod m` | Reduces clustering; may not visit all slots  |
| Double hashing    | `(h₁(k) + i · h₂(k)) mod m` | Best distribution; two hash computations     |

Open addressing is more cache-friendly (no pointer chasing) but requires the load factor to stay well below 1 and complicates deletion (typically uses **tombstones**).

|                 | Chaining         | Open addressing     |
| --------------- | ---------------- | ------------------- |
| Max load factor | > 1 acceptable   | < 1, usually ≤ 0.7  |
| Cache behaviour | Worse (pointers) | Better (contiguous) |
| Deletion        | Easy             | Requires tombstones |
| Memory overhead | Per-entry node   | Empty slots         |

## Load factor

`α = n / m`, where `n` is the number of entries and `m` the capacity. As `α` grows, expected probe length grows. When `α` exceeds a threshold (typically 0.7 for open addressing, 1–2 for chaining), the table is **resized** — a new larger array is allocated (usually 2× capacity) and all entries are rehashed into it.

A single rehash is O(n) but happens rarely enough to give O(1) amortized insertion.

## Complexity

| Op     | Average        | Worst |
| ------ | -------------- | ----- |
| Lookup | O(1)           | O(n)  |
| Insert | O(1) amortized | O(n)  |
| Delete | O(1)           | O(n)  |

Worst case occurs when many keys collide. With a good hash function and bounded load factor it is vanishingly unlikely on random input.

## Hash DoS attacks

If the hash function is public and unsalted, an attacker can craft many colliding keys, forcing all operations into the worst-case O(n) chain. This was a real vulnerability in early Python, PHP, and Java web frameworks.

Defences:

- **Randomised seed** chosen at process start (Python, Rust).
- **Keyed hash** like SipHash that is fast yet hard to invert without the key.

## See also

- [[Bloom Filter]]
- [[../algorithms/Searching|Searching]]
- [[../algorithms/Complexity|Complexity]]
