"""Generates resources/pictures/integral_showcase.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "integral_showcase.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
LW = _CFG["lines"]["linewidth"]

FIG_SIZE = (5.5, 3.8)


def f(x: float | np.ndarray) -> float | np.ndarray:
    return -0.4 * (x - 2.5) ** 2 + 3.5


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

    x_min, x_max = -0.2, 5.0
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(-0.2, 4.0)

    # Plot curve
    x_vals = np.linspace(0, 4.8, 200)
    y_vals = f(x_vals)
    ax.plot(x_vals, y_vals, color=BLACK, linewidth=LW)

    # Shaded region
    a, b = 1.0, 4.0
    x_fill = np.linspace(a, b, 100)
    y_fill = f(x_fill)

    # Use fill_between to shade
    ax.fill_between(x_fill, 0, y_fill, color=RED, alpha=0.2)

    # Boundary lines
    ax.plot([a, a], [0, f(a)], color=RED, linestyle="--", linewidth=LW * 0.8)
    ax.plot([b, b], [0, f(b)], color=RED, linestyle="--", linewidth=LW * 0.8)

    # Labels
    ax.text(a, -0.1, "$a$", ha="center", va="top", fontsize=_FS["label"], color=RED)
    ax.text(b, -0.1, "$b$", ha="center", va="top", fontsize=_FS["label"], color=RED)

    ax.text(
        x_max, -0.1, "$x$", ha="center", va="top", fontsize=_FS["label"], style="italic"
    )
    ax.text(
        -0.1, 4.0, "$y$", ha="right", va="center", fontsize=_FS["label"], style="italic"
    )

    # Formula in the center of the shaded region
    mid_x = (a + b) / 2
    mid_y = f(mid_x) / 2
    ax.text(
        mid_x,
        mid_y,
        r"$\int_a^b f(x)\,dx$",
        ha="center",
        va="center",
        fontsize=_FS["formula"],
        color=RED,
    )

    # Curve label
    ax.text(4.2, f(4.2) + 0.3, "$f(x)$", fontsize=_FS["label"])

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
