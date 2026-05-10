"""Generates resources/pictures/reduction_diagram.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "reduction_diagram.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
BLUE = _COL["blue"]
GREEN = _COL["green"]
ORANGE = _COL["orange"]
WHITE = _COL["white"]


def _node(ax: plt.Axes, xy: tuple[float, float], text: str, fill: str) -> None:
    x, y = xy
    ax.add_patch(
        FancyBboxPatch(
            (x - 1.0, y - 0.42),
            2.0,
            0.84,
            boxstyle="round,pad=0.05,rounding_size=0.12",
            facecolor=fill,
            edgecolor=BLACK,
            linewidth=LW,
        )
    )
    ax.text(x, y, text, ha="center", va="center", fontsize=_FS["body"], color=BLACK)


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 9)
    ax.set_ylim(0.6, 4.8)
    ax.axis("off")
    _node(ax, (1.4, 3.2), "instance x of A", BLUE)
    _node(ax, (4.5, 3.2), "f(x) for B", ORANGE)
    _node(ax, (7.6, 3.2), "solver for B", GREEN)
    ax.add_patch(
        FancyArrowPatch(
            (2.42, 3.2),
            (3.48, 3.2),
            arrowstyle="-|>",
            mutation_scale=16,
            linewidth=LW,
            color=BLACK,
        )
    )
    ax.text(2.95, 3.55, "poly-time f", ha="center", fontsize=_FS["small"], color=GRAY)
    ax.add_patch(
        FancyArrowPatch(
            (5.52, 3.2),
            (6.58, 3.2),
            arrowstyle="-|>",
            mutation_scale=16,
            linewidth=LW,
            color=BLACK,
        )
    )
    ax.add_patch(
        FancyArrowPatch(
            (7.6, 2.76),
            (1.4, 1.65),
            arrowstyle="-|>",
            mutation_scale=16,
            linewidth=LW,
            color=GRAY,
            connectionstyle="arc3,rad=-0.2",
        )
    )
    ax.text(
        4.5,
        1.25,
        r"x in A  iff  f(x) in B",
        ha="center",
        fontsize=_FS["formula"],
        color=BLACK,
    )
    ax.text(
        4.5,
        0.78,
        "if B is easy, A becomes easy; if A is hard, B inherits hardness",
        ha="center",
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
    fig, ax = plt.subplots(figsize=(8.8, 4.8), layout="constrained")
    fig.suptitle(
        "Polynomial-Time Reduction", fontsize=_FS["suptitle"], fontweight="black"
    )
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
