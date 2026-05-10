"""Generates resources/pictures/linked_list_variants.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "linked_list_variants.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
BLUE = _COL["blue"]
GREEN = _COL["green"]
ORANGE = _COL["orange"]
WHITE = _COL["white"]

NODE_W = 0.75
NODE_H = 0.42
ARROW_SCALE = 12


def _node(ax: plt.Axes, x: float, y: float, label: str, color: str = WHITE) -> None:
    ax.add_patch(
        FancyBboxPatch(
            (x - NODE_W / 2, y - NODE_H / 2),
            NODE_W,
            NODE_H,
            boxstyle="round,pad=0.04",
            facecolor=color,
            edgecolor=BLACK,
            linewidth=LW,
        )
    )
    ax.text(x, y, label, ha="center", va="center", fontsize=_FS["body"], color=BLACK)


def _arrow(
    ax: plt.Axes, a: tuple[float, float], b: tuple[float, float], rad: float = 0.0
) -> None:
    ax.add_patch(
        FancyArrowPatch(
            a,
            b,
            arrowstyle="-|>",
            mutation_scale=ARROW_SCALE,
            linewidth=LW,
            color=BLACK,
            connectionstyle=f"arc3,rad={rad}",
        )
    )


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5.5)
    ax.set_aspect("equal")
    ax.axis("off")
    rows = [("singly", 4.4, BLUE), ("doubly", 2.8, GREEN), ("circular", 1.2, ORANGE)]
    xs = [2.5, 4.2, 5.9, 7.6]
    for title, y, color in rows:
        ax.text(
            0.9, y, title, ha="right", va="center", fontsize=_FS["label"], color=BLACK
        )
        for i, x in enumerate(xs[:3]):
            _node(ax, x, y, chr(ord("A") + i), color)
        _arrow(ax, (xs[0] + NODE_W / 2, y), (xs[1] - NODE_W / 2, y))
        _arrow(ax, (xs[1] + NODE_W / 2, y), (xs[2] - NODE_W / 2, y))
        if title == "doubly":
            _arrow(ax, (xs[1] - NODE_W / 2, y - 0.12), (xs[0] + NODE_W / 2, y - 0.12))
            _arrow(ax, (xs[2] - NODE_W / 2, y - 0.12), (xs[1] + NODE_W / 2, y - 0.12))
        if title == "circular":
            _arrow(ax, (xs[2], y - NODE_H / 2), (xs[0], y - NODE_H / 2), rad=-0.32)
    ax.text(
        5,
        0.08,
        "links make edits local, but traversal is sequential",
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
    fig, ax = plt.subplots(figsize=(9, 5), layout="constrained")
    fig.suptitle("Linked List Variants", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
