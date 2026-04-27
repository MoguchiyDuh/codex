from abc import ABC, abstractmethod
from decimal import ROUND_HALF_UP, Decimal, InvalidOperation


def format_amount(amount: object) -> str:
    try:
        return f"${Decimal(str(amount)).quantize(Decimal('0.01'))}"
    except (InvalidOperation, ValueError, TypeError):
        return repr(amount)


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str: ...


class LegacyPayAPI:
    def make_payment(self, cents: int) -> str:
        return f"processed {cents} cents"


class LegacyPayAdapter(PaymentProcessor):
    def __init__(self, legacy_api: LegacyPayAPI) -> None:
        self._legacy_api = legacy_api

    def pay(self, amount: float) -> str:
        cents = self._dollars_to_cents(amount)
        legacy_result = self._legacy_api.make_payment(cents)
        return f"paid {format_amount(amount)} via legacy gateway ({legacy_result})"

    @staticmethod
    def _dollars_to_cents(amount: float) -> int:
        try:
            dollars = Decimal(str(amount))
        except InvalidOperation as exc:
            raise ValueError("amount must be numeric") from exc

        if dollars <= 0:
            raise ValueError("amount must be greater than 0")

        cents = (dollars * Decimal("100")).quantize(
            Decimal("1"), rounding=ROUND_HALF_UP
        )
        return int(cents)


class SecurePaymentService:
    def __init__(self) -> None:
        print("Initializing secure payment service...")

    def process(self, processor: PaymentProcessor, amount: float) -> str:
        return processor.pay(amount)


class PaymentProxy(PaymentProcessor):
    _ALLOWED_ROLES = {"admin", "billing"}

    def __init__(self, processor: PaymentProcessor, user_role: str) -> None:
        self._processor = processor
        self._user_role = user_role
        self._service: SecurePaymentService | None = None

    def pay(self, amount: float) -> str:
        if self._user_role not in self._ALLOWED_ROLES:
            raise PermissionError("payment access denied")

        if self._service is None:
            self._service = SecurePaymentService()

        return self._service.process(self._processor, amount)


class LoggingProxy(PaymentProcessor):
    def __init__(self, processor: PaymentProcessor) -> None:
        self._processor = processor

    def pay(self, amount: float) -> str:
        print(f"Starting payment for {format_amount(amount)}")
        result = self._processor.pay(amount)
        print(f"Finished payment: {result}")
        return result


if __name__ == "__main__":
    legacy_api = LegacyPayAPI()
    adapter = LegacyPayAdapter(legacy_api)

    blocked = PaymentProxy(adapter, "guest")
    try:
        blocked.pay(12.99)
    except PermissionError as exc:
        print(f"Unauthorized payment blocked: {exc}")

    authorized = PaymentProxy(adapter, "admin")
    print(authorized.pay(12.99))
    print(authorized.pay(5.50))

    logged = LoggingProxy(PaymentProxy(adapter, "billing"))
    print(logged.pay(3.25))
