"""Generates resources/pictures/euler_tour.png."""

from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "euler_tour.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
WHITE = _COL["white"]

NODE_R = 0.17
N = 5
ORDER = [0, 1, 2, 3, 4, 0, 2, 4, 1, 3, 0]
STEP_FS = _FS["label"]


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(-1.25, 1.25)
    ax.set_ylim(-1.35, 1.35)
    ax.set_aspect("equal")
    ax.axis("off")
    pts = [
        (
            math.cos(2 * math.pi * i / N + math.pi / 2),
            math.sin(2 * math.pi * i / N + math.pi / 2),
        )
        for i in range(N)
    ]
    for step, (i, j) in enumerate(zip(ORDER[:-1], ORDER[1:], strict=True), 1):
        color = RED if step <= 5 else BLUE
        ax.add_patch(
            FancyArrowPatch(
                pts[i],
                pts[j],
                arrowstyle="-|>",
                mutation_scale=11,
                linewidth=LW,
                color=color,
                shrinkA=11,
                shrinkB=11,
                zorder=1,
            )
        )
        mx = (pts[i][0] + pts[j][0]) / 2
        my = (pts[i][1] + pts[j][1]) / 2
        ax.text(
            mx, my, str(step), ha="center", va="center", fontsize=STEP_FS, color=BLACK
        )
    for i, p in enumerate(pts):
        ax.add_patch(
            Circle(p, NODE_R, facecolor=WHITE, edgecolor=BLACK, linewidth=LW, zorder=3)
        )
        ax.text(
            *p,
            str(i),
            ha="center",
            va="center",
            fontsize=_FS["small"],
            color=BLACK,
            zorder=4,
        )
    ax.text(
        0,
        -1.2,
        "each edge is used exactly once",
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
    fig, ax = plt.subplots(figsize=(5.5, 5.2), layout="constrained")
    fig.suptitle("Euler Tour", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
