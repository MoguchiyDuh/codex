# C Exercises — Phases 1–6

Work through these in order. Each references the relevant note.

## Status

| Exercise | Topic                                             | Status |
| -------- | ------------------------------------------------- | ------ |
| E1       | Split vec — multi-file, opaque type, Makefile     | done   |
| E2       | Split hashmap — multi-file, opaque type, Makefile | done   |
| E3       | str_reverse                                       | done   |
| E4       | str_trim                                          | done   |
| E5       | str_split                                         | done   |
| E6       | Layout inspector — struct padding                 | done   |
| E7       | Tagged union                                      | done   |
| E8       | file_copy — buffered binary copy, errno preserved | done   |
| E9       | read_file — heap read, realloc, null-terminate    | done   |
| E10      | safe_add_i32 — signed addition, no UB             | done   |
| E11      | fork+wait — basic process lifecycle               | —      |
| E12      | pipe producer/consumer — IPC via pipe             | —      |
| E13      | sigaction SIGINT handler — graceful shutdown      | —      |
| E14      | Atomic counter — thread-safe increment            | —      |
| E15      | MMIO poller — volatile register simulation        | —      |
| E16      | restrict vec_add — SIMD-friendly array op         | —      |

---

## Multi-file Refactoring

**E1 — Split vec**
Split `src/vec.c` into `src/vec.h` + `src/vec.c` + `src/vec_main.c`.

- `Vec` must be an opaque type — internals hidden from `vec_main.c`
- `vec_main.c` can only use `Vec *`, never access fields directly
- Write a `Makefile` that compiles it with `-Wall -Wextra -fsanitize=address,undefined`
- All existing tests must still pass

**E2 — Split hashmap**
Same treatment for `src/hashmap.c` → `src/hashmap.h` + `src/hashmap.c` + `src/hashmap_main.c`.

- Opaque `HashMap` and `Entry`
- `Makefile` target
- All tests pass

---

## Strings

**E3 — str_reverse**
Add to `src/str.c`:

```c
void str_reverse(char *s);
```

Reverses a string in-place. No allocation. Handle NULL and empty string.
Write tests with `assert`.

**E4 — str_trim**
Add to `src/str.c`:

```c
char *str_trim(char *s);
```

Removes leading and trailing whitespace in-place. Returns pointer to first
non-whitespace char (into the original buffer). Handle NULL.
Write tests.

**E5 — str_split**
Add to `src/str.c`:

```c
size_t str_split(char *s, char delim, char **out, size_t max);
```

Splits `s` on `delim`, writes pointers into `out`, null-terminates each token
in-place (modifies `s`). Returns number of tokens. No allocation.
Write tests including: empty string, no delimiter found, more tokens than `max`.

---

## Structs & Padding

**E6 — Layout inspector**
In `src/structs.c`, define these four structs and for each print `sizeof` and
`offsetof` every field. Then reorder fields to minimize size and verify:

```c
struct A { char a; int b; char c; double d; };
struct B { double d; int b; char a; char c; };
struct C { char a; char b; int c; char d; char e; int f; };
struct D { char a; char b; char c; char d; int e; };
```

**E7 — Tagged union**
Implement a `Value` type that can hold an `int`, `double`, or `char *` (string).

```c
typedef enum { VAL_INT, VAL_DOUBLE, VAL_STR } ValType;
typedef struct { ValType type; union { ... } as; } Value;
```

Write `value_print(const Value *v)` that prints the correct type.
Write 3 tests — one for each variant.

---

## Preprocessor & Macros

**E8 — Safe macros**
In a new file `src/macros.c`, implement and test:

```c
#define MIN(a, b)    // safe — no double evaluation issue... wait, is there one?
#define MAX(a, b)    // same
#define CLAMP(x, lo, hi)   // clamp x between lo and hi
#define SWAP(T, a, b)      // swap two variables of type T using a temp
```

For each: show a case where a naive version breaks, verify your version handles it.

**E9 — static local**
Write a function `gen_id(const char *prefix)` that returns a heap-allocated string
like `"req_001"`, `"req_002"`, etc. — auto-incrementing ID per prefix.
Use a `static` local counter. Caller owns the returned string (must `free` it).

---

## Linkage & Headers

**E10 — extern global**
Create `src/config.c` + `src/config.h`:

- Define `extern int log_level` (values 0–3)
- Define `extern const char *log_level_name(void)` — returns `"debug"`, `"info"`, etc.
- Include from two other files and verify only one definition exists

**E11 — static vs non-static collision**
Create two files that both define a function called `helper(void)`.
Compile them together without `static` — observe the linker error.
Fix it by making both `static`. Verify both can coexist.

---

## Processes & Signals

**E11 — fork + wait**
In `src/fork_wait.c`:

- Fork a child that computes the sum of `1..100` and exits with the result mod 256 as the exit code
- Parent waits, retrieves the exit code with `WEXITSTATUS`, prints it
- Fork a second child that calls `abort()` — parent detects it was killed by a signal using `WIFSIGNALED` and `WTERMSIG`, prints the signal number

**E12 — pipe producer/consumer**
In `src/pipe_ipc.c`:

- Create a pipe, fork one child
- Parent writes 10 integers (binary, `write(fd, &n, sizeof(int))`) into the write end, then closes it
- Child reads them from the read end, sums them, prints the result
- Parent waits for child and asserts exit code is 0
- Close unused ends in each process — verify no fd leak with `strace` or by checking `/proc/self/fd`

**E13 — sigaction SIGINT handler**
In `src/sigint.c`:

- Install a `sigaction` handler for `SIGINT` that sets a `volatile sig_atomic_t` flag
- Main loop prints a counter every 200ms until the flag is set
- On flag set, print "caught SIGINT, shutting down" and exit cleanly
- Verify: `SIG_DFL` behavior before installing, that `signal()` is NOT used (use `sigaction` only)

---

## Qualifiers & Atomics

**E14 — Atomic counter**
In `src/atomic_counter.c`, implement a thread-safe counter using `pthreads`:

- Spawn 4 threads, each incrementing a shared counter 100,000 times
- Use `atomic_int` — no mutex
- After all threads join, assert the result is exactly 400,000
- Repeat with a plain `int` counter, observe the wrong result

Compile with `-lpthread`. Run a few times — the plain `int` version should produce different wrong answers each run.

**E15 — MMIO poller**
In `src/mmio.c`, simulate a memory-mapped register:

```c
volatile uint32_t fake_reg = 0;
```

- In one thread, sleep 100ms then set bit 3 of `fake_reg`
- In the main thread, spin-poll until bit 3 is set, then print elapsed time
- Remove `volatile` and compile with `-O2` — observe the compiler optimizes the loop away (infinite loop or immediate exit depending on register caching)

**E16 — restrict vec_add**
In `src/vec_add.c`, implement:

```c
void vec_add(const float *restrict a, const float *restrict b,
             float *restrict out, size_t n);
```

- Compile with `-O2 -march=native` and dump assembly: `gcc -O2 -march=native -S vec_add.c`
- Check the output for SIMD instructions (`vmovups`, `vaddps`, etc.)
- Remove `restrict`, recompile, compare the assembly — verify the difference

---

## Bonus (harder)

**E17 — Generic vec**
Modify `vec` to store `void *` elements with a `size_t elem_size`.
`vec_push` takes a `const void *` and copies `elem_size` bytes.
`vec_get` writes into a caller-provided `void *out`.
Test with both `int` and a struct.

**E18 — HashMap load factor + rehash**
Add to `hashmap.c`:

```c
static float hm_load(const HashMap *hm);  // (float)len / cap
```

When `hm_load > 0.7` on insert, rehash — allocate new bucket array with `cap * 2`,
reinsert all entries. Test that all keys survive rehashing.
