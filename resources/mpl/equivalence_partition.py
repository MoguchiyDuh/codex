"""Generates resources/pictures/equivalence_partition.png."""

from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "equivalence_partition.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
BLUE = _COL["blue"]
GREEN = _COL["green"]
ORANGE = _COL["orange"]
WHITE = _COL["white"]

GROUPS = [
    ((1.8, 2.25), BLUE, ["-3", "0", "3", "6"], "[0]"),
    ((4.55, 2.25), GREEN, ["-2", "1", "4"], "[1]"),
    ((7.15, 2.25), ORANGE, ["-1", "2", "5"], "[2]"),
]
GROUP_R = 1.15


def _group(
    ax: plt.Axes, center: tuple[float, float], color: str, labels: list[str], name: str
) -> None:
    ax.add_patch(
        Circle(center, GROUP_R, facecolor=WHITE, edgecolor=color, linewidth=LW)
    )
    for i, label in enumerate(labels):
        theta = 2 * math.pi * i / len(labels)
        ax.text(
            center[0] + 0.52 * math.cos(theta),
            center[1] + 0.52 * math.sin(theta),
            label,
            ha="center",
            va="center",
            fontsize=_FS["body"],
            color=BLACK,
        )
    ax.text(center[0], 0.55, name, ha="center", fontsize=_FS["label"], color=color)


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 4.4)
    ax.set_aspect("equal")
    ax.axis("off")
    for args in GROUPS:
        _group(ax, *args)
    ax.text(
        4.5,
        3.95,
        r"congruence modulo $3$ partitions $\mathbb{Z}$",
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
    fig, ax = plt.subplots(figsize=(7.8, 4.2), layout="constrained")
    fig.suptitle(
        "Equivalence Classes Form a Partition",
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
