"""Generates resources/pictures/hash_open_addressing.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "hash_open_addressing.png"
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
WHITE = _COL["white"]


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 3)
    ax.set_aspect("equal")
    ax.axis("off")
    vals = ["", "A", "B", "", "C", "", "", ""]
    for i, val in enumerate(vals):
        color = BLUE if val else WHITE
        ax.add_patch(
            Rectangle(
                (0.8 + i * 0.8, 1.3),
                0.8,
                0.55,
                facecolor=color,
                edgecolor=BLACK,
                linewidth=LW,
            )
        )
        ax.text(
            1.2 + i * 0.8,
            1.58,
            val or str(i),
            ha="center",
            va="center",
            fontsize=_FS["body"],
            color=BLACK if val else GRAY,
        )
    for a, b in [(2, 3), (3, 4)]:
        ax.add_patch(
            FancyArrowPatch(
                (1.2 + a * 0.8, 2.05),
                (1.2 + b * 0.8, 2.05),
                arrowstyle="-|>",
                mutation_scale=12,
                linewidth=LW,
                color=RED,
            )
        )
    ax.text(
        4,
        0.55,
        "collision: probe forward until an open slot",
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
    fig, ax = plt.subplots(figsize=(7.5, 3), layout="constrained")
    fig.suptitle("Open Addressing", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
