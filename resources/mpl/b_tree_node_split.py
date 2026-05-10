"""Generates resources/pictures/b_tree_node_split.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "b_tree_node_split.png"
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
GREEN = _COL["green"]
WHITE = _COL["white"]


def _node(
    ax: plt.Axes, x: float, y: float, keys: list[int], color: str = WHITE
) -> None:
    for i, key in enumerate(keys):
        ax.add_patch(
            Rectangle(
                (x + i * 0.55, y),
                0.55,
                0.45,
                facecolor=color,
                edgecolor=BLACK,
                linewidth=LW,
            )
        )
        ax.text(
            x + i * 0.55 + 0.275,
            y + 0.225,
            str(key),
            ha="center",
            va="center",
            fontsize=_FS["body"],
        )


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 8.5)
    ax.set_ylim(0.4, 3.2)
    ax.set_aspect("equal")
    ax.axis("off")
    _node(ax, 0.8, 1.55, [5, 10, 15, 20, 25], BLUE)
    ax.text(2.2, 2.35, "full node", ha="center", fontsize=_FS["label"])
    ax.add_patch(
        FancyArrowPatch(
            (3.8, 1.8),
            (4.7, 1.8),
            arrowstyle="-|>",
            mutation_scale=16,
            linewidth=LW,
            color=RED,
        )
    )
    _node(ax, 5.1, 2.35, [15], RED)
    _node(ax, 4.65, 1.25, [5, 10], GREEN)
    _node(ax, 6.25, 1.25, [20, 25], GREEN)
    ax.text(
        5.9,
        0.65,
        "median moves up; halves become siblings",
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
    fig, ax = plt.subplots(figsize=(8, 3.4), layout="constrained")
    fig.suptitle("B-Tree Node Split", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
