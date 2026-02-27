---
tags: [c, os]
status: stub
source: wc.c
---

# Standard I/O

> C I/O is buffered by default and routed through file descriptors — `printf` and `scanf` are high-level wrappers over OS syscalls.

## Streams

### `stdin`, `stdout`, `stderr`

### Line-buffered vs fully-buffered vs unbuffered

### `fflush`

## `printf` and format specifiers

| Specifier   | Type           |
| ----------- | -------------- |
| `%d` / `%i` | `int`          |
| `%u`        | `unsigned int` |
| `%ld`       | `long`         |
| `%zu`       | `size_t`       |
| `%f`        | `double`       |
| `%s`        | `char *`       |
| `%p`        | pointer        |
| `%x` / `%X` | hex            |

### Width and precision: `%5d`, `%.2f`, `%-10s`

## `scanf`

### Why `&` is required

### Buffer overrun with `%s` — always use `%Ns`

### Return value — number of matched items

## Character I/O

### `getchar`, `putchar`

### `fgets` — safe line reading

### `gets` — never use

## File I/O

### `fopen` modes: `"r"`, `"w"`, `"a"`, `"rb"`, `"wb"`

### `fclose` — always close, check return value

### `fread` / `fwrite` — binary I/O

### `fgets` / `fputs` — text line I/O

### `feof`, `ferror`

### `rewind`, `fseek`, `ftell`

## `argc` and `argv`

### `argv[0]` is always the program name

### Parsing command-line arguments

## Tasks

1. **Word counter** — read a file from `argv[1]` and print character, word, and line counts (like `wc`). Work in `src/wc.c`.
2. **Safe scanf** — write a program that reads a name with `scanf("%49s", buf)` and prints it. Test with a 60-character input.
3. **Binary copy** — use `fread`/`fwrite` to copy a file byte-for-byte. Verify with `diff`.
4. **CSV parser** — read a CSV file line by line with `fgets`, split on `,` using `strtok`, print each field. Handle quoted fields.
5. **Hex dump** — read a file in binary mode and print each byte as two hex digits, 16 per line.

## See also

- [[Strings]]
- [[../../theory/os/Syscalls]]
- [[Processes & Signals]]
