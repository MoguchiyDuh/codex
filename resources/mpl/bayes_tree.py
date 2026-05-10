"""Generates resources/pictures/bayes_tree.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "bayes_tree.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
GREEN = _COL["green"]
WHITE = _COL["white"]

NODE_R = 0.38
PROB_FS = _FS["label"]
NODES = {
    "start": (0.9, 2.5),
    "d": (3.0, 3.6),
    "n": (3.0, 1.4),
    "dp": (6.0, 4.2),
    "dn": (6.0, 3.0),
    "np": (6.0, 2.0),
    "nn": (6.0, 0.8),
}
EDGES = [
    ("start", "d", "0.01"),
    ("start", "n", "0.99"),
    ("d", "dp", "0.99"),
    ("d", "dn", "0.01"),
    ("n", "np", "0.01"),
    ("n", "nn", "0.99"),
]
LABELS = {
    "start": "pop",
    "d": "D",
    "n": "not D",
    "dp": "+",
    "dn": "-",
    "np": "+",
    "nn": "-",
}


def _node(ax: plt.Axes, key: str, color: str = WHITE) -> None:
    x, y = NODES[key]
    ax.add_patch(
        Circle((x, y), NODE_R, facecolor=color, edgecolor=BLACK, linewidth=LW, zorder=3)
    )
    ax.text(
        x,
        y,
        LABELS[key],
        ha="center",
        va="center",
        fontsize=_FS["body"],
        color=BLACK,
        zorder=4,
    )


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 8.5)
    ax.set_ylim(0.25, 4.75)
    ax.set_aspect("equal")
    ax.axis("off")
    for a, b, label in EDGES:
        ax.add_patch(
            FancyArrowPatch(
                NODES[a],
                NODES[b],
                arrowstyle="-|>",
                mutation_scale=13,
                linewidth=LW,
                color=BLACK,
                shrinkA=24,
                shrinkB=24,
                zorder=1,
            )
        )
        x0, y0 = NODES[a]
        x1, y1 = NODES[b]
        ax.text(
            (x0 + x1) / 2,
            (y0 + y1) / 2 + 0.12,
            label,
            ha="center",
            fontsize=PROB_FS,
            color=BLACK,
        )
    for key in NODES:
        _node(ax, key, BLUE if key == "d" else GREEN if key == "n" else WHITE)
    ax.text(
        7.15,
        3.25,
        "positive tests:\nD and not-D\nare equally likely",
        ha="center",
        fontsize=_FS["body"],
        color=RED,
    )
    ax.text(
        4.1,
        0.35,
        "low base rate can dominate test accuracy",
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
    fig, ax = plt.subplots(figsize=(8, 4.8), layout="constrained")
    fig.suptitle("Bayes Tree", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
