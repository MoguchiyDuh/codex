#include "vec.h"
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

void test_vec_new(void) {
  Vec *v = vec_new();
  assert(v != NULL);
  assert(vec_len(v) == 0);
  assert(vec_cap(v) == 4);
  vec_free(v);
  printf("test_vec_new: ok\n");
}

void test_vec_push(void) {
  Vec *v = vec_new();

  vec_push(v, 10);
  assert(vec_len(v) == 1);
  assert(vec_get(v, 0) == 10);

  vec_push(v, 20);
  vec_push(v, 30);
  assert(vec_len(v) == 3);

  vec_free(v);
  printf("test_vec_push: ok\n");
}

void test_vec_grow(void) {
  Vec *v = vec_new();
  assert(vec_cap(v) == 4);

  // fill to capacity
  for (int i = 0; i < 4; ++i)
    vec_push(v, i);
  assert(vec_len(v) == 4 && vec_cap(v) == 4);

  // push one more — triggers realloc, cap doubles
  vec_push(v, 99);
  assert(vec_len(v) == 5);
  assert(vec_cap(v) == 8);

  // values intact after grow
  for (size_t i = 0; i < 4; ++i)
    assert(vec_get(v, i) == (int)i);
  assert(vec_get(v, 4) == 99);

  vec_free(v);
  printf("test_vec_grow: ok\n");
}

void test_vec_get(void) {
  Vec *v = vec_new();
  vec_push(v, 10);
  vec_push(v, 20);
  vec_push(v, 30);

  assert(vec_get(v, 0) == 10);
  assert(vec_get(v, 1) == 20);
  assert(vec_get(v, 2) == 30);

  // out of bounds
  assert(vec_get(v, 3) == -1);
  // size_t cast for negative test if we want, but vec_get handles large i
  assert(vec_get(v, (size_t)-1) == -1);

  // null vec
  assert(vec_get(NULL, 0) == -1);

  vec_free(v);
  printf("test_vec_get: ok\n");
}

void test_vec_free(void) {
  Vec *v = vec_new();
  vec_push(v, 1);
  vec_push(v, 2);
  vec_free(v);
  // Cannot safely check internals after free in opaque mode
  printf("test_vec_free: ok\n");
}

void test_null_safety(void) {
  vec_push(NULL, 1); // should not crash
  vec_free(NULL);    // should not crash
  vec_print(NULL);   // should not crash
  printf("test_null_safety: ok\n");
}

int main(void) {
  test_vec_new();
  test_vec_push();
  test_vec_grow();
  test_vec_get();
  test_vec_free();
  test_null_safety();
  printf("all vec tests passed\n");
  return 0;
}
