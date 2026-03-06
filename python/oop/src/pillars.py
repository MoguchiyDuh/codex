# OOP Pillars — Encapsulation, Abstraction, Inheritance, Polymorphism


# ── Encapsulation ────────────────────────────────────────────────────────────
# Bundle data + behavior. Control access to internals.

class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self._balance = balance          # protected by convention
        self.__history: list[float] = [] # name-mangled → truly private-ish

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        self._balance += amount
        self.__history.append(amount)

    def withdraw(self, amount: float) -> None:
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount
        self.__history.append(-amount)

    @property
    def balance(self) -> float:
        return self._balance  # read-only outside class


# ── Abstraction ──────────────────────────────────────────────────────────────
# Expose what, hide how. Caller doesn't need to know internals.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...

    def describe(self) -> str:
        return f"{type(self).__name__}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"


# ── Inheritance ──────────────────────────────────────────────────────────────
# Reuse and extend. `is-a` relationship.

import math

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, w: float, h: float) -> None:
        self.w = w
        self.h = h

    def area(self) -> float:
        return self.w * self.h

    def perimeter(self) -> float:
        return 2 * (self.w + self.h)


# ── Polymorphism ─────────────────────────────────────────────────────────────
# Same interface, different behavior. Runtime dispatch.

shapes: list[Shape] = [Circle(5), Rectangle(3, 4), Circle(1)]

for s in shapes:
    print(s.describe())  # each calls its own area() / perimeter()


# Dunder-based polymorphism (duck typing)
class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"


if __name__ == "__main__":
    acc = BankAccount("kirill", 100)
    acc.deposit(50)
    acc.withdraw(30)
    print(acc.balance)  # 120.0

    v = Vector(1, 2) + Vector(3, 4)
    print(v)  # Vector(4, 6)
