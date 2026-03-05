#include <errno.h>
#include <stdio.h>

char *read_file(const char *path, size_t *out_size);
// returns NULL on error, sets errno

long get_file_size(const char *filename) {
  FILE *fp = fopen(filename, "rb");
  if (fp == NULL)
    return -1;

  fseek(fp, 0L, SEEK_END); // Move pointer to the end
  long size = ftell(fp);   // Read the pointer position
  fclose(fp);

  return size;
}

int main(void) {
  const char *file = "test_src.txt";
  size_t size = (size_t)get_file_size(file);
  read_file(file, &size);
}
