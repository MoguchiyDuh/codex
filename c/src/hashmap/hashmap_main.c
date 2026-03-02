#include "hashmap.h"
#include <assert.h>
#include <stdio.h>
#include <string.h>

/* test_hash removed because hash() is now an internal static function */

void test_hm_new(void) {
  HashMap *hm = hm_new(8);
  assert(hm != NULL);
  assert(hm_len(hm) == 0);
  assert(hm_cap(hm) == 8);
  hm_free(hm);

  // cap <= 0 returns NULL (size_t handles negative, so 0 is the check)
  assert(hm_new(0) == NULL);
  printf("test_hm_new: ok\n");
}

void test_hm_set(void) {
  HashMap *hm = hm_new(8);

  // insert
  hm_set(hm, "a", "1");
  assert(hm_len(hm) == 1);
  assert(strcmp(hm_get(hm, "a"), "1") == 0);

  // insert another key
  hm_set(hm, "b", "2");
  assert(hm_len(hm) == 2);

  // update existing key — value changes, len stays same
  hm_set(hm, "a", "updated");
  assert(hm_len(hm) == 2);
  assert(strcmp(hm_get(hm, "a"), "updated") == 0);

  // update with longer value
  hm_set(hm, "a", "this is a much longer value than before");
  assert(strcmp(hm_get(hm, "a"), "this is a much longer value than before") ==
         0);

  // null safety — none of these should crash
  hm_set(NULL, "k", "v");
  hm_set(hm, NULL, "v");
  hm_set(hm, "k", NULL);

  hm_free(hm);
  printf("test_hm_set: ok\n");
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
  printf("test_hm_get: ok\n");
}

void test_hm_delete(void) {
  HashMap *hm = hm_new(8);
  hm_set(hm, "x", "1");
  hm_set(hm, "y", "2");
  assert(hm_len(hm) == 2);

  // delete existing key
  hm_delete(hm, "x");
  assert(hm_len(hm) == 1);
  assert(hm_get(hm, "x") == NULL);
  assert(strcmp(hm_get(hm, "y"), "2") == 0); // other key untouched

  // delete non-existent key — no crash, len unchanged
  hm_delete(hm, "x");
  assert(hm_len(hm) == 1);

  // null safety
  hm_delete(NULL, "y");
  hm_delete(hm, NULL);

  hm_free(hm);
  printf("test_hm_delete: ok\n");
}

void test_hm_collision(void) {
  // cap=1 forces every key into bucket 0 — tests chaining
  HashMap *hm = hm_new(1);
  hm_set(hm, "a", "1");
  hm_set(hm, "b", "2");
  hm_set(hm, "c", "3");
  assert(hm_len(hm) == 3);

  assert(strcmp(hm_get(hm, "a"), "1") == 0);
  assert(strcmp(hm_get(hm, "b"), "2") == 0);

  assert(strcmp(hm_get(hm, "c"), "3") == 0);

  // delete middle of chain
  hm_delete(hm, "b");
  assert(hm_len(hm) == 2);
  assert(hm_get(hm, "b") == NULL);
  assert(strcmp(hm_get(hm, "a"), "1") == 0);
  assert(strcmp(hm_get(hm, "c"), "3") == 0);

  hm_free(hm);
  printf("test_hm_collision: ok\n");
}

int main(void) {
  test_hm_new();
  test_hm_set();
  test_hm_get();
  test_hm_delete();
  test_hm_collision();
  printf("all hashmap tests passed\n");
  return 0;
}
