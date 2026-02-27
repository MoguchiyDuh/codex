---
tags: [theory, concurrency, race-conditions, atomicity]
status: stub
---

# Race Conditions & Atomicity

> What goes wrong when multiple threads access shared data without synchronization.

## Race condition

### Definition: outcome depends on scheduling order

### Classic example: `counter++` is not atomic

## What "atomic" means

### Read-modify-write as one uninterruptible unit

### Hardware atomics: CAS (Compare-And-Swap)

## Critical section

### The region of code that must not run concurrently

## Data race vs race condition

## Memory visibility

### CPU caches and write buffers — changes not immediately visible to other cores

## Happens-before relationship

## See also

- [[Mutex, Semaphore, Monitor]]
- [[Memory Models]]
- [[../os/Processes & Threads|Processes & Threads]]
