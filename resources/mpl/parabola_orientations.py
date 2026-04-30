"""Generates resources/pictures/parabola_orientations.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "parabola_orientations.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
LW = _CFG["lines"]["linewidth"]

FIG_SIZE = (7.0, 3.5)


def main() -> None:
    plt.rcParams["font.family"] = _CFG["font"]["family"]
    plt.rcParams["font.sans-serif"] = _CFG["font"]["sans_serif"]
    plt.rcParams["text.color"] = BLACK

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FIG_SIZE, layout="constrained")

    for ax in (ax1, ax2):
        ax.spines["top"].set_color("none")
        ax.spines["right"].set_color("none")
        ax.spines["left"].set_position("zero")
        ax.spines["bottom"].set_position("zero")
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlim(-3, 3)
        ax.set_ylim(-3, 3)

    t = np.linspace(-3, 3, 100)

    # 1. Vertical parabolas
    ax1.plot(t, t**2, color=BLACK, linewidth=LW)
    ax1.plot(t, -(t**2), color=RED, linewidth=LW)

    ax1.set_title("Vertical Form\n$y = a(x-h)^2 + k$", fontsize=_FS["title"])
    ax1.text(
        0,
        2.0,
        "$a > 0$ (Up)",
        color=BLACK,
        fontsize=_FS["label"],
        ha="center",
        va="center",
    )
    ax1.text(
        0,
        -2.0,
        "$a < 0$ (Down)",
        color=RED,
        fontsize=_FS["label"],
        ha="center",
        va="center",
    )

    # 2. Horizontal parabolas
    ax2.plot(t**2, t, color=BLACK, linewidth=LW)
    ax2.plot(-(t**2), t, color=RED, linewidth=LW)

    ax2.set_title("Horizontal Form\n$x = a(y-k)^2 + h$", fontsize=_FS["title"])
    ax2.text(
        2.0,
        0,
        "$a > 0$\n(Right)",
        color=BLACK,
        fontsize=_FS["label"],
        ha="center",
        va="center",
    )
    ax2.text(
        -2.0,
        0,
        "$a < 0$\n(Left)",
        color=RED,
        fontsize=_FS["label"],
        ha="center",
        va="center",
    )

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
