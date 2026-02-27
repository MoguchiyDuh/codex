#include <limits.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>

// ── task 1: type sizes
// ─────────────────────────────────────────────────────

void print_sizes(void) {
  printf("%-20s %zu\n", "char",        sizeof(char));
  printf("%-20s %zu\n", "short",       sizeof(short));
  printf("%-20s %zu\n", "int",         sizeof(int));
  printf("%-20s %zu\n", "long",        sizeof(long));
  printf("%-20s %zu\n", "long long",   sizeof(long long));
  printf("%-20s %zu\n", "float",       sizeof(float));
  printf("%-20s %zu\n", "double",      sizeof(double));
  printf("%-20s %zu\n", "long double", sizeof(long double));
  printf("%-20s %zu\n", "void *",      sizeof(void *));
  printf("%-20s %zu\n", "bool",        sizeof(bool));
}

// ── task 2: overflow — signed UB vs unsigned wrap
// ───────────────────────────────────

void overflow_demo(void) {
  // unsigned wraps by spec — defined behavior
  unsigned int u = UINT_MAX;
  printf("UINT_MAX + 1 = %u\n", u + 1);  // always 0

  // signed overflow is UB — with -fsanitize=undefined this crashes
  // without sanitizer the compiler assumes it never happens and
  // may optimize away the check entirely (classic optimizer trap)
  int s = INT_MAX;
  printf("INT_MAX     = %d\n", s);
  printf("INT_MAX + 1 = %d  (UB — sanitizer will catch this)\n", s + 1);
}

// ── task 3 & 4: bitwise permission flags with uint8_t
// ───────────────────────────

#define READ   ((uint8_t)(1 << 0))  // 0b00000001
#define WRITE  ((uint8_t)(1 << 1))  // 0b00000010
#define EXEC   ((uint8_t)(1 << 2))  // 0b00000100
#define STICKY ((uint8_t)(1 << 3))  // 0b00001000

uint8_t set_flag(uint8_t perms, uint8_t flag)   { return perms | flag; }
uint8_t clear_flag(uint8_t perms, uint8_t flag) { return perms & (uint8_t)~flag; }
bool    has_flag(uint8_t perms, uint8_t flag)   { return (perms & flag) != 0; }

void flags_demo(void) {
  printf("sizeof(uint8_t) = %zu  (expected 1)\n", sizeof(uint8_t));

  uint8_t perms = 0;
  perms = set_flag(perms, READ | WRITE);

  printf("after set READ|WRITE:  has_read=%d  has_exec=%d\n",
         has_flag(perms, READ), has_flag(perms, EXEC));

  perms = set_flag(perms, EXEC);
  perms = clear_flag(perms, WRITE);

  printf("after set EXEC, clear WRITE: 0x%02X\n", perms);
  printf("  READ=%d WRITE=%d EXEC=%d STICKY=%d\n",
         has_flag(perms, READ),
         has_flag(perms, WRITE),
         has_flag(perms, EXEC),
         has_flag(perms, STICKY));
}

// ── task 5: precedence trap
// ──────────────────────────────────────────────────

void precedence_trap(void) {
  int x = 0;

  // `0xFF == 0` evaluates first (precedence 9) → 0
  // then `x & 0` → always 0, regardless of x
  int wrong = x & 0xFF == 0;
  printf("x & 0xFF == 0   → %d  (WRONG: always 0)\n", wrong);

  // correct: parentheses force the AND first
  int correct = (x & 0xFF) == 0;
  printf("(x & 0xFF) == 0 → %d  (correct)\n", correct);
}

// ── main
// ─────────────────────────────────────────────────────────────────────

int main(void) {
  printf("=== type sizes ===\n");
  print_sizes();

  printf("\n=== overflow ===\n");
  overflow_demo();

  printf("\n=== flags (uint8_t) ===\n");
  flags_demo();

  printf("\n=== precedence trap ===\n");
  precedence_trap();

  return 0;
}
