# Concurrency — Course Roadmap

Language-agnostic theory + C (`pthreads`) and Rust implementations.

---

## Phases

### Phase 1 — Concurrency vs Parallelism
Topics: definitions and distinction, CPU-bound vs I/O-bound, thread vs process vs coroutine,
why concurrency is hard (non-determinism, interleaving).

**Exam status:** not taken
**Grade:** —

---

### Phase 2 — Race Conditions & Mutual Exclusion
Topics: data races vs race conditions, mutex, spinlock, TTAS, lock granularity,
coarse vs fine-grained locking trade-offs.

**Exam status:** not taken
**Grade:** —

---

### Phase 3 — Semaphores & Condition Variables
Topics: binary vs counting semaphore, producer-consumer with semaphores,
condition variables (`pthread_cond_wait`), spurious wakeups, monitors.

**Exam status:** not taken
**Grade:** —

---

### Phase 4 — Deadlock & Livelock
Topics: Coffman conditions, lock ordering as prevention,
trylock-based avoidance, livelock, priority inversion, priority inheritance.

**Exam status:** not taken
**Grade:** —

---

### Phase 5 — Memory Models
Topics: memory ordering (sequentially consistent, acquire-release, relaxed),
happens-before relation, CPU reordering, compiler reordering,
`_Atomic` in C, `std::sync::atomic` in Rust.

**Exam status:** not taken
**Grade:** —

---

### Phase 6 — Lock-Free Data Structures
Topics: CAS (compare-and-swap), ABA problem, lock-free stack, lock-free queue concept,
when lock-free is actually faster (and when it isn't).

**Exam status:** not taken
**Grade:** —

---

## Completion

All 6 phases passed (grade ≥ C).
