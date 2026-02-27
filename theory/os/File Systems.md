---
tags: [theory, os, file-systems, inodes]
status: stub
---

# File Systems

> How the OS organizes and stores data on disk.

## Abstraction: files and directories

## Inodes

### What an inode stores (metadata, not name)

### Hard links vs soft links

## Directory structure

### Directory as a mapping of name → inode number

## File descriptors

### Per-process table of open files

### stdin (0), stdout (1), stderr (2)

### `open()`, `read()`, `write()`, `close()`

## Common file systems

### ext4, NTFS, FAT32, APFS

## Journaling — crash consistency

## Disk layout: superblock, inode table, data blocks

## See also

- [[Syscalls]]
- [[Virtual Memory]]
- [[Processes & Threads]]
