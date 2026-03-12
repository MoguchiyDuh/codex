#include <stddef.h>
#include <stdio.h>

double add_op(double a, double b) { return a + b; }
double sub_op(double a, double b) { return a - b; }
double div_op(double a, double b) {
  if (b == 0.0)
    return 0.0;
  return a / b;
}
double mul_op(double a, double b) { return a * b; }

typedef double (*CalcOp)(double a, double b);

typedef struct {
  char symbol;
  CalcOp operation;
} DispatchEntry;

#define TABLE_LEN 4

DispatchEntry table[] = {
    {'+', add_op}, {'-', sub_op}, {'*', mul_op}, {'/', div_op}};

double calculate(char op, double a, double b) {
  for (size_t i = 0; i < TABLE_LEN; i++) {
    if (table[i].symbol == op) {
      return table[i].operation(a, b);
    }
  }
  return 0;
}

int main(void) {
  printf("%f\n", calculate('+', 2, 2));
  printf("%f\n", calculate('-', 2, 2));
  printf("%f\n", calculate('/', 2, 2));
  printf("%f\n", calculate('*', 2, 2));
  return 0;
}
