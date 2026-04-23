#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int *insertion_sort(int arr[], size_t len) {
  if (len == 0)
    return NULL;
  int *out = malloc(len * sizeof(int));
  if (out == NULL)
    return NULL;
  memcpy(out, arr, len * sizeof(int));

  int key;
  for (size_t i = 1; i < len; i++) {
    key = out[i];
    size_t j = i;

    while (j > 0 && out[j - 1] > key) {
      out[j] = out[j - 1];
      --j;
    }
    out[j] = key;
  }

  return out;
}

int main(void) {
  int arr[] = {5, 4, 3, 2, 1};
  size_t len = sizeof(arr) / sizeof(arr[0]);
  int *sorted_arr = insertion_sort(arr, len);
  for (size_t i = 0; i < len; i++)
    printf("%d ", sorted_arr[i]);
  free(sorted_arr);
  return 0;
}
