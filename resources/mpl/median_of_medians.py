"""Generates resources/pictures/median_of_medians.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "median_of_medians.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
GREEN = _COL["green"]
PURPLE = _COL["purple"]
WHITE = _COL["white"]

GROUPS = [[4, 9, 1, 7, 3], [18, 12, 16, 11, 14], [6, 20, 2, 5, 8], [13, 19, 15, 10, 17]]


def _box(
    ax: plt.Axes,
    x: float,
    y: float,
    label: str,
    fill: str = WHITE,
    fs: float | None = None,
) -> None:
    ax.add_patch(
        Rectangle(
            (x - 0.24, y - 0.2),
            0.48,
            0.4,
            facecolor=fill,
            edgecolor=BLACK,
            linewidth=LW,
        )
    )
    ax.text(
        x, y, label, ha="center", va="center", fontsize=fs or _FS["small"], color=BLACK
    )


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6.2)
    ax.axis("off")
    ax.text(0.35, 5.35, "1. groups of 5", fontsize=_FS["label"], color=BLACK)
    ax.text(0.35, 3.55, "2. medians", fontsize=_FS["label"], color=BLACK)
    ax.text(0.35, 1.75, "3. median of medians", fontsize=_FS["label"], color=BLACK)

    medians: list[tuple[float, int]] = []
    for g, values in enumerate(GROUPS):
        sorted_values = sorted(values)
        median = sorted_values[2]
        x0 = 2.0 + g * 1.75
        for i, value in enumerate(sorted_values):
            fill = BLUE if value == median else WHITE
            _box(ax, x0 + i * 0.32, 5.0, str(value), fill)
        mx = x0 + 2 * 0.32
        medians.append((mx, median))
        ax.add_patch(
            FancyArrowPatch(
                (mx, 4.72),
                (mx, 3.9),
                arrowstyle="-|>",
                mutation_scale=12,
                linewidth=LW,
                color=GRAY,
            )
        )
        _box(ax, mx, 3.55, str(median), BLUE, _FS["body"])

    sorted_medians = sorted(v for _, v in medians)
    pivot = sorted_medians[len(sorted_medians) // 2]
    px = 5.2
    ax.add_patch(
        FancyArrowPatch(
            (5.2, 3.25),
            (5.2, 2.08),
            arrowstyle="-|>",
            mutation_scale=14,
            linewidth=LW,
            color=GRAY,
        )
    )
    _box(ax, px, 1.75, str(pivot), PURPLE, _FS["label"])
    ax.text(px + 0.5, 1.75, "pivot", va="center", fontsize=_FS["label"], color=PURPLE)

    ax.add_patch(
        Rectangle(
            (1.25, 0.45), 2.55, 0.55, facecolor=GREEN, edgecolor=BLACK, linewidth=LW
        )
    )
    ax.add_patch(
        Rectangle(
            (6.15, 0.45), 2.55, 0.55, facecolor=RED, edgecolor=BLACK, linewidth=LW
        )
    )
    ax.text(
        2.52,
        0.72,
        r"at least $3n/10$ smaller",
        ha="center",
        va="center",
        fontsize=_FS["body"],
        color=BLACK,
    )
    ax.text(
        7.42,
        0.72,
        r"at least $3n/10$ larger",
        ha="center",
        va="center",
        fontsize=_FS["body"],
        color=BLACK,
    )
    ax.text(
        5.0,
        0.18,
        r"recurse on at most $7n/10$ elements",
        ha="center",
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
    fig, ax = plt.subplots(figsize=(9.5, 6), layout="constrained")
    fig.suptitle("Median of Medians", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
