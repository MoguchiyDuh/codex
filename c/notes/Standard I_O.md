---
tags: [c, io, stdio]
status: complete
source: src/file_copy.c, src/file_read.c, src/wc.c
---

# Standard I/O

> C I/O is buffered by default and routed through `FILE *` handles — `printf` and `fopen` are high-level wrappers over OS syscalls.

## Streams

Three pre-opened streams available at program start:

| Stream | Buffering | Use |
|--------|-----------|-----|
| `stdin` | line-buffered (terminal) | input |
| `stdout` | line-buffered (terminal), fully-buffered (pipe/file) | output |
| `stderr` | unbuffered | errors — always gets out |

### Buffering modes

| Mode | Constant | Flush trigger |
|------|----------|---------------|
| Fully buffered | `_IOFBF` | buffer full |
| Line buffered | `_IOLBF` | `\n` written |
| Unbuffered | `_IONBF` | every write |

`stdout` switches from line-buffered to fully-buffered when redirected to a file or pipe. Classic trap: `printf` debug output appears out of order or disappears when piped.

```c
setvbuf(f, NULL, _IONBF, 0);  // make stream unbuffered
fflush(stdout);                // flush specific stream
fflush(NULL);                  // flush all open streams
```

Always `fflush` after critical writes to files — a crash leaves buffered data unwritten.

## `printf` and format specifiers

| Specifier | Type | Notes |
|-----------|------|-------|
| `%d` / `%i` | `int` | |
| `%u` | `unsigned int` | |
| `%ld` / `%lu` | `long` / `unsigned long` | |
| `%lld` / `%llu` | `long long` / `unsigned long long` | C99+ |
| `%zu` | `size_t` | use this, never `%d` for sizes |
| `%td` | `ptrdiff_t` | |
| `%f` | `double` | `float` promoted to `double` |
| `%s` | `char *` | null-terminated |
| `%p` | pointer | |
| `%x` / `%X` | hex | |

Wrong specifier → **undefined behavior**, not just garbage output.

```c
size_t n = 42;
printf("%d\n", n);   // UB on 64-bit — size_t is 8 bytes, int is 4
printf("%zu\n", n);  // correct
```

Width and precision: `%5d` (right-align, width 5), `%.2f` (2 decimal places), `%-10s` (left-align).

File variant: `fprintf(stderr, "error: %s\n", msg)`.

## `scanf`

`scanf` is dangerous with `%s` — no bounds checking by default:

```c
char buf[8];
scanf("%s", buf);    // reads until whitespace — stack overflow if input > 7 chars
scanf("%7s", buf);   // safe — limits to 7 chars + null terminator
```

Return value = number of items successfully matched. Check it.

`&` required because C passes by value — `scanf` needs the address to write into.

## Character I/O

```c
int c = getchar();          // reads one char from stdin, returns int (EOF is -1)
putchar('x');               // writes one char to stdout

fgets(buf, sizeof(buf), f); // reads one line — safe, includes '\n', null-terminates
// gets() — never use, no bounds checking, removed in C11
```

`fgets` stops at `\n` or `n-1` bytes, whichever comes first. The `\n` is included in the buffer.

## File I/O

```c
FILE *f = fopen("data.txt", "r");  // returns NULL on failure, errno set
if (!f) { perror("fopen"); return -1; }
fclose(f);  // always — check return value for writable files
```

**Mode strings:**

| Mode | Meaning |
|------|---------|
| `"r"` | read, file must exist |
| `"w"` | write, truncates or creates |
| `"a"` | append |
| `"r+"` | read+write, must exist |
| `"rb"` / `"wb"` | binary mode — disables newline translation |

Use binary mode for non-text files. On Unix there's no difference; on Windows `\r\n` translation happens in text mode.

### `fread` / `fwrite`

```c
size_t fread(void *ptr, size_t size, size_t count, FILE *stream);
size_t fwrite(const void *ptr, size_t size, size_t count, FILE *stream);
```

Return value = items read/written (not bytes). Short count means EOF or error.

```c
size_t n = fread(buf, 1, sizeof(buf), f);  // size=1 so return == bytes
if (n < sizeof(buf)) {
    if (feof(f))   { /* EOF */ }
    if (ferror(f)) { /* error */ }
}
```

Use `size=1` to get byte-level count. `fread(buf, 4, 10, f)` returning `7` = 28 bytes read.

`fwrite` returning less than `count` always means an error (unlike `fread` which can hit EOF).

### `fclose` return value

`fclose` flushes the write buffer. If the flush fails (disk full, network error), it returns `EOF`. **Always check it for writable files** — ignoring it is silent data loss.

```c
if (fclose(f) != 0) {
    perror("fclose");  // buffer flush failed
}
```

### `fseek` / `ftell` / `rewind`

```c
fseek(f, 0, SEEK_END);   // seek to end
long size = ftell(f);     // byte offset — returns long, not size_t
rewind(f);                // equivalent to fseek(f, 0, SEEK_SET) + clears error flag
```

`ftell` returns `long` — limited to ~2GB on 32-bit systems. Use `fseeko`/`ftello` with `off_t` for large files.

`fseek`/`ftell` is unreliable on non-regular files (pipes, stdin). Don't use it to pre-measure size when writing a generic `read_file`.

## `errno`, `perror`, `strerror`

```c
#include <errno.h>
#include <string.h>

FILE *f = fopen("missing.txt", "r");
if (!f) {
    perror("fopen");                          // "fopen: No such file or directory"
    fprintf(stderr, "%s\n", strerror(errno)); // manual equivalent
}
```

**Rules:**
1. Check `errno` immediately — the next syscall overwrites it
2. `errno` is only meaningful after a function returned an error indicator
3. Save it before calling anything else (including `fclose`) if you need it later

```c
int e = errno;
fclose(f);     // may overwrite errno
errno = e;     // restore
```

Common values: `ENOENT` (no such file), `EACCES` (permission denied), `ENOMEM` (out of memory), `EBADF` (bad file descriptor), `EINVAL` (invalid argument).

## Error propagation pattern

Standard C idiom: return `-1` or `NULL`, set `errno`, let the caller handle it.

```c
int open_config(const char *path, FILE **out) {
    *out = fopen(path, "r");
    if (!*out) return -1;  // errno already set by fopen
    return 0;
}
```

When opening multiple files, check each independently — a second `fopen` failure overwrites the first `errno`.

## Exercises

See `EXERCISES.md` — E8, E9.

1. **file_copy** — copy src to dst using `fread`/`fwrite`, 4096-byte buffer, preserve errno. `src/file_copy.c`
2. **read_file** — read entire file into heap buffer, realloc as needed, null-terminate, return size. `src/file_read.c`

## See also

- [[Strings & size_t]]
- [[Processes & Signals]]
- [[../../theory/os/Syscalls]]
