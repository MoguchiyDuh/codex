#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  struct __attribute__((packed)) Network {
    char message_type;
    short pl_len;
    int seq_number;
  };
  printf("%zu\n", offsetof(struct Network, message_type));
  printf("%zu\n", offsetof(struct Network, pl_len));
  printf("%zu\n", offsetof(struct Network, seq_number));
  printf("%zu\n", sizeof(struct Network));
  struct Network n = {'a', 1, 1};
  printf("%c %d %d\n", n.message_type, n.pl_len, n.seq_number);
}
