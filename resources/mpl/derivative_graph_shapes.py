"""Generates resources/pictures/derivative_graph_shapes.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "derivative_graph_shapes.png"

# ── config aliases ─────────────────────────────────────────────────────────────
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
LW = _CFG["lines"]["linewidth"]

FIG_SIZE = (6.0, 7.5)


def main() -> None:
    plt.rcParams["font.family"] = _CFG["font"]["family"]
    plt.rcParams["font.sans-serif"] = _CFG["font"]["sans_serif"]
    plt.rcParams["text.color"] = BLACK

    fig, (ax1, ax2, ax3) = plt.subplots(
        3, 1, figsize=FIG_SIZE, sharex=True, layout="constrained"
    )

    x = np.linspace(-2.2, 2.2, 200)

    y = (x**3) / 3 - x
    dy = x**2 - 1
    d2y = 2 * x

    for ax in (ax1, ax2, ax3):
        ax.spines["top"].set_color("none")
        ax.spines["right"].set_color("none")
        ax.spines["left"].set_position("zero")
        ax.spines["bottom"].set_position("zero")
        ax.set_xticks([-1, 1])
        ax.set_xticklabels(["$-1$", "$1$"], fontsize=_FS["body"])
        ax.set_yticks([])

        ax.axvline(-1, color=GRAY, linestyle=":", linewidth=LW * 0.8)
        ax.axvline(1, color=GRAY, linestyle=":", linewidth=LW * 0.8)
        ax.axvline(0, color=GRAY, linestyle=":", linewidth=LW * 0.8)

    # ── f(x) ──────────────────────────────────────────────────────────────────
    ax1.plot(x, y, color=BLACK, linewidth=LW)
    ax1.text(-1.8, 1.2, "$f(x)$", fontsize=_FS["suptitle"], color=BLACK)

    y_max = 2 / 3
    y_min = -2 / 3
    ax1.plot(
        [-1, 1], [y_max, y_min], marker="o", markersize=5, color=BLACK, linestyle="none"
    )
    ax1.plot([0], [0], marker="o", markersize=5, color=RED, linestyle="none")

    ax1.text(
        -1,
        y_max + 0.15,
        "Local Max",
        ha="center",
        va="bottom",
        fontsize=_FS["label"],
        color=BLACK,
    )
    ax1.text(
        1,
        y_min - 0.15,
        "Local Min",
        ha="center",
        va="top",
        fontsize=_FS["label"],
        color=BLACK,
    )
    ax1.text(
        0.1,
        0.15,
        "Inflection",
        ha="left",
        va="bottom",
        fontsize=_FS["label"],
        color=RED,
    )

    # ── f'(x) ─────────────────────────────────────────────────────────────────
    ax2.plot(x, dy, color=BLACK, linewidth=LW)
    ax2.text(-1.5, 2.5, "$f'(x)$", fontsize=_FS["suptitle"], color=BLACK, ha="center")

    ax2.plot([-1, 1], [0, 0], marker="o", markersize=5, color=BLACK, linestyle="none")
    ax2.plot([0], [-1], marker="o", markersize=5, color=RED, linestyle="none")

    ax2.text(-1, 0.5, "$f'=0$", ha="center", va="bottom", fontsize=_FS["label"])
    ax2.text(1, 0.5, "$f'=0$", ha="center", va="bottom", fontsize=_FS["label"])
    ax2.text(
        0, -1.15, "Min slope", ha="center", va="top", fontsize=_FS["label"], color=RED
    )

    ax2.fill_between(x, dy, where=(dy > 0), color=GRAY, alpha=0.2)
    ax2.fill_between(x, dy, where=(dy < 0), color=RED, alpha=0.2)

    # ── f''(x) ────────────────────────────────────────────────────────────────
    ax3.plot(x, d2y, color=BLACK, linewidth=LW)
    ax3.text(-1.5, 2.0, "$f''(x)$", fontsize=_FS["suptitle"], color=BLACK, ha="center")

    ax3.plot([0], [0], marker="o", markersize=5, color=RED, linestyle="none")
    ax3.text(
        -0.2, 0.5, "$f''=0$", ha="right", va="bottom", fontsize=_FS["label"], color=RED
    )
    ax3.fill_between(x, d2y, where=(d2y > 0), color=GRAY, alpha=0.2)
    ax3.fill_between(x, d2y, where=(d2y < 0), color=RED, alpha=0.2)

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
