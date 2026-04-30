"""Generates resources/pictures/quadratic_inequalities.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "quadratic_inequalities.png"

# ── config aliases ─────────────────────────────────────────────────────────────
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
LW = _CFG["lines"]["linewidth"]

FIG_SIZE = (7.5, 3.5)


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

    # ── Frame 1: Graphical Method ─────────────────────────────────────────────
    x_min, x_max = 0.5, 4.5
    ax1.set_xlim(x_min, x_max)
    ax1.set_ylim(-1.5, 3.5)

    x_vals = np.linspace(x_min, x_max, 200)
    y_vals = x_vals**2 - 5 * x_vals + 6

    ax1.plot(x_vals, y_vals, color=BLACK, linewidth=LW)

    x_neg = np.linspace(2, 3, 100)
    y_neg = x_neg**2 - 5 * x_neg + 6
    ax1.plot(x_neg, y_neg, color=RED, linewidth=LW * 1.5)
    ax1.fill_between(x_neg, 0, y_neg, color=RED, alpha=0.2)

    ax1.plot(
        [2],
        [0],
        marker="o",
        markersize=6,
        markerfacecolor="white",
        markeredgecolor=RED,
        markeredgewidth=LW,
    )
    ax1.plot(
        [3],
        [0],
        marker="o",
        markersize=6,
        markerfacecolor="white",
        markeredgecolor=RED,
        markeredgewidth=LW,
    )

    ax1.text(2, 0.2, "$2$", ha="right", va="bottom", fontsize=_FS["body"])
    ax1.text(3, 0.2, "$3$", ha="left", va="bottom", fontsize=_FS["body"])

    ax1.set_title("Graphical Method\n$x^2 - 5x + 6 < 0$", fontsize=_FS["title"])
    ax1.text(
        2.5, -0.6, "$y < 0$", ha="center", va="top", fontsize=_FS["label"], color=RED
    )

    # ── Frame 2: Number Line Method ───────────────────────────────────────────
    ax2.set_xlim(x_min, x_max)
    ax2.set_ylim(-1, 1)
    ax2.spines["left"].set_color("none")

    ax2.plot([2, 3], [0, 0], color=RED, linewidth=LW * 2.5)

    ax2.plot(
        [2],
        [0],
        marker="o",
        markersize=8,
        markerfacecolor="white",
        markeredgecolor=RED,
        markeredgewidth=LW,
    )
    ax2.plot(
        [3],
        [0],
        marker="o",
        markersize=8,
        markerfacecolor="white",
        markeredgecolor=RED,
        markeredgewidth=LW,
    )

    ax2.text(2, -0.15, "$2$", ha="center", va="top", fontsize=_FS["body"])
    ax2.text(3, -0.15, "$3$", ha="center", va="top", fontsize=_FS["body"])

    ax2.text(
        1.25, 0.15, "$+$", ha="center", va="bottom", fontsize=_FS["label"], color=BLACK
    )
    ax2.text(
        2.5, 0.15, "$-$", ha="center", va="bottom", fontsize=_FS["label"], color=RED
    )
    ax2.text(
        3.75, 0.15, "$+$", ha="center", va="bottom", fontsize=_FS["label"], color=BLACK
    )

    ax2.set_title("Interval (Sign) Method\n" + r"$x \in (2, 3)$", fontsize=_FS["title"])

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
