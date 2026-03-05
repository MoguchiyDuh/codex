#include <errno.h>
#include <stdio.h>
#include <stdlib.h>

char *read_file(const char *path, size_t *out_size) {
  if (path == NULL || out_size == NULL) {
    return NULL;
  }

  FILE *file = fopen(path, "rb");
  if (!file)
    return NULL;

  size_t capacity = 4096;
  size_t used = 0;
  size_t n;
  char *buf = malloc(capacity);
  if (buf == NULL) {
    int e = errno;
    fclose(file);
    errno = e;
    return NULL;
  }

  while ((n = fread(buf + used, 1, capacity - used, file)) > 0) {
    used += n;
    if (used == capacity) {
      capacity *= 2;
      char *new_buf = realloc(buf, capacity);
      if (!new_buf)
        goto fail;
      buf = new_buf;
    }
  }

  if (ferror(file))
    goto fail;

  char *new_buf = realloc(buf, used + 1);
  if (!new_buf)
    goto fail;
  buf = new_buf;
  buf[used] = '\0';

  *out_size = used;
  fclose(file);
  return buf;

fail:;
  int e = errno;
  free(buf);
  fclose(file);
  errno = e;
  return NULL;
}

int main(void) {
  const char *file = "test_src.txt";
  size_t size;
  char *buf_ptr = read_file(file, &size);
  printf("%zu\n", size);
  printf("%s\n", buf_ptr);
  free(buf_ptr);
}
