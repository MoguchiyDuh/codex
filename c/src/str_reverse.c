#include <stdio.h>
#include <string.h>

void str_reverse(char *str) {
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
  str_reverse(string1);
  printf("%s\n", string1);
}
