"""Generates resources/pictures/heap_sift.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "heap_sift.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
WHITE = _COL["white"]

NODE_R = 0.24


def _tree(ax: plt.Axes, xoff: float, title: str, values: list[int], hi: int) -> None:
    pts = [
        (xoff + 2.5, 3.25),
        (xoff + 1.5, 2.2),
        (xoff + 3.5, 2.2),
        (xoff + 1.0, 1.15),
        (xoff + 2.0, 1.15),
    ]
    edges = [(0, 1), (0, 2), (1, 3), (1, 4)]
    ax.text(xoff + 2.5, 3.85, title, ha="center", fontsize=_FS["label"], color=BLACK)
    for i, j in edges:
        ax.plot(
            [pts[i][0], pts[j][0]], [pts[i][1], pts[j][1]], color=BLACK, linewidth=LW
        )
    for i, p in enumerate(pts):
        color = RED if i == hi else BLUE if i in [0, 1] else WHITE
        ax.add_patch(
            Circle(p, NODE_R, facecolor=color, edgecolor=BLACK, linewidth=LW, zorder=2)
        )
        ax.text(
            *p,
            str(values[i]),
            ha="center",
            va="center",
            fontsize=_FS["body"],
            color=BLACK,
        )


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 10)
    ax.set_ylim(0.35, 4.2)
    ax.set_aspect("equal")
    ax.axis("off")
    _tree(ax, 0.0, "after insert", [4, 8, 7, 12, 3], 4)
    _tree(ax, 5.0, "after sift up", [3, 4, 7, 12, 8], 0)
    ax.add_patch(
        FancyArrowPatch(
            (4.55, 2.15),
            (5.35, 2.15),
            arrowstyle="-|>",
            mutation_scale=16,
            linewidth=LW,
            color=RED,
        )
    )
    ax.text(
        5.0,
        0.6,
        "swap with parent until heap order is restored",
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
    fig, ax = plt.subplots(figsize=(9, 4.2), layout="constrained")
    fig.suptitle("Heap Sift Up", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
