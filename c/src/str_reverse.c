#include <assert.h>
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

void test_str_reverse() {
  // Test Case 1: Standard string (odd length)
  char s1[] = "hello";
  str_reverse(s1);
  assert(strcmp(s1, "olleh") == 0);

  // Test Case 2: Standard string (even length)
  char s2[] = "code";
  str_reverse(s2);
  assert(strcmp(s2, "edoc") == 0);

  // Test Case 3: Single character
  char s3[] = "a";
  str_reverse(s3);
  assert(strcmp(s3, "a") == 0);

  // Test Case 4: Empty string
  char s4[] = "";
  str_reverse(s4);
  assert(strcmp(s4, "") == 0);

  // Test Case 5: Palindrome
  char s5[] = "racecar";
  str_reverse(s5);
  assert(strcmp(s5, "racecar") == 0);

  // Test Case 6: String with spaces
  char s6[] = "hi you";
  str_reverse(s6);
  assert(strcmp(s6, "uoy ih") == 0);

  // Test Case 7: Null pointer (should return without crash)
  str_reverse(NULL);
}

int main(void) {
  test_str_reverse();
  printf("All tests passed.\n");
  return 0;
}
