#include "vec.h"
#include <stdio.h>
#include <stdlib.h>

struct Vec {
  int *data;
  size_t len;
  size_t cap;
};

Vec *vec_new(void) {
  Vec *v = malloc(sizeof(Vec));
  if (v == NULL) {
    return NULL;
  }

  v->data = malloc(4 * sizeof(int));
  if (v->data == NULL) {
    free(v);
    return NULL;
  }

  v->len = 0;
  v->cap = 4;
  return v;
}

void vec_push(Vec *v, int val) {
  if (v == NULL)
    return;
  if (v->len == v->cap) {
    size_t new_cap = v->cap * 2;
    int *temp = realloc(v->data, new_cap * sizeof(int));
    if (temp == NULL)
      return;
    v->data = temp;
    v->cap = new_cap;
  }
  v->data[v->len++] = val;
}

int vec_get(const Vec *v, size_t i) {
  if (v == NULL || i >= v->len)
    return -1;
  return v->data[i];
}

void vec_free(Vec *v) {
  if (v == NULL)
    return;
  free(v->data);
  free(v);
}

void vec_print(const Vec *v) {
  if (v == NULL)
    return;
  printf("len=%zu cap=%zu [", v->len, v->cap);
  for (size_t i = 0; i < v->len; ++i) {
    printf("%d%s", v->data[i], i < v->len - 1 ? ", " : "");
  }
  printf("]\n");
}

size_t vec_len(const Vec *v) { return v ? v->len : 0; }

size_t vec_cap(const Vec *v) { return v ? v->cap : 0; }
