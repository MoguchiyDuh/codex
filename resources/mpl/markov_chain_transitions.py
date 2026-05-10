"""Generates resources/pictures/markov_chain_transitions.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "markov_chain_transitions.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
BLUE = _COL["blue"]
GREEN = _COL["green"]
WHITE = _COL["white"]

NODE_R = 0.48
SUNNY = (2.0, 2.0)
RAINY = (5.0, 2.0)


def _node(ax: plt.Axes, xy: tuple[float, float], label: str, color: str) -> None:
    ax.add_patch(
        Circle(xy, NODE_R, facecolor=color, edgecolor=BLACK, linewidth=LW, zorder=3)
    )
    ax.text(
        *xy,
        label,
        ha="center",
        va="center",
        fontsize=_FS["label"],
        fontweight="bold",
        color=BLACK,
        zorder=4,
    )


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 4)
    ax.set_aspect("equal")
    ax.axis("off")
    _node(ax, SUNNY, "S", BLUE)
    _node(ax, RAINY, "R", GREEN)
    ax.add_patch(
        FancyArrowPatch(
            SUNNY,
            RAINY,
            arrowstyle="-|>",
            mutation_scale=14,
            linewidth=LW,
            color=BLACK,
            shrinkA=34,
            shrinkB=34,
            connectionstyle="arc3,rad=0.15",
        )
    )
    ax.add_patch(
        FancyArrowPatch(
            RAINY,
            SUNNY,
            arrowstyle="-|>",
            mutation_scale=14,
            linewidth=LW,
            color=BLACK,
            shrinkA=34,
            shrinkB=34,
            connectionstyle="arc3,rad=0.15",
        )
    )
    ax.add_patch(
        FancyArrowPatch(
            (1.65, 2.45),
            (1.65, 1.55),
            arrowstyle="-|>",
            mutation_scale=13,
            linewidth=LW,
            color=BLUE,
            connectionstyle="arc3,rad=1.4",
        )
    )
    ax.add_patch(
        FancyArrowPatch(
            (5.35, 1.55),
            (5.35, 2.45),
            arrowstyle="-|>",
            mutation_scale=13,
            linewidth=LW,
            color=GREEN,
            connectionstyle="arc3,rad=1.4",
        )
    )
    ax.text(3.5, 2.45, "0.1", ha="center", fontsize=_FS["label"], color=BLACK)
    ax.text(3.5, 1.25, "0.5", ha="center", fontsize=_FS["label"], color=BLACK)
    ax.text(1.05, 2.0, "0.9", ha="center", fontsize=_FS["label"], color=BLACK)
    ax.text(5.95, 2.0, "0.5", ha="center", fontsize=_FS["label"], color=BLACK)
    ax.text(
        3.5,
        0.35,
        "each row of the transition matrix sums to 1",
        ha="center",
        fontsize=_FS["body"],
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
    fig, ax = plt.subplots(figsize=(6.5, 4), layout="constrained")
    fig.suptitle(
        "Markov Chain Transitions", fontsize=_FS["suptitle"], fontweight="black"
    )
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
