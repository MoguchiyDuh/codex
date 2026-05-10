"""Generates resources/pictures/function_types.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "function_types.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
BLUE = _COL["blue"]
GREEN = _COL["green"]
PURPLE = _COL["purple"]
WHITE = _COL["white"]

NODE_R = 0.18
PANELS = [
    ("injective", 0.6, 3, 4, [(0, 0), (1, 1), (2, 2)]),
    ("surjective", 4.2, 4, 3, [(0, 0), (1, 1), (2, 1), (3, 2)]),
    ("bijective", 7.8, 3, 3, [(0, 0), (1, 1), (2, 2)]),
]


def _node(ax: plt.Axes, x: float, y: float, label: str, color: str) -> None:
    ax.add_patch(
        Circle((x, y), NODE_R, facecolor=color, edgecolor=BLACK, linewidth=LW, zorder=3)
    )
    ax.text(
        x,
        y,
        label,
        ha="center",
        va="center",
        fontsize=_FS["small"],
        color=BLACK,
        zorder=4,
    )


def _arrow(ax: plt.Axes, x0: float, y0: float, x1: float, y1: float) -> None:
    ax.add_patch(
        FancyArrowPatch(
            (x0 + NODE_R, y0),
            (x1 - NODE_R, y1),
            arrowstyle="-|>",
            mutation_scale=12,
            linewidth=LW,
            color=PURPLE,
            zorder=2,
        )
    )


def _panel(
    ax: plt.Axes,
    title: str,
    x0: float,
    left_n: int,
    right_n: int,
    arrows: list[tuple[int, int]],
) -> None:
    ax.text(x0 + 1.25, 3.45, title, ha="center", fontsize=_FS["label"], color=BLACK)
    left_y = [2.75 - i * 0.75 for i in range(left_n)]
    right_y = [2.75 - i * 0.75 for i in range(right_n)]
    for i, y in enumerate(left_y):
        _node(ax, x0, y, chr(ord("a") + i), BLUE)
    for i, y in enumerate(right_y):
        _node(ax, x0 + 2.5, y, str(i + 1), GREEN)
    for i, j in arrows:
        _arrow(ax, x0, left_y[i], x0 + 2.5, right_y[j])


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 11)
    ax.set_ylim(0.05, 3.8)
    ax.set_aspect("equal")
    ax.axis("off")
    for panel in PANELS:
        _panel(ax, *panel)


def main() -> None:
    plt.rcParams.update(
        {
            "figure.facecolor": _CFG["figure"]["facecolor"],
            "font.family": _CFG["font"]["family"],
            "font.sans-serif": _CFG["font"]["sans_serif"],
        }
    )
    fig, ax = plt.subplots(figsize=(10, 3.8), layout="constrained")
    fig.suptitle(
        "Injective, Surjective, Bijective", fontsize=_FS["suptitle"], fontweight="black"
    )
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
