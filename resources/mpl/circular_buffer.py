"""Generates resources/pictures/circular_buffer.png."""

from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Wedge

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "circular_buffer.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
BLUE = _COL["blue"]
GREEN = _COL["green"]
RED = _COL["red"]
WHITE = _COL["white"]

N = 8
R_OUT = 1.8
R_IN = 0.9


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(-3.0, 3.0)
    ax.set_ylim(-2.5, 2.8)
    ax.set_aspect("equal")
    ax.axis("off")
    for i in range(N):
        theta1 = 90 - (i + 1) * 360 / N
        theta2 = 90 - i * 360 / N
        color = BLUE if i in [1, 2, 3, 4] else WHITE
        ax.add_patch(
            Wedge(
                (0, 0),
                R_OUT,
                theta1,
                theta2,
                width=R_OUT - R_IN,
                facecolor=color,
                edgecolor=BLACK,
                linewidth=LW,
            )
        )
        mid = math.radians((theta1 + theta2) / 2)
        ax.text(
            1.35 * math.cos(mid),
            1.35 * math.sin(mid),
            str(i),
            ha="center",
            va="center",
            fontsize=_FS["body"],
            color=BLACK,
        )
    for idx, label, color in [(1, "head", GREEN), (5, "tail", RED)]:
        mid = math.radians(90 - (idx + 0.5) * 360 / N)
        x, y = 2.35 * math.cos(mid), 2.35 * math.sin(mid)
        ax.add_patch(
            FancyArrowPatch(
                (x, y),
                (1.78 * math.cos(mid), 1.78 * math.sin(mid)),
                arrowstyle="-|>",
                mutation_scale=15,
                linewidth=LW,
                color=color,
            )
        )
        ax.text(
            x, y, label, ha="center", va="center", fontsize=_FS["label"], color=color
        )
    ax.text(
        0,
        -2.25,
        "indices advance modulo capacity",
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
    fig, ax = plt.subplots(figsize=(5.6, 5.2), layout="constrained")
    fig.suptitle("Circular Buffer", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
