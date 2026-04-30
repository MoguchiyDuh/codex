"""Generates resources/pictures/discontinuity.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "discontinuity.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
LW = _CFG["lines"]["linewidth"]

FIG_SIZE = (8.0, 3.0)


def main() -> None:
    plt.rcParams["font.family"] = _CFG["font"]["family"]
    plt.rcParams["font.sans-serif"] = _CFG["font"]["sans_serif"]
    plt.rcParams["text.color"] = BLACK

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=FIG_SIZE, layout="constrained")

    for ax in (ax1, ax2, ax3):
        ax.spines["top"].set_color("none")
        ax.spines["right"].set_color("none")
        ax.spines["left"].set_position("zero")
        ax.spines["bottom"].set_position("zero")
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 3)

    bbox_white = dict(facecolor="white", edgecolor="none", pad=2)

    # ── Removable Discontinuity ───────────────────────────────────────────────
    x1 = np.linspace(-2, -0.1, 50)
    x2 = np.linspace(0.1, 2, 50)

    ax1.plot(x1, 1 - 0.5 * x1**2, color=BLACK, linewidth=LW)
    ax1.plot(x2, 1 - 0.5 * x2**2, color=BLACK, linewidth=LW)

    ax1.plot(
        [0],
        [1],
        marker="o",
        markersize=6,
        markerfacecolor="white",
        markeredgecolor=BLACK,
        markeredgewidth=LW * 0.8,
    )
    ax1.plot([0], [2], marker="o", markersize=6, color=BLACK)

    ax1.set_title("Removable", fontsize=_FS["title"])
    ax1.text(
        0,
        -1.8,
        "Limit exists\n$f(a)$ differs or undefined",
        ha="center",
        fontsize=_FS["body"],
        color=BLACK,
        bbox=bbox_white,
    )

    # ── Jump Discontinuity ────────────────────────────────────────────────────
    x3 = np.linspace(-2, 0, 50)
    x4 = np.linspace(0.001, 2, 50)

    ax2.plot(x3, x3 + 1, color=BLACK, linewidth=LW)
    ax2.plot(x4, x4 - 1, color=BLACK, linewidth=LW)

    ax2.plot([0], [1], marker="o", markersize=6, color=BLACK)
    ax2.plot(
        [0],
        [-1],
        marker="o",
        markersize=6,
        markerfacecolor="white",
        markeredgecolor=BLACK,
        markeredgewidth=LW * 0.8,
    )

    ax2.set_title("Jump", fontsize=_FS["title"])
    ax2.text(
        0,
        -1.8,
        "One-sided limits\nexist but differ",
        ha="center",
        fontsize=_FS["body"],
        color=BLACK,
        bbox=bbox_white,
    )

    # ── Infinite Discontinuity ────────────────────────────────────────────────
    x5 = np.linspace(-2, -0.1, 50)
    x6 = np.linspace(0.1, 2, 50)

    ax3.plot(x5, -1 / x5, color=BLACK, linewidth=LW)
    ax3.plot(x6, 1 / x6, color=BLACK, linewidth=LW)

    ax3.axvline(0, color=RED, linestyle="--", linewidth=LW * 0.8)

    ax3.set_title("Infinite", fontsize=_FS["title"])
    ax3.text(
        0,
        -1.8,
        "Vertical asymptote",
        ha="center",
        fontsize=_FS["body"],
        color=BLACK,
        bbox=bbox_white,
    )

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
