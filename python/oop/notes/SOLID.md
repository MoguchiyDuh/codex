---
tags: [theory, oop, solid, design-principles]
status: complete
---

# SOLID

> Five principles for writing maintainable, extensible object-oriented code.

**Code:** `../src/solid.py`

---

## S — Single Responsibility Principle

**A class should have one reason to change.**

One class = one job. If a class handles data logic, formatting, *and* persistence, any of those three concerns changing forces you to touch the same file.

```python
# BAD — three reasons to change
class Report:
    def generate(self): ...
    def save_to_file(self): ...
    def send_email(self): ...

# GOOD — separate classes, each with one job
class Report:           # holds data
    title: str
    content: str

class ReportFormatter:  # knows how to render
    def to_html(self, report: Report) -> str: ...

class ReportExporter:   # knows how to persist
    def save(self, report: Report, path: str) -> None: ...
```

---

## O — Open/Closed Principle

**Open for extension, closed for modification.**

Add behavior by adding new code, not by editing existing code. Editing existing code risks breaking things that already work.

```python
class Discount(ABC):
    @abstractmethod
    def apply(self, price: float) -> float: ...

class PercentDiscount(Discount):
    def apply(self, price: float) -> float:
        return price * (1 - self.pct / 100)

# New discount type — no existing code touched
class BlackFridayDiscount(Discount):
    def apply(self, price: float) -> float:
        return price * 0.5
```

Strategy pattern and dependency injection are the primary tools for achieving OCP.

---

## L — Liskov Substitution Principle

**Subtypes must be substitutable for their base types.**

If `S` extends `T`, anywhere `T` is used, `S` must work correctly — same preconditions, same or weaker postconditions. No surprising behavior.

Classic violation — `Square` extends `Rectangle`:

```python
class Rectangle:
    def set_width(self, w): self.w = w
    def set_height(self, h): self.h = h
    def area(self): return self.w * self.h

class Square(Rectangle):
    def set_width(self, w):
        self.w = self.h = w   # side effect — breaks Rectangle contract

r: Rectangle = Square()
r.set_width(4)
r.set_height(5)
print(r.area())  # expected 20, got 25 — LSP violated
```

Fix: don't inherit. `Square` and `Rectangle` are separate types — composition or unrelated classes.

---

## I — Interface Segregation Principle

**Many small interfaces > one fat interface.**

Don't force clients to implement methods they don't use. A `SimplePrinter` shouldn't have to implement `fax()`.

```python
# BAD — fat interface forces unused methods
class Machine(ABC):
    @abstractmethod
    def print(self): ...
    @abstractmethod
    def scan(self): ...
    @abstractmethod
    def fax(self): ...

# GOOD — split by capability
class Printable(ABC):
    @abstractmethod
    def print(self) -> None: ...

class Scannable(ABC):
    @abstractmethod
    def scan(self) -> None: ...

class SimplePrinter(Printable):       # only implements what it supports
    def print(self) -> None: ...

class AllInOne(Printable, Scannable):
    def print(self) -> None: ...
    def scan(self) -> None: ...
```

In Python this maps naturally to Protocol or small ABCs.

---

## D — Dependency Inversion Principle

**Depend on abstractions, not concretions.**

High-level modules (business logic) should not import low-level modules (email client, DB driver) directly. Both should depend on an abstraction. This is what makes code testable.

```python
# BAD — high-level hardcodes low-level
class NotificationService:
    def notify(self, msg: str) -> None:
        EmailClient().send(msg)  # coupled, untestable

# GOOD — depend on abstraction, inject the implementation
class MessageSender(ABC):
    @abstractmethod
    def send(self, msg: str) -> None: ...

class NotificationService:
    def __init__(self, sender: MessageSender) -> None:
        self._sender = sender   # injected from outside

    def notify(self, msg: str) -> None:
        self._sender.send(msg)

svc = NotificationService(EmailSender())
svc = NotificationService(SmsSender())      # swap without touching service
svc = NotificationService(MockSender())     # inject mock in tests
```

---

## How the Principles Interact

- **SRP** keeps classes small → easier to satisfy ISP and OCP
- **OCP** is enabled by **DIP** — extend via abstractions, not by modifying concrete code
- **LSP** is a correctness constraint on inheritance — if it can't be satisfied, use composition instead (→ [[Composition vs Inheritance]])
- **ISP** prevents fat interfaces that would force LSP violations
- Together they push toward small, focused classes with injected dependencies

---

## See also

- [[OOP Pillars]]
- [[Composition vs Inheritance]]
- [[Design Patterns]]
