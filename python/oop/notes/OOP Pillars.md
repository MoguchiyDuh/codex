---
tags: [theory, oop, pillars]
status: complete
---

# OOP Pillars

> The four core concepts that define object-oriented programming.

**Code:** `../src/pillars.py`

---

## Encapsulation

Bundle data and behavior into a single unit (class). Control what's accessible from outside.

- **Public** — accessible anywhere (`self.name`)
- **Protected** — convention-only, internal use (`self._balance`)
- **Private** — name-mangled by Python, hard to access externally (`self.__history` → `_BankAccount__history`)

Why it matters: callers depend on the interface, not the internals. You can change the implementation without breaking outside code. Invariants (e.g. balance can't go negative) are enforced in one place.

```python
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self._balance = balance
        self.__history: list[float] = []

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        self._balance += amount

    @property
    def balance(self) -> float:
        return self._balance  # read-only outside — no setter
```

---

## Abstraction

Expose *what* an object does, hide *how*. Callers work against an interface, not an implementation.

Tools: `ABC` + `@abstractmethod`. Subclasses must implement all abstract methods or instantiation fails.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...

    def describe(self) -> str:          # concrete — shared by all subclasses
        return f"area={self.area():.2f}"
```

`Shape()` raises `TypeError` — can't instantiate an abstract class directly.

---

## Inheritance

Reuse and extend behavior. Models an `is-a` relationship.

```python
class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
```

- `super().__init__(...)` — call parent constructor explicitly
- Python supports multiple inheritance (MRO via C3 linearization)
- Problems: tight coupling to parent internals, fragile base class (changing parent silently breaks subclasses), deep hierarchies become hard to reason about

---

## Polymorphism

Same interface, different behavior depending on the actual type. Python dispatches method calls at runtime based on the object's real class.

```python
shapes: list[Shape] = [Circle(5), Rectangle(3, 4)]

for s in shapes:
    print(s.describe())  # each calls its own area() / perimeter()
```

No vtable in Python — attribute lookup walks `__mro__` at runtime.

**Compile-time polymorphism** (overloading) doesn't exist in Python the same way. Use `@singledispatch` or default args instead.

**Duck typing** — Python doesn't require inheritance for polymorphism. If it has the right methods, it works:

```python
class Vector:
    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

Vector(1, 2) + Vector(3, 4)  # __add__ dispatch — no base class needed
```

---

## See also

- [[Composition vs Inheritance]]
- [[Interfaces & Abstract Classes]]
- [[SOLID]]
