# Interfaces & Abstract Classes
# Python has no `interface` keyword — ABC + abstractmethod is the pattern.
# Protocol is the structural-typing (duck typing) alternative.

from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable

# ── Abstract class ───────────────────────────────────────────────────────────
# Can have state, partial implementation, single inheritance.


class Logger(ABC):
    def __init__(self, prefix: str) -> None:
        self.prefix = prefix  # state allowed

    @abstractmethod
    def write(self, msg: str) -> None: ...

    def log(self, msg: str) -> None:  # concrete method shared by all subclasses
        self.write(f"[{self.prefix}] {msg}")


class ConsoleLogger(Logger):
    def write(self, msg: str) -> None:
        print(msg)


class FileLogger(Logger):
    def __init__(self, prefix: str, path: str) -> None:
        super().__init__(prefix)
        self.path = path

    def write(self, msg: str) -> None:
        with open(self.path, "a") as f:
            f.write(msg + "\n")


# ── Protocol (structural / duck typing) ─────────────────────────────────────
# No inheritance required — just implement the right methods.
# Equivalent to Go interfaces or C++ concepts.


@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> None: ...


class Sprite:
    def draw(self) -> None:
        print("drawing sprite")


class Widget:
    def draw(self) -> None:
        print("drawing widget")


class AudioClip:
    def play(self) -> None:
        print("playing audio")


def render_all(items: list[Drawable]) -> None:
    for item in items:
        item.draw()


# ── Interface vs Abstract Class ──────────────────────────────────────────────
# Use Protocol when:  you want structural typing, no shared state/logic
# Use ABC when:       you want to enforce a contract AND share partial impl


# Multiple "interfaces" via multiple Protocol inheritance
class Serializable(Protocol):
    def serialize(self) -> bytes: ...


class Versioned(Protocol):
    @property
    def version(self) -> int: ...


if __name__ == "__main__":
    logger = ConsoleLogger("INFO")
    logger.log("server started")

    drawables: list[Drawable] = [Sprite(), Widget()]
    render_all(drawables)

    # runtime_checkable lets isinstance work
    print(isinstance(Sprite(), Drawable))  # True
    print(isinstance(AudioClip(), Drawable))  # False
