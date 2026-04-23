#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int *bubble_sort(int arr[], size_t len) {
  if (len == 0)
    return NULL;
  int *out = malloc(len * sizeof(int));
  if (out == NULL)
    return NULL;
  memcpy(out, arr, len * sizeof(int));

  int temp;
  size_t i, j;
  int swapped;
  for (i = 0; i < len - 1; ++i) {
    swapped = 0;
    for (j = 0; j < len - i - 1; j++) {
      if (out[j] > out[j + 1]) {
        temp = out[j];
        out[j] = out[j + 1];
        out[j + 1] = temp;
        swapped = 1;
      }
    }
    if (swapped == 0)
      break;
  }
  return out;
}

int main(void) {
  int arr[] = {5, 4, 3, 2, 1};
  size_t len = sizeof(arr) / sizeof(arr[0]);
  int *sorted_arr = bubble_sort(arr, len);
  for (size_t i = 0; i < len; ++i)
    printf("%d ", sorted_arr[i]);
  free(sorted_arr);
  return 0;
}
