---
tags: [theory, databases, indexes, b-tree]
status: stub
---

# Indexes

> Data structures that speed up reads at the cost of write overhead and storage.

## Why indexes

### Full table scan vs index scan

## B-tree index

### Structure: balanced tree on the indexed column(s)

### Supports range queries, ORDER BY, equality

### Most common — default in Postgres, MySQL, SQLite

## Hash index

### O(1) equality lookup, no range queries

## Composite indexes

### Column order matters

### Left-prefix rule

## Covering index — query answered from index alone

## When NOT to index

### Low-cardinality columns

### Write-heavy tables

### Small tables

## Index and query plan — `EXPLAIN`

## See also

- [[SQL Basics]]
- [[Relational Model]]
- [[../data_structures/Trees|Trees]]
