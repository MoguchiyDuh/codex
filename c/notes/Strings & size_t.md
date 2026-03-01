---
tags: [c, memory, types, computing]
status: complete
---

# Strings & size_t

> C strings are null-terminated byte arrays — all their traps come from forgetting that.

## size_t and ptrdiff_t

Both in `<stddef.h>` (included transitively by most headers).

**`size_t`** — unsigned, platform-wide. Big enough to hold the size of any object.
`sizeof`, `malloc`, `strlen` all use it.

```c
size_t len = strlen("hello");  // correct
int len    = strlen("hello");  // wrong — signed/unsigned mismatch
```

Format specifier: `%zu`.

**`ptrdiff_t`** — signed, result of subtracting two pointers.

```c
int arr[] = {10, 20, 30, 40};
ptrdiff_t diff = &arr[3] - &arr[1];  // 2 — correct type
```

Pointer subtraction is only valid within the same array (or one past end). Otherwise UB.

| Type | Signed | Use for |
|------|--------|---------|
| `size_t` | no | sizes, lengths, indices |
| `ptrdiff_t` | yes | pointer differences, signed offsets |
| `int` | yes | neither of the above |

**Reverse iteration with `size_t`** — can't use `i >= 0` since unsigned never goes negative:

```c
size_t n = sizeof(arr) / sizeof(arr[0]);
for (size_t i = n; i-- > 0; ) {
    printf("%d\n", arr[i]);
}
// i-- evaluates old value for comparison, then decrements
// when i == 0: checks 0 > 0 (false, exits) — never enters body at SIZE_MAX
```

## Stack vs Heap vs Data Segment Strings

```c
char buf[] = "hello";   // array on stack — writable, copies literal
char *p    = "hello";   // pointer to read-only data segment — NOT stack
char *h    = malloc(6); // pointer to heap — writable
```

`char *p = "hello"` — the stack holds only the pointer. The string lives in a read-only
data segment. Writing through it is UB (segfault on most systems).
Always use `const char *` for string literals.

```c
const char *p = "hello";  // correct
p[0] = 'H';               // compiler error — caught early
```

## The Three Traps

**1. Returning a pointer to a stack buffer — dangling pointer:**

```c
char *get_name(void) {
    char buf[] = "kirill";
    return buf;   // UB — stack frame gone on return
}
```

Fix: heap-allocate and return (caller frees), or take a caller-owned buffer as parameter:

```c
void get_name(char *buf, size_t size) { ... }  // preferred in systems code
```

**2. Forgetting `+1` for null terminator:**

```c
char *s = malloc(strlen("hello"));      // wrong — no room for '\0'
char *s = malloc(strlen("hello") + 1);  // correct
```

**3. Standard `strncpy` doesn't null-terminate:**

```c
char buf[5];
strncpy(buf, "hello world", 5);  // copies 5 bytes, no '\0' added
printf("%s\n", buf);              // reads garbage past buf
```

Always manually add `buf[n-1] = '\0'` after standard `strncpy`, or use a safe wrapper
that always null-terminates (like `my_strncpy` in `str.c`).

## Exercises

See `EXERCISES.md` — E3, E4, E5.

1. **Reverse in-place** — `str_reverse(char *s)` — reverses a string in place, no allocation. `src/str.c`
2. **Trim whitespace** — `str_trim(char *s)` — removes leading and trailing whitespace in-place. `src/str.c`
3. **Split** — `str_split(char *s, char delim, char **out, size_t max)` — splits on delimiter, fills `out` with pointers into original string, null-terminates each token in-place. `src/str.c`

## See also

- [[Pointers & const]]
- [[Memory & Pointers]]
- [[Heap Memory]]
