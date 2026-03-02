---
tags: [c, data-structures]
status: complete
source: src/hashmap/
---

# HashMap

> A C implementation of a hash table — string keys to string values, separate chaining for collision resolution.

## Structure

```c
typedef struct Entry {
    char *key;
    char *value;
    struct Entry *next;   // next node in the chain
} Entry;

typedef struct {
    Entry **buckets;   // array of chain heads
    size_t len;        // number of stored keys
    size_t cap;        // number of buckets
} HashMap;
```

`buckets` is `calloc`'d so all chain heads start as `NULL`.

## Hash function

Polynomial rolling hash — multiply accumulator by prime 31 per character, then mod by capacity:

```c
unsigned int hash(const char *key, size_t cap) {
    unsigned int h = 0;
    while (*key) h = h * 31 + *key++;
    return h % cap;
}
```

Same key always maps to the same bucket. Multiplying by a prime distributes bits and reduces collisions.

## Insert (`hm_set`)

If the key exists, update the value in place with `realloc`. Otherwise allocate a new `Entry`, copy key and value onto the heap, prepend to the bucket chain:

```c
new_entry->next = hm->buckets[idx];
hm->buckets[idx] = new_entry;
hm->len++;
```

Prepend is O(1). The map owns heap copies of key and value — the caller's strings are not retained.

## Get (`hm_get`)

Hash the key, walk the chain with `strcmp` until match or `NULL`. Returns a pointer to the stored value, or `NULL` if not found.

## Delete (`hm_delete`)

Requires a `prev` pointer to relink the chain after removing the target:

```c
if (prev == NULL)
    hm->buckets[idx] = curr->next;   // removing head
else
    prev->next = curr->next;          // removing mid-chain

free(curr->key); free(curr->value); free(curr);
hm->len--;
```

## Memory ownership

The map heap-allocates copies of every key and value on insert. `hm_free` must walk all chains — freeing only `buckets` leaks every `Entry`.

## Common bugs

| Bug                                  | Cause                                                        |
| ------------------------------------ | ------------------------------------------------------------ |
| Using pointer after `realloc`        | `realloc` may move the block — always assign to a temp first |
| `malloc(strlen(key))`                | Off-by-one — missing `+1` for `'\0'`                         |
| `free(hm->buckets)` only             | Entire `Entry` chains leaked                                 |
| Leak on `calloc` failure in `hm_new` | `hm` allocated but not freed before returning `NULL`         |

## Exercises

See `EXERCISES.md` — E2, E14.

1. **Split into multi-file** — `hashmap.h` + `hashmap.c` + `hashmap_main.c`, opaque types, Makefile. `src/hashmap.c`
2. **Iteration** — add `hm_each(HashMap *hm, void (*fn)(const char *key, const char *value))` that walks all entries. `src/hashmap.c`
3. **Load factor + rehash** — `hm_load` returning `(float)len / cap`, auto-rehash at 0.7. `src/hashmap.c`
4. **Collision stress test** — `cap = 1` forces all keys into one bucket. Insert 1000 entries, compare lookup time vs `cap = 1024`. `src/hashmap.c`
5. **Generic values** — change value from `char *` to `void *` with `size_t value_size`. `src/hashmap.c`

## See also

- [[../../theory/data_structures/Hash Tables]]
- [[../../theory/data_structures/Linked List]]
- [[Heap Memory]]
