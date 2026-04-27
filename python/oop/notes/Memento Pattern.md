---
tags: [python, oop, patterns, memento]
status: complete
source: src/editor_memento.py
---

# Memento Pattern

> Memento captures object state as a snapshot so a caretaker can restore it later without reaching into the object's internals.

## Three roles

The pattern only makes sense when the responsibilities stay separated:

- originator — the object whose state matters
- memento — the snapshot value
- caretaker — the history manager

The caretaker stores snapshots but does not interpret or mutate their internal contents.

## Why it exists

Memento is the classic undo pattern when the main concern is restoring state, not replaying commands.

That is the contrast with the command-based editor showcase. Command undo stores procedural reversal logic. Memento undo stores snapshots of state.

## Encapsulation benefit

Without mementos, outside code often starts poking at internal fields directly to implement history.

With mementos, the originator remains the only object that truly knows how to save and restore itself.

## Tradeoff

Memento is simple when state is small and copyable. It can become memory-heavy when snapshots are large or frequent.

That is why command history and memento history are not interchangeable. One stores actions; the other stores state.

## Source files

- `src/editor_memento.py` — editor snapshots plus caretaker-managed undo stack

## See also

- [[Strategy, Command & Observer]]
- [[Python OOP Basics]]
