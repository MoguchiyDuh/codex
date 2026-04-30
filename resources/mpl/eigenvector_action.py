"""Generates resources/pictures/eigenvector_action.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "eigenvector_action.png"

# ── config aliases ─────────────────────────────────────────────────────────────
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
BLUE = _COL["blue"]
LW = _CFG["lines"]["linewidth"]

GRID_COL = _COL["gray"]
TGRID_COL = _COL["green"]
GHOST_ALPHA = 0.25

# ── layout constants ───────────────────────────────────────────────────────────
FIG_SIZE = (7, 4)
LIM = 4

A = np.array([[1.3, 0.4], [0.2, 1.1]])
V = np.array([2.0, 1.0])
U1 = np.array([1.5, 0.0])
U2 = np.array([0.0, 1.5])


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
            fontsize=_FS["label"],
            ha="center",
            va="center",
            fontweight="bold",
        )


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
        ax.plot(xs_v, ys_v, color=color, lw=LW * lw_scale, alpha=alpha, zorder=0)
        ax.plot(xs_h, ys_h, color=color, lw=LW * lw_scale, alpha=alpha, zorder=0)


def main() -> None:
    plt.rcParams["font.family"] = _CFG["font"]["family"]
    plt.rcParams["font.sans-serif"] = _CFG["font"]["sans_serif"]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FIG_SIZE, layout="constrained")

    for ax, title in zip(
        [ax1, ax2], ["Standard Grid", "Transformed Grid"], strict=True
    ):
        ax.set_title(title, fontsize=_FS["title"], pad=10)
        ax.set_aspect("equal")
        ax.set_xlim(-LIM, LIM)
        ax.set_ylim(-LIM, LIM)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.spines[:].set_visible(False)

    # ── Frame 1: Standard grid ────────────────────────────────────────────────
    draw_grid(ax1, color=GRID_COL)
    ax1.plot([-LIM, LIM], [0, 0], color=BLACK, lw=LW, zorder=1)
    ax1.plot([0, 0], [-LIM, LIM], color=BLACK, lw=LW, zorder=1)

    t = np.linspace(-LIM, LIM, 2)
    ax1.plot(t, 0.5 * t, color=BLUE, linestyle="--", lw=LW * 0.8, zorder=2)

    draw_vector(ax1, V, BLUE, r"$\mathbf{v}$", (1.5, 1.3))
    draw_vector(ax1, U1, BLACK, r"$\mathbf{u}_1$", (1.3, -0.35))
    draw_vector(ax1, U2, BLACK, r"$\mathbf{u}_2$", (-0.4, 1.3))

    # ── Frame 2: Transformed grid ─────────────────────────────────────────────
    draw_grid(ax2, color=GRID_COL, lw_scale=0.5, alpha=GHOST_ALPHA)
    ax2.plot([-LIM, LIM], [0, 0], color=BLACK, lw=LW, alpha=GHOST_ALPHA, zorder=1)
    ax2.plot([0, 0], [-LIM, LIM], color=BLACK, lw=LW, alpha=GHOST_ALPHA, zorder=1)

    draw_grid(ax2, matrix=A, color=TGRID_COL, lw_scale=0.5, alpha=0.4)
    AX_LONG = LIM * 4
    origin_x = A @ np.array([[-AX_LONG, AX_LONG], [0, 0]])
    origin_y = A @ np.array([[0, 0], [-AX_LONG, AX_LONG]])
    ax2.plot(origin_x[0], origin_x[1], color=BLACK, lw=LW, zorder=2)
    ax2.plot(origin_y[0], origin_y[1], color=BLACK, lw=LW, zorder=2)

    ax2.plot(t, 0.5 * t, color=BLUE, linestyle="--", lw=LW * 0.8, zorder=2)

    AV = A @ V
    AU1 = A @ U1
    AU2 = A @ U2
    draw_vector(ax2, AV, BLUE, r"$A\mathbf{v}$", (2.6, 1.8))
    draw_vector(ax2, AU1, BLACK, r"$A\mathbf{u}_1$", (1.9, -0.3))
    draw_vector(ax2, AU2, BLACK, r"$A\mathbf{u}_2$", (0.35, 2.1))

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
