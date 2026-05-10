"""Generates resources/pictures/topological_sort.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "topological_sort.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
BLUE = _COL["blue"]
GREEN = _COL["green"]
WHITE = _COL["white"]

NODES = {
    "cook": (1.2, 3.8),
    "eat": (3.5, 4.2),
    "wash": (5.8, 3.8),
    "shop": (1.2, 2.0),
    "prep": (3.5, 2.2),
    "serve": (5.8, 2.0),
}
EDGES = [
    ("shop", "prep"),
    ("prep", "cook"),
    ("cook", "eat"),
    ("prep", "serve"),
    ("serve", "eat"),
    ("eat", "wash"),
]
ORDER = ["shop", "prep", "cook", "serve", "eat", "wash"]


def _arrow(ax: plt.Axes, a: str, b: str) -> None:
    x0, y0 = NODES[a]
    x1, y1 = NODES[b]
    ax.add_patch(
        FancyArrowPatch(
            (x0, y0),
            (x1, y1),
            arrowstyle="-|>",
            mutation_scale=14,
            linewidth=LW,
            color=BLACK,
            shrinkA=22,
            shrinkB=22,
        )
    )


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0.2, 7.2)
    ax.set_ylim(0.25, 5.05)
    ax.axis("off")
    for a, b in EDGES:
        _arrow(ax, a, b)
    for name, (x, y) in NODES.items():
        ax.add_patch(
            Circle(
                (x, y), 0.34, facecolor=BLUE, edgecolor=BLACK, linewidth=LW, zorder=2
            )
        )
        ax.text(
            x,
            y,
            name,
            ha="center",
            va="center",
            fontsize=_FS["small"],
            color=BLACK,
            zorder=3,
        )

    y = 0.75
    for i, name in enumerate(ORDER):
        x = 0.75 + i * 1.02
        ax.add_patch(
            Rectangle(
                (x, y - 0.22),
                0.82,
                0.44,
                facecolor=GREEN if i < 2 else WHITE,
                edgecolor=BLACK,
                linewidth=LW,
            )
        )
        ax.text(
            x + 0.41,
            y,
            name,
            ha="center",
            va="center",
            fontsize=_FS["small"],
            color=BLACK,
        )
        if i < len(ORDER) - 1:
            ax.text(
                x + 0.9,
                y,
                "<",
                ha="center",
                va="center",
                fontsize=_FS["body"],
                color=GRAY,
            )
    ax.text(
        0.75,
        0.28,
        "a valid order places every prerequisite before its dependent",
        fontsize=_FS["body"],
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
    fig.suptitle("Topological Sort", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
