from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


def _normalize_text(value: str, field_name: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be a string")

    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{field_name} must not be empty")
    return normalized


@dataclass(frozen=True)
class Request:
    url: str
    method: str
    headers: dict[str, str] = field(default_factory=dict)
    payload: Any = None
    timeout_seconds: int = 10


class RequestBuilder:
    _ALLOWED_METHODS = {"GET", "POST", "PUT", "PATCH", "DELETE"}

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> RequestBuilder:
        self._url: str | None = None
        self._method = "GET"
        self._headers: dict[str, str] = {}
        self._payload: Any = None
        self._timeout_seconds = 10
        return self

    def set_url(self, url: str) -> RequestBuilder:
        normalized = _normalize_text(url, "url")
        if not normalized.startswith(("http://", "https://")):
            raise ValueError("url must start with http:// or https://")
        self._url = normalized
        return self

    def set_method(self, method: str) -> RequestBuilder:
        normalized = _normalize_text(method, "method").upper()
        if normalized not in self._ALLOWED_METHODS:
            raise ValueError(f"method must be one of {sorted(self._ALLOWED_METHODS)}")
        self._method = normalized
        return self

    def add_header(self, key: str, value: str) -> RequestBuilder:
        self._headers[_normalize_text(key, "header key")] = _normalize_text(
            value, "header value"
        )
        return self

    def set_payload(self, payload: Any) -> RequestBuilder:
        self._payload = payload
        return self

    def set_timeout(self, timeout_seconds: int) -> RequestBuilder:
        if isinstance(timeout_seconds, bool) or not isinstance(timeout_seconds, int):
            raise TypeError("timeout_seconds must be an integer")
        if timeout_seconds <= 0:
            raise ValueError("timeout_seconds must be greater than 0")
        self._timeout_seconds = timeout_seconds
        return self

    def build(self) -> Request:
        if self._url is None:
            raise ValueError("url must be set before build()")

        request = Request(
            url=self._url,
            method=self._method,
            headers=dict(self._headers),
            payload=self._payload,
            timeout_seconds=self._timeout_seconds,
        )
        self.reset()
        return request


if __name__ == "__main__":
    builder = RequestBuilder()

    print("=== Build request ===")
    request = (
        builder.set_url("https://api.example.com/v1/orders")
        .set_method("post")
        .add_header("Authorization", "Bearer secret-token")
        .add_header("Content-Type", "application/json")
        .set_payload({"sku": "BOOK-001", "qty": 2})
        .set_timeout(5)
        .build()
    )
    print(request)

    print("\n=== Builder reset after build ===")
    second_request = builder.set_url("https://api.example.com/v1/ping").build()
    print(second_request)

    print("\n=== Validation ===")
    try:
        RequestBuilder().set_method("TRACE")
    except ValueError as exc:
        print(f"Invalid method: {exc}")

    try:
        RequestBuilder().build()
    except ValueError as exc:
        print(f"Missing URL: {exc}")
