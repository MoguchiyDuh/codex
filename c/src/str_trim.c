#include <assert.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

char *str_trim(char *str) {
  if (str == NULL)
    return NULL;

  char *end = str + strlen(str);
  while (end > str && isspace((unsigned char)*(end - 1)))
    --end;
  *end = '\0';

  char *start = str;
  while (isspace((unsigned char)*start))
    ++start;

  if (start != str)
    memmove(str, start, (size_t)(end - start) + 1);

  return str;
}

void test_trim(void) {
  char t1[] = "   hello   ";
  assert(strcmp(str_trim(t1), "hello") == 0);

  char t2[] = "world   ";
  assert(strcmp(str_trim(t2), "world") == 0);

  char t3[] = "   leading";
  assert(strcmp(str_trim(t3), "leading") == 0);

  char t4[] = "   ";
  assert(strcmp(str_trim(t4), "") == 0);

  char t5[] = "";
  assert(strcmp(str_trim(t5), "") == 0);

  char t6[] = "middle space";
  assert(strcmp(str_trim(t6), "middle space") == 0);
}

int main(void) {
  test_trim();
  printf("all tests passed\n");
  return 0;
}
