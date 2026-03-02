#include "hashmap.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Entry {
  char *key;
  char *value;
  struct Entry *next;
} Entry;

struct HashMap {
  Entry **buckets;
  size_t len;
  size_t cap;
};

static unsigned int hash(const char *key, size_t cap) {
  unsigned int h = 0;
  while (*key)
    h = h * 31 + (unsigned char)*key++;
  return h % cap;
}

HashMap *hm_new(size_t cap) {
  if (cap == 0)
    return NULL;

  HashMap *hm = malloc(sizeof(HashMap));
  if (hm == NULL) {
    return NULL;
  }

  hm->buckets = calloc(cap, sizeof(Entry *));
  if (hm->buckets == NULL) {
    free(hm);
    return NULL;
  }
  hm->len = 0;
  hm->cap = cap;

  return hm;
}

void hm_set(HashMap *hm, const char *key, const char *val) {
  if (hm == NULL || key == NULL || val == NULL) {
    return;
  }
  unsigned int key_hash = hash(key, hm->cap);
  Entry *entry = hm->buckets[key_hash];

  while (entry != NULL) {
    if (strcmp(entry->key, key) == 0) {
      char *new_val = realloc(entry->value, strlen(val) + 1);
      if (new_val == NULL)
        return;
      entry->value = new_val;
      strcpy(entry->value, val);
      return;
    }
    entry = entry->next;
  }

  Entry *new_entry = malloc(sizeof(Entry));
  if (new_entry == NULL)
    return;

  new_entry->key = malloc(strlen(key) + 1);
  new_entry->value = malloc(strlen(val) + 1);

  if (new_entry->key == NULL || new_entry->value == NULL) {
    free(new_entry->key);
    free(new_entry->value);
    free(new_entry);
    return;
  }

  strcpy(new_entry->key, key);
  strcpy(new_entry->value, val);

  new_entry->next = hm->buckets[key_hash];
  hm->buckets[key_hash] = new_entry;
  ++hm->len;
}

char *hm_get(const HashMap *hm, const char *key) {
  if (hm == NULL || key == NULL)
    return NULL;

  unsigned int key_hash = hash(key, hm->cap);
  Entry *entry = hm->buckets[key_hash];
  while (entry != NULL) {
    if (strcmp(entry->key, key) == 0) {
      return entry->value;
    }
    entry = entry->next;
  }

  return NULL;
}

void hm_delete(HashMap *hm, const char *key) {
  if (hm == NULL || key == NULL) {
    return;
  }

  unsigned int key_hash = hash(key, hm->cap);
  Entry *curr = hm->buckets[key_hash];
  Entry *prev = NULL;

  while (curr != NULL) {
    if (strcmp(curr->key, key) == 0) {
      if (prev == NULL) {
        hm->buckets[key_hash] = curr->next;
      } else {
        prev->next = curr->next;
      }

      free(curr->key);
      free(curr->value);
      free(curr);
      hm->len--;
      return;
    }
    prev = curr;
    curr = curr->next;
  }
}

void hm_free(HashMap *hm) {
  if (hm == NULL)
    return;

  for (size_t i = 0; i < hm->cap; ++i) {
    Entry *entry = hm->buckets[i];
    while (entry != NULL) {
      Entry *next = entry->next;
      free(entry->key);
      free(entry->value);
      free(entry);
      entry = next;
    }
  }
  free(hm->buckets);
  free(hm);
}

void hm_print(const HashMap *hm) {
  if (hm == NULL)
    return;
  printf("len: %zu, cap: %zu\n", hm->len, hm->cap);
  printf("{\n");
  for (size_t i = 0; i < hm->cap; ++i) {
    Entry *entry = hm->buckets[i];
    while (entry != NULL) {
      printf("%s: %s (next: %s)\n", entry->key, entry->value,
             entry->next != NULL ? entry->next->key : "nil");
      entry = entry->next;
    }
  }
  printf("}\n");
}

size_t hm_len(const HashMap *hm) { return hm ? hm->len : 0; }

size_t hm_cap(const HashMap *hm) { return hm ? hm->cap : 0; }
