---
tags:
  - c
  - heap
  - memory
  - malloc
  - dynamic-array
source: vec.c
---

# Heap Memory

## The four heap functions

```c
#include <stdlib.h>

void *malloc(size_t size);              // allocate uninitialized bytes
void *calloc(size_t n, size_t size);   // allocate n*size bytes, zeroed
void *realloc(void *ptr, size_t size); // resize allocation
void  free(void *ptr);                 // release
```

All return `void*` — cast to the target type. Always check for NULL.

```c
int *p = malloc(4 * sizeof(int));
if (p == NULL) {
    // allocation failed — handle it, don't continue
    return 1;
}
```

## `malloc` vs `calloc`

```c
int *a = malloc(n * sizeof(int));   // uninitialized — garbage values
int *b = calloc(n, sizeof(int));    // zeroed — all elements are 0
```

`calloc` is slightly slower due to zeroing, but avoids reading uninitialized memory.

## `realloc`

Resizes an existing allocation. May move it to a new address:

```c
int *temp = realloc(ptr, new_size * sizeof(int));
if (temp == NULL) {
    // original ptr still valid — handle failure before overwriting
    return;
}
ptr = temp;     // update pointer only on success
```

Never assign `realloc` directly to the original pointer — if it fails, you lose the original.

## Rules for safe heap use

1. **Check every allocation** — `malloc`/`calloc`/`realloc` can return NULL.
2. **Free everything** — every `malloc` needs exactly one `free`.
3. **Set to NULL after free** — prevents use-after-free from silently succeeding:
   ```c
   free(p);
   p = NULL;
   ```
4. **Never free stack memory** — only free what `malloc`/`calloc`/`realloc` returned.
5. **Never use after free** — even if the pointer still "works", it's UB (Undefined Behavior).

## The four corruption types

| Type                | What happens                          | Detection                   |
| ------------------- | ------------------------------------- | --------------------------- |
| **Use-after-free**  | Read/write freed memory               | `-fsanitize=address`        |
| **Double-free**     | `free()` called twice on same pointer | `-fsanitize=address`, crash |
| **Buffer overflow** | Write past allocated size             | `-fsanitize=address`        |
| **Memory leak**     | Allocated memory never freed          | Valgrind, `-fsanitize=leak` |

## Dynamic array (`Vec`)

A heap-allocated growable array with `len`, `cap`, and a doubling strategy:

```c
typedef struct {
    int *data;
    int  len;
    int  cap;
} Vec;

Vec vec_new(void) {
    void *ptr = malloc(4 * sizeof(int));
    if (ptr == NULL) { Vec empty = {NULL, 0, 0}; return empty; }
    Vec v = {ptr, 0, 4};
    return v;
}

void vec_push(Vec *v, int val) {
    if (v->len == v->cap) {
        int *temp = realloc(v->data, v->cap * 2 * sizeof(int));
        if (temp == NULL) return;   // keep old data on failure
        v->data = temp;
        v->cap *= 2;
    }
    v->data[v->len++] = val;
}

void vec_free(Vec *v) {
    free(v->data);
    v->data = NULL;
    v->len = v->cap = 0;
}
```

Doubling strategy: capacity doubles on each grow, so `push` is O(1) amortized — total copies across all pushes is O(n).
