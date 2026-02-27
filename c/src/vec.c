#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

// structures

typedef struct {
  int *data;
  int len;
  int cap;
} Vec;

Vec vec_new(void) {
  void *ptr = malloc(4 * sizeof(int));
  if (ptr == NULL) {
    Vec empty = {NULL, 0, 0};
    return empty;
  }
  Vec v = {ptr, 0, 4};
  return v;
}

void vec_push(Vec *v, int val) {
  if (v == NULL)
    return;
  if (v->len == v->cap) {
    int new_cap = v->cap * 2;
    int *temp = realloc(v->data, new_cap * sizeof(int));
    if (temp == NULL)
      return;
    v->data = temp;
    v->cap = new_cap;
  }
  v->data[v->len++] = val;
}

// Returns element at index i, or -1 if out of bounds.
int vec_get(Vec *v, int i) {
  if (v == NULL || i < 0 || i >= v->len)
    return -1;
  return v->data[i];
}

void vec_free(Vec *v) {
  if (v == NULL)
    return;
  free(v->data);
  v->data = NULL;
  v->len = 0;
  v->cap = 0;
}

void vec_print(Vec *v) {
  if (v == NULL)
    return;
  printf("len=%d cap=%d [", v->len, v->cap);
  for (int i = 0; i < v->len; i++) {
    printf("%d%s", v->data[i], i < v->len - 1 ? ", " : "");
  }
  printf("]\n");
}

// tests

void test_vec_new(void) {
  Vec v = vec_new();
  assert(v.data != NULL);
  assert(v.len == 0);
  assert(v.cap == 4);
  vec_free(&v);
  printf("vec_new:  ok\n");
}

void test_vec_push(void) {
  Vec v = vec_new();

  vec_push(&v, 10);
  assert(v.len == 1);
  assert(v.data[0] == 10);

  vec_push(&v, 20);
  vec_push(&v, 30);
  assert(v.len == 3);

  vec_free(&v);
  printf("vec_push: ok\n");
}

void test_vec_grow(void) {
  Vec v = vec_new();
  assert(v.cap == 4);

  // fill to capacity
  for (int i = 0; i < 4; i++)
    vec_push(&v, i);
  assert(v.len == 4 && v.cap == 4);

  // push one more — triggers realloc, cap doubles
  vec_push(&v, 99);
  assert(v.len == 5);
  assert(v.cap == 8);

  // values intact after grow
  for (int i = 0; i < 4; i++)
    assert(v.data[i] == i);
  assert(v.data[4] == 99);

  vec_free(&v);
  printf("vec_grow: ok\n");
}

void test_vec_get(void) {
  Vec v = vec_new();
  vec_push(&v, 10);
  vec_push(&v, 20);
  vec_push(&v, 30);

  assert(vec_get(&v, 0) == 10);
  assert(vec_get(&v, 1) == 20);
  assert(vec_get(&v, 2) == 30);

  // out of bounds
  assert(vec_get(&v, 3) == -1);
  assert(vec_get(&v, -1) == -1);

  // null vec
  assert(vec_get(NULL, 0) == -1);

  vec_free(&v);
  printf("vec_get:  ok\n");
}

void test_vec_free(void) {
  Vec v = vec_new();
  vec_push(&v, 1);
  vec_push(&v, 2);
  vec_free(&v);

  // after free: data NULL, len/cap zeroed
  assert(v.data == NULL);
  assert(v.len == 0);
  assert(v.cap == 0);

  // double free — safe because data is NULL (free(NULL) is a no-op)
  vec_free(&v);

  printf("vec_free: ok\n");
}

void test_null_safety(void) {
  vec_push(NULL, 1); // should not crash
  vec_free(NULL);    // should not crash
  vec_print(NULL);   // should not crash
  printf("null safety: ok\n");
}

int main(void) {
  test_vec_new();
  test_vec_push();
  test_vec_grow();
  test_vec_get();
  test_vec_free();
  test_null_safety();
  printf("all tests passed\n");
  return 0;
}
