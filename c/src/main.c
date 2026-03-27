#include <stdint.h>

volatile uint32_t *const REG = (volatile uint32_t *)0x40002000;

void poll_reg(void) {
  while (!(*REG & 0x01)) {
  }
}

int main(void) { return 0; }
