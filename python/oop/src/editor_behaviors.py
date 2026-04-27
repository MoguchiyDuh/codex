from abc import ABC, abstractmethod


def _validate_text(value: str, field_name: str = "text") -> str:
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be a string")
    return value


class TextFormatter(ABC):
    @abstractmethod
    def format(self, text: str) -> str: ...


class UppercaseFormatter(TextFormatter):
    def format(self, text: str) -> str:
        return text.upper()


class LowercaseFormatter(TextFormatter):
    def format(self, text: str) -> str:
        return text.lower()


class TitleFormatter(TextFormatter):
    def format(self, text: str) -> str:
        return text.title()


class Observer(ABC):
    @abstractmethod
    def update(self, event: str, editor: "Editor") -> None: ...


class Editor:
    def __init__(self, text: str = "") -> None:
        self._text = _validate_text(text)
        self._formatter: TextFormatter = UppercaseFormatter()
        self._observers: list[Observer] = []

    @property
    def text(self) -> str:
        return self._text

    def append(self, text: str) -> None:
        self._text += _validate_text(text)
        self._notify("append")

    def clear(self) -> None:
        self._text = ""
        self._notify("clear")

    def replace(self, text: str) -> None:
        self._text = _validate_text(text)
        self._notify("replace")

    def set_formatter(self, formatter: TextFormatter) -> None:
        if not isinstance(formatter, TextFormatter):
            raise TypeError("formatter must implement TextFormatter")
        self._formatter = formatter

    def formatted_text(self) -> str:
        return self._formatter.format(self.text)

    def subscribe(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def _notify(self, event: str) -> None:
        for observer in self._observers:
            observer.update(event, self)


class Command(ABC):
    @abstractmethod
    def execute(self) -> None: ...

    @abstractmethod
    def undo(self) -> None: ...


class AppendTextCommand(Command):
    def __init__(self, editor: Editor, text: str) -> None:
        self._editor = editor
        self._text = text
        self._previous_text = ""

    def execute(self) -> None:
        self._previous_text = self._editor.text
        self._editor.append(self._text)

    def undo(self) -> None:
        self._editor.replace(self._previous_text)


class ClearTextCommand(Command):
    def __init__(self, editor: Editor) -> None:
        self._editor = editor
        self._previous_text = ""

    def execute(self) -> None:
        self._previous_text = self._editor.text
        self._editor.clear()

    def undo(self) -> None:
        self._editor.replace(self._previous_text)


class ReplaceTextCommand(Command):
    def __init__(self, editor: Editor, text: str) -> None:
        self._editor = editor
        self._text = text
        self._previous_text = ""

    def execute(self) -> None:
        self._previous_text = self._editor.text
        self._editor.replace(self._text)

    def undo(self) -> None:
        self._editor.replace(self._previous_text)


class CommandManager:
    def __init__(self) -> None:
        self._undo_stack: list[tuple[Command, str]] = []

    def run(self, command: Command) -> None:
        previous_text = command._editor.text
        command.execute()
        self._undo_stack.append((command, previous_text))

    def undo_last(self) -> None:
        if not self._undo_stack:
            return

        command, previous_text = self._undo_stack.pop()
        command._previous_text = previous_text
        command.undo()


class ConsoleLogger(Observer):
    def update(self, event: str, editor: Editor) -> None:
        print(f"[event] {event:<7} text={editor.text!r}")


class StatsObserver(Observer):
    def __init__(self) -> None:
        self.changes = 0
        self.current_length = 0

    def update(self, event: str, editor: Editor) -> None:
        self.changes += 1
        self.current_length = len(editor.text)

    def __repr__(self) -> str:
        return (
            f"StatsObserver(changes={self.changes}, "
            f"current_length={self.current_length})"
        )


class HistoryObserver(Observer):
    def __init__(self) -> None:
        self.events: list[str] = []

    def update(self, event: str, editor: Editor) -> None:
        self.events.append(event)

    def __repr__(self) -> str:
        return f"HistoryObserver(events={self.events!r})"


if __name__ == "__main__":
    editor = Editor("hello")
    manager = CommandManager()

    logger = ConsoleLogger()
    stats = StatsObserver()
    history = HistoryObserver()

    editor.subscribe(logger)
    editor.subscribe(stats)
    editor.subscribe(history)

    print("=== Strategy ===")
    editor.set_formatter(UppercaseFormatter())
    print(f"raw   : {editor.text}")
    print(f"upper : {editor.formatted_text()}")

    print("\n=== Commands + Observer notifications ===")
    manager.run(AppendTextCommand(editor, " world"))
    manager.run(ReplaceTextCommand(editor, "strategy command observer"))
    manager.run(AppendTextCommand(editor, " patterns"))
    manager.run(ClearTextCommand(editor))

    print("\n=== Undo ===")
    manager.undo_last()
    manager.undo_last()

    print(f"raw   : {editor.text}")
    print(f"upper : {editor.formatted_text()}")

    editor.set_formatter(TitleFormatter())
    print(f"title : {editor.formatted_text()}")

    editor.set_formatter(LowercaseFormatter())
    print(f"lower : {editor.formatted_text()}")

    print("\n=== Observer state ===")
    print(stats)
    print(history)
