from __future__ import annotations

from abc import ABC, abstractmethod


def _validate_message(message: str) -> str:
    if not isinstance(message, str):
        raise TypeError("message must be a string")
    normalized = message.strip()
    if not normalized:
        raise ValueError("message must not be empty")
    return normalized


class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> None: ...


class EmailNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"Email: {_validate_message(message)}")


class NotifierDecorator(Notifier):
    def __init__(self, wrapped: Notifier) -> None:
        self._wrapped = wrapped

    def send(self, message: str) -> None:
        self._wrapped.send(message)


class SmsDecorator(NotifierDecorator):
    def send(self, message: str) -> None:
        normalized = _validate_message(message)
        super().send(normalized)
        print(f"SMS: {normalized}")


class SlackDecorator(NotifierDecorator):
    def send(self, message: str) -> None:
        normalized = _validate_message(message)
        super().send(normalized)
        print(f"Slack: {normalized}")


class AuditDecorator(NotifierDecorator):
    def __init__(self, wrapped: Notifier) -> None:
        super().__init__(wrapped)
        self.sent_count = 0

    def send(self, message: str) -> None:
        normalized = _validate_message(message)
        self.sent_count += 1
        print(f"[audit] send #{self.sent_count}")
        super().send(normalized)


if __name__ == "__main__":
    print("=== Plain notifier ===")
    EmailNotifier().send("Build succeeded")

    print("\n=== Decorated notifier ===")
    notifier = AuditDecorator(SlackDecorator(SmsDecorator(EmailNotifier())))
    notifier.send("Deploy to staging")
    notifier.send("Deploy to production")

    print("\n=== Validation ===")
    try:
        notifier.send("   ")
    except ValueError as exc:
        print(f"Invalid message: {exc}")
