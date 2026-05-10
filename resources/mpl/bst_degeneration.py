"""Generates resources/pictures/bst_degeneration.png."""

from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "bst_degeneration.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
WHITE = _COL["white"]

NODE_R = 0.28
NODES = [
    (1.2, 4.15, "1"),
    (2.2, 3.35, "2"),
    (3.2, 2.55, "3"),
    (4.2, 1.75, "4"),
    (5.2, 0.95, "5"),
]


def _edge(
    ax: plt.Axes, a: tuple[float, float, str], b: tuple[float, float, str]
) -> None:
    x0, y0, _ = a
    x1, y1, _ = b
    dx = x1 - x0
    dy = y1 - y0
    dist = math.hypot(dx, dy)
    ux = dx / dist
    uy = dy / dist
    ax.plot(
        [x0 + ux * NODE_R, x1 - ux * NODE_R],
        [y0 + uy * NODE_R, y1 - uy * NODE_R],
        color=BLACK,
        linewidth=LW,
        zorder=1,
    )


def _node(ax: plt.Axes, x: float, y: float, label: str) -> None:
    ax.add_patch(
        mpatches.Circle(
            (x, y), NODE_R, facecolor=WHITE, edgecolor=BLACK, linewidth=LW, zorder=2
        )
    )
    ax.text(
        x,
        y,
        label,
        ha="center",
        va="center",
        fontsize=_FS["label"],
        color=BLACK,
        zorder=3,
    )


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0.3, 7.1)
    ax.set_ylim(0.25, 4.9)
    ax.set_aspect("equal")
    ax.axis("off")
    for a, b in zip(NODES[:-1], NODES[1:], strict=True):
        _edge(ax, a, b)
    for x, y, label in NODES:
        _node(ax, x, y, label)
    ax.add_patch(
        mpatches.FancyArrowPatch(
            (0.75, 4.6),
            (5.85, 0.55),
            arrowstyle="-|>",
            mutation_scale=16,
            linewidth=LW,
            color=RED,
            connectionstyle="arc3,rad=-0.10",
        )
    )
    ax.text(
        3.25,
        4.45,
        "sorted inserts keep following right links",
        ha="center",
        fontsize=_FS["label"],
        color=RED,
    )
    ax.text(
        6.0,
        2.65,
        "height = n - 1\nsearch is O(n)",
        ha="center",
        va="center",
        fontsize=_FS["label"],
        color=BLACK,
    )
    ax.text(
        3.2,
        0.45,
        "a plain BST can collapse into a linked list",
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
    fig, ax = plt.subplots(figsize=(7, 5), layout="constrained")
    fig.suptitle("BST Degeneration", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
