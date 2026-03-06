---
tags: [theory, oop, interfaces, abstract-classes]
status: complete
---

# Interfaces & Abstract Classes

> Tools for defining contracts — what something does, not how.

**Code:** `../src/interfaces_abstract.py`

---

## Abstract Class (`ABC`)

Partial implementation. Mix of concrete and abstract methods. Can hold state.

```python
from abc import ABC, abstractmethod

class Logger(ABC):
    def __init__(self, prefix: str) -> None:
        self.prefix = prefix            # state — allowed

    @abstractmethod
    def write(self, msg: str) -> None: ...  # subclass must implement

    def log(self, msg: str) -> None:        # shared concrete logic
        self.write(f"[{self.prefix}] {msg}")
```

- Can't instantiate directly — `Logger("x")` raises `TypeError`
- Subclasses that don't implement all abstract methods are also abstract
- Python only has single class inheritance (but multiple ABC mixins are fine)

```python
class ConsoleLogger(Logger):
    def write(self, msg: str) -> None:
        print(msg)
```

---

## Protocol (Structural Typing)

No inheritance required. A class satisfies a Protocol if it has the right methods — like Go interfaces or C++ concepts.

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> None: ...

class Sprite:           # doesn't inherit anything
    def draw(self) -> None:
        print("drawing sprite")

def render_all(items: list[Drawable]) -> None:
    for item in items:
        item.draw()

render_all([Sprite()])  # works — Sprite is structurally Drawable
```

`@runtime_checkable` allows `isinstance(obj, Drawable)` — without it, Protocol is type-checker only.

---

## Interface vs Abstract Class

| | Abstract Class (`ABC`) | Protocol |
|---|---|---|
| State (fields) | Yes | No |
| Shared implementation | Yes | No |
| Inheritance required | Yes | No |
| Multiple "interfaces" | Via mixin ABCs | Yes, naturally |
| `isinstance` check | Always | Only with `@runtime_checkable` |

**Use ABC when:** you want to enforce a contract AND share partial implementation or state.
**Use Protocol when:** you want structural typing — caller defines the shape, no inheritance overhead.

---

## Default Methods

ABCs can provide default implementations that subclasses can override:

```python
class Serializable(ABC):
    def serialize(self) -> str:
        import json
        return json.dumps(self.__dict__)   # default — override if needed

    @abstractmethod
    def validate(self) -> bool: ...
```

---

## Duck Typing

Python's default mode. No formal interface needed — if it walks like a duck and quacks like a duck, it's a duck.

```python
def make_it_quack(duck):
    duck.quack()   # works on anything with .quack() — no type annotation needed
```

Protocol formalizes this for type checkers without changing runtime behavior.

---

## See also

- [[OOP Pillars]]
- [[SOLID]]
- [[Composition vs Inheritance]]
