"""Generates resources/pictures/induction_dominoes.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.transforms as transforms
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "induction_dominoes.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
PURPLE = _COL["purple"]
WHITE = _COL["white"]

DOMINO_W = 0.26
DOMINO_H = 1.45
DOMINO_Y = 1.05
DOMINO_ANGLE = -18


def _domino(ax: plt.Axes, x: float, label: str, angle: float) -> None:
    rect = Rectangle(
        (-DOMINO_W / 2, 0),
        DOMINO_W,
        DOMINO_H,
        facecolor=WHITE,
        edgecolor=BLACK,
        linewidth=LW,
    )
    rect.set_transform(
        transforms.Affine2D().rotate_deg_around(0, 0, angle).translate(x, DOMINO_Y)
        + ax.transData
    )
    ax.add_patch(rect)
    ax.text(
        x, 0.62, label, ha="center", va="center", fontsize=_FS["small"], color=BLACK
    )


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.set_aspect("equal")
    ax.axis("off")
    xs = [1.0 + i * 1.05 for i in range(8)]
    for i, x in enumerate(xs):
        _domino(ax, x, rf"$P({i})$", 0 if i == 0 else DOMINO_ANGLE)
    ax.add_patch(
        FancyArrowPatch(
            (1.05, 3.1),
            (8.15, 3.1),
            arrowstyle="-|>",
            mutation_scale=18,
            linewidth=LW,
            color=PURPLE,
        )
    )
    ax.text(
        4.65,
        3.35,
        "base case plus inductive step",
        ha="center",
        fontsize=_FS["label"],
        color=BLACK,
    )
    ax.text(
        4.65,
        0.18,
        "Once P(0) holds, P(n) -> P(n+1) propagates forever",
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
    fig, ax = plt.subplots(figsize=(8, 3.8), layout="constrained")
    fig.suptitle("Induction as Dominoes", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
