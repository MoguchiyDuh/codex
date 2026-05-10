"""Generates resources/pictures/hash_collision_chaining.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "hash_collision_chaining.png"
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
BLUE = _COL["blue"]
ORANGE = _COL["orange"]
WHITE = _COL["white"]


def _box(ax: plt.Axes, x: float, y: float, label: str, color: str = WHITE) -> None:
    ax.add_patch(
        Rectangle((x, y), 0.75, 0.42, facecolor=color, edgecolor=BLACK, linewidth=LW)
    )
    ax.text(x + 0.375, y + 0.21, label, ha="center", va="center", fontsize=_FS["body"])


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 4.2)
    ax.set_aspect("equal")
    ax.axis("off")
    for i in range(5):
        _box(ax, 0.8, 3.3 - i * 0.65, str(i), WHITE)
    for j, label in enumerate(["k1", "k7", "k9"]):
        _box(ax, 2.4 + j * 1.25, 2.0, label, BLUE if j == 0 else ORANGE)
        if j < 2:
            ax.add_patch(
                FancyArrowPatch(
                    (3.15 + j * 1.25, 2.21),
                    (3.65 + j * 1.25, 2.21),
                    arrowstyle="-|>",
                    mutation_scale=12,
                    linewidth=LW,
                    color=BLACK,
                )
            )
    ax.add_patch(
        FancyArrowPatch(
            (1.55, 2.21),
            (2.4, 2.21),
            arrowstyle="-|>",
            mutation_scale=12,
            linewidth=LW,
            color=BLACK,
        )
    )
    ax.text(
        4,
        0.55,
        "colliding keys share a bucket chain",
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
    fig, ax = plt.subplots(figsize=(7.5, 4), layout="constrained")
    fig.suptitle("Separate Chaining", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
