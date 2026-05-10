"""Generates resources/pictures/tree_traversals.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "tree_traversals.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
BLUE = _COL["blue"]
GREEN = _COL["green"]
ORANGE = _COL["orange"]
WHITE = _COL["white"]

NODES = {
    "A": (4, 4.1),
    "B": (2.4, 2.8),
    "C": (5.6, 2.8),
    "D": (1.5, 1.5),
    "E": (3.3, 1.5),
    "F": (4.8, 1.5),
    "G": (6.6, 1.5),
}
EDGES = [("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"), ("C", "F"), ("C", "G")]
NODE_R = 0.23


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 8.5)
    ax.set_ylim(0, 5)
    ax.set_aspect("equal")
    ax.axis("off")
    for a, b in EDGES:
        x0, y0 = NODES[a]
        x1, y1 = NODES[b]
        ax.plot([x0, x1], [y0, y1], color=BLACK, linewidth=LW)
    for label, p in NODES.items():
        ax.add_patch(
            Circle(p, NODE_R, facecolor=WHITE, edgecolor=BLACK, linewidth=LW, zorder=2)
        )
        ax.text(*p, label, ha="center", va="center", fontsize=_FS["label"], color=BLACK)
    rows = [
        ("preorder", "A B D E C F G", BLUE),
        ("inorder", "D B E A F C G", GREEN),
        ("postorder", "D E B F G C A", ORANGE),
    ]
    for i, (name, seq, color) in enumerate(rows):
        y = 0.85 - i * 0.28
        ax.text(0.2, y, name, ha="left", fontsize=_FS["body"], color=color)
        ax.text(1.55, y, seq, ha="left", fontsize=_FS["body"], color=BLACK)
    ax.text(
        6.4,
        0.28,
        "same tree, different visit order",
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
    fig, ax = plt.subplots(figsize=(8, 5), layout="constrained")
    fig.suptitle("Tree Traversals", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
