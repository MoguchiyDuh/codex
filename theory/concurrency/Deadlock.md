---
tags: [theory, concurrency, deadlock]
status: stub
---

# Deadlock

> A cycle of threads each waiting for a resource held by the next — everyone waits forever.

## The four Coffman conditions

### Mutual exclusion

### Hold and wait

### No preemption

### Circular wait

### (All four must hold — break any one to prevent deadlock)

## Prevention

### Lock ordering — always acquire in the same order

### Try-lock with timeout

## Detection

### Resource allocation graph

### Cycle detection

## Recovery

### Kill a process

### Preempt a resource

## Livelock — busy but making no progress

## Starvation — always losing to higher-priority threads

## See also

- [[Mutex, Semaphore, Monitor]]
- [[../os/Scheduling|Scheduling]]
