"""Generates resources/pictures/red_black_tree_example.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "red_black_tree_example.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
WHITE = _COL["white"]

NODES = {
    "10": (4, 4.0, BLACK),
    "5": (2.5, 2.8, RED),
    "15": (5.5, 2.8, RED),
    "3": (1.6, 1.6, BLACK),
    "7": (3.2, 1.6, BLACK),
    "12": (4.8, 1.6, BLACK),
    "18": (6.4, 1.6, BLACK),
}
EDGES = [("10", "5"), ("10", "15"), ("5", "3"), ("5", "7"), ("15", "12"), ("15", "18")]


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0.5, 7.5)
    ax.set_ylim(0.7, 4.6)
    ax.set_aspect("equal")
    ax.axis("off")
    for a, b in EDGES:
        ax.plot(
            [NODES[a][0], NODES[b][0]],
            [NODES[a][1], NODES[b][1]],
            color=BLACK,
            linewidth=LW,
        )
    for label, (x, y, color) in NODES.items():
        ax.add_patch(
            Circle(
                (x, y), 0.28, facecolor=color, edgecolor=BLACK, linewidth=LW, zorder=2
            )
        )
        ax.text(
            x,
            y,
            label,
            ha="center",
            va="center",
            fontsize=_FS["body"],
            color=WHITE if color == BLACK else BLACK,
        )
    ax.text(
        4,
        0.95,
        "red nodes have black children; black-height is uniform",
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
    fig, ax = plt.subplots(figsize=(7, 4.5), layout="constrained")
    fig.suptitle(
        "Red-Black Tree Invariants", fontsize=_FS["suptitle"], fontweight="black"
    )
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
