"""Generates resources/pictures/cantor_pairing.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "cantor_pairing.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
WHITE = _COL["white"]

N = 5
NODE_R = 0.14


def _node(ax: plt.Axes, x: int, y: int, label: str) -> None:
    ax.add_patch(
        Circle(
            (x, y),
            NODE_R,
            facecolor=WHITE,
            edgecolor=BLACK,
            linewidth=LW * 0.7,
            zorder=3,
        )
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


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(-0.55, 5.5)
    ax.set_ylim(-0.55, 5.8)
    ax.set_aspect("equal")
    ax.axis("off")
    for t in range(N + 1):
        ax.plot([t, t], [0, N], color=GRAY, linewidth=0.8, linestyle=":")
        ax.plot([0, N], [t, t], color=GRAY, linewidth=0.8, linestyle=":")
    points = [(i, s - i) for s in range(N + 1) for i in range(s + 1)]
    for label, (x, y) in enumerate(points):
        _node(ax, x, y, str(label))
    for a, b in zip(points[:-1], points[1:], strict=True):
        ax.add_patch(
            FancyArrowPatch(
                a,
                b,
                arrowstyle="-|>",
                mutation_scale=10,
                linewidth=LW,
                color=RED,
                zorder=2,
            )
        )
    ax.text(
        2.5,
        5.45,
        r"enumerate $\mathbb{N}\times\mathbb{N}$ by diagonals",
        ha="center",
        fontsize=_FS["label"],
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
    fig, ax = plt.subplots(figsize=(6, 5.8), layout="constrained")
    fig.suptitle("Cantor Pairing", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
