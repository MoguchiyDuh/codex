"""Generates resources/pictures/vertical_asymptote.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "vertical_asymptote.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
LW = _CFG["lines"]["linewidth"]

FIG_SIZE = (5.5, 4.0)


def main() -> None:
    plt.rcParams["font.family"] = _CFG["font"]["family"]
    plt.rcParams["font.sans-serif"] = _CFG["font"]["sans_serif"]
    plt.rcParams["text.color"] = BLACK

    fig, ax = plt.subplots(figsize=FIG_SIZE, layout="constrained")

    ax.spines["top"].set_color("none")
    ax.spines["right"].set_color("none")
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")

    ax.set_xticks([])
    ax.set_yticks([])

    ax.set_xlim(-1, 5)
    ax.set_ylim(-1, 6)

    a = 2.0
    L = 1.0

    x_left = np.linspace(-1, a - 0.1, 100)
    y_left = 1 / (x_left - a) ** 2 + L
    ax.plot(x_left, y_left, color=BLACK, linewidth=LW)

    x_right = np.linspace(a + 0.1, 5, 100)
    y_right = 1 / (x_right - a) ** 2 + L
    ax.plot(x_right, y_right, color=BLACK, linewidth=LW)

    ax.plot([a, a], [0, 6], color=RED, linestyle="--", linewidth=LW * 0.8)
    ax.plot([0, 5], [L, L], color=RED, linestyle="--", linewidth=LW * 0.8)

    ax.text(a, -0.2, "$a$", ha="center", va="top", fontsize=_FS["label"], color=RED)
    ax.text(-0.2, L, "$L$", ha="right", va="center", fontsize=_FS["label"], color=RED)

    ax.text(
        5, -0.2, "$x$", ha="center", va="top", fontsize=_FS["label"], style="italic"
    )
    ax.text(
        -0.2, 6, "$y$", ha="right", va="center", fontsize=_FS["label"], style="italic"
    )

    ax.text(
        0.2,
        4.0,
        "Vertical Asymptote\n$\\lim_{x\\to a} f(x) = \\infty$",
        color=RED,
        fontsize=_FS["small"],
        va="center",
        ha="left",
    )

    ax.text(
        4.8,
        L - 0.2,
        "Horizontal Asymptote\n$\\lim_{x\\to \\infty} f(x) = L$",
        color=RED,
        fontsize=_FS["small"],
        ha="right",
        va="top",
    )

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
