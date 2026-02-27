#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>

int main(int argc, char **argv) {
  FILE *f;

  if (argc < 2) {
    f = stdin;
  } else {
    f = fopen(argv[1], "rb");
    if (f == NULL) {
      fprintf(stderr, "error: cannot open %s\n", argv[1]);
      return 1;
    }
  }

  unsigned int lines = 0;
  unsigned int words = 0;
  unsigned int bytes = 0;
  bool in_word = false;
  int ch;

  while ((ch = fgetc(f)) != EOF) {
    ++bytes;

    if (ch == '\n') {
      ++lines;
    }

    if (isspace(ch)) {
      in_word = false;
    } else if (!in_word) {
      in_word = true;
      ++words;
    }
  }

  printf("%7u %7u %7u %s\n", lines, words, bytes, (argc < 2) ? "" : argv[1]);

  if (f != stdin) {
    fclose(f);
  }

  return 0;
}
