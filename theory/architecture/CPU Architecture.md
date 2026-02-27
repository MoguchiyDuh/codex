---
tags: [theory, architecture, cpu]
status: stub
---

# CPU Architecture

> How the CPU fetches, decodes, and executes instructions — the Von Neumann model.

## Von Neumann architecture

### Stored-program concept — instructions and data in the same memory

### Bottleneck: memory bus shared by instructions and data

## Key components

### ALU — does the math

### Control unit — orchestrates everything

### Registers — fastest storage, on-chip

### Program counter (PC) — address of next instruction

### Instruction register (IR) — currently executing instruction

### Stack pointer (SP), base pointer (BP)

## Fetch / Decode / Execute cycle

### Fetch — load instruction from memory[PC] into IR, increment PC

### Decode — control unit interprets the opcode

### Execute — ALU or memory operation

### Writeback — result stored to register or memory

## Datapath vs control path

## Harvard vs Von Neumann

### Harvard: separate instruction and data memory (used in microcontrollers)

## See also

- [[ALU]]
- [[Sequential Circuits]]
- [[Instruction Set Architecture]]
- [[Pipelining]]
- [[Memory Hierarchy]]
