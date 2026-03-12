# C — Course Roadmap

Accelerated track. Basics skipped where proficiency was demonstrated in code review.
Teaching order follows dependency graph, not textbook order.

---

## Phases

### Phase 1 — Types, Operators, Compilation Model

**Focus:** Gaps only. You know control flow and basic types.
Topics: integer promotion rules, implicit conversions, `sizeof`, compilation pipeline
(preprocessor → compiler → assembler → linker), object files, symbols, static vs dynamic linking.

**Exam status:** passed
**Grade:** A

---

### Phase 2 — Pointers & `const` Correctness

**Focus:** You use pointers correctly but without `const`. Fill that gap.
Topics: pointer decay, `const T *` vs `T * const` vs `const T * const`, `restrict`,
pointer arithmetic UB, `void *`, pointer-to-pointer.

**Exam status:** passed
**Grade:** A

---

### Phase 3 — Strings, Arrays, `size_t`

**Focus:** You implement string ops correctly but use `int` for sizes everywhere.
Topics: `size_t` and `ptrdiff_t`, signed/unsigned comparison warnings, `strlen` return type,
array-pointer duality, stack-allocated vs heap-allocated strings.

**Exam status:** passed
**Grade:** A

---

### Phase 4 — Structs, Unions, Padding, Alignment

**Focus:** You use structs but haven't touched unions or alignment.
Topics: struct layout, padding rules, `__attribute__((packed))`, `offsetof`, unions,
flexible array members, designated initializers.

**Exam status:** passed
**Grade:** B

---

### Phase 5 — Preprocessor, Headers, Multi-file Projects

**Focus:** Unknown territory. All your code is single-file.
Topics: `#define`, `#include` mechanics, header guards, `#pragma once`, macros vs inline,
`#ifdef` / `#ifndef`, conditional compilation, multi-file compilation, `.h` / `.c` split,
`extern`, `static` linkage.

**Exam status:** passed
**Grade:** B

---

### Phase 6 — Standard I/O, File I/O, `errno`

**Focus:** Unknown territory.
Topics: `printf` / `scanf` format strings, `fopen` / `fread` / `fwrite` / `fclose`,
buffered vs unbuffered I/O, `errno`, `perror`, `strerror`, error propagation patterns.

**Exam status:** passed
**Grade:** A

---

### Phase 7 — Integer Types, Undefined Behavior, Overflow

**Focus:** You use `int` where `size_t` / `uint32_t` belong. UB not yet encountered.
Topics: `<stdint.h>` fixed-width types, signed overflow (UB), unsigned wraparound (defined),
integer promotion and usual arithmetic conversions, `-fsanitize=undefined`.

**Exam status:** passed
**Grade:** A

---

### Phase 8 — Function Pointers & Callbacks

**Focus:** Not present in any of your code.
Topics: function pointer syntax and typedef, passing callbacks, dispatch tables,
comparison with Rust traits / Python callables, `qsort` as canonical example.

**Exam status:** passed
**Grade:** A

---

### Phase 9 — Processes & Signals

**Focus:** Unknown territory.
Topics: `fork`, `exec`, `wait`, `exit`, signal handling (`sigaction`), `SIGINT` / `SIGSEGV`,
`pipe`, basic IPC.

**Exam status:** not taken
**Grade:** —

---

### Phase 10 — Advanced Qualifiers & Atomics

**Focus:** Production-level C.
Topics: `volatile`, `restrict`, `_Atomic`, memory order basics, `<stdatomic.h>`,
when each qualifier actually matters and when it's cargo-culted.

**Exam status:** not taken
**Grade:** —

---

## Completion

Course complete when all 10 phases passed (grade ≥ C).
Final grade = weighted average (later phases weighted higher).
