---
tags: [theory, architecture, memory, cache]
status: stub
---

# Memory Hierarchy

> Faster memory is smaller and more expensive — layers of storage trading speed for capacity.

## The hierarchy

```
Registers   ~1 cycle      bytes
L1 cache    ~4 cycles     32–64 KB
L2 cache    ~12 cycles    256 KB – 1 MB
L3 cache    ~40 cycles    4–32 MB
RAM         ~100 cycles   GB
SSD         ~100k cycles  TB
HDD         ~10M cycles   TB
```

## Why it works — locality

### Temporal locality — recently used data will be used again

### Spatial locality — nearby data will be used soon

## Cache

### Cache line — unit of transfer (typically 64 bytes)

### Cache hit vs cache miss

### Direct-mapped, set-associative, fully associative

### Eviction policies: LRU, LFU, random

### Write-through vs write-back

### Cache coherence in multicore — MESI protocol

## TLB as a cache for page table entries

## Practical implications

### Row-major vs column-major traversal

### False sharing in multithreaded code

### Prefetching

## See also

- [[CPU Architecture]]
- [[Pipelining]]
- [[../os/Virtual Memory|Virtual Memory]]
- [[../concurrency/Memory Models|Memory Models]]
