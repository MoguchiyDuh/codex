---
tags: [c, os]
status: complete
source: vec.c
---

# Heap Memory

> Dynamic memory in C — explicitly allocated and freed, with no garbage collector.

## Allocation functions

```c
#include <stdlib.h>

void *malloc(size_t size);             // allocate uninitialized bytes
void *calloc(size_t n, size_t size);   // n*size bytes, zeroed
void *realloc(void *ptr, size_t size); // resize; may move the allocation
void  free(void *ptr);                 // release
```

All return `void *` — cast to the target type. All can return `NULL` on failure; always check.

## `malloc` vs `calloc`

```c
int *a = malloc(n * sizeof(int));   // uninitialized — garbage values
int *b = calloc(n, sizeof(int));    // zeroed — all elements are 0
```

## `realloc`

May move the allocation to a new address. Never assign directly to the original pointer — on failure it returns `NULL` and the original is still valid:

```c
int *tmp = realloc(ptr, new_cap * sizeof(int));
if (tmp == NULL) return;   // ptr still valid, handle failure
ptr = tmp;
```

## Rules

| Rule                    | Why                                              |
| ----------------------- | ------------------------------------------------ |
| Check every allocation  | `NULL` return means failure — proceeding is UB   |
| One `free` per `malloc` | Double-free corrupts the allocator               |
| `NULL` after `free`     | Prevents use-after-free from silently succeeding |
| Never free stack memory | Only free what the allocator returned            |

## Corruption types

| Type            | Cause                                 | Detection                   |
| --------------- | ------------------------------------- | --------------------------- |
| Memory leak     | Allocated block never freed           | Valgrind, `-fsanitize=leak` |
| Use-after-free  | Read/write freed memory               | `-fsanitize=address`        |
| Double-free     | `free()` called twice on same pointer | `-fsanitize=address`, crash |
| Buffer overflow | Write past allocated size             | `-fsanitize=address`        |

## Dynamic array

Capacity doubles on each grow — `push` is O(1) amortized. Total copies across all pushes is O(n):

```c
typedef struct {
    int *data;
    int  len;
    int  cap;
} Vec;

void vec_push(Vec *v, int val) {
    if (v->len == v->cap) {
        int *tmp = realloc(v->data, v->cap * 2 * sizeof(int));
        if (tmp == NULL) return;   // keep old data on failure
        v->data = tmp;
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

## Tasks

1. **Vec** — implement a growable `Vec` with `vec_new`, `vec_push`, `vec_get`, `vec_free`. Verify with `-fsanitize=address` that no leaks or overflows occur. `src/vec.c`
2. **realloc trap** — write code that assigns `realloc` directly to the original pointer. Show that this leaks on failure. Fix it. `src/vec.c`
3. **calloc vs malloc** — allocate an array with `malloc`, print the uninitialized values. Then repeat with `calloc`. Explain the difference. `src/vec.c`
4. **free trace** — wrap `malloc` and `free` in macros that print the address. Run the Vec and verify every allocation is freed exactly once. `src/vec.c`

## See also

- [[../../theory/os/Stack vs Heap]]
- [[Memory & Pointers]]
