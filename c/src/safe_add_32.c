#include <limits.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>

int safe_add_i32(int32_t a, int32_t b, int32_t *out) {
  // If 'a' is greater than 0, check if adding 'b' would exceed INT32_MAX
  if (a > 0 && b > INT32_MAX - a) {
    return -1; // Overflow
  }
  // If 'a' is less than 0, check if adding 'b' would be less than INT32_MIN
  if (a < 0 && b < INT32_MIN - a) {
    return -1; // Underflow
  }

  *out = a + b;
  return 0;
}

int main(void) {
  int32_t a = INT32_MAX;
  int32_t b = 2;
  int32_t out;
  int result = safe_add_i32(a, b, &out);
  printf("%d (%d)\n", out, result);
  return 0;
}
