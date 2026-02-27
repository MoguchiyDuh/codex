#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Entry {
  char *key;
  char *value;
  struct Entry *next; // linked list for chaining
} Entry;

typedef struct {
  Entry **buckets; // array of pointers to Entry
  int len;         // number of stored keys
  int cap;         // number of buckets
} HashMap;

unsigned int hash(char *key, int cap) {
  unsigned int h = 0;
  while (*key)
    h = h * 31 + *key++;
  return h % cap;
}

HashMap *hm_new(int cap) {
  // allocate map + buckets
  if (cap <= 0)
    return NULL;

  HashMap *hm = malloc(sizeof(HashMap));
  if (hm == NULL) {
    return NULL;
  }

  hm->buckets = calloc(cap, sizeof(Entry *));
  if (hm->buckets == NULL) {
    free(hm);  // fix: hm was malloc'd — must free before returning NULL
    return NULL;
  }
  hm->len = 0;
  hm->cap = cap;

  return hm;
}

void hm_set(HashMap *hm, char *key, char *val) {
  // insert or update
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
  hm->len++;
}

char *hm_get(HashMap *hm, char *key) {
  // lookup, NULL if missing
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

void hm_delete(HashMap *hm, char *key) {
  // remove a key
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
  // free everything
  if (hm == NULL)
    return;

  for (int i = 0; i < hm->cap; i++) {
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
  hm->buckets = NULL;
  free(hm);
}

void hm_print(HashMap *hm) {
  // print all entries
  if (hm == NULL)
    return;
  printf("len: %d, cap: %d\n", hm->len, hm->cap);
  printf("{\n");
  for (int i = 0; i < hm->cap; i++) {
    Entry *entry = hm->buckets[i];
    while (entry != NULL) {
      printf("%s: %s (next: %s)\n", entry->key, entry->value,
             entry->next != NULL ? entry->next->key : "nil");
      entry = entry->next;
    }
  }
  printf("}\n");
}

// tests

void test_hash(void) {
  int cap = 100;

  // deterministic — same key, same hash
  assert(hash("abc", cap) == hash("abc", cap));

  // in-range
  assert(hash("abc", cap) < (unsigned int)cap);
  assert(hash("hello world", cap) < (unsigned int)cap);

  // different keys differ (for these specific values)
  assert(hash("abc", cap) != hash("zxc", cap));

  // empty string hashes to 0 (h starts at 0, loop never runs)
  assert(hash("", cap) == 0);

  printf("hash:      ok\n");
}

void test_hm_new(void) {
  HashMap *hm = hm_new(8);
  assert(hm != NULL);
  assert(hm->len == 0);
  assert(hm->cap == 8);
  assert(hm->buckets != NULL);
  hm_free(hm);

  // cap <= 0 returns NULL
  assert(hm_new(0) == NULL);
  assert(hm_new(-1) == NULL);

  printf("hm_new:    ok\n");
}

void test_hm_set(void) {
  HashMap *hm = hm_new(8);

  // insert
  hm_set(hm, "a", "1");
  assert(hm->len == 1);
  assert(strcmp(hm_get(hm, "a"), "1") == 0);

  // insert another key
  hm_set(hm, "b", "2");
  assert(hm->len == 2);

  // update existing key — value changes, len stays same
  hm_set(hm, "a", "updated");
  assert(hm->len == 2);
  assert(strcmp(hm_get(hm, "a"), "updated") == 0);

  // update with longer value (exercises realloc path)
  hm_set(hm, "a", "this is a much longer value than before");
  assert(strcmp(hm_get(hm, "a"), "this is a much longer value than before") == 0);

  // null safety — none of these should crash
  hm_set(NULL, "k", "v");
  hm_set(hm, NULL, "v");
  hm_set(hm, "k", NULL);

  hm_free(hm);
  printf("hm_set:    ok\n");
}

void test_hm_get(void) {
  HashMap *hm = hm_new(8);
  hm_set(hm, "key", "value");

  // found
  assert(strcmp(hm_get(hm, "key"), "value") == 0);

  // not found
  assert(hm_get(hm, "missing") == NULL);

  // null safety
  assert(hm_get(NULL, "k") == NULL);
  assert(hm_get(hm, NULL) == NULL);

  hm_free(hm);
  printf("hm_get:    ok\n");
}

void test_hm_delete(void) {
  HashMap *hm = hm_new(8);
  hm_set(hm, "x", "1");
  hm_set(hm, "y", "2");
  assert(hm->len == 2);

  // delete existing key
  hm_delete(hm, "x");
  assert(hm->len == 1);
  assert(hm_get(hm, "x") == NULL);
  assert(strcmp(hm_get(hm, "y"), "2") == 0); // other key untouched

  // delete non-existent key — no crash, len unchanged
  hm_delete(hm, "x");
  assert(hm->len == 1);

  // null safety
  hm_delete(NULL, "y");
  hm_delete(hm, NULL);

  hm_free(hm);
  printf("hm_delete: ok\n");
}

void test_hm_collision(void) {
  // cap=1 forces every key into bucket 0 — tests chaining
  HashMap *hm = hm_new(1);
  hm_set(hm, "a", "1");
  hm_set(hm, "b", "2");
  hm_set(hm, "c", "3");
  assert(hm->len == 3);

  assert(strcmp(hm_get(hm, "a"), "1") == 0);
  assert(strcmp(hm_get(hm, "b"), "2") == 0);
  assert(strcmp(hm_get(hm, "c"), "3") == 0);

  // delete middle of chain
  hm_delete(hm, "b");
  assert(hm->len == 2);
  assert(hm_get(hm, "b") == NULL);
  assert(strcmp(hm_get(hm, "a"), "1") == 0);
  assert(strcmp(hm_get(hm, "c"), "3") == 0);

  hm_free(hm);
  printf("collision: ok\n");
}

int main(void) {
  test_hash();
  test_hm_new();
  test_hm_set();
  test_hm_get();
  test_hm_delete();
  test_hm_collision();
  printf("all tests passed\n");
  return 0;
}
