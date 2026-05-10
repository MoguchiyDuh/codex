"""Generates resources/pictures/heap_array_layout.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "heap_array_layout.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
BLUE = _COL["blue"]
WHITE = _COL["white"]

VALUES = [4, 8, 7, 12, 9, 10, 14]
NODES = [
    (4, 4.1),
    (2.4, 2.9),
    (5.6, 2.9),
    (1.5, 1.7),
    (3.3, 1.7),
    (4.8, 1.7),
    (6.6, 1.7),
]
EDGES = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 8.2)
    ax.set_ylim(0, 4.9)
    ax.set_aspect("equal")
    ax.axis("off")
    for i, j in EDGES:
        ax.plot(
            [NODES[i][0], NODES[j][0]],
            [NODES[i][1], NODES[j][1]],
            color=BLACK,
            linewidth=LW,
        )
    for i, (x, y) in enumerate(NODES):
        ax.add_patch(
            Circle(
                (x, y), 0.24, facecolor=BLUE, edgecolor=BLACK, linewidth=LW, zorder=2
            )
        )
        ax.text(
            x,
            y,
            str(VALUES[i]),
            ha="center",
            va="center",
            fontsize=_FS["body"],
            color=BLACK,
        )
    x0, y0 = 1.2, 0.55
    for i, v in enumerate(VALUES):
        ax.add_patch(
            Rectangle(
                (x0 + i * 0.75, y0),
                0.75,
                0.45,
                facecolor=WHITE,
                edgecolor=BLACK,
                linewidth=LW,
            )
        )
        ax.text(
            x0 + i * 0.75 + 0.375,
            y0 + 0.225,
            str(v),
            ha="center",
            va="center",
            fontsize=_FS["body"],
        )
        ax.text(
            x0 + i * 0.75 + 0.375,
            y0 - 0.22,
            str(i),
            ha="center",
            fontsize=_FS["small"],
            color=GRAY,
        )
    ax.text(
        6.9,
        0.8,
        r"children: $2i+1$, $2i+2$",
        ha="left",
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
    fig.suptitle("Heap Array Layout", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
