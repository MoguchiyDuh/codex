"""Generates resources/pictures/n_queens_tree.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "n_queens_tree.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
BLUE = _COL["blue"]
RED = _COL["red"]
GREEN = _COL["green"]

NODES = [
    ("start", 4.0, 4.3, BLUE),
    ("r0", 1.6, 3.2, RED),
    ("r1", 3.2, 3.2, GREEN),
    ("r2", 4.8, 3.2, GREEN),
    ("r3", 6.4, 3.2, RED),
    ("conflict", 2.4, 2.0, RED),
    ("safe", 3.8, 2.0, GREEN),
    ("safe", 5.2, 2.0, GREEN),
    ("conflict", 6.6, 2.0, RED),
    ("solution", 4.5, 0.95, GREEN),
]
EDGES = [(0, 1), (0, 2), (0, 3), (0, 4), (2, 5), (2, 6), (3, 7), (3, 8), (6, 9), (7, 9)]


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0.5, 7.4)
    ax.set_ylim(0.35, 4.9)
    ax.axis("off")
    for i, j in EDGES:
        ax.plot(
            [NODES[i][1], NODES[j][1]],
            [NODES[i][2], NODES[j][2]],
            color=GRAY,
            linewidth=LW,
        )
    for label, x, y, color in NODES:
        ax.add_patch(
            Circle(
                (x, y), 0.3, facecolor=color, edgecolor=BLACK, linewidth=LW, zorder=2
            )
        )
        ax.text(
            x,
            y,
            label,
            ha="center",
            va="center",
            fontsize=_FS["small"],
            color=BLACK,
            zorder=3,
        )
    ax.text(
        0.75, 4.55, "each level places one column", fontsize=_FS["body"], color=BLACK
    )
    ax.text(
        0.75,
        0.55,
        "red branches are pruned as soon as a queen attacks",
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
    fig.suptitle(
        "N-Queens Backtracking Tree", fontsize=_FS["suptitle"], fontweight="black"
    )
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
