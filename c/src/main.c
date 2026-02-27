#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  typedef struct {
    size_t len;
    uint8_t data[]; // zero size here
  } Buffer;
  Buffer *b = malloc(sizeof(Buffer));
  printf("%zu\n", sizeof(*b));
  free(b);
  return 0;
}
