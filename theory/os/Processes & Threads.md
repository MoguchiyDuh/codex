---
tags: [theory, os, processes, threads]
status: stub
---

# Processes & Threads

> The OS units of execution — isolated programs vs lightweight execution paths within them.

## Process

### What it is: program in execution

### PCB (Process Control Block) — what the OS tracks

### Process memory layout: text, data, stack, heap

### Isolation — separate address spaces

## Thread

### Lightweight process — shares address space with siblings

### What threads share vs what's per-thread (stack, registers, PC)

### Kernel threads vs user threads

## Context switching

### What gets saved/restored

### Cost — why it's not free

## User space vs kernel space

## Process states: running, ready, blocked, zombie

## Creation: `fork()` / `exec()` on Unix

## See also

- [[Scheduling]]
- [[Virtual Memory]]
- [[../concurrency/Race Conditions & Atomicity|Race Conditions & Atomicity]]
- [[../networking/Sockets|Sockets]]
