#include <assert.h>
#include <stdio.h>
#include <string.h>

size_t str_split(char *str, char delim, char **out, size_t max) {
  if (str == NULL || out == NULL || max == 0 || *str == '\0')
    return 0;

  char *cur = str;
  size_t i = 0;

  while (i < max) {
    out[i] = cur;
    ++i;

    char *ptr = strchr(cur, delim);
    if (ptr == NULL)
      break;

    *ptr = '\0';
    cur = ptr + 1;
  }
  return i;
}

void test_str_split(void) {
  char *out[8];
  size_t count;

  // 1. standard
  char s1[] = "apple,banana,cherry";
  count = str_split(s1, ',', out, 5);
  assert(count == 3);
  assert(strcmp(out[0], "apple") == 0);
  assert(strcmp(out[1], "banana") == 0);
  assert(strcmp(out[2], "cherry") == 0);

  // 2. no delimiter
  char s2[] = "hello world";
  count = str_split(s2, ',', out, 5);
  assert(count == 1);
  assert(strcmp(out[0], "hello world") == 0);

  // 3. more tokens than max
  char s3[] = "a:b:c:d";
  count = str_split(s3, ':', out, 2);
  assert(count == 2);
  assert(strcmp(out[0], "a") == 0);
  assert(strcmp(out[1], "b") == 0);

  // 4. empty string
  char s4[] = "";
  count = str_split(s4, ',', out, 5);
  assert(count == 0);

  // 5. trailing delimiter
  char s5[] = "ext,";
  count = str_split(s5, ',', out, 5);
  assert(count == 2);
  assert(strcmp(out[0], "ext") == 0);
  assert(strcmp(out[1], "") == 0);

  // 6. leading delimiter
  char s6[] = ",hello";
  count = str_split(s6, ',', out, 5);
  assert(count == 2);
  assert(strcmp(out[0], "") == 0);
  assert(strcmp(out[1], "hello") == 0);

  // 7. consecutive delimiters
  char s7[] = "a,,b";
  count = str_split(s7, ',', out, 5);
  assert(count == 3);
  assert(strcmp(out[0], "a") == 0);
  assert(strcmp(out[1], "") == 0);
  assert(strcmp(out[2], "b") == 0);

  // 8. single token no delim
  char s8[] = "solo";
  count = str_split(s8, ',', out, 5);
  assert(count == 1);
  assert(strcmp(out[0], "solo") == 0);

  // 9. all delimiters
  char s9[] = ",,,";
  count = str_split(s9, ',', out, 5);
  assert(count == 4);
  assert(strcmp(out[0], "") == 0);
  assert(strcmp(out[1], "") == 0);
  assert(strcmp(out[2], "") == 0);
  assert(strcmp(out[3], "") == 0);

  // 10. max=1 stops after first token
  char s10[] = "a,b,c";
  count = str_split(s10, ',', out, 1);
  assert(count == 1);
  assert(strcmp(out[0], "a") == 0);
}

int main(void) {
  test_str_split();
  printf("All tests passed\n");
  return 0;
}
