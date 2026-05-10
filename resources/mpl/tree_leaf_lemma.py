"""Generates resources/pictures/tree_leaf_lemma.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "tree_leaf_lemma.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
GREEN = _COL["green"]
WHITE = _COL["white"]

PATH = [(0.8, 2.25), (2.0, 3.25), (3.35, 2.85), (4.75, 2.05), (6.15, 2.85), (7.2, 1.65)]
BRANCHES = [((3.35, 2.85), (3.05, 1.35)), ((4.75, 2.05), (4.35, 0.95))]
NODE_R = 0.17


def _edge(
    ax: plt.Axes, a: tuple[float, float], b: tuple[float, float], color: str
) -> None:
    ax.plot([a[0], b[0]], [a[1], b[1]], color=color, linewidth=LW, zorder=1)


def _node(
    ax: plt.Axes, p: tuple[float, float], color: str = WHITE, label: str = ""
) -> None:
    r = 0.28 if label else NODE_R
    ax.add_patch(Circle(p, r, facecolor=color, edgecolor=BLACK, linewidth=LW, zorder=2))
    if label:
        ax.text(
            *p,
            label,
            ha="center",
            va="center",
            fontsize=_FS["small"],
            color=BLACK,
            zorder=3,
        )


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 8)
    ax.set_ylim(0.35, 4.6)
    ax.set_aspect("equal")
    ax.axis("off")
    for a, b in zip(PATH[:-1], PATH[1:], strict=True):
        _edge(ax, a, b, RED)
    for a, b in BRANCHES:
        _edge(ax, a, b, BLACK)
        _node(ax, b)
    for p in PATH:
        _node(ax, p)
    _node(ax, PATH[0], GREEN, "leaf")
    _node(ax, PATH[-1], GREEN, "leaf")
    ax.text(
        4,
        4.15,
        "endpoints of a longest path cannot branch",
        ha="center",
        fontsize=_FS["label"],
        color=BLACK,
    )
    ax.text(
        4,
        0.55,
        "a branch would extend the path or create a cycle",
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
    fig, ax = plt.subplots(figsize=(7, 4.4), layout="constrained")
    fig.suptitle("Tree Leaf Lemma", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
