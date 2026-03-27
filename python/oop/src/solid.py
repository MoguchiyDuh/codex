# SOLID Principles

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable

# ── S — Single Responsibility ────────────────────────────────────────────────
# One reason to change. Split concerns into separate classes.

# BAD: Report handles both data logic and formatting
# class Report:
#     def generate(self): ...
#     def save_to_file(self): ...   # different concern
#     def send_email(self): ...     # different concern again


@dataclass
class Report:
    title: str
    content: str


class ReportFormatter:
    def to_html(self, report: Report) -> str:
        return f"<h1>{report.title}</h1><p>{report.content}</p>"


class ReportExporter:
    def save(self, report: Report, path: str) -> None:
        with open(path, "w") as f:
            f.write(report.content)


# ── O — Open/Closed ──────────────────────────────────────────────────────────
# Open for extension, closed for modification.
# Add behavior by adding code, not editing existing code.


class Discount(ABC):
    @abstractmethod
    def apply(self, price: float) -> float: ...


class NoDiscount(Discount):
    def apply(self, price: float) -> float:
        return price


class PercentDiscount(Discount):
    def __init__(self, pct: float) -> None:
        self.pct = pct

    def apply(self, price: float) -> float:
        return price * (1 - self.pct / 100)


class BlackFridayDiscount(Discount):  # extend without touching existing classes
    def apply(self, price: float) -> float:
        return price * 0.5


def checkout(price: float, discount: Discount) -> float:
    return discount.apply(price)


# ── L — Liskov Substitution ──────────────────────────────────────────────────
# Subtype must be fully substitutable for base type.
# Classic violation: Square extends Rectangle (breaks setters).


class Rectangle:
    def __init__(self, w: float, h: float) -> None:
        self.w = w
        self.h = h

    def area(self) -> float:
        return self.w * self.h


# BAD — Square overrides setters, breaks Rectangle contract
# class Square(Rectangle):
#     def set_width(self, v): self.w = self.h = v  # surprising side effect


# FIX — don't inherit, use separate types or composition
@dataclass
class Square:
    side: float

    def area(self) -> float:
        return self.side**2


# ── I — Interface Segregation ────────────────────────────────────────────────
# Many small interfaces > one fat interface.
# Don't force clients to implement methods they don't use.


class Printable(ABC):
    @abstractmethod
    def print(self) -> None: ...


class Scannable(ABC):
    @abstractmethod
    def scan(self) -> None: ...


class Faxable(ABC):
    @abstractmethod
    def fax(self) -> None: ...


# Printer only implements what it supports
class SimplePrinter(Printable):
    def print(self) -> None:
        print("printing")


class AllInOne(Printable, Scannable, Faxable):
    def print(self) -> None:
        print("printing")

    def scan(self) -> None:
        print("scanning")

    def fax(self) -> None:
        print("faxing")


# ── D — Dependency Inversion ─────────────────────────────────────────────────
# Depend on abstractions, not concretions.
# High-level modules shouldn't import low-level modules directly.


class MessageSender(ABC):
    @abstractmethod
    def send(self, msg: str) -> None: ...


class EmailSender(MessageSender):
    def send(self, msg: str) -> None:
        print(f"email: {msg}")


class SmsSender(MessageSender):
    def send(self, msg: str) -> None:
        print(f"sms: {msg}")


class NotificationService:
    def __init__(self, sender: MessageSender) -> None:
        self._sender = sender  # injected — not hard-coded

    def notify(self, msg: str) -> None:
        self._sender.send(msg)


if __name__ == "__main__":
    print(checkout(100, PercentDiscount(20)))  # 80.0
    print(checkout(100, BlackFridayDiscount()))  # 50.0

    svc = NotificationService(EmailSender())
    svc.notify("deploy done")

    svc2 = NotificationService(SmsSender())
    svc2.notify("alert: disk full")
