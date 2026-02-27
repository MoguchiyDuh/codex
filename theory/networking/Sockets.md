---
tags: [theory, networking, sockets]
status: stub
---

# Sockets

> The OS API for network communication — how connections actually work at the code level.

## What a socket is

### File descriptor that represents a network endpoint

### IP address + port = endpoint

## Socket types

### Stream socket (SOCK_STREAM) — TCP

### Datagram socket (SOCK_DGRAM) — UDP

### Unix domain socket — IPC on same machine

## Server lifecycle

### `socket()` → `bind()` → `listen()` → `accept()` → `read()`/`write()` → `close()`

## Client lifecycle

### `socket()` → `connect()` → `read()`/`write()` → `close()`

## Blocking vs non-blocking sockets

## I/O multiplexing

### `select()`, `poll()`, `epoll()` — handling many connections at once

## See also

- [[TCP vs UDP]]
- [[../os/Syscalls|Syscalls]]
- [[../os/Processes & Threads|Processes & Threads]]
