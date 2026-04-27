---
tags: [python, oop, patterns, behavioral]
status: complete
source: src/editor_behaviors.py
---

# Strategy, Command & Observer

> These three behavioral patterns answer three different questions: how to swap behavior, how to represent an action, and how to notify interested parties.

## Strategy

Strategy extracts an algorithm behind a stable interface so behavior can change without conditionals spread through the client.

In the editor showcase, formatting is the strategy boundary. Uppercase, lowercase, and title case all solve the same problem through interchangeable objects.

The value is runtime substitution, not just moving code into more classes.

## Command

Command turns an action into an object.

That matters when actions need to be stored, sequenced, retried, logged, or undone. In the editor example, append, clear, and replace all become explicit objects with `execute()` and `undo()`.

Once actions are objects, a `CommandManager` can own history rather than the editor itself.

## Observer

Observer decouples state change from reaction.

The editor changes text. Observers decide what to do with that fact. One prints, another tracks counts, another records history.

That keeps the editor from knowing every secondary concern attached to text changes.

## Why these patterns fit together

The editor example works because each pattern owns a different dimension:

- Strategy controls formatting behavior
- Command controls mutation workflow and undo
- Observer controls side effects after mutation

When patterns solve different problems, combining them is clean. When they overlap, combining them usually means overengineering.

## Source files

- `src/editor_behaviors.py` — runtime formatting strategies, undoable commands, and subscribed observers

## See also

- [[Memento Pattern]]
- [[Abstract Classes vs Protocols]]
