"""Generates resources/pictures/vector_addition.png.

Illustrates vector addition using the parallelogram rule.
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "vector_addition.png"

# ── config aliases ─────────────────────────────────────────────────────────────
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
PURPLE = _COL["purple"]
LW = _CFG["lines"]["linewidth"]


def draw_vector(ax, start, end, color, label=None, offset=(0.1, 0.1), fs="formula"):
    arrow = FancyArrowPatch(
        start,
        end,
        mutation_scale=15,
        color=color,
        linewidth=LW * 1.5,
        arrowstyle="-|>",
        zorder=5,
    )
    ax.add_patch(arrow)
    if label:
        ax.text(
            end[0] + offset[0],
            end[1] + offset[1],
            label,
            color=color,
            fontsize=_FS[fs],
            fontweight="bold",
            ha="center",
            va="center",
        )


def main() -> None:
    plt.rcParams["font.family"] = _CFG["font"]["family"]
    plt.rcParams["font.sans-serif"] = _CFG["font"]["sans_serif"]

    fig, ax = plt.subplots(figsize=(6, 5), layout="constrained")
    ax.set_title(
        "Vector Addition", fontsize=_FS["suptitle"], fontweight="black", pad=20
    )
    ax.set_aspect("equal")
    ax.set_xlim(-0.5, 5)
    ax.set_ylim(-0.5, 4.5)
    ax.axis("off")

    U = np.array([3, 1])
    V = np.array([1, 3])
    W = U + V

    for i in range(6):
        ax.axhline(i, color=GRAY, lw=0.5, zorder=0)
        ax.axvline(i, color=GRAY, lw=0.5, zorder=0)

    ax.plot(
        [V[0], W[0]], [V[1], W[1]], color=BLACK, linestyle="--", lw=LW * 0.8, zorder=1
    )

    draw_vector(ax, (0, 0), U, BLUE, r"$\mathbf{u}$", (0.3, -0.2))
    draw_vector(ax, (0, 0), V, RED, r"$\mathbf{v}$", (-0.3, 0.2))

    arrow_v_prime = FancyArrowPatch(
        U,
        W,
        mutation_scale=12,
        color=RED,
        alpha=0.5,
        linewidth=LW,
        arrowstyle="-|>",
        zorder=5,
    )
    ax.add_patch(arrow_v_prime)
    ax.text(
        (U[0] + W[0]) / 2 + 0.3,
        (U[1] + W[1]) / 2 + 0.3,
        r"$\mathbf{v}'$",
        color=RED,
        alpha=0.5,
        fontsize=_FS["formula"],
        fontweight="bold",
    )

    draw_vector(ax, (0, 0), W, PURPLE, r"$\mathbf{u} + \mathbf{v}$", (0.6, 0.3))

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
