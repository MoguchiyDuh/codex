"""Generates resources/pictures/adjacency_list_layout.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "adjacency_list_layout.png"
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
BLUE = _COL["blue"]
WHITE = _COL["white"]


def _box(ax: plt.Axes, x: float, y: float, label: str, color: str = WHITE) -> None:
    ax.add_patch(
        Rectangle((x, y), 0.7, 0.42, facecolor=color, edgecolor=BLACK, linewidth=LW)
    )
    ax.text(x + 0.35, y + 0.21, label, ha="center", va="center", fontsize=_FS["body"])


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 4.5)
    ax.set_aspect("equal")
    ax.axis("off")
    lists = {0: [1, 2], 1: [2, 3], 2: [3], 3: [0]}
    for row, (v, ns) in enumerate(lists.items()):
        y = 3.5 - row * 0.75
        _box(ax, 0.8, y, f"adj[{v}]", BLUE)
        x = 2.1
        for n in ns:
            _box(ax, x, y, str(n))
            ax.add_patch(
                FancyArrowPatch(
                    (x - 0.35, y + 0.21),
                    (x, y + 0.21),
                    arrowstyle="-|>",
                    mutation_scale=10,
                    linewidth=LW,
                    color=BLACK,
                )
            )
            x += 0.95
    ax.text(
        4,
        0.35,
        "each vertex stores exactly its outgoing neighbours",
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
    fig, ax = plt.subplots(figsize=(7.5, 4.2), layout="constrained")
    fig.suptitle("Adjacency List Layout", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
