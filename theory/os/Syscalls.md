---
tags: [theory, os, syscalls, kernel]
status: stub
---

# Syscalls

> The interface between user-space programs and the OS kernel.

## What a syscall is

### Crossing the user/kernel boundary

### Why not just call kernel functions directly

## How it works

### Software interrupt / `syscall` instruction

### Kernel mode switch — cost

## Common syscalls by category

### Process: `fork`, `exec`, `exit`, `wait`

### Memory: `mmap`, `brk`

### File I/O: `open`, `read`, `write`, `close`, `stat`

### Network: `socket`, `bind`, `listen`, `accept`, `connect`

### Sync: `futex`

## `errno` — how errors are reported

## Wrapper functions in libc

## Syscall cost vs function call cost

## See also

- [[Processes & Threads]]
- [[File Systems]]
- [[../networking/Sockets|Sockets]]
