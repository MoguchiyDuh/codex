---
tags: [theory, algorithms, graphs, shortest-path, dijkstra]
status: stub
---

# Shortest Path

> Finding the minimum-cost path between nodes in a weighted graph.

## Problem variants

### Single-source shortest path

### All-pairs shortest path

## Dijkstra's algorithm

### Precondition: non-negative weights

### Priority queue implementation — O((V + E) log V)

### Why it fails with negative edges

## Bellman-Ford

### Handles negative weights

### Detects negative cycles

### Time: O(VE) — slower but more general

## Floyd-Warshall (all-pairs)

### Dynamic programming on adjacency matrix

### Time: O(V³)

## When to use what

## See also

- [[Graph Basics]]
- [[../data_structures/Heap|Heap]]
- [[Complexity]]
