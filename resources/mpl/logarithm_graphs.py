"""Generates resources/pictures/logarithm_graphs.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "logarithm_graphs.png"

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

    ax.set_xticks([1, 2, 4, np.exp(1)])
    ax.set_xticklabels(["$1$", "$2$", "$4$", "$e$"])
    ax.set_yticks([-2, -1, 1, 2])
    ax.set_yticklabels(["$-2$", "$-1$", "$1$", "$2$"])

    x_min, x_max = -0.5, 7.5
    y_min, y_max = -2.5, 2.5
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)

    x_vals = np.linspace(0.01, x_max, 400)

    # Plots
    ax.plot(x_vals, np.log2(x_vals), color=BLACK, linewidth=LW)
    ax.plot(x_vals, np.log(x_vals), color=RED, linewidth=LW)
    ax.plot(x_vals, np.log10(x_vals), color=GRAY, linewidth=LW, linestyle="--")

    # Intersection point (1, 0)
    ax.plot([1], [0], marker="o", markersize=6, color=BLACK)
    ax.text(
        1.1, -0.2, "$(1, 0)$", ha="left", va="top", fontsize=_FS["small"], color=BLACK
    )

    # Text labels directly on the lines
    ax.text(
        4.5,
        np.log2(4.5) - 0.15,
        r"$y = \log_2 x$",
        color=BLACK,
        fontsize=_FS["label"],
        ha="left",
        va="top",
    )
    ax.text(
        5.5,
        np.log(5.5) - 0.1,
        r"$y = \ln x$",
        color=RED,
        fontsize=_FS["label"],
        ha="left",
        va="top",
    )
    ax.text(
        6.0,
        np.log10(6.0) - 0.2,
        r"$y = \log_{10} x$",
        color=GRAY,
        fontsize=_FS["label"],
        ha="left",
        va="top",
    )

    # Axes labels
    ax.text(
        x_max, -0.2, "$x$", ha="center", va="top", fontsize=_FS["label"], style="italic"
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
