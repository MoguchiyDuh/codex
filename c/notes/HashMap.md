---
tags: [c, hashmap, hash-table, data-structures]
source: hashmap.c
---

# HashMap

## What it is

A hash table maps string keys to string values in O(1) average time. Internally it's an array of buckets — the key is hashed to an index, and the value is stored there.

```
key → hash(key) % cap → bucket index → Entry { key, value, *next }
```

## Hash function

A polynomial rolling hash: accumulate character codes into a running value, multiply by 31 each step.

```c
unsigned int hash(char *key, int cap) {
    unsigned int h = 0;
    while (*key)
        h = h * 31 + *key++;
    return h % cap;
}
```

- Multiplying by a prime (31) distributes bits better and reduces collisions.
- `% cap` keeps the index in bounds.
- Empty string → `h` stays 0, returns 0.
- Same key always produces the same index (deterministic).

## Collision resolution: separate chaining

When two keys hash to the same bucket, a linked list threads through them:

```
bucket[3] → Entry{"hello", "1", next} → Entry{"world", "2", NULL}
```

Each `Entry` holds a heap-allocated key, heap-allocated value, and a `next` pointer. Lookup walks the chain comparing keys with `strcmp`.

```c
typedef struct Entry {
    char *key;
    char *value;
    struct Entry *next;
} Entry;
```

New entries are prepended (O(1)) — bucket pointer points to the new entry, which points to the old head.

## Structure layout

```c
typedef struct {
    Entry **buckets;  // array of pointers to Entry (each is a chain head)
    int len;          // number of stored keys
    int cap;          // number of buckets
} HashMap;
```

`buckets` is allocated with `calloc` so all pointers start as NULL (empty chains).

## API

| Function | What it does |
|---|---|
| `hm_new(cap)` | Allocate map + zero-init bucket array |
| `hm_set(hm, key, val)` | Insert or update; copies key+value onto heap |
| `hm_get(hm, key)` | Return pointer to value, or NULL if not found |
| `hm_delete(hm, key)` | Unlink entry from chain, free its key/value/node |
| `hm_free(hm)` | Walk all chains, free every entry, free buckets, free map |

## Insert (`hm_set`)

Two paths:

1. **Key exists** — walk chain, find match, `realloc` value to new size, `strcpy` new value.
2. **New key** — allocate `Entry`, `malloc` + `strcpy` key and value, prepend to bucket chain, increment `len`.

```c
new_entry->next = hm->buckets[key_hash];   // point to old head
hm->buckets[key_hash] = new_entry;         // new entry is now head
hm->len++;
```

## Delete (`hm_delete`)

Needs a `prev` pointer to relink the chain after removing the target:

```c
Entry *curr = hm->buckets[key_hash];
Entry *prev = NULL;

while (curr != NULL) {
    if (strcmp(curr->key, key) == 0) {
        if (prev == NULL)
            hm->buckets[key_hash] = curr->next;  // head removal
        else
            prev->next = curr->next;              // mid-chain removal

        free(curr->key);
        free(curr->value);
        free(curr);
        hm->len--;
        return;
    }
    prev = curr;
    curr = curr->next;
}
```

## Memory ownership

Every key and value is `strdup`-style heap-allocated on insert — the map owns copies, not the original strings. `hm_free` must walk all chains to free them; just `free(hm->buckets)` leaks every `Entry`.

```c
void hm_free(HashMap *hm) {
    for (int i = 0; i < hm->cap; i++) {
        Entry *e = hm->buckets[i];
        while (e != NULL) {
            Entry *next = e->next;   // save before freeing
            free(e->key);
            free(e->value);
            free(e);
            e = next;
        }
    }
    free(hm->buckets);
    free(hm);
}
```

## Load factor

As entries increase relative to buckets, chains get longer and performance degrades toward O(n). Production hash tables resize when `len / cap` exceeds ~0.7. This implementation uses a fixed cap — fine for learning.

## Common bugs

| Bug | Cause |
|---|---|
| Leak on `calloc` failure in `hm_new` | Allocated `hm` but returned NULL without `free(hm)` |
| Using pointer after `realloc` | `realloc` may move the block; always assign to temp first |
| Missing null-terminator | `malloc(strlen(key))` without `+1` |
| Leaking entries on `hm_free` | Only freeing the bucket array, not walking chains |
