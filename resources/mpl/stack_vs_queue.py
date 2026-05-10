"""Generates resources/pictures/stack_vs_queue.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "stack_vs_queue.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
BLUE = _COL["blue"]
GREEN = _COL["green"]
RED = _COL["red"]
WHITE = _COL["white"]

CELL_W = 0.72
CELL_H = 0.50


def _cell(ax: plt.Axes, x: float, y: float, label: str, color: str) -> None:
    ax.add_patch(
        Rectangle(
            (x, y), CELL_W, CELL_H, facecolor=color, edgecolor=BLACK, linewidth=LW
        )
    )
    ax.text(
        x + CELL_W / 2,
        y + CELL_H / 2,
        label,
        ha="center",
        va="center",
        fontsize=_FS["body"],
        color=BLACK,
    )


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 4.5)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.text(2.1, 3.95, "Stack: LIFO", ha="center", fontsize=_FS["title"], color=BLACK)
    for i, label in enumerate(["A", "B", "C"]):
        _cell(ax, 1.75, 1.0 + i * CELL_H, label, BLUE if i < 2 else RED)
    ax.add_patch(
        FancyArrowPatch(
            (2.1, 3.1),
            (2.1, 2.6),
            arrowstyle="-|>",
            mutation_scale=14,
            linewidth=LW,
            color=RED,
        )
    )
    ax.text(2.1, 3.22, "push/pop", ha="center", fontsize=_FS["body"], color=RED)
    ax.text(6.7, 3.95, "Queue: FIFO", ha="center", fontsize=_FS["title"], color=BLACK)
    xs = [5.2, 5.95, 6.7, 7.45]
    for x, label in zip(xs, ["A", "B", "C", ""], strict=True):
        _cell(ax, x, 1.7, label, GREEN if label else WHITE)
    ax.add_patch(
        FancyArrowPatch(
            (4.65, 1.95),
            (5.2, 1.95),
            arrowstyle="-|>",
            mutation_scale=14,
            linewidth=LW,
            color=RED,
        )
    )
    ax.add_patch(
        FancyArrowPatch(
            (8.17, 1.95),
            (8.75, 1.95),
            arrowstyle="-|>",
            mutation_scale=14,
            linewidth=LW,
            color=RED,
        )
    )
    ax.text(4.6, 2.28, "dequeue", ha="center", fontsize=_FS["body"], color=RED)
    ax.text(8.45, 2.28, "enqueue", ha="center", fontsize=_FS["body"], color=RED)
    ax.text(
        4.5,
        0.35,
        "restricted access gives O(1) operations at designated ends",
        ha="center",
        fontsize=_FS["body"],
        color=GRAY,
    )


def main() -> None:
    plt.rcParams.update(
        {
            "figure.facecolor": _CFG["figure"]["facecolor"],
            "font.family": _CFG["font"]["family"],
            "font.sans-serif": _CFG["font"]["sans_serif"],
        }
    )
    fig, ax = plt.subplots(figsize=(8.5, 4.2), layout="constrained")
    fig.suptitle("Stack vs Queue", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
