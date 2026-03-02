#pragma once

#include <stddef.h>

typedef struct Vec Vec;

Vec *vec_new(void);
void vec_push(Vec *v, int val);
int vec_get(const Vec *v, size_t i);
void vec_free(Vec *v);
void vec_print(const Vec *v);

size_t vec_len(const Vec *v);
size_t vec_cap(const Vec *v);

