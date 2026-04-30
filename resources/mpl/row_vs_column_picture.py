"""Generates resources/pictures/row_vs_column_picture.png.

Three readings of the linear system 2x - y = 0, -x + 2y = 3 (x=1, y=2):
  Panel 1 — column picture:      x*a1 + y*a2 = b shown as tip-to-tail addition
  Panel 2 — row picture:         each equation is a line; solution = intersection
  Panel 3 — matrix transformation: A maps the input vector x to the output b

Style mirrors resources/mpl/basis_vectors_land.py and eigenvector_action.py:
  - integer grid via draw_grid(matrix=...) helper, axes drawn separately
  - dimmed/ghost elements use inline alpha at the call site (no shared constant)
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "row_vs_column_picture.png"

# ── config aliases ─────────────────────────────────────────────────────────────
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
GREEN = _COL["green"]
LW = _CFG["lines"]["linewidth"]

GRID_COL = GRAY
TGRID_COL = GREEN

# ── layout constants ───────────────────────────────────────────────────────────
FIG_SIZE = (18, 6)
LIM = 4

# System: 2x - y = 0; -x + 2y = 3  =>  x=1, y=2
A = np.array([[2.0, -1.0], [-1.0, 2.0]])
B_VEC = np.array([0.0, 3.0])
X_SOL = np.array([1.0, 2.0])


# ── helpers ────────────────────────────────────────────────────────────────────
def draw_vector(ax, end, color, start=(0, 0), label=None, label_pos=None, alpha=1.0):
    arrow = FancyArrowPatch(
        start,
        end,
        mutation_scale=14,
        color=color,
        linewidth=LW * 1.3,
        arrowstyle="-|>",
        zorder=5,
        alpha=alpha,
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
            alpha=alpha,
        )


def draw_grid(ax, matrix=None, color=GRID_COL, lw_scale=0.5, alpha=1.0):
    """Integer grid lines, skipping t=0 (axes drawn separately)."""
    ticks = [t for t in range(-int(LIM) - 3, int(LIM) + 4) if t != 0]
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


def setup_axes(ax, title):
    ax.set_title(title, fontsize=_FS["title"], pad=10)
    ax.set_aspect("equal")
    ax.set_xlim(-LIM, LIM)
    ax.set_ylim(-LIM, LIM)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines[:].set_visible(False)


def draw_axis_lines(ax, alpha=1.0):
    ax.plot([-LIM * 4, LIM * 4], [0, 0], color=BLACK, lw=LW, alpha=alpha, zorder=1)
    ax.plot([0, 0], [-LIM * 4, LIM * 4], color=BLACK, lw=LW, alpha=alpha, zorder=1)


# ── panel 1: column picture ───────────────────────────────────────────────────
def panel_column(ax):
    """Solid a1, a2 as reference; dimmed 2*a2 from origin then dimmed 1*a1 from
    its tip lands exactly on b. Tip-to-tail addition reads as a1 (ref) + the
    dimmed chain showing where the scaling takes you."""
    ax.set_ylim(-LIM + 2, LIM + 2)
    draw_grid(ax)
    draw_axis_lines(ax)

    a1, a2 = A[:, 0], A[:, 1]  # [2, -1] and [-1, 2]
    x, y = float(X_SOL[0]), float(X_SOL[1])

    draw_vector(ax, tuple(a1), BLUE, label=r"$\mathbf{a}_1$", label_pos=(1.7, -0.4))
    draw_vector(ax, tuple(a2), GREEN, label=r"$\mathbf{a}_2$", label_pos=(-1.4, 1.7))

    scaled2 = y * a2
    draw_vector(
        ax,
        tuple(scaled2),
        GREEN,
        label=r"$2\mathbf{a}_2$",
        label_pos=(-2.3, 3.5),
        alpha=0.4,
    )

    draw_vector(
        ax,
        tuple(scaled2 + x * a1),
        BLUE,
        start=tuple(scaled2),
        label=r"$1\mathbf{a}_1$",
        label_pos=(-0.7, 3.8),
        alpha=0.4,
    )

    draw_vector(ax, tuple(B_VEC), RED, label=r"$\mathbf{b}$", label_pos=(0.5, 2.5))


# ── panel 2: row picture ──────────────────────────────────────────────────────
def panel_row(ax):
    draw_grid(ax)
    draw_axis_lines(ax)

    t = np.linspace(-LIM, LIM, 300)
    ax.plot(t, 2 * t, color=BLUE, lw=LW, zorder=2)  # 2x - y = 0
    ax.plot(t, (t + 3) / 2, color=GREEN, lw=LW, zorder=2)  # -x + 2y = 3

    ax.scatter(*X_SOL, color=RED, s=70, zorder=6)
    ax.text(
        0.2,
        2.2,
        r"$(1,\,2)$",
        color=RED,
        fontsize=_FS["label"],
        fontweight="bold",
    )

    ax.plot(
        [X_SOL[0], X_SOL[0]], [0, X_SOL[1]], color=GRAY, lw=0.8, linestyle=":", zorder=2
    )
    ax.plot(
        [0, X_SOL[0]], [X_SOL[1], X_SOL[1]], color=GRAY, lw=0.8, linestyle=":", zorder=2
    )

    ax.text(
        2.25,
        1.1,
        r"$2x - y = 0$",
        color=BLUE,
        fontsize=_FS["label"],
        fontweight="bold",
        ha="right",
        va="bottom",
    )
    ax.text(
        -2.95,
        -0.2,
        r"$-x + 2y = 3$",
        color=GREEN,
        fontsize=_FS["label"],
        fontweight="bold",
        ha="left",
        va="top",
    )


# ── panel 3: matrix transformation ────────────────────────────────────────────
def panel_matrix(ax):
    draw_grid(ax, color=GRID_COL, alpha=0.25)
    draw_axis_lines(ax, alpha=0.25)

    draw_grid(ax, matrix=A, color=TGRID_COL, alpha=0.4)
    AX_LONG = LIM * 4
    origin_x = A @ np.array([[-AX_LONG, AX_LONG], [0, 0]])
    origin_y = A @ np.array([[0, 0], [-AX_LONG, AX_LONG]])
    ax.plot(origin_x[0], origin_x[1], color=BLACK, lw=LW, zorder=2)
    ax.plot(origin_y[0], origin_y[1], color=BLACK, lw=LW, zorder=2)

    draw_vector(ax, tuple(X_SOL), BLUE, label=r"$\mathbf{x}$", label_pos=(1.3, 1.8))

    draw_vector(
        ax,
        tuple(B_VEC),
        RED,
        label=r"$A\mathbf{x}=\mathbf{b}$",
        label_pos=(-0.7, 2.8),
    )

    ax.annotate(
        "",
        xy=tuple(B_VEC),
        xytext=tuple(X_SOL),
        arrowprops=dict(
            arrowstyle="-|>",
            color=BLACK,
            lw=LW * 0.8,
            connectionstyle="arc3,rad=-0.35",
            mutation_scale=10,
        ),
        zorder=4,
    )
    ax.text(-0.5, -0.5, r"$A$", color=BLACK, fontsize=_FS["label"], fontweight="bold")


# ── main ──────────────────────────────────────────────────────────────────────
def main() -> None:
    plt.rcParams["font.family"] = _CFG["font"]["family"]
    plt.rcParams["font.sans-serif"] = _CFG["font"]["sans_serif"]

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=FIG_SIZE, layout="constrained")
    fig.suptitle(
        r"$\left[ \genfrac{}{}{0}{0}{2x - y = 0}{-x + 2y = 3} \right] \quad \Rightarrow \quad \left[ \genfrac{}{}{0}{0}{x = 1}{y = 2} \right]$",
        fontsize=_FS["formula"],
        fontweight="bold",
    )

    titles = ["Column picture", "Row picture", "Matrix transformation"]
    for ax, title in zip([ax1, ax2, ax3], titles, strict=True):
        setup_axes(ax, title)

    panel_column(ax1)
    panel_row(ax2)
    panel_matrix(ax3)

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
