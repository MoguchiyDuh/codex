#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static void quicksort_impl(int *arr, size_t start, size_t end) {
  if (start >= end)
    return;

  size_t i = start;
  size_t j = end;
  int pivot = arr[start + (end - start) / 2];

  while (i <= j) {
    while (arr[i] < pivot)
      ++i;
    while (arr[j] > pivot) {
      if (j == 0)
        break;
      --j;
    }

    if (i <= j) {
      int tmp = arr[i];
      arr[i] = arr[j];
      arr[j] = tmp;
      ++i;
      if (j == 0)
        break;
      --j;
    }
  }

  if (j > start)
    quicksort_impl(arr, start, j);
  if (i < end)
    quicksort_impl(arr, i, end);
}

int *quick_sort(const int arr[], size_t len) {
  if (len == 0)
    return NULL;

  int *out = malloc(len * sizeof(int));
  if (!out)
    return NULL;

  memcpy(out, arr, len * sizeof(int));
  quicksort_impl(out, 0, len - 1);
  return out;
}

int main(void) {
  int arr[] = {5, 4, 3, 2, 1};
  size_t len = sizeof(arr) / sizeof(arr[0]);
  int *sorted_arr = quick_sort(arr, len);
  for (size_t i = 0; i < len; ++i)
    printf("%d ", sorted_arr[i]);
  free(sorted_arr);
  return 0;
}
