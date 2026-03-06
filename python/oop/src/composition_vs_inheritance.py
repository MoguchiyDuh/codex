# Composition vs Inheritance
# "Favor composition over inheritance" — prefer has-a over is-a.


# ── Problem: deep inheritance is fragile ─────────────────────────────────────

class Animal:
    def breathe(self) -> str:
        return "breathing"

class FlyingAnimal(Animal):
    def fly(self) -> str:
        return "flying"

class SwimmingAnimal(Animal):
    def swim(self) -> str:
        return "swimming"

# What about a duck? Flies AND swims.
# Multiple inheritance creates the diamond problem in complex hierarchies.
class Duck(FlyingAnimal, SwimmingAnimal):  # works here, gets messy at scale
    pass


# ── Composition solution ─────────────────────────────────────────────────────
# Inject behavior as components. Easy to swap, test, extend.

from dataclasses import dataclass, field
from typing import Protocol

class Flyer(Protocol):
    def fly(self) -> str: ...

class Swimmer(Protocol):
    def swim(self) -> str: ...


@dataclass
class WingFlight:
    speed: float = 30.0
    def fly(self) -> str:
        return f"flying at {self.speed} km/h"

@dataclass
class JetFlight:
    speed: float = 900.0
    def fly(self) -> str:
        return f"flying at {self.speed} km/h"

@dataclass
class PaddleSwim:
    def swim(self) -> str:
        return "paddling"


@dataclass
class Bird:
    name: str
    _flyer: WingFlight = field(default_factory=WingFlight)
    _swimmer: PaddleSwim | None = None

    def fly(self) -> str:
        return self._flyer.fly()

    def swim(self) -> str:
        if self._swimmer is None:
            raise NotImplementedError(f"{self.name} can't swim")
        return self._swimmer.swim()


# Swap flight impl without touching Bird
eagle = Bird("eagle", WingFlight(speed=80))
mallard = Bird("mallard", WingFlight(speed=50), PaddleSwim())


# ── Mixin as middle ground ───────────────────────────────────────────────────
# Mixin = small, focused class that adds behavior via multiple inheritance.
# No state of its own (ideally), never instantiated alone.

class JsonMixin:
    def to_json(self) -> str:
        import json
        return json.dumps(self.__dict__)

class ReprMixin:
    def __repr__(self) -> str:
        attrs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{type(self).__name__}({attrs})"

@dataclass
class Config(JsonMixin, ReprMixin):
    host: str = "localhost"
    port: int = 8080


# ── When inheritance IS right ────────────────────────────────────────────────
# - True is-a: Dog is-a Animal (biologically fixed, not a design choice)
# - Framework base classes (Django Model, unittest.TestCase)
# - Liskov holds: subtype can fully substitute parent

if __name__ == "__main__":
    print(eagle.fly())
    print(mallard.swim())

    cfg = Config()
    print(cfg.to_json())
    print(repr(cfg))
