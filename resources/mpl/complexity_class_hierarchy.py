"""Generates resources/pictures/complexity_class_hierarchy.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "complexity_class_hierarchy.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
BLUE = _COL["blue"]
PURPLE = _COL["purple"]
ORANGE = _COL["orange"]
WHITE = _COL["white"]


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.add_patch(
        Ellipse((5, 3), 8.4, 5.0, facecolor=WHITE, edgecolor=BLACK, linewidth=LW)
    )
    ax.text(8.2, 5.1, "EXP", fontsize=_FS["label"], color=BLACK)
    ax.add_patch(
        Ellipse(
            (4.35, 3),
            5.4,
            3.2,
            facecolor=ORANGE,
            edgecolor=BLACK,
            linewidth=LW,
            alpha=0.35,
        )
    )
    ax.text(1.75, 4.3, "NP", fontsize=_FS["label"], color=BLACK)
    ax.add_patch(
        Ellipse(
            (5.65, 3),
            5.4,
            3.2,
            facecolor=PURPLE,
            edgecolor=BLACK,
            linewidth=LW,
            alpha=0.35,
        )
    )
    ax.text(7.05, 4.3, "co-NP", fontsize=_FS["label"], color=BLACK)
    ax.add_patch(
        Ellipse((5, 3), 2.0, 1.35, facecolor=BLUE, edgecolor=BLACK, linewidth=LW)
    )
    ax.text(
        5,
        3,
        "P",
        ha="center",
        va="center",
        fontsize=_FS["formula"],
        color=BLACK,
        fontweight="bold",
    )
    ax.text(
        5,
        1.2,
        "known: P is inside both NP and co-NP",
        ha="center",
        fontsize=_FS["body"],
        color=BLACK,
    )
    ax.text(
        5,
        0.82,
        "open: whether P = NP, and whether NP = co-NP",
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
    fig, ax = plt.subplots(figsize=(8.5, 5.5), layout="constrained")
    fig.suptitle(
        "Complexity Class Containment", fontsize=_FS["suptitle"], fontweight="black"
    )
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
