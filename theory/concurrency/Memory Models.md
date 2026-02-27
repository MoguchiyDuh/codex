---
tags: [theory, concurrency, memory-model, cache-coherence]
status: stub
---

# Memory Models

> The rules governing when writes by one thread become visible to others.

## The problem

### CPUs reorder instructions and cache writes

### Compiler also reorders for optimization

## Memory ordering guarantees

### Sequential consistency — strongest, slowest

### Acquire / release — the practical middle ground

### Relaxed — fastest, hardest to reason about

## Happens-before

### Formal definition of visibility

## Memory barriers / fences

### Forcing ordering at the hardware level

## Cache coherence protocols (MESI)

## C++ / Rust / Java memory models

## See also

- [[Race Conditions & Atomicity]]
- [[Mutex, Semaphore, Monitor]]
