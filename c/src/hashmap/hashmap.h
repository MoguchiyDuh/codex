#pragma once

#include <stddef.h>

typedef struct HashMap HashMap;

HashMap *hm_new(size_t cap);
void hm_set(HashMap *hm, const char *key, const char *val);
char *hm_get(const HashMap *hm, const char *key);
void hm_delete(HashMap *hm, const char *key);
void hm_free(HashMap *hm);
void hm_print(const HashMap *hm);

size_t hm_len(const HashMap *hm);
size_t hm_cap(const HashMap *hm);
