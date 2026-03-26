---
tags: [c, os]
status: complete
source: fork_child.c, fork_child2.c, signals.c
---

# Processes & Signals

> Processes are isolated address spaces managed by the OS — signals are asynchronous notifications sent to a process by the kernel or another process.

## Processes

### What a process is

A process is a running program with its own isolated address space, file descriptors, PID, and state. Separate processes don't share memory — a write in one is invisible to another (unlike threads).

```c
getpid()   // current process PID
getppid()  // parent process PID
```

### `fork` — duplicate the calling process

`fork` creates an exact copy of the current process. Both processes continue from the same point. The only difference is the return value:

```c
pid_t pid = fork();

if (pid < 0) {
    perror("fork");   // failed — out of resources
} else if (pid == 0) {
    // CHILD — pid is 0
} else {
    // PARENT — pid is the child's PID
}
```

The child gets a copy of the parent's memory, file descriptors, and program counter. Copy-on-write means no physical copy happens until one side writes — `fork` is cheap. After `exec`, the copy is thrown away entirely.

### `exec` family — replace process image

`exec` replaces the calling process with a new program. PID stays the same, everything else is wiped.

```c
execvp("ls", (char *[]){"ls", "-la", NULL});
perror("execvp");   // only reached on failure
exit(1);
```

- First arg: program name (searched in `PATH`)
- Second arg: `argv` array — `argv[0]` is the program name by convention, `NULL`-terminated
- If `execvp` returns, it failed

| Function | PATH search | Args | Env |
|----------|-------------|------|-----|
| `execvp` | Yes | `char *[]` | inherited |
| `execv`  | No (full path) | `char *[]` | inherited |
| `execve` | No | `char *[]` | explicit |
| `execlp` | Yes | variadic | inherited |

**`fork` + `exec` pattern** — the Unix way to spawn a new program:

```c
pid_t pid = fork();
if (pid == 0) {
    execvp("ls", (char *[]){"ls", "-la", NULL});
    perror("execvp");
    exit(1);
}
// parent continues
```

Fork first so the parent survives. Exec in the child to replace it with the target binary. Equivalent to Python's `subprocess.run(["ls", "-la"])`.

### `wait` / `waitpid` — reap children, avoid zombies

When a child exits before the parent calls `wait`, it becomes a **zombie** — dead but holding its exit status in the kernel. Always wait for your children.

```c
int status;
wait(&status);              // blocks until ANY child exits
waitpid(pid, &status, 0);  // blocks until specific child exits
waitpid(pid, &status, WNOHANG);  // non-blocking — returns 0 if not done

if (WIFEXITED(status))
    printf("exited with %d\n", WEXITSTATUS(status));
```

To wait for N children:
```c
for (int i = 0; i < n; i++)
    wait(NULL);   // NULL if you don't need the exit status
```

### `exit` vs `return` from `main`

Both terminate the process and flush stdio buffers. `exit(0)` from anywhere, `return 0` only from `main`. In the child after `exec` fails, always use `exit` — never `return`, since you don't want to run the parent's cleanup code.

## Signals

### What a signal is

An asynchronous notification delivered to a process by the kernel or another process. The process is interrupted mid-execution, jumps to the handler, then resumes (or terminates).

### Common signals

| Signal | Default | Meaning |
|--------|---------|---------|
| `SIGINT` | terminate | Ctrl+C |
| `SIGTERM` | terminate | polite kill (`kill <pid>`) |
| `SIGKILL` | terminate | force kill — cannot be caught or ignored |
| `SIGSEGV` | core dump | segfault |
| `SIGCHLD` | ignore | child exited |
| `SIGPIPE` | terminate | write to broken pipe |
| `SIGALRM` | terminate | timer expired |

Sending a signal: `kill(pid, SIGTERM)` — despite the name, not always fatal.

### `sigaction` — install a signal handler

Always use `sigaction` over the old `signal()` — portable, explicit, doesn't reset after delivery.

```c
struct sigaction sa = {0};
sa.sa_handler = handle_sigint;  // handler function
sigemptyset(&sa.sa_mask);       // no extra signals blocked during handler
sa.sa_flags = 0;

sigaction(SIGINT, &sa, NULL);   // install for SIGINT
```

Handler signature must be `void fn(int)` — the OS requires it.

### `volatile sig_atomic_t` — the correct flag type

Signal handlers run asynchronously — they can interrupt any instruction. Two rules:

- `sig_atomic_t` — guaranteed to read/write atomically, no half-written state
- `volatile` — prevents the compiler from caching the value in a register across loop iterations

```c
static volatile sig_atomic_t running = 1;

void handle_sigint(int sig) {
    (void)sig;
    running = 0;   // set flag — that's all
}

int main(void) {
    // install handler...

    while (running) {
        printf("running...\n");
        fflush(stdout);
        sleep(1);
    }
    printf("shutdown cleanly\n");
}
```

### Signal safety

Inside a handler, you can only call **async-signal-safe** functions. Most libc functions are not — `printf` holds an internal lock; calling it from a handler while `main` holds the same lock → deadlock.

Safe in handlers: `write()`, setting a `sig_atomic_t` flag.
Unsafe: `printf`, `malloc`, `free`, most libc.

Keep handlers minimal — set a flag, let `main` do the work.

## See also

- [[Standard I_O]]
- [[../../theory/os/Processes & Threads]]
- [[../../theory/os/Syscalls]]
