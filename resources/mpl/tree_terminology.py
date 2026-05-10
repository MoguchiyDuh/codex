"""Generates resources/pictures/tree_terminology.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "tree_terminology.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
PURPLE = _COL["purple"]
WHITE = _COL["white"]

NODE_R = 0.22
NODES = {
    "root": (4, 4.5),
    "a": (2.4, 3.2),
    "b": (5.6, 3.2),
    "c": (1.4, 1.9),
    "d": (3.1, 1.9),
    "e": (4.8, 1.9),
    "f": (6.6, 1.9),
}
EDGES = [("root", "a"), ("root", "b"), ("a", "c"), ("a", "d"), ("b", "e"), ("b", "f")]


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 8)
    ax.set_ylim(0.6, 5.2)
    ax.set_aspect("equal")
    ax.axis("off")
    for a, b in EDGES:
        x0, y0 = NODES[a]
        x1, y1 = NODES[b]
        ax.plot([x0, x1], [y0, y1], color=BLACK, linewidth=LW, zorder=1)
    for p in NODES.values():
        ax.add_patch(
            Circle(p, NODE_R, facecolor=WHITE, edgecolor=BLACK, linewidth=LW, zorder=2)
        )
    ax.text(4, 4.9, "root", ha="center", fontsize=_FS["label"], color=RED)
    ax.text(0.75, 1.9, "leaf", ha="center", fontsize=_FS["label"], color=BLUE)
    ax.text(
        7.2, 3.2, "depth 1", ha="left", va="center", fontsize=_FS["body"], color=GRAY
    )
    ax.text(
        7.2, 1.9, "depth 2", ha="left", va="center", fontsize=_FS["body"], color=GRAY
    )
    ax.add_patch(
        FancyBboxPatch(
            (4.45, 1.55),
            2.55,
            2.05,
            boxstyle="round,pad=0.08",
            facecolor="none",
            edgecolor=PURPLE,
            linewidth=LW,
        )
    )
    ax.text(5.75, 1.1, "subtree", ha="center", fontsize=_FS["label"], color=PURPLE)


def main() -> None:
    plt.rcParams.update(
        {
            "figure.facecolor": _CFG["figure"]["facecolor"],
            "font.family": _CFG["font"]["family"],
            "font.sans-serif": _CFG["font"]["sans_serif"],
        }
    )
    fig, ax = plt.subplots(figsize=(7, 5), layout="constrained")
    fig.suptitle("Tree Terminology", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
