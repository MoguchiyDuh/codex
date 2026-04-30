---
tags:
  - data-structures
  - trees
  - b-tree
  - database
status: complete
---

# B-Tree

> A self-balancing search tree where each node holds many keys and has many children — designed to minimise disk I/O on block-oriented storage.

## Why high fanout

Disk and SSD reads happen in blocks (typically 4 KiB or larger). A binary tree of `n` keys does `log₂ n` random reads; a B-tree of order `t` does `log_t n`. With `t` in the hundreds, even a billion-key index has tree height around 4 — meaning four block reads per query.

## Definition (order *t*)

A B-tree of minimum degree `t ≥ 2`:

1. Every node holds between `t − 1` and `2t − 1` keys (root may hold fewer).
2. An internal node with `k` keys has exactly `k + 1` children.
3. Keys within a node are sorted; child `i` holds keys between key `i−1` and key `i` of the parent.
4. All leaves are at the same depth.

A node maps cleanly to one disk block; `t` is chosen so the node fills the block.

## Operations

| Op | Cost |
|---|---|
| Search | O(log_t n) block reads, O(log n) comparisons |
| Insert | O(log_t n) |
| Delete | O(log_t n) |

### Search

Linear or binary scan within a node to find the right child, then descend. Total comparisons stay O(log n); total *block reads* are O(log_t n) — the metric that matters on disk.

### Insert

Descend to the target leaf. If the leaf has `2t − 1` keys it is **split** at the median: median key moves up to the parent, the two halves become two nodes. Splits propagate up; if the root splits, the tree grows by one level. Splits are pre-emptive in the standard formulation: split a full node on the way down.

### Delete

Descend to the key. To remove from a non-leaf, replace with in-order predecessor or successor. To keep nodes ≥ `t − 1` keys, **borrow** from a sibling or **merge** with a sibling on the way down.

## Variants

- **B+ tree** — all data lives in leaves; internal nodes hold only routing keys. Leaves are linked in a list for fast range scans. This is the form used in nearly all relational databases (PostgreSQL, MySQL InnoDB, SQLite) and many filesystems (ext4 htree, NTFS, HFS+).
- **B* tree** — keeps nodes 2/3 full instead of 1/2, reducing splits.

## Where you'll see it

- Database indexes (B+ tree variant)
- Filesystem directory and extent indexes
- Key-value stores backed by disk

In-memory workloads usually prefer a [[Red-Black Tree]] or hash table; B-trees pay off when nodes live on slower storage.

## Video references

- ![Michael Sambol - B-trees in 4 minutes — Intro](https://youtu.be/FgWbADOG44s)
- ![Michael Sambol - Binary search in 4 minutes](https://youtu.be/fDKIpRe8GW4)

## See also

- [[Trees]]
- [[Binary Search Tree]]
- [[Hash Tables]]
