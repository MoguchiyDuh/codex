"""Generates resources/pictures/radix_sort_passes.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "radix_sort_passes.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
BLUE = _COL["blue"]
GREEN = _COL["green"]
ORANGE = _COL["orange"]
WHITE = _COL["white"]

ROWS = [
    ("input", [329, 457, 657, 839, 436, 720, 355]),
    ("ones", [720, 355, 436, 457, 657, 329, 839]),
    ("tens", [720, 329, 436, 839, 355, 457, 657]),
    ("hundreds", [329, 355, 436, 457, 657, 720, 839]),
]
HIGHLIGHTS = [None, 2, 1, 0]


def _digit(number: int, pos: int) -> str:
    return f"{number:03d}"[pos]


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 9.8)
    ax.set_ylim(0.4, 5.1)
    ax.axis("off")

    for r, (label, values) in enumerate(ROWS):
        y = 4.45 - r * 1.05
        ax.text(
            0.35, y, label, ha="right", va="center", fontsize=_FS["label"], color=BLACK
        )
        for i, value in enumerate(values):
            x = 0.75 + i * 1.15
            ax.add_patch(
                Rectangle(
                    (x, y - 0.28),
                    0.88,
                    0.56,
                    facecolor=WHITE,
                    edgecolor=BLACK,
                    linewidth=LW,
                )
            )
            text = f"{value:03d}"
            hi = HIGHLIGHTS[r]
            for j, ch in enumerate(text):
                color = BLACK if hi != j else [BLUE, GREEN, ORANGE][r - 1]
                ax.text(
                    x + 0.24 + j * 0.2,
                    y,
                    ch,
                    ha="center",
                    va="center",
                    fontsize=_FS["body"],
                    fontweight="bold" if hi == j else "normal",
                    color=color,
                )
        if r < len(ROWS) - 1:
            ax.add_patch(
                FancyArrowPatch(
                    (8.95, y - 0.32),
                    (8.95, y - 0.72),
                    arrowstyle="-|>",
                    mutation_scale=14,
                    linewidth=LW,
                    color=GRAY,
                )
            )

    ax.text(
        0.75,
        0.75,
        "stable pass: equal current digits keep the previous order",
        fontsize=_FS["body"],
        color=BLACK,
    )
    ax.text(
        6.1,
        0.75,
        r"LSD radix sort: $d$ stable counting-sort passes",
        fontsize=_FS["body"],
        color=BLACK,
    )


def main() -> None:
    plt.rcParams.update(
        {
            "figure.facecolor": _CFG["figure"]["facecolor"],
            "font.family": _CFG["font"]["family"],
            "font.sans-serif": _CFG["font"]["sans_serif"],
        }
    )
    fig, ax = plt.subplots(figsize=(9.5, 5.2), layout="constrained")
    fig.suptitle("Radix Sort Passes", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
