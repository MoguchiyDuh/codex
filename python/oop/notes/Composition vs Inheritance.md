---
tags: [theory, oop, composition, inheritance]
status: complete
---

# Composition vs Inheritance

> "Favor composition over inheritance" — one of the most repeated rules in OOP.

**Code:** `../src/composition_vs_inheritance.py`

---

## Inheritance Recap

`is-a` relationship. Subclass gets parent's interface and implementation for free.

```python
class FlyingAnimal(Animal):
    def fly(self) -> str: ...

class SwimmingAnimal(Animal):
    def swim(self) -> str: ...
```

**What you get:** reuse, polymorphism, `isinstance` checks.
**What you pay:**
- Tight coupling — subclass depends on parent internals
- Fragile base class — changing parent breaks subclasses silently
- Deep hierarchies — hard to follow, hard to test
- Rigid — can't swap behavior at runtime

---

## Composition

`has-a` relationship. Behavior is delegated to contained objects, injected at construction.

```python
@dataclass
class Bird:
    name: str
    _flyer: WingFlight = field(default_factory=WingFlight)
    _swimmer: PaddleSwim | None = None

    def fly(self) -> str:
        return self._flyer.fly()   # delegate to component
```

Swap behavior without touching `Bird`:

```python
eagle   = Bird("eagle", WingFlight(speed=80))
jet     = Bird("experiment", JetFlight(speed=500))  # same class, different behavior
mallard = Bird("mallard", WingFlight(speed=50), PaddleSwim())
```

**What you get:** loose coupling, easy to test (inject mocks), swappable at runtime.
**What you pay:** slightly more boilerplate — explicit delegation methods.

---

## The Diamond Problem

With multiple inheritance, method resolution becomes ambiguous:

```
     Animal
    /      \
Flying   Swimming
    \      /
      Duck
```

Python resolves via **MRO** (C3 linearization) — `Duck.__mro__` shows the lookup order. It works, but deep diamonds are a design smell. Composition avoids the problem entirely.

---

## Mixins as Middle Ground

Small, focused classes that add behavior via multiple inheritance. No state of their own (ideally), never instantiated alone.

```python
class JsonMixin:
    def to_json(self) -> str:
        import json
        return json.dumps(self.__dict__)

class ReprMixin:
    def __repr__(self) -> str:
        attrs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{type(self).__name__}({attrs})"

class Config(JsonMixin, ReprMixin):
    host: str = "localhost"
    port: int = 8080
```

Mixins are acceptable multiple inheritance because they're additive — they don't form a diamond of shared state.

---

## When Inheritance Is Actually Right

- True `is-a` that won't change: `Dog` is-a `Animal` (biological fact, not a design decision)
- Framework base classes: `django.db.models.Model`, `unittest.TestCase` — the framework owns the hierarchy
- Liskov holds: subtype is fully substitutable for the parent everywhere the parent is used
- Small, shallow hierarchy (1–2 levels)

---

## Real Example: Same Problem Both Ways

**With inheritance:**
```python
class AuthHTTPClient(HTTPClient):   # coupled to HTTPClient internals
    def get(self, url):
        self.headers["Authorization"] = self.token
        return super().get(url)
```

**With composition:**
```python
class AuthHTTPClient:
    def __init__(self, client: HTTPClient, token: str) -> None:
        self._client = client
        self._token = token

    def get(self, url: str) -> Response:
        return self._client.get(url, headers={"Authorization": self._token})
```

Composition version: swap `client` for a mock in tests, zero base class coupling.

---

## See also

- [[OOP Pillars]]
- [[SOLID]]
- [[Design Patterns]]
