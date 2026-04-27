from __future__ import annotations

from threading import Lock


class SingletonMeta(type):
    _instances: dict[type, object] = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class ConfigRegistry(metaclass=SingletonMeta):
    def __init__(self) -> None:
        if hasattr(self, "_settings"):
            return
        self._settings: dict[str, str] = {}

    def set(self, key: str, value: str) -> None:
        self._settings[self._normalize(key, "key")] = self._normalize(value, "value")

    def get(self, key: str, default: str | None = None) -> str | None:
        return self._settings.get(self._normalize(key, "key"), default)

    def all(self) -> dict[str, str]:
        return dict(self._settings)

    @staticmethod
    def _normalize(value: str, field_name: str) -> str:
        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be a string")
        normalized = value.strip()
        if not normalized:
            raise ValueError(f"{field_name} must not be empty")
        return normalized


if __name__ == "__main__":
    print("=== Shared singleton instance ===")
    config_a = ConfigRegistry()
    config_b = ConfigRegistry()

    config_a.set("db_url", "postgres://localhost:5432/app")
    config_b.set("env", "development")

    print(f"Same object: {config_a is config_b}")
    print(f"db_url via config_b: {config_b.get('db_url')}")
    print(f"All settings: {config_a.all()}")

    print("\n=== Re-instantiation does not reset state ===")
    config_c = ConfigRegistry()
    print(f"env via config_c: {config_c.get('env')}")

    print("\n=== Validation ===")
    try:
        config_a.set(" ", "value")
    except ValueError as exc:
        print(f"Invalid key: {exc}")
