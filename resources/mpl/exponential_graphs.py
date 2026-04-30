"""Generates resources/pictures/exponential_graphs.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "exponential_graphs.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
LW = _CFG["lines"]["linewidth"]

FIG_SIZE = (6.0, 4.5)


def main() -> None:
    plt.rcParams["font.family"] = _CFG["font"]["family"]
    plt.rcParams["font.sans-serif"] = _CFG["font"]["sans_serif"]
    plt.rcParams["text.color"] = BLACK

    fig, ax = plt.subplots(figsize=FIG_SIZE, layout="constrained")

    ax.spines["top"].set_color("none")
    ax.spines["right"].set_color("none")
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")

    # Grid and ticks
    ax.set_xticks([-2, -1, 1, 2])
    ax.set_xticklabels(["$-2$", "$-1$", "$1$", "$2$"])
    ax.set_yticks([1, 2, 4, 6])
    ax.set_yticklabels(["$1$", "$2$", "$4$", "$6$"])

    x_min, x_max = -2.5, 2.5
    y_min, y_max = -0.5, 7.5
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)

    x_vals = np.linspace(x_min, x_max, 200)

    # Plots
    ax.plot(x_vals, 2**x_vals, color=BLACK, linewidth=LW, label=r"$y = 2^x$")
    ax.plot(x_vals, np.exp(x_vals), color=RED, linewidth=LW, label=r"$y = e^x$")
    ax.plot(
        x_vals,
        (1 / 2) ** x_vals,
        color=GRAY,
        linewidth=LW,
        linestyle="--",
        label=r"$y = (1/2)^x$",
    )

    # Intersection point (0, 1)
    ax.plot([0], [1], marker="o", markersize=6, color=BLACK)
    ax.text(
        -0.1,
        1.2,
        "$(0, 1)$",
        ha="right",
        va="bottom",
        fontsize=_FS["small"],
        color=BLACK,
    )

    # Text labels directly on the lines
    ax.text(
        1.8,
        2**1.8 - 0.2,
        "$y = 2^x$",
        color=BLACK,
        fontsize=_FS["label"],
        ha="left",
        va="top",
    )
    ax.text(
        1.4,
        np.exp(1.4) + 0.2,
        "$y = e^x$",
        color=RED,
        fontsize=_FS["label"],
        ha="right",
        va="bottom",
    )
    ax.text(
        -1.8,
        (1 / 2) ** -1.8 + 0.2,
        "$y = (1/2)^x$",
        color=GRAY,
        fontsize=_FS["label"],
        ha="left",
        va="bottom",
    )

    # Axes labels
    ax.text(
        x_max, -0.3, "$x$", ha="center", va="top", fontsize=_FS["label"], style="italic"
    )
    ax.text(
        -0.2,
        y_max,
        "$y$",
        ha="right",
        va="center",
        fontsize=_FS["label"],
        style="italic",
    )

    # Origin
    bbox_white = dict(facecolor="white", edgecolor="none", pad=1)
    ax.text(
        -0.15, -0.15, "0", ha="right", va="top", fontsize=_FS["body"], bbox=bbox_white
    )

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
