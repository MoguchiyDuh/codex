---
tags: [python, oop, typing, interfaces]
status: complete
source: src/notifications.py
---

# Abstract Classes vs Protocols

> `ABC` gives you an explicit inheritance contract; `Protocol` gives you a structural contract based on behavior shape.

## `ABC` — nominal typing

An abstract base class says: to count as this type, you must explicitly inherit from it or be registered into that hierarchy.

That is useful when you want a controlled family of official implementations. In the notification example, `MessageSender` defines the sanctioned sender hierarchy.

The value is not just abstract methods. The value is a shared taxonomy and, when needed, shared implementation.

## `Protocol` — structural typing

A protocol says: if an object has the required methods with the expected shape, it is good enough.

That is closer to Python's duck-typing model. `SlackClient` does not inherit from `MessageSender`, but it still satisfies `SupportsSend` because it has a compatible `send()` method.

This makes protocols a better fit when you want loose coupling or want to accept third-party objects without forcing them into your hierarchy.

## When to choose which

Choose `ABC` when you want an explicit family, controlled extension points, or shared base behavior.

Choose `Protocol` when you want to describe what the client needs without forcing inheritance.

In practice, `ABC` is about ownership of a hierarchy. `Protocol` is about compatibility at the call site.

## Runtime checks are secondary

`@runtime_checkable` exists, but protocol value is still mostly design-time and type-checker-time. A runtime protocol check only tells you that the object exposes the required attribute names; it does not prove deep semantic correctness.

## Source files

- `src/notifications.py` — `MessageSender` as `ABC`, `SupportsSend` as `Protocol`, `SlackClient` as structural implementation

## See also

- [[Python OOP Basics]]
- [[Strategy, Command & Observer]]
