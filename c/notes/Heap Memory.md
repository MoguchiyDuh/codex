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

## Exercises

See `EXERCISES.md` — E1, E13.

1. **Split vec into multi-file** — `vec.h` + `vec.c` + `vec_main.c`, opaque type, Makefile. `src/vec.c`
2. **realloc trap** — assign `realloc` directly to the original pointer, show it leaks on failure, fix it. `src/vec.c`
3. **calloc vs malloc** — allocate with `malloc`, print uninitialized values, repeat with `calloc`. `src/vec.c`
4. **Generic vec** — store `void *` elements with `size_t elem_size`, test with `int` and a struct. `src/vec.c`

## See also

- [[../../theory/os/Stack vs Heap]]
- [[Memory & Pointers]]
