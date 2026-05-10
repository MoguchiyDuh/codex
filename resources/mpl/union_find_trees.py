"""Generates resources/pictures/union_find_trees.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "union_find_trees.png"
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
BLUE = _COL["blue"]
GREEN = _COL["green"]
WHITE = _COL["white"]

NODES = {
    "a": (1.5, 1.2),
    "b": (2.5, 2.1),
    "c": (3.5, 1.2),
    "r1": (2.5, 3.0),
    "d": (5.2, 1.4),
    "e": (6.3, 2.4),
    "r2": (6.3, 3.3),
}
EDGES = [("a", "b"), ("c", "b"), ("b", "r1"), ("d", "e"), ("e", "r2")]


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0.5, 7.4)
    ax.set_ylim(0.6, 3.9)
    ax.set_aspect("equal")
    ax.axis("off")
    for a, b in EDGES:
        ax.add_patch(
            FancyArrowPatch(
                NODES[a],
                NODES[b],
                arrowstyle="-|>",
                mutation_scale=12,
                linewidth=LW,
                color=BLACK,
                shrinkA=14,
                shrinkB=14,
            )
        )
    for k, p in NODES.items():
        color = GREEN if k.startswith("r") else BLUE
        ax.add_patch(Circle(p, 0.22, facecolor=color, edgecolor=BLACK, linewidth=LW))
        ax.text(*p, k, ha="center", va="center", fontsize=_FS["body"])
    ax.text(
        4,
        0.8,
        "parent pointers lead to a root representative",
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
    fig, ax = plt.subplots(figsize=(7, 4), layout="constrained")
    fig.suptitle("Union-Find Forest", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
