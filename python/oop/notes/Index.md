---
tags: [python, oop]
status: complete
---

# Python OOP

> Python OOP notes — object design, contracts, and design patterns grounded in showcase files under `src/`.

## Core OOP

- [[Python OOP Basics]] — classes, inheritance, composition, properties, state transitions, useful dunder methods
- [[Abstract Classes vs Protocols]] — `abc.ABC` vs `typing.Protocol`, nominal vs structural typing, when to use each

## Creational Patterns

- [[Factory Method & Abstract Factory]] — one product vs family of related products, consistency boundaries
- [[Builder]] — stepwise construction for complex objects with many optional parts
- [[Singleton]] — shared instance control, why Python modules often cover the same use case

## Structural Patterns

- [[Adapter & Proxy]] — interface translation, access control, lazy initialization
- [[Decorator Pattern]] — runtime behavior stacking via object wrappers, not `@decorator` syntax

## Behavioral Patterns

- [[Strategy, Command & Observer]] — pluggable behavior, undoable actions, event subscribers
- [[Memento Pattern]] — originator snapshots and caretaker-managed undo history

## See also

- [[../ROADMAP|ROADMAP]]
