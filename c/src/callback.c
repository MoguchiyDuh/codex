#include <stddef.h>
#include <stdio.h>

typedef int (*callback_type)(int);

void map(int *arr, size_t len, callback_type callback) {
  if (arr == NULL || !len || !callback)
    return;
  for (size_t i = 0; i < len; ++i) {
    arr[i] = callback(arr[i]);
  }
}

int double_value(int value) { return value * 2; }

void print_arr(const int *arr, size_t len) {
  if (arr == NULL || !len) {
    printf("[]\n");
    return;
  }

  printf("[");
  for (size_t i = 0; i < len; ++i) {
    printf("%d", arr[i]);
    if (i < len - 1) {
      printf(" ");
    }
  }
  printf("]\n");
}

int main(void) {
  int arr[] = {1, 2, 3, 4, 5};

  print_arr(arr, sizeof(arr) / sizeof(arr[0]));
  map(arr, sizeof(arr) / sizeof(arr[0]), double_value);
  print_arr(arr, sizeof(arr) / sizeof(arr[0]));
  return 0;
}
