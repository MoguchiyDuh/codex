# Design Patterns — Creational, Structural, Behavioral

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Callable

# ════════════════════════════════════════════════════════════════════════════
# CREATIONAL
# ════════════════════════════════════════════════════════════════════════════

# ── Singleton ────────────────────────────────────────────────────────────────
# One instance, global access. Use sparingly — hides dependencies.


class Config:
    _instance: Config | None = None

    def __new__(cls) -> Config:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.debug = False
        return cls._instance


# Config() is Config()  → True


# ── Factory Method ───────────────────────────────────────────────────────────
# Delegate instantiation to subclasses / factory functions.


class Serializer(ABC):
    @abstractmethod
    def serialize(self, data: dict) -> str: ...


class JsonSerializer(Serializer):
    def serialize(self, data: dict) -> str:
        import json

        return json.dumps(data)


class XmlSerializer(Serializer):
    def serialize(self, data: dict) -> str:
        pairs = "".join(f"<{k}>{v}</{k}>" for k, v in data.items())
        return f"<root>{pairs}</root>"


def get_serializer(fmt: str) -> Serializer:
    match fmt:
        case "json":
            return JsonSerializer()
        case "xml":
            return XmlSerializer()
        case _:
            raise ValueError(f"unknown format: {fmt}")


# ── Abstract Factory ─────────────────────────────────────────────────────────
# Factory for families of related objects. Swap the factory, get a consistent set.


class Button(ABC):
    @abstractmethod
    def render(self) -> str: ...


class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str: ...


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button: ...
    @abstractmethod
    def create_checkbox(self) -> Checkbox: ...


class WindowsButton(Button):
    def render(self) -> str:
        return "[Windows Button]"


class WindowsCheckbox(Checkbox):
    def render(self) -> str:
        return "[Windows Checkbox]"


class MacButton(Button):
    def render(self) -> str:
        return "(Mac Button)"


class MacCheckbox(Checkbox):
    def render(self) -> str:
        return "(Mac Checkbox)"


class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


def render_ui(factory: GUIFactory) -> None:
    btn = factory.create_button()
    chk = factory.create_checkbox()
    print(btn.render(), chk.render())


# render_ui(WindowsFactory())  →  [Windows Button] [Windows Checkbox]
# render_ui(MacFactory())      →  (Mac Button) (Mac Checkbox)


# ── Prototype ────────────────────────────────────────────────────────────────
# Clone an existing object instead of constructing from scratch.
# Useful when construction is expensive and you have a configured base to copy from.

import copy


@dataclass
class EnemyConfig:
    hp: int
    damage: int
    speed: float
    abilities: list[str] = field(default_factory=list)

    def clone(self) -> "EnemyConfig":
        return copy.deepcopy(self)


# Define once, clone and tweak
base_goblin = EnemyConfig(hp=30, damage=5, speed=1.2, abilities=["bite"])
elite_goblin = base_goblin.clone()
elite_goblin.hp = 80
elite_goblin.abilities.append("poison")  # doesn't affect base_goblin


# ── Builder ──────────────────────────────────────────────────────────────────
# Construct complex objects step by step. Avoids telescoping constructors.


@dataclass
class HttpRequest:
    url: str
    method: str = "GET"
    headers: dict[str, str] = field(default_factory=dict)
    body: str | None = None
    timeout: int = 30


class HttpRequestBuilder:
    def __init__(self, url: str) -> None:
        self._req = HttpRequest(url=url)

    def method(self, m: str) -> HttpRequestBuilder:
        self._req.method = m
        return self

    def header(self, k: str, v: str) -> HttpRequestBuilder:
        self._req.headers[k] = v
        return self

    def body(self, b: str) -> HttpRequestBuilder:
        self._req.body = b
        return self

    def timeout(self, t: int) -> HttpRequestBuilder:
        self._req.timeout = t
        return self

    def build(self) -> HttpRequest:
        return self._req


# ════════════════════════════════════════════════════════════════════════════
# STRUCTURAL
# ════════════════════════════════════════════════════════════════════════════

# ── Adapter ──────────────────────────────────────────────────────────────────
# Make incompatible interfaces work together.


class LegacyPrinter:
    def print_document(self, text: str) -> None:
        print(f"[legacy] {text}")


class Printer(ABC):
    @abstractmethod
    def print(self, text: str) -> None: ...


class PrinterAdapter(Printer):
    def __init__(self, legacy: LegacyPrinter) -> None:
        self._legacy = legacy

    def print(self, text: str) -> None:
        self._legacy.print_document(text)


# ── Decorator ────────────────────────────────────────────────────────────────
# Add behavior without subclassing. Wraps the original object.


class TextProcessor(ABC):
    @abstractmethod
    def process(self, text: str) -> str: ...


class PlainText(TextProcessor):
    def process(self, text: str) -> str:
        return text


class UpperCaseDecorator(TextProcessor):
    def __init__(self, wrapped: TextProcessor) -> None:
        self._wrapped = wrapped

    def process(self, text: str) -> str:
        return self._wrapped.process(text).upper()


class TrimDecorator(TextProcessor):
    def __init__(self, wrapped: TextProcessor) -> None:
        self._wrapped = wrapped

    def process(self, text: str) -> str:
        return self._wrapped.process(text).strip()


# Stack decorators: trim → upper → plain
# processor = UpperCaseDecorator(TrimDecorator(PlainText()))


# ── Facade ───────────────────────────────────────────────────────────────────
# Simplified interface to a complex subsystem.


class AuthService:
    def authenticate(self, token: str) -> bool:
        return token == "valid"


class OrderService:
    def create_order(self, item: str) -> int:
        return 42  # order id


class PaymentService:
    def charge(self, order_id: int, amount: float) -> bool:
        return True


class ShopFacade:
    def __init__(self) -> None:
        self._auth = AuthService()
        self._orders = OrderService()
        self._payment = PaymentService()

    def purchase(self, token: str, item: str, price: float) -> str:
        if not self._auth.authenticate(token):
            return "unauthorized"
        order_id = self._orders.create_order(item)
        if not self._payment.charge(order_id, price):
            return "payment failed"
        return f"order {order_id} confirmed"


# ════════════════════════════════════════════════════════════════════════════
# BEHAVIORAL
# ════════════════════════════════════════════════════════════════════════════

# ── Observer ─────────────────────────────────────────────────────────────────
# Pub/sub — notify subscribers when state changes.


class EventEmitter:
    def __init__(self) -> None:
        self._listeners: dict[str, list[Callable]] = {}

    def on(self, event: str, cb: Callable) -> None:
        self._listeners.setdefault(event, []).append(cb)

    def emit(self, event: str, *args) -> None:
        for cb in self._listeners.get(event, []):
            cb(*args)


# ── Strategy ─────────────────────────────────────────────────────────────────
# Swap algorithms at runtime. Open/Closed in practice.

SortStrategy = Callable[[list], list]


def bubble_sort(data: list) -> list:
    d = data[:]
    for i in range(len(d)):
        for j in range(len(d) - i - 1):
            if d[j] > d[j + 1]:
                d[j], d[j + 1] = d[j + 1], d[j]
    return d


def builtin_sort(data: list) -> list:
    return sorted(data)


class Sorter:
    def __init__(self, strategy: SortStrategy) -> None:
        self._strategy = strategy

    def sort(self, data: list) -> list:
        return self._strategy(data)


# ── Command ──────────────────────────────────────────────────────────────────
# Encapsulate a request as an object. Enables undo, queuing, logging.


class Command(ABC):
    @abstractmethod
    def execute(self) -> None: ...
    @abstractmethod
    def undo(self) -> None: ...


class TextEditor:
    def __init__(self) -> None:
        self.text = ""
        self._history: list[Command] = []

    def execute(self, cmd: Command) -> None:
        cmd.execute()
        self._history.append(cmd)

    def undo(self) -> None:
        if self._history:
            self._history.pop().undo()


class InsertCommand(Command):
    def __init__(self, editor: TextEditor, text: str) -> None:
        self._editor = editor
        self._text = text

    def execute(self) -> None:
        self._editor.text += self._text

    def undo(self) -> None:
        self._editor.text = self._editor.text[: -len(self._text)]


if __name__ == "__main__":
    # Factory
    s = get_serializer("json")
    print(s.serialize({"a": 1}))

    # Abstract Factory
    render_ui(WindowsFactory())
    render_ui(MacFactory())

    # Prototype
    base = EnemyConfig(hp=30, damage=5, speed=1.2, abilities=["bite"])
    elite = base.clone()
    elite.hp = 80
    elite.abilities.append("poison")
    print(base, elite)

    # Builder
    req = (
        HttpRequestBuilder("https://api.example.com/data")
        .method("POST")
        .header("Content-Type", "application/json")
        .body('{"x": 1}')
        .build()
    )
    print(req)

    # Facade
    shop = ShopFacade()
    print(shop.purchase("valid", "book", 19.99))

    # Observer
    emitter = EventEmitter()
    emitter.on("login", lambda u: print(f"user logged in: {u}"))
    emitter.emit("login", "kirill")

    # Command + undo
    editor = TextEditor()
    editor.execute(InsertCommand(editor, "hello"))
    editor.execute(InsertCommand(editor, " world"))
    print(editor.text)  # hello world
    editor.undo()
    print(editor.text)  # hello
