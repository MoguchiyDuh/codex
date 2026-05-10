"""Generates resources/pictures/tsp_2_approx.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "tsp_2_approx.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
BLUE = _COL["blue"]
GREEN = _COL["green"]
ORANGE = _COL["orange"]

PTS = {
    "A": (1.0, 3.0),
    "B": (2.1, 4.2),
    "C": (3.9, 3.7),
    "D": (4.5, 2.0),
    "E": (2.6, 1.3),
    "F": (0.8, 1.6),
}
MST = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "F")]
TOUR = ["A", "B", "C", "D", "E", "F", "A"]


def _draw_points(ax: plt.Axes, dx: float) -> None:
    for label, (x, y) in PTS.items():
        ax.add_patch(
            Circle(
                (x + dx, y),
                0.16,
                facecolor=BLUE,
                edgecolor=BLACK,
                linewidth=LW,
                zorder=3,
            )
        )
        ax.text(
            x + dx, y + 0.28, label, ha="center", fontsize=_FS["small"], color=BLACK
        )


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 10)
    ax.set_ylim(0.5, 5.0)
    ax.axis("off")
    ax.text(2.5, 4.65, "MST", ha="center", fontsize=_FS["title"], color=BLACK)
    ax.text(
        7.4,
        4.65,
        "shortcut preorder walk",
        ha="center",
        fontsize=_FS["title"],
        color=BLACK,
    )
    _draw_points(ax, 0)
    for a, b in MST:
        x0, y0 = PTS[a]
        x1, y1 = PTS[b]
        ax.plot([x0, x1], [y0, y1], color=GREEN, linewidth=LW * 1.7)
    _draw_points(ax, 4.8)
    for a, b in zip(TOUR[:-1], TOUR[1:], strict=True):
        x0, y0 = PTS[a]
        x1, y1 = PTS[b]
        ax.add_patch(
            FancyArrowPatch(
                (x0 + 4.8, y0),
                (x1 + 4.8, y1),
                arrowstyle="-|>",
                mutation_scale=11,
                linewidth=LW,
                color=ORANGE,
                shrinkA=12,
                shrinkB=12,
            )
        )
    ax.text(
        0.7,
        0.9,
        r"walk tree cost $\leq 2 \cdot MST$",
        fontsize=_FS["body"],
        color=BLACK,
    )
    ax.text(
        5.5,
        0.9,
        "triangle inequality makes shortcuts no longer",
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
    fig, ax = plt.subplots(figsize=(9.2, 5.0), layout="constrained")
    fig.suptitle(
        "Metric TSP 2-Approximation", fontsize=_FS["suptitle"], fontweight="black"
    )
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
