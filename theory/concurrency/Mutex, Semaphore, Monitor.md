---
tags: [theory, concurrency, mutex, semaphore, monitor]
status: stub
---

# Mutex, Semaphore, Monitor

> The primitives for coordinating access to shared resources.

## Mutex (Mutual Exclusion Lock)

### Binary — locked or unlocked

### Only the locking thread can unlock

### Use case: protecting a critical section

## Semaphore

### Counter-based — allows N concurrent accessors

### Binary semaphore ≠ mutex (any thread can signal)

### Use case: resource pools, producer-consumer signaling

## Monitor

### Mutex + condition variables bundled together

### `wait()`, `signal()`, `broadcast()`

### What most language-level locking is built on

## Condition variables

### Waiting for a condition, not just a lock

### Spurious wakeups — why you loop on the condition

## Spinlock

### Busy-waiting — when it's faster than blocking

## See also

- [[Race Conditions & Atomicity]]
- [[Deadlock]]
