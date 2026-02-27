---
tags: [c, computing]
status: complete
source: str.c
---

# Strings

> C has no string type — just `char` arrays terminated by `'\0'`, with conventions and library functions built around that.

## Null-terminated char arrays

A C string ends with `'\0'` (value 0). `strlen` counts up to but not including it; `sizeof` on an array literal includes it.

```c
char s[] = "hello";   // {'h','e','l','l','o','\0'} — 6 bytes
char *p  = "hello";   // pointer to a string literal — stored in read-only memory, do not modify
```

## `sizeof` decay problem

Arrays decay to `char *` when passed to functions. `sizeof` then returns the pointer size, not the string length:

```c
void f(char *s) {
    sizeof(s);   // 8 — pointer size, not length
}

char buf[64];
sizeof(buf);     // 64 — still an array in this scope
```

Always pass length explicitly or use `strlen`.

## `strlen`

Walks until `'\0'`, counts steps. O(n) — does not cache the result.

```c
int my_strlen(char *s) {
    int n = 0;
    while (s[n] != '\0') n++;
    return n;
}
```

## `strcpy` and bounds safety

Standard `strcpy` has no bounds check — always prefer a bounds-checked version that guarantees `'\0'`-termination:

```c
char *my_strcpy(char *dst, char *src, int dst_size) {
    int i = 0;
    while (i < dst_size - 1 && src[i] != '\0')
        dst[i++] = src[i];
    dst[i] = '\0';
    return dst;
}
```

## `strcmp`

Returns `0` on equality, negative if `a < b`, positive if `a > b`. Not guaranteed to be ±1 — only the sign matters.

```c
int my_strcmp(char *a, char *b) {
    while (*a && *a == *b) { a++; b++; }
    return *a - *b;
}
```

Never compare strings with `==` — that compares pointer addresses, not contents.

## `strchr`

Returns a pointer to the first occurrence of `c` in the string, or `NULL`. Returns a pointer into the original string, not a copy.

```c
char *my_strchr(char *s, char c) {
    while (*s != c) {
        if (*s == '\0') return NULL;
        s++;
    }
    return s;
}
```

## Buffer overflow

Writing past a `char` array's end corrupts adjacent memory:

```c
char buf[5];
strcpy(buf, "too long");   // corrupts stack — UB, classic vulnerability
```

Always verify `dst_size > strlen(src)` before copying.

## Tasks

1. **Implement the stdlib** — write `my_strlen`, `my_strcpy`, `my_strcmp`, `my_strchr` from scratch. Test against their standard equivalents on the same inputs. `src/str.c`
2. **Reverse in-place** — write `str_reverse(char *s)` that reverses a string in place without allocating. `src/str.c`
3. **Trim whitespace** — write `str_trim(char *s)` that removes leading and trailing whitespace in-place. `src/str.c`
4. **Split** — write `str_split(char *s, char delim, char **out, int max)` that splits on a delimiter and fills `out` with pointers into the original string (modify in-place with null bytes). `src/str.c`
5. **Safe format** — use `snprintf` to build a string `"Hello, <name>!"` into a fixed-size buffer. Verify truncation is handled correctly. `src/str.c`

## See also

- [[../../theory/computing/Data Representation]]
- [[Memory & Pointers]]
