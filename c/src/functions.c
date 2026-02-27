#include <assert.h>
#include <limits.h>
#include <stdarg.h>
#include <stdio.h>

int divmod(int a, int b, int *quot, int *rem) {
  if (b == 0)
    return -1;

  if (quot != NULL)
    *quot = a / b;
  if (rem != NULL)
    *rem = a % b;

  return 0;
}

typedef int (*BinOp)(int, int);

typedef struct {
  char sym;
  BinOp fn;
} Op;

int add(int a, int b) { return a + b; }
int sub(int a, int b) { return a - b; }
int mul(int a, int b) { return a * b; }
int div_safe(int a, int b) {
  if (b == 0)
    return INT_MIN;
  return a / b;
}

static const Op ops[] = {{'+', add}, {'-', sub}, {'*', mul}, {'/', div_safe}};

int apply(char sym, int a, int b) {
  int n = (int)(sizeof(ops) / sizeof(ops[0]));
  for (int i = 0; i < n; ++i) {
    if (ops[i].sym == sym) {
      return ops[i].fn(a, b);
    }
  }
  return INT_MIN;
}

int next_id() {
  // init only once then it is skipped
  static int counter = 0;
  return ++counter;
}

int sum_n(int count, ...) {
  int total = 0;
  va_list args;

  va_start(args, count);
  for (int i = 0; i < count; ++i) {
    total += va_arg(args, int);
  }
  va_end(args);

  return total;
}

void test_divmod() {
  int q, r;

  // Test standard division
  assert(divmod(10, 3, &q, &r) == 0);
  assert(q == 3);
  assert(r == 1);

  // Test division by zero
  assert(divmod(10, 0, &q, &r) == -1);

  // Test negative values
  assert(divmod(-10, 3, &q, &r) == 0);
  assert(q == -3);
  assert(r == -1);

  // Test null pointers (defensive handling)
  assert(divmod(10, 3, (void *)0, &r) == 0);
  assert(r == 1);
  printf("divmod: ok\n");
}

void test_apply() {
  // Test basic operations
  assert(apply('+', 10, 5) == 15);
  assert(apply('-', 10, 5) == 5);
  assert(apply('*', 10, 5) == 50);
  assert(apply('/', 10, 5) == 2);

  // Test division by zero (div_safe logic)
  assert(apply('/', 10, 0) == INT_MIN);

  // Test unknown symbol
  assert(apply('%', 10, 5) == INT_MIN);
  assert(apply('?', 1, 1) == INT_MIN);

  // Test negative numbers
  assert(apply('+', -5, -5) == -10);
  assert(apply('*', -2, 4) == -8);
  printf("apply ops: ok\n");
}

void test_next_id() {
  assert(next_id() == 1);
  assert(next_id() == 2);

  printf("next_id: ok\n");
}

void test_sum_n(void) {
  // Summing 3 integers: 10 + 20 + 30 = 60
  int result1 = sum_n(3, 10, 20, 30);
  assert(result1 == 60);

  // Summing 5 integers: 1 + 2 + 3 + 4 + 5 = 15
  int result2 = sum_n(5, 1, 2, 3, 4, 5);
  assert(result2 == 15);

  // Summing 1 integer: 100 = 100
  int result3 = sum_n(1, 100);
  assert(result3 == 100);

  // Summing 0 integers: = 0
  int result4 = sum_n(0);
  assert(result4 == 0);
  printf("sum_n variadic: ok\n");
}

int main() {
  test_divmod();
  test_apply();
  test_next_id();
  test_sum_n();

  printf("all tests passed\n");
  return 0;
}
