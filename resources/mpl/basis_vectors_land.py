"""Generates resources/pictures/basis_vectors_land.png.

Shows how standard basis vectors i_hat, j_hat land after a linear transformation.
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "basis_vectors_land.png"

# ── config aliases ─────────────────────────────────────────────────────────────
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
LW = _CFG["lines"]["linewidth"]

# ── layout constants ───────────────────────────────────────────────────────────
FIG_SIZE = (7, 4)
LIM = 3.5

A = np.array([[2.0, 1.0], [0.5, 1.5]])
I_HAT = np.array([1, 0])
J_HAT = np.array([0, 1])

GRID_COL = _COL["gray"]
TGRID_COL = _COL["green"]
GHOST_ALPHA = 0.25


def draw_grid(ax, matrix=None, color=GRID_COL, lw_scale=0.5, alpha=1.0):
    """Draw integer grid lines, skipping t=0 (drawn separately as axes)."""
    ticks = [t for t in range(-int(LIM) - 1, int(LIM) + 2) if t != 0]
    for t in ticks:
        xs_v = np.array([t, t], dtype=float)
        ys_v = np.array([-LIM * 4, LIM * 4], dtype=float)
        xs_h = np.array([-LIM * 4, LIM * 4], dtype=float)
        ys_h = np.array([t, t], dtype=float)

        if matrix is not None:
            pts_v = matrix @ np.array([xs_v, ys_v])
            xs_v, ys_v = pts_v[0], pts_v[1]
            pts_h = matrix @ np.array([xs_h, ys_h])
            xs_h, ys_h = pts_h[0], pts_h[1]

        ax.plot(
            xs_v,
            ys_v,
            color=color,
            lw=LW * lw_scale,
            linestyle="-",
            alpha=alpha,
            zorder=0,
        )
        ax.plot(
            xs_h,
            ys_h,
            color=color,
            lw=LW * lw_scale,
            linestyle="-",
            alpha=alpha,
            zorder=0,
        )


def draw_vector(ax, end, color, label=None, label_pos=None):
    arrow = FancyArrowPatch(
        (0, 0),
        end,
        mutation_scale=12,
        color=color,
        linewidth=LW * 1.2,
        arrowstyle="-|>",
        zorder=5,
    )
    ax.add_patch(arrow)
    if label and label_pos is not None:
        ax.text(
            *label_pos,
            label,
            color=color,
            fontsize=_FS["body"],
            ha="center",
            va="center",
            fontweight="bold",
        )


def main() -> None:
    plt.rcParams["font.family"] = _CFG["font"]["family"]
    plt.rcParams["font.sans-serif"] = _CFG["font"]["sans_serif"]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FIG_SIZE, layout="constrained")

    for ax, title in zip(
        [ax1, ax2], ["Standard Basis", "Transformed Space"], strict=True
    ):
        ax.set_title(title, fontsize=_FS["title"], pad=10)
        ax.set_aspect("equal")
        ax.set_xlim(-LIM, LIM)
        ax.set_ylim(-LIM, LIM)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.spines[:].set_visible(False)

    # ── Frame 1: Standard Basis ───────────────────────────────────────────────
    draw_grid(ax1, color=GRID_COL)
    ax1.plot([-LIM, LIM], [0, 0], color=BLACK, lw=LW, zorder=1)
    ax1.plot([0, 0], [-LIM, LIM], color=BLACK, lw=LW, zorder=1)

    draw_vector(ax1, I_HAT, RED, r"$\hat{\mathbf{i}}$", (0.6, -0.4))
    draw_vector(ax1, J_HAT, BLUE, r"$\hat{\mathbf{j}}$", (-0.55, 0.7))

    # ── Frame 2: Transformed ──────────────────────────────────────────────────
    draw_grid(ax2, color=GRID_COL, lw_scale=0.5, alpha=GHOST_ALPHA)
    ax2.plot([-LIM, LIM], [0, 0], color=BLACK, lw=LW, alpha=GHOST_ALPHA, zorder=1)
    ax2.plot([0, 0], [-LIM, LIM], color=BLACK, lw=LW, alpha=GHOST_ALPHA, zorder=1)

    draw_grid(ax2, matrix=A, color=TGRID_COL, lw_scale=0.5, alpha=0.5)
    AX_LONG = LIM * 4
    origin_x = A @ np.array([[-AX_LONG, AX_LONG], [0, 0]])
    origin_y = A @ np.array([[0, 0], [-AX_LONG, AX_LONG]])
    ax2.plot(origin_x[0], origin_x[1], color=BLACK, lw=LW, zorder=2)
    ax2.plot(origin_y[0], origin_y[1], color=BLACK, lw=LW, zorder=2)

    TI = A @ I_HAT
    TJ = A @ J_HAT
    draw_vector(ax2, TI, RED, r"$T(\hat{\mathbf{i}})$", (TI[0], TI[1] - 0.4))
    draw_vector(ax2, TJ, BLUE, r"$T(\hat{\mathbf{j}})$", (TJ[0] - 0.5, TJ[1] + 0.1))

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
