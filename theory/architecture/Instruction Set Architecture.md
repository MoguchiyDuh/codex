---
tags: [theory, architecture, isa, risc, cisc]
status: stub
---

# Instruction Set Architecture

> The contract between software and hardware — what instructions the CPU understands.

## What an ISA defines

### Instruction format and encoding

### Register set

### Addressing modes

### Memory model

## Instruction types

### Data transfer: MOV, LOAD, STORE

### Arithmetic/logic: ADD, SUB, AND, OR, SHL

### Control flow: JMP, JZ, CALL, RET

### Comparison: CMP, TEST

## Addressing modes

### Immediate — value in the instruction itself

### Register — operand is a register

### Direct — operand is a memory address

### Indirect — register holds the address

### Indexed — base + offset

## RISC vs CISC

| | RISC | CISC |
|---|---|---|
| Instructions | Few, simple, fixed-width | Many, complex, variable-width |
| Cycles per instr | 1 (usually) | Variable |
| Examples | ARM, RISC-V, MIPS | x86, x86-64 |
| Load/store | Only way to access memory | Instructions can address memory directly |

## x86-64 registers

### General: rax, rbx, rcx, rdx, rsi, rdi, r8–r15

### Special: rsp (stack pointer), rbp (base pointer), rip (instruction pointer)

### Calling convention — which registers are caller/callee saved

## See also

- [[CPU Architecture]]
- [[Pipelining]]
