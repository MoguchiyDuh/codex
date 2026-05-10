"""Generates resources/pictures/path_compression.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "path_compression.png"
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
WHITE = _COL["white"]


def _node(ax: plt.Axes, p: tuple[float, float], label: str, color: str) -> None:
    ax.add_patch(Circle(p, 0.2, facecolor=color, edgecolor=BLACK, linewidth=LW))
    ax.text(*p, label, ha="center", va="center", fontsize=_FS["body"])


def _arrow(
    ax: plt.Axes, a: tuple[float, float], b: tuple[float, float], color: str = BLACK
) -> None:
    ax.add_patch(
        FancyArrowPatch(
            a,
            b,
            arrowstyle="-|>",
            mutation_scale=12,
            linewidth=LW,
            color=color,
            shrinkA=14,
            shrinkB=14,
        )
    )


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 9)
    ax.set_ylim(0.5, 3.8)
    ax.set_aspect("equal")
    ax.axis("off")
    before = [(1.2, 1), (2.1, 1.7), (3.0, 2.4), (3.9, 3.1)]
    after = [(5.4, 1), (6.3, 1.7), (7.2, 2.4), (7.2, 3.1)]
    ax.text(2.5, 3.55, "before find(x)", ha="center", fontsize=_FS["label"])
    ax.text(6.6, 3.55, "after compression", ha="center", fontsize=_FS["label"])
    for pts in [before, after]:
        for i, p in enumerate(pts):
            _node(ax, p, "r" if i == 3 else chr(ord("x") + i), BLUE if i < 3 else RED)
    for a, b in zip(before[:-1], before[1:], strict=True):
        _arrow(ax, a, b)
    for p in after[:-1]:
        _arrow(ax, p, after[-1], RED)
    ax.text(
        4.5,
        0.65,
        "visited nodes now point directly at the root",
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
    fig, ax = plt.subplots(figsize=(8.5, 4), layout="constrained")
    fig.suptitle("Path Compression", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
