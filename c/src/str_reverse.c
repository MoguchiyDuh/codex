#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void str_reverse_alloc(char *str) {
  if (str == NULL || *str == '\0')
    return;

  size_t len = strlen(str);
  char str_reversed[len + 1]; // \0

  for (size_t i = 0; i < len; ++i) {
    str_reversed[i] = str[len - 1 - i];
  }

  str_reversed[len] = '\0';
  strcpy(str, str_reversed);
}

void str_reverse_no_alloc(char *str) {
  if (str == NULL || *str == '\0')
    return;

  size_t len = strlen(str);
  size_t l = 0;
  size_t r = len - 1;
  while (l < r) {
    char tmp = str[l];
    str[l++] = str[r];
    str[r--] = tmp;
  }
}

int main(void) {
  char string1[] = "hello";
  printf("%s\n", string1);
  str_reverse_alloc(string1);
  printf("%s\n", string1);
  str_reverse_no_alloc(string1);
  printf("%s\n", string1);
}
