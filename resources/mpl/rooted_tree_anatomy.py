"""Generates resources/pictures/rooted_tree_anatomy.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "rooted_tree_anatomy.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
PURPLE = _COL["purple"]
WHITE = _COL["white"]

NODES = {
    "r": (4.0, 4.35),
    "a": (2.3, 3.1),
    "b": (5.7, 3.1),
    "c": (1.3, 1.85),
    "d": (3.1, 1.85),
    "e": (5.0, 1.85),
    "f": (6.8, 1.85),
}
EDGES = [("r", "a"), ("r", "b"), ("a", "c"), ("a", "d"), ("b", "e"), ("b", "f")]
NODE_R = 0.2


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 8)
    ax.set_ylim(0.4, 5.25)
    ax.set_aspect("equal")
    ax.axis("off")
    for a, b in EDGES:
        x0, y0 = NODES[a]
        x1, y1 = NODES[b]
        ax.plot([x0, x1], [y0, y1], color=BLACK, linewidth=LW, zorder=1)
    for x, y in NODES.values():
        ax.add_patch(
            Circle(
                (x, y), NODE_R, facecolor=WHITE, edgecolor=BLACK, linewidth=LW, zorder=2
            )
        )
    ax.text(4.0, 4.82, "root", ha="center", fontsize=_FS["label"], color=RED)
    ax.text(0.78, 1.85, "leaf", ha="center", fontsize=_FS["body"], color=GRAY)
    ax.text(
        7.25, 3.1, "depth 1", ha="left", va="center", fontsize=_FS["body"], color=GRAY
    )
    ax.text(
        7.25, 1.85, "depth 2", ha="left", va="center", fontsize=_FS["body"], color=GRAY
    )
    ax.add_patch(
        FancyBboxPatch(
            (4.55, 1.45),
            2.75,
            2.05,
            boxstyle="round,pad=0.08",
            facecolor="none",
            edgecolor=PURPLE,
            linewidth=LW,
        )
    )
    ax.text(5.95, 1.05, "subtree", ha="center", fontsize=_FS["label"], color=PURPLE)


def main() -> None:
    plt.rcParams.update(
        {
            "figure.facecolor": _CFG["figure"]["facecolor"],
            "font.family": _CFG["font"]["family"],
            "font.sans-serif": _CFG["font"]["sans_serif"],
        }
    )
    fig, ax = plt.subplots(figsize=(7, 5), layout="constrained")
    fig.suptitle("Rooted Tree Anatomy", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
