---
tags: [c, strings, arrays, null-terminated]
source: str.c
---

# Strings

## Null-terminated `char` arrays

A C string is a `char` array where the last element is `'\0'` (null terminator, value 0). There is no string type — just a convention.

```c
char s[] = "hello";     // {'h','e','l','l','o','\0'} — 6 bytes
char *p = "hello";      // pointer to string literal (read-only memory — don't modify)
```

`strlen` returns the number of chars **not counting** `'\0'`. `sizeof` on an array literal includes the `'\0'`.

## `sizeof` breaks inside functions

Arrays decay to `char*` when passed to functions. `sizeof` then returns the pointer size (8), not the array size:

```c
void broken(char *s) {
    sizeof(s);  // 8 — pointer size, not string length
}

char buf[64];
sizeof(buf);    // 64 — works here because buf is still an array
```

Always pass length explicitly, or use `strlen`.

## `my_strlen`

Walks until `'\0'`, counts steps:

```c
int my_strlen(char *s) {
    if (!s) return 0;
    int len = 0;
    while (s[len] != '\0') len++;
    return len;
}
```

## `my_strcpy` (bounds-checked)

Copies `src` into `dst`, truncating to `dst_size - 1` to always leave room for `'\0'`:

```c
char *my_strcpy(char *dst, char *src, int dst_size) {
    if (!dst || !src || dst_size == 0) return dst;
    int i = 0;
    while (i < dst_size - 1 && src[i] != '\0') {
        dst[i] = src[i];
        i++;
    }
    dst[i] = '\0';  // always null-terminate
    return dst;
}
```

Standard `strcpy` has no bounds check — always prefer `strncpy` or a bounds-checked wrapper.

## `my_strcmp`

Compares char-by-char, returns the difference at the first mismatch (0 = equal):

```c
int my_strcmp(char *a, char *b) {
    while (*a && *a == *b) { a++; b++; }
    return *a - *b;     // 0 if both hit '\0' simultaneously
}
```

Return value: `0` = equal, `< 0` = a < b, `> 0` = a > b. Not guaranteed to be −1/0/1 — just sign matters.

## `my_strchr`

Returns a pointer to the first occurrence of `c`, or NULL:

```c
char *my_strchr(char *s, char c) {
    if (!s) return NULL;
    while (*s != (char)c) {
        if (*s == '\0') return NULL;
        s++;
    }
    return (char *)s;
}
```

Returns a pointer into the original string (not a copy). Can find `'\0'` itself.

## Buffer overflows

Writing past the end of a `char` array corrupts adjacent memory:

```c
char buf[5];
strcpy(buf, "this is too long");   // writes past buf — corrupts stack
```

Classic vulnerability. Use bounds-checked functions and always verify `dst_size > strlen(src)`.
