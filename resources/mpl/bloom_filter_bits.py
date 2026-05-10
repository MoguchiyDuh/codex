"""Generates resources/pictures/bloom_filter_bits.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "bloom_filter_bits.png"
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
GREEN = _COL["green"]
WHITE = _COL["white"]


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 9)
    ax.set_ylim(0.4, 4.2)
    ax.set_aspect("equal")
    ax.axis("off")
    ones = {1, 3, 4, 7}
    for i in range(10):
        color = GREEN if i in ones else WHITE
        ax.add_patch(
            Rectangle(
                (1.5 + i * 0.55, 1.35),
                0.55,
                0.55,
                facecolor=color,
                edgecolor=BLACK,
                linewidth=LW,
            )
        )
        ax.text(
            1.775 + i * 0.55,
            1.625,
            "1" if i in ones else "0",
            ha="center",
            va="center",
            fontsize=_FS["body"],
        )
    ax.text(0.7, 3.35, "x", ha="center", fontsize=_FS["label"], color=BLACK)
    for j, idx in enumerate([1, 4, 7]):
        ax.text(
            1.4 + j * 1.1,
            3.35,
            f"h{j + 1}(x)",
            ha="center",
            fontsize=_FS["body"],
            color=BLUE,
        )
        ax.add_patch(
            FancyArrowPatch(
                (1.4 + j * 1.1, 3.15),
                (1.775 + idx * 0.55, 1.95),
                arrowstyle="-|>",
                mutation_scale=12,
                linewidth=LW,
                color=BLUE,
            )
        )
    ax.text(
        5.2,
        0.75,
        "all queried bits are 1 => probably present; any 0 => definitely absent",
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
    fig, ax = plt.subplots(figsize=(8.5, 4), layout="constrained")
    fig.suptitle("Bloom Filter Bits", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
