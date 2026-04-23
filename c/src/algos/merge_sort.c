#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int merge(int *a, int *tmp, size_t left, size_t mid, size_t right) {
  size_t i = left;
  size_t j = mid;
  size_t k = left;

  while (i < mid && j < right) {
    if (a[i] <= a[j]) {
      tmp[k++] = a[i++];
    } else {
      tmp[k++] = a[j++];
    }
  }

  while (i < mid) {
    tmp[k++] = a[i++];
  }

  while (j < right) {
    tmp[k++] = a[j++];
  }

  for (k = left; k < right; k++) {
    a[k] = tmp[k];
  }

  return 1;
}

static int merge_sort_impl(int *a, int *tmp, size_t left, size_t right) {
  if (right - left < 2) {
    return 1;
  }

  size_t mid = left + (right - left) / 2;

  if (!merge_sort_impl(a, tmp, left, mid)) {
    return 0;
  }
  if (!merge_sort_impl(a, tmp, mid, right)) {
    return 0;
  }

  return merge(a, tmp, left, mid, right);
}

int *merge_sort(const int arr[], size_t len) {
  if (len == 0) {
    return NULL;
  }

  int *out = malloc(len * sizeof(*out));
  if (out == NULL) {
    return NULL;
  }

  int *tmp = malloc(len * sizeof(*tmp));
  if (tmp == NULL) {
    free(out);
    return NULL;
  }

  memcpy(out, arr, len * sizeof(*out));

  if (!merge_sort_impl(out, tmp, 0, len)) {
    free(tmp);
    free(out);
    return NULL;
  }

  free(tmp);
  return out;
}

int main(void) {
  int arr[] = {5, 4, 3, 2, 1};
  size_t len = sizeof(arr) / sizeof(arr[0]);

  int *sorted = merge_sort(arr, len);
  if (sorted == NULL && len != 0) {
    return 1;
  }

  for (size_t i = 0; i < len; i++) {
    printf("%d ", sorted[i]);
  }
  printf("\n");

  free(sorted);
  return 0;
}
