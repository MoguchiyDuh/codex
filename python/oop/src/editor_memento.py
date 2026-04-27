from __future__ import annotations

from dataclasses import dataclass


def _validate_text(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError("text must be a string")
    return value


@dataclass(frozen=True)
class EditorMemento:
    text: str


class Editor:
    def __init__(self, text: str = "") -> None:
        self._text = _validate_text(text)

    @property
    def text(self) -> str:
        return self._text

    def write(self, chunk: str) -> None:
        self._text += _validate_text(chunk)

    def replace(self, text: str) -> None:
        self._text = _validate_text(text)

    def save(self) -> EditorMemento:
        return EditorMemento(self._text)

    def restore(self, memento: EditorMemento) -> None:
        if not isinstance(memento, EditorMemento):
            raise TypeError("memento must be an EditorMemento")
        self._text = memento.text


class History:
    def __init__(self) -> None:
        self._undo_stack: list[EditorMemento] = []

    def backup(self, memento: EditorMemento) -> None:
        self._undo_stack.append(memento)

    def undo(self) -> EditorMemento | None:
        if not self._undo_stack:
            return None
        return self._undo_stack.pop()


if __name__ == "__main__":
    editor = Editor()
    history = History()

    print("=== Editing ===")
    editor.write("Hello")
    history.backup(editor.save())
    print(editor.text)

    editor.write(", world")
    history.backup(editor.save())
    print(editor.text)

    editor.replace("Goodbye")
    print(editor.text)

    print("\n=== Undo via mementos ===")
    snapshot = history.undo()
    if snapshot is not None:
        editor.restore(snapshot)
        print(editor.text)

    snapshot = history.undo()
    if snapshot is not None:
        editor.restore(snapshot)
        print(editor.text)

    print("\n=== Empty history ===")
    print(history.undo())
