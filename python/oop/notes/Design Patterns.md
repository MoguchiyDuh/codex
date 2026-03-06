---
tags: [theory, oop, design-patterns]
status: complete
---

# Design Patterns

> Reusable solutions to recurring design problems — a shared vocabulary for structure.

**Code:** `../src/design_patterns.py`

---

## Creational — how objects are created

### Singleton

One instance, global access point. Useful for config, registries, connection pools.

```python
class Config:
    _instance: Config | None = None

    def __new__(cls) -> Config:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

Config() is Config()  # True
```

**Smell:** global state hides dependencies, makes testing hard. Prefer dependency injection when possible. Singleton is justified when the object represents a truly singular resource (e.g. hardware interface).

---

### Factory Method

Delegate instantiation to a function or subclass. Caller asks for an object without knowing the concrete type.

```python
def get_serializer(fmt: str) -> Serializer:
    match fmt:
        case "json": return JsonSerializer()
        case "xml":  return XmlSerializer()
        case _: raise ValueError(fmt)

s = get_serializer("json")
s.serialize({"key": "value"})
```

Keeps instantiation logic in one place. Add a new format → add one case, nothing else changes (OCP).

---

### Abstract Factory

Factory for _families_ of related objects. Instead of one factory for one type, you have a factory that produces a coordinated set. Swap the factory, get a whole different family — consistently.

```python
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button: ...
    @abstractmethod
    def create_checkbox(self) -> Checkbox: ...

class WindowsFactory(GUIFactory):
    def create_button(self) -> Button: return WindowsButton()
    def create_checkbox(self) -> Checkbox: return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button: return MacButton()
    def create_checkbox(self) -> Checkbox: return MacCheckbox()

def render_ui(factory: GUIFactory) -> None:
    btn = factory.create_button()
    chk = factory.create_checkbox()
    print(btn.render(), chk.render())

render_ui(WindowsFactory())  # [Windows Button] [Windows Checkbox]
render_ui(MacFactory())      # (Mac Button) (Mac Checkbox)
```

Key difference from Factory Method: Factory Method creates _one_ type, Abstract Factory creates _a family_. Swap one factory object → entire product family changes together.

---

### Prototype

Clone an existing configured object instead of constructing from scratch. Useful when construction is expensive, or you have a base object you want to tweak per-instance.

```python
import copy

@dataclass
class EnemyConfig:
    hp: int
    damage: int
    abilities: list[str] = field(default_factory=list)

    def clone(self) -> "EnemyConfig":
        return copy.deepcopy(self)

base_goblin = EnemyConfig(hp=30, damage=5, abilities=["bite"])
elite_goblin = base_goblin.clone()
elite_goblin.hp = 80
elite_goblin.abilities.append("poison")  # base_goblin unaffected
```

`copy.deepcopy` is Python's built-in prototype mechanism. Shallow copy (`copy.copy`) works when there are no nested mutable objects. Common in game entities, test fixtures, config templates.

---

### Builder

Construct complex objects step by step. Avoids constructors with 10 optional parameters (telescoping constructor smell).

```python
req = (HttpRequestBuilder("https://api.example.com/data")
    .method("POST")
    .header("Content-Type", "application/json")
    .body('{"x": 1}')
    .timeout(10)
    .build())
```

Each method returns `self` → fluent chaining. `.build()` validates and returns the final immutable object.

---

## Structural — how objects are composed

### Adapter

Make incompatible interfaces work together. Wraps a legacy/third-party class to match the expected interface.

```python
class LegacyPrinter:
    def print_document(self, text: str) -> None: ...  # wrong method name

class PrinterAdapter(Printer):   # Printer expects .print()
    def __init__(self, legacy: LegacyPrinter) -> None:
        self._legacy = legacy

    def print(self, text: str) -> None:
        self._legacy.print_document(text)  # translates the call
```

Adapter doesn't change either class — it's a translation layer between them.

---

### Decorator

Add behavior to an object without subclassing. Wraps the original, calls through to it, adds before/after logic.

```python
class UpperCaseDecorator(TextProcessor):
    def __init__(self, wrapped: TextProcessor) -> None:
        self._wrapped = wrapped

    def process(self, text: str) -> str:
        return self._wrapped.process(text).upper()

# Stack decorators — outermost runs first
processor = UpperCaseDecorator(TrimDecorator(PlainText()))
processor.process("  hello world  ")  # "HELLO WORLD"
```

Each decorator is unaware of others. Python's `@functools.lru_cache`, `@dataclass` are decorator pattern examples in stdlib.

---

### Facade

Simplified interface to a complex subsystem. Hides internal coordination from the caller.

```python
class ShopFacade:
    def purchase(self, token: str, item: str, price: float) -> str:
        if not self._auth.authenticate(token):
            return "unauthorized"
        order_id = self._orders.create_order(item)
        if not self._payment.charge(order_id, price):
            return "payment failed"
        return f"order {order_id} confirmed"
```

Caller does `shop.purchase(...)` — doesn't know about `AuthService`, `OrderService`, `PaymentService`. The subsystem can be refactored freely without changing callers.

---

## Behavioral — how objects communicate

### Observer

Subscribe to events, get notified when state changes. Decouples producer from consumers.

```python
emitter = EventEmitter()
emitter.on("login", lambda user: print(f"logged in: {user}"))
emitter.on("login", audit_log)  # multiple subscribers on the same event

emitter.emit("login", "kirill")  # notifies all
```

Used everywhere: UI event systems, Django signals, asyncio, game engines, reactive streams.

---

### Strategy

Swap algorithms at runtime without changing the caller.

```python
class Sorter:
    def __init__(self, strategy: SortStrategy) -> None:
        self._strategy = strategy

    def sort(self, data: list) -> list:
        return self._strategy(data)

fast = Sorter(builtin_sort)
slow = Sorter(bubble_sort)
```

In Python, strategies are often just callables — no need for a Strategy ABC unless the interface is complex. This is OCP in practice.

---

### Command

Encapsulate a request as an object. Enables undo, queuing, logging, replay.

```python
class InsertCommand(Command):
    def execute(self) -> None:
        self._editor.text += self._text

    def undo(self) -> None:
        self._editor.text = self._editor.text[: -len(self._text)]

editor.execute(InsertCommand(editor, "hello"))
editor.execute(InsertCommand(editor, " world"))
editor.undo()   # removes " world"
```

History stack = list of executed commands. Undo = pop and call `.undo()`. Redo = re-execute.

---

### Iterator

Sequential access without exposing internal structure. Python builds this in via `__iter__` / `__next__`.

```python
class CountUp:
    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.current = 0

    def __iter__(self): return self

    def __next__(self) -> int:
        if self.current >= self.limit:
            raise StopIteration
        self.current += 1
        return self.current

list(CountUp(5))  # [1, 2, 3, 4, 5]
```

Generator functions (`yield`) are sugar for the iterator protocol and cover most use cases.

---

## Anti-patterns

**God Object** — one class that knows and does everything. Violates SRP, impossible to test, impossible to reuse. Split by responsibility.

**Singleton Abuse** — using Singleton for things that aren't truly global (e.g. a service per request). Global state is hidden coupling. Prefer passing dependencies explicitly (DIP).

**Premature Abstraction** — adding Factory/Strategy/Observer for a single implementation. Add patterns when variation _actually exists_, not in anticipation of it.

---

## See also

- [[SOLID]]
- [[Composition vs Inheritance]]
- [[OOP Pillars]]
