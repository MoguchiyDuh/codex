"""Generates resources/pictures/quadratic_discriminant.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "quadratic_discriminant.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
PURPLE = _COL["purple"]
LW = _CFG["lines"]["linewidth"]

FIG_SIZE = (9, 3.5)


def main() -> None:
    plt.rcParams["font.family"] = _CFG["font"]["family"]
    plt.rcParams["font.sans-serif"] = _CFG["font"]["sans_serif"]
    plt.rcParams["text.color"] = BLACK

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=FIG_SIZE, layout="constrained")

    x = np.linspace(-2, 2, 200)

    ax1.plot(x, x**2 - 1, color=RED, linewidth=LW)
    ax1.set_title("$D > 0$\nTwo real roots", fontsize=_FS["title"])
    ax1.plot([-1, 1], [0, 0], marker="o", color=RED, linestyle="None")

    ax2.plot(x, x**2, color=BLUE, linewidth=LW)
    ax2.set_title("$D = 0$\nOne repeated root", fontsize=_FS["title"])
    ax2.plot([0], [0], marker="o", color=BLUE, linestyle="None")

    ax3.plot(x, x**2 + 1, color=PURPLE, linewidth=LW)
    ax3.set_title("$D < 0$\nNo real roots", fontsize=_FS["title"])

    for ax in (ax1, ax2, ax3):
        ax.axhline(0, color=BLACK, linewidth=LW / 2)
        ax.axvline(0, color=GRAY, linewidth=LW / 2, linestyle=":")
        ax.set_xlim(-2, 2)
        ax.set_ylim(-1.5, 3)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
        ax.spines["bottom"].set_visible(False)

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
