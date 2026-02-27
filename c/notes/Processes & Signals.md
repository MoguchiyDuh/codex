---
tags: [c, os]
status: stub
source: processes.c
---

# Processes & Signals

> Processes are isolated address spaces managed by the OS — signals are asynchronous notifications sent to a process by the kernel or another process.

## Processes

### What a process is — address space, file descriptors, PID

### `fork` — duplicates the calling process

```c
pid_t pid = fork();
if (pid == 0) {
    // child
} else if (pid > 0) {
    // parent, pid is child's PID
} else {
    // error
}
```

### `exec` family — replace process image

### `wait` / `waitpid` — reap a child, avoid zombies

### `exit` vs `return` from `main`

## File descriptors

### `0`, `1`, `2` — stdin, stdout, stderr

### `open`, `read`, `write`, `close` — syscall layer beneath `<stdio.h>`

### `dup2` — redirect file descriptors

## Signals

### What a signal is — async interrupt delivered to a process

### Common signals

| Signal    | Default action | Meaning                     |
| --------- | -------------- | --------------------------- |
| `SIGINT`  | Terminate      | Ctrl+C                      |
| `SIGTERM` | Terminate      | Polite kill request         |
| `SIGKILL` | Terminate      | Cannot be caught or ignored |
| `SIGSEGV` | Core dump      | Invalid memory access       |
| `SIGCHLD` | Ignore         | Child terminated            |
| `SIGALRM` | Terminate      | Timer expired               |

### `signal` — register a handler (simple, limited)

### `sigaction` — register a handler (portable, preferred)

### Signal safety — only async-signal-safe functions in handlers

### `volatile sig_atomic_t` — the correct type for a flag set in a handler

## `argc` and `argv`

### Parsing with `getopt`

## Tasks

1. **Fork and wait** — fork a child that prints its PID and exits. Parent waits and prints the child's exit status.
2. **Signal handler** — register a `SIGINT` handler that sets a `volatile sig_atomic_t` flag. Main loop checks the flag and shuts down cleanly instead of dying immediately.
3. **Pipe** — use `pipe` + `fork` to send a string from child to parent through a file descriptor.
4. **exec** — fork a child, then `execvp` to run `/bin/ls` with arguments. Parent waits and prints exit code.
5. **Alarm** — use `SIGALRM` to implement a timeout: start a slow operation and abort it after 2 seconds.

## See also

- [[Standard I/O]]
- [[../../theory/os/Processes & Threads]]
- [[../../theory/os/Syscalls]]
