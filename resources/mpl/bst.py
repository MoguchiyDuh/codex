"""Generates resources/pictures/bst.png."""

from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "bst.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
BLUE = _COL["blue"]
GREEN = _COL["green"]
PURPLE = _COL["purple"]
WHITE = _COL["white"]

NODE_R = 0.28
NODES: dict[str, tuple[float, float, str, str]] = {
    "15": (4.0, 4.2, "15", BLUE),
    "6": (2.0, 3.0, "6", GREEN),
    "18": (6.0, 3.0, "18", PURPLE),
    "3": (1.1, 1.9, "3", WHITE),
    "7": (2.9, 1.9, "7", WHITE),
    "17": (5.1, 1.9, "17", WHITE),
    "20": (6.9, 1.9, "20", WHITE),
    "8": (3.65, 0.9, "8", WHITE),
}

EDGES = [
    ("15", "6"),
    ("15", "18"),
    ("6", "3"),
    ("6", "7"),
    ("18", "17"),
    ("18", "20"),
    ("7", "8"),
]


def _edge(ax: plt.Axes, parent: str, child: str) -> None:
    x0, y0, _, _ = NODES[parent]
    x1, y1, _, _ = NODES[child]
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


def _node(ax: plt.Axes, x: float, y: float, label: str, color: str) -> None:
    ax.add_patch(
        mpatches.Circle(
            (x, y), NODE_R, facecolor=color, edgecolor=BLACK, linewidth=LW, zorder=3
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
        zorder=4,
    )


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 8.2)
    ax.set_ylim(0.1, 4.9)
    ax.set_aspect("equal")
    ax.axis("off")

    for parent, child in EDGES:
        _edge(ax, parent, child)
    for x, y, label, color in NODES.values():
        _node(ax, x, y, label, color)

    ax.text(
        2.0,
        0.55,
        "left of 15: smaller keys",
        ha="center",
        fontsize=_FS["body"],
        color=GREEN,
    )
    ax.text(
        6.0,
        0.55,
        "right of 15: larger keys",
        ha="center",
        fontsize=_FS["body"],
        color=PURPLE,
    )
    ax.text(
        4.0,
        4.75,
        "each node splits keys into smaller-left and larger-right",
        ha="center",
        fontsize=_FS["title"],
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
    fig, ax = plt.subplots(figsize=(8, 5), layout="constrained")
    fig.suptitle("Binary Search Tree", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
