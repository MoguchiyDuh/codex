"""Generates resources/pictures/avl_rotations.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "avl_rotations.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
WHITE = _COL["white"]

NODE_R = 0.20


def _node(ax: plt.Axes, x: float, y: float, label: str, color: str = WHITE) -> None:
    ax.add_patch(
        Circle((x, y), NODE_R, facecolor=color, edgecolor=BLACK, linewidth=LW, zorder=2)
    )
    ax.text(x, y, label, ha="center", va="center", fontsize=_FS["body"], color=BLACK)


def _edge(ax: plt.Axes, a: tuple[float, float], b: tuple[float, float]) -> None:
    ax.plot([a[0], b[0]], [a[1], b[1]], color=BLACK, linewidth=LW)


def _case(ax: plt.Axes, x: float, title: str, left_heavy: bool) -> None:
    ax.text(x + 1.2, 3.55, title, ha="center", fontsize=_FS["label"], color=BLACK)
    pts = [
        (x + 1.2, 2.9),
        (x + (0.55 if left_heavy else 1.85), 2.1),
        (x + (0.15 if left_heavy else 2.25), 1.3),
    ]
    for a, b in [(pts[0], pts[1]), (pts[1], pts[2])]:
        _edge(ax, a, b)
    for label, p in zip(["z", "y", "x"], pts, strict=True):
        _node(ax, *p, label, RED if label == "z" else WHITE)
    ax.add_patch(
        FancyArrowPatch(
            (x + 0.35, 0.65),
            (x + 2.05, 0.65),
            arrowstyle="<->",
            mutation_scale=12,
            linewidth=LW,
            color=BLUE,
        )
    )
    ax.text(x + 1.2, 0.35, "rotate", ha="center", fontsize=_FS["body"], color=BLUE)


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.set_aspect("equal")
    ax.axis("off")
    _case(ax, 0.2, "LL / right rotation", True)
    _case(ax, 2.75, "RR / left rotation", False)
    _case(ax, 5.25, "LR / double", True)
    _case(ax, 7.7, "RL / double", False)
    ax.text(
        5,
        0.05,
        "rotations are local pointer changes that preserve BST order",
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
    fig, ax = plt.subplots(figsize=(10, 4), layout="constrained")
    fig.suptitle("AVL Rotation Cases", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
