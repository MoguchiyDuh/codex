---
tags: [c, memory, concurrency, qualifiers]
status: complete
---

# Qualifiers & Atomics

> `volatile`, `restrict`, and `_Atomic` — what each qualifier guarantees, what it doesn't, and when to reach for each.

## volatile

Tells the compiler: every read and write to this variable must happen exactly as written — no register caching, no elimination, no reordering relative to other volatile accesses.

```c
volatile uint32_t *const uart_status = (volatile uint32_t *)0x40001000;
while (!(*uart_status & 0x1)) { }  // hardware sets bit 0; compiler cannot hoist this
```

**Legitimate use cases:**

| Use case | Reason |
|----------|--------|
| Memory-mapped hardware registers | hardware writes the value outside of program control |
| Signal handler shared variable | handler runs outside normal control flow |
| `setjmp`/`longjmp` locals | value must survive the non-local jump |

**What `volatile` does NOT do:**

- Not thread-safe — no mutual exclusion, no atomicity
- Not a memory barrier — CPU can still reorder volatile vs non-volatile accesses (ARM)
- Not for inter-thread communication — use `_Atomic` instead

```c
// WRONG: volatile does not prevent data race
volatile int counter = 0;
counter++;  // still three ops: load, add, store — raceable
```

Old codebases use `volatile` for threading. It appears to work on x86 (strong memory model) but is technically UB and breaks on ARM or with aggressive compilers.

## restrict

A promise to the compiler that a pointer is the only way to access that memory for its scope — no other pointer aliases it. Enables alias-free optimizations like auto-vectorization (SIMD).

```c
void add(float *restrict a, float *restrict out, size_t n, float factor) {
    for (size_t i = 0; i < n; i++)
        out[i] = a[i] * factor;  // compiler can vectorize — no aliasing possible
}
```

Without `restrict`, the compiler must reload `a[i]` every iteration in case the write to `out` modified it. With `restrict`, it can batch reads and use SIMD.

**The contract:** if you lie and the pointers do alias, the behavior is undefined. The compiler generates wrong code silently.

**`memcpy` vs `memmove`:**

```c
void *memcpy(void *restrict dst, const void *restrict src, size_t n);  // no overlap allowed
void *memmove(void *dst, const void *src, size_t n);                   // overlap explicitly handled
```

`memmove` has no `restrict` because it's designed for overlapping buffers — promising non-aliasing would be a lie.

Use `restrict` only on numeric kernels or bulk array ops where non-aliasing is structurally guaranteed.

## _Atomic

C11 atomic types for lock-free inter-thread communication. Operations on `_Atomic` types are indivisible — no thread observes a partial state.

```c
#include <stdatomic.h>

atomic_int counter = 0;
atomic_bool flag = false;

counter++;                        // desugars to atomic_fetch_add
atomic_store(&flag, true);
int val = atomic_load(&counter);
atomic_fetch_add(&counter, 1);    // returns old value, adds 1
```

`_Atomic int` vs `volatile int` for threading:

| | `volatile int` | `_Atomic int` |
|--|---------------|--------------|
| Prevents register caching | yes | yes |
| Indivisible read-modify-write | no | yes |
| Memory ordering guarantees | no | yes |
| Safe for inter-thread use | no | yes |

## Memory Orders

Every atomic operation takes an optional memory order that controls how it interacts with surrounding non-atomic accesses.

```c
atomic_store_explicit(&flag, 1, memory_order_release);
int val = atomic_load_explicit(&flag, memory_order_acquire);
```

| Order | Guarantee |
|-------|-----------|
| `memory_order_relaxed` | atomic, no ordering relative to other ops |
| `memory_order_acquire` | no subsequent reads/writes can move before this load |
| `memory_order_release` | no prior reads/writes can move after this store |
| `memory_order_seq_cst` | full sequential consistency — default |

**Acquire/release pair — producer/consumer:**

```c
// producer
data = 42;
atomic_store_explicit(&ready, 1, memory_order_release);  // data write happens before this

// consumer
while (!atomic_load_explicit(&ready, memory_order_acquire)) { }
x = data;  // guaranteed to see data=42
```

`memory_order_relaxed` for stats counters — atomicity needed but nobody gates on the value:

```c
atomic_fetch_add_explicit(&hit_count, 1, memory_order_relaxed);
```

Default (`seq_cst`) is always safe. Use explicit orders in hot paths only when you understand the tradeoff.

## See also

- [[Processes & Signals]]
- [[Integer Types]]
- [[Tooling]]
