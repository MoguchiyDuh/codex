# Rust — Course Roadmap

Assumes C knowledge (memory, pointers). Focus: ownership model, type system, idiomatic Rust.
Goal: write production Rust without AI/docs.

---

## Phases

### Phase 1 — Ownership, Borrowing, Lifetimes
Topics: move semantics, copy vs move types, borrow rules, lifetime annotations,
`'static`, lifetime elision rules, dangling reference prevention.

**Exam status:** not taken
**Grade:** —

---

### Phase 2 — Type System: Enums, Pattern Matching, Option/Result
Topics: algebraic data types, `match` exhaustiveness, `if let` / `while let`,
`Option<T>`, `Result<T, E>`, `?` operator, never type `!`.

**Exam status:** not taken
**Grade:** —

---

### Phase 3 — Traits & Generics
Topics: trait definition and impl, trait bounds, `where` clauses, blanket impls,
associated types vs generics, coherence rules, `dyn Trait` vs `impl Trait`,
monomorphization, object safety.

**Exam status:** not taken
**Grade:** —

---

### Phase 4 — Standard Traits
Topics: `Clone`, `Copy`, `Debug`, `Display`, `PartialEq`, `Eq`, `Hash`,
`From`/`Into`, `AsRef`/`AsMut`, `Deref`/`DerefMut`, `Iterator`, `IntoIterator`.

**Exam status:** not taken
**Grade:** —

---

### Phase 5 — Collections & Iterators
Topics: `Vec`, `HashMap`, `BTreeMap`, `HashSet`, iterator adapters (`map`, `filter`,
`flat_map`, `fold`, `chain`), lazy evaluation, `collect`, iterator performance.

**Exam status:** not taken
**Grade:** —

---

### Phase 6 — Error Handling
Topics: custom error types, `std::error::Error`, `thiserror`, `anyhow`,
error propagation patterns, when to use which approach.

**Exam status:** not taken
**Grade:** —

---

### Phase 7 — Smart Pointers & Interior Mutability
Topics: `Box<T>`, `Rc<T>`, `Arc<T>`, `RefCell<T>`, `Mutex<T>`,
`Cell<T>`, `Cow<T>`, when each is appropriate.

**Exam status:** not taken
**Grade:** —

---

### Phase 8 — Concurrency
Topics: `Send` / `Sync`, threads, channels (`mpsc`), `Mutex` / `RwLock`,
`Arc` patterns, `rayon` for data parallelism, async basics.

**Exam status:** not taken
**Grade:** —

---

### Phase 9 — Async / Await
Topics: futures model, `async fn`, `.await`, executor model, `tokio` runtime,
`spawn`, `select!`, async traits, common pitfalls (blocking in async, `Send` bounds).

**Exam status:** not taken
**Grade:** —

---

### Phase 10 — Unsafe Rust
Topics: raw pointers, `unsafe` blocks and functions, valid unsafe operations,
`Send`/`Sync` manual impl, FFI basics, aliasing rules, when unsafe is justified.

**Exam status:** not taken
**Grade:** —

---

## Completion

All 10 phases passed (grade ≥ C). Final grade = weighted average.
