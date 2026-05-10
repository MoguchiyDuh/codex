"""Generates resources/pictures/binary_tree_induction.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "binary_tree_induction.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
BLUE = _COL["blue"]
GREEN = _COL["green"]
PURPLE = _COL["purple"]
WHITE = _COL["white"]

NODE_R = 0.27

NODES = {
    "root": (3.5, 4.2, "I", BLUE),
    "l": (2.0, 3.0, "I", BLUE),
    "r": (5.0, 3.0, "I", BLUE),
    "ll": (1.2, 1.65, "L", GREEN),
    "lr": (2.8, 1.65, "L", GREEN),
    "rl": (4.2, 1.65, "L", GREEN),
    "rr": (5.8, 1.65, "L", GREEN),
}
EDGES = [
    ("root", "l"),
    ("root", "r"),
    ("l", "ll"),
    ("l", "lr"),
    ("r", "rl"),
    ("r", "rr"),
]


def _edge(ax: plt.Axes, a: str, b: str) -> None:
    x0, y0, _, _ = NODES[a]
    x1, y1, _, _ = NODES[b]
    ax.plot([x0, x1], [y0, y1], color=BLACK, linewidth=LW, zorder=1)


def _node(ax: plt.Axes, x: float, y: float, label: str, color: str) -> None:
    ax.add_patch(
        Circle((x, y), NODE_R, facecolor=color, edgecolor=BLACK, linewidth=LW, zorder=2)
    )
    ax.text(
        x,
        y,
        label,
        ha="center",
        va="center",
        fontsize=_FS["label"],
        fontweight="bold",
        color=BLACK,
        zorder=3,
    )


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 7)
    ax.set_ylim(0.4, 4.9)
    ax.set_aspect("equal")
    ax.axis("off")
    for a, b in EDGES:
        _edge(ax, a, b)
    for x, y, label, color in NODES.values():
        _node(ax, x, y, label, color)
    ax.text(
        3.5,
        0.75,
        r"combine two smaller trees: leaves = internal nodes + 1",
        ha="center",
        fontsize=_FS["label"],
        color=PURPLE,
    )


def main() -> None:
    plt.rcParams.update(
        {
            "figure.facecolor": _CFG["figure"]["facecolor"],
            "font.family": _CFG["font"]["family"],
            "font.sans-serif": _CFG["font"]["sans_serif"],
        }
    )
    fig, ax = plt.subplots(figsize=(6.4, 4.8), layout="constrained")
    fig.suptitle(
        "Structural Induction on Binary Trees",
        fontsize=_FS["suptitle"],
        fontweight="black",
    )
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
