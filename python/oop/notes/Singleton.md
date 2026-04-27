---
tags: [python, oop, patterns, singleton]
status: complete
source: src/config_singleton.py
---

# Singleton

> Singleton enforces one shared instance, but in Python that often overlaps with simpler module-level state.

## What Singleton solves

Singleton is about controlled shared state: one registry, one coordinator, one global access point.

In the showcase, the shared object is a configuration registry. Different call sites interact with the same underlying settings store.

## Metaclass approach

The metaclass form centralizes instance control in `__call__`. The business class stays focused on its own state and operations.

That keeps singleton machinery out of the domain methods.

## Python reality

Most of the time, a module-level object is enough. Import caching already makes modules act like shared singletons.

So the right question is not "Can I implement Singleton?" but "Do I really need class-level instance control, or would a module object be clearer?"

## Main risk

Singleton introduces global mutable state. That makes testing, reset behavior, and hidden coupling harder.

Use it when shared identity is the actual requirement, not just because many callers need access to the same data.

## Source files

- `src/config_singleton.py` — metaclass-based shared config registry with stable state across re-instantiation

## See also

- [[Factory Method & Abstract Factory]]
- [[Builder]]
