#include <errno.h>
#include <stdio.h>

int file_copy(const char *src, const char *dst) {
  if (src == NULL || dst == NULL)
    return -1;

  FILE *file_src = fopen(src, "rb");
  if (!file_src)
    return -1;

  FILE *file_dst = fopen(dst, "wb");
  if (!file_dst) {
    fclose(file_src);
    return -1;
  }

  char buf[4096];
  size_t n;
  int result = 0;

  while ((n = fread(buf, 1, sizeof(buf), file_src)) > 0) {
    if (fwrite(buf, 1, n, file_dst) != n) {
      result = -1;
      break;
    }
  }

  if (result == 0 && ferror(file_src)) {
    result = -1;
  }

  // Save errno in case fclose modifies it
  int saved_errno = (result == -1) ? errno : 0;

  fclose(file_src);
  if (fclose(file_dst) != 0)
    result = -1;

  if (saved_errno != 0)
    errno = saved_errno;

  return result;
}

int main(void) {
  const char *file1 = "test_src.txt";
  const char *file2 = "test_dst.txt";
  int out = file_copy(file1, file2);
  printf("success? %d\n", out);
  return 0;
}
