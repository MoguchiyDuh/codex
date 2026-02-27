#include <assert.h>
#include <stdio.h>
#include <string.h>

// strlen
//
// Returns number of chars before '\0'. Returns 0 for NULL.
int my_strlen(char *s) {
  if (!s)
    return 0;
  int len = 0;
  while (s[len] != '\0')
    len++;
  return len;
}

// strcpy
//
// Copies src into dst until '\0'. No bounds check — dst must fit src.
// Returns dst.
char *my_strcpy(char *dst, char *src) {
  if (!dst || !src)
    return dst;
  int i = 0;
  while (src[i] != '\0') {
    dst[i] = src[i];
    i++;
  }
  dst[i] = '\0';
  return dst;
}

//  strncpy
//
// Bounds-checked copy: writes at most dst_size-1 chars, always null-terminates.
// Returns dst.
char *my_strncpy(char *dst, char *src, int dst_size) {
  if (!dst || !src || dst_size == 0)
    return dst;
  int i = 0;
  while (i < dst_size - 1 && src[i] != '\0') {
    dst[i] = src[i];
    i++;
  }
  dst[i] = '\0';
  return dst;
}

// strcmp
//
// Returns 0 if equal, <0 if a < b, >0 if a > b.
int my_strcmp(char *a, char *b) {
  if (!a || !b)
    return (a == b) ? 0 : (!a ? -1 : 1);
  while (*a && *a == *b) {
    a++;
    b++;
  }
  return *a - *b;
}

// strchr
//
// Returns pointer to first occurrence of c in s, NULL if not found.
// Can find '\0' itself.
char *my_strchr(char *s, char c) {
  if (!s)
    return NULL;
  while (*s != c) {
    if (*s == '\0')
      return NULL;
    s++;
  }
  return s;
}

//  tests
void test_my_strlen(void) {
  assert(my_strlen("hello") == 5);
  assert(my_strlen("a") == 1);
  assert(my_strlen("") == 0);
  assert(my_strlen(NULL) == 0);
  printf("strlen:  ok\n");
}

void test_my_strcpy(void) {
  char dst[16];

  assert(strcmp(my_strcpy(dst, "hello"), "hello") == 0);
  assert(strcmp(my_strcpy(dst, ""), "") == 0);
  assert(my_strcpy(dst, "abc") == dst); // returns dst

  // null safety
  assert(my_strcpy(NULL, "src") == NULL);
  assert(my_strcpy(dst, NULL) == dst);

  printf("strcpy:  ok\n");
}

void test_my_strncpy(void) {
  char buf[8];

  // normal copy
  my_strncpy(buf, "hello", sizeof(buf));
  assert(strcmp(buf, "hello") == 0);

  // truncation — always null-terminates
  my_strncpy(buf, "toolongstring", 5);
  assert(strcmp(buf, "tool") == 0);
  assert(buf[4] == '\0');

  // dst_size == 1 → empty string
  char tiny[1];
  my_strncpy(tiny, "anything", 1);
  assert(tiny[0] == '\0');

  // empty src
  my_strncpy(buf, "", sizeof(buf));
  assert(strcmp(buf, "") == 0);

  // null safety
  assert(my_strncpy(NULL, "src", 5) == NULL);

  printf("strncpy: ok\n");
}

void test_my_strcmp(void) {
  assert(my_strcmp("abc", "abc") == 0);
  assert(my_strcmp("abc", "abd") < 0);
  assert(my_strcmp("abd", "abc") > 0);
  assert(my_strcmp("", "") == 0);
  assert(my_strcmp("a", "") > 0);
  assert(my_strcmp("", "a") < 0);
  assert(my_strcmp("apple", "apples") < 0); // prefix shorter
  assert(my_strcmp("apples", "apple") > 0);

  // null handling
  assert(my_strcmp(NULL, NULL) == 0);
  assert(my_strcmp(NULL, "a") < 0);
  assert(my_strcmp("a", NULL) > 0);

  printf("strcmp:  ok\n");
}

void test_my_strchr(void) {
  char str[] = "hello world";

  assert(my_strchr(str, 'h') == &str[0]);
  assert(my_strchr(str, 'e') == &str[1]);
  assert(my_strchr(str, 'o') == &str[4]); // first 'o', not second
  assert(my_strchr(str, 'z') == NULL);
  assert(my_strchr(str, '\0') == &str[11]); // finds null terminator

  // single char string
  char single[] = "x";
  assert(my_strchr(single, 'x') == &single[0]);
  assert(my_strchr(single, 'y') == NULL);

  // empty string
  char empty[] = "";
  assert(my_strchr(empty, 'a') == NULL);
  assert(my_strchr(empty, '\0') == &empty[0]);

  // null safety
  assert(my_strchr(NULL, 'a') == NULL);

  printf("strchr:  ok\n");
}

int main(void) {
  test_my_strlen();
  test_my_strcpy();
  test_my_strncpy();
  test_my_strcmp();
  test_my_strchr();
  printf("all tests passed\n");
  return 0;
}
