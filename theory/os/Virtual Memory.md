---
tags: [theory, os, virtual-memory, paging]
status: stub
---

# Virtual Memory

> Each process gets its own address space — the OS and hardware map it to physical RAM.

## Why virtual memory

### Isolation between processes

### More address space than physical RAM

## Paging

### Pages and frames

### Page table — maps virtual page → physical frame

### Page table entry: present bit, dirty bit, access bit

## TLB (Translation Lookaside Buffer)

### Cache for page table entries

### TLB miss — what happens

## Page faults

### Minor (page not yet mapped)

### Major (page swapped to disk)

## Swapping / demand paging

## Address space layout

### Text, data, BST, heap, stack segments

### ASLR (Address Space Layout Randomization)

## See also

- [[Processes & Threads]]
- [[../computing/Stack vs Heap|Stack vs Heap]]
- [[File Systems]]
