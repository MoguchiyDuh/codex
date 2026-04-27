from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable


def validate_message(recipient: str, message: str) -> None:
    if not isinstance(recipient, str) or not recipient.strip():
        raise ValueError("recipient must not be empty")
    if not isinstance(message, str) or not message.strip():
        raise ValueError("message must not be empty")


class MessageSender(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> None: ...

    @abstractmethod
    def name(self) -> str: ...

    def _validate(self, recipient: str, message: str) -> None:
        validate_message(recipient, message)


class EmailSender(MessageSender):
    def send(self, recipient: str, message: str) -> None:
        self._validate(recipient, message)
        print(f"Email to {recipient}: {message}")

    def name(self) -> str:
        return "EmailSender"


class SmsSender(MessageSender):
    def send(self, recipient: str, message: str) -> None:
        self._validate(recipient, message)
        print(f"SMS to {recipient}: {message}")

    def name(self) -> str:
        return "SmsSender"


@runtime_checkable
class SupportsSend(Protocol):
    def send(self, recipient: str, message: str) -> None: ...


class SlackClient:
    def send(self, recipient: str, message: str) -> None:
        validate_message(recipient, message)
        print(f"Slack message to {recipient}: {message}")


def broadcast_via_protocol(
    sender: SupportsSend,
    recipients: list[str],
    message: str,
) -> None:
    for recipient in recipients:
        sender.send(recipient, message)


def describe_sender(sender: MessageSender) -> str:
    return f"Official sender: {sender.name()}"


if __name__ == "__main__":
    email = EmailSender()
    sms = SmsSender()
    slack = SlackClient()

    print("=== Individual sends ===")
    email.send("alice@example.com", "Hello from email")
    sms.send("+381601234567", "Hello from SMS")
    slack.send("general", "Hello from Slack")

    print("\n=== Broadcast via Protocol ===")
    recipients = ["bob@example.com", "charlie@example.com"]
    broadcast_via_protocol(email, recipients, "Broadcast email")
    broadcast_via_protocol(sms, ["+381609999999"], "Broadcast SMS")
    broadcast_via_protocol(slack, ["announcements"], "Broadcast Slack")

    print("\n=== describe_sender (ABC hierarchy only) ===")
    print(describe_sender(email))
    print(describe_sender(sms))
    # describe_sender(slack)  ← mypy/pyright would reject this at type-check time

    print("\n=== isinstance checks (runtime_checkable) ===")
    for obj in (email, sms, slack):
        print(
            f"{obj.__class__.__name__:12} satisfies SupportsSend: {isinstance(obj, SupportsSend)}"
        )

    print("\n=== Validation ===")
    try:
        email.send("", "oops")
    except ValueError as e:
        print(f"Caught: {e}")

    try:
        slack.send("general", "  ")
    except ValueError as e:
        print(f"Caught: {e}")
