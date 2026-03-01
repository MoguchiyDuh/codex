# C Exercises — Phases 1–5

Work through these in order. Each references the relevant note.

## Status

| Exercise | Topic | Status |
|----------|-------|--------|
| E1 | Split vec — multi-file, opaque type, Makefile | — |
| E2 | Split hashmap — multi-file, opaque type, Makefile | — |
| E3 | str_reverse | done |
| E4 | str_trim | — |
| E5 | str_split | — |
| E6 | Layout inspector — struct padding | — |
| E7 | Packed network packet | — |
| E8 | Tagged union | — |
| E9 | Safe macros (MIN, MAX, CLAMP, SWAP) | — |
| E10 | static local ID generator | — |
| E11 | extern global (config) | — |
| E12 | static linkage collision demo | — |
| E13 | Generic vec (void *) | — |
| E14 | HashMap load factor + rehash | — |

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

**E7 — Packed network packet**
Define a packed struct for this exact wire format and verify with `offsetof`:

```
1 byte  — version
1 byte  — message type
2 bytes — payload length
4 bytes — sequence number
4 bytes — checksum
```

Use `uint8_t`, `uint16_t`, `uint32_t`. Print `sizeof` — must be exactly 12.

**E8 — Tagged union**
Implement a `Value` type that can hold an `int`, `double`, or `char *` (string).

```c
typedef enum { VAL_INT, VAL_DOUBLE, VAL_STR } ValType;
typedef struct { ValType type; union { ... } as; } Value;
```

Write `value_print(const Value *v)` that prints the correct type.
Write 3 tests — one for each variant.

---

## Preprocessor & Macros

**E9 — Safe macros**
In a new file `src/macros.c`, implement and test:

```c
#define MIN(a, b)    // safe — no double evaluation issue... wait, is there one?
#define MAX(a, b)    // same
#define CLAMP(x, lo, hi)   // clamp x between lo and hi
#define SWAP(T, a, b)      // swap two variables of type T using a temp
```

For each: show a case where a naive version breaks, verify your version handles it.

**E10 — static local**
Write a function `gen_id(const char *prefix)` that returns a heap-allocated string
like `"req_001"`, `"req_002"`, etc. — auto-incrementing ID per prefix.
Use a `static` local counter. Caller owns the returned string (must `free` it).

---

## Linkage & Headers

**E11 — extern global**
Create `src/config.c` + `src/config.h`:

- Define `extern int log_level` (values 0–3)
- Define `extern const char *log_level_name(void)` — returns `"debug"`, `"info"`, etc.
- Include from two other files and verify only one definition exists

**E12 — static vs non-static collision**
Create two files that both define a function called `helper(void)`.
Compile them together without `static` — observe the linker error.
Fix it by making both `static`. Verify both can coexist.

---

## Bonus (harder)

**E13 — Generic vec**
Modify `vec` to store `void *` elements with a `size_t elem_size`.
`vec_push` takes a `const void *` and copies `elem_size` bytes.
`vec_get` writes into a caller-provided `void *out`.
Test with both `int` and a struct.

**E14 — HashMap load factor + rehash**
Add to `hashmap.c`:

```c
static float hm_load(const HashMap *hm);  // (float)len / cap
```

When `hm_load > 0.7` on insert, rehash — allocate new bucket array with `cap * 2`,
reinsert all entries. Test that all keys survive rehashing.
