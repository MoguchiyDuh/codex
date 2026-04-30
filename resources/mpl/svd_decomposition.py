"""Generates resources/pictures/svd_decomposition.png.

Illustrates the geometric interpretation of SVD: A = U Σ V^T.
Shows rotation (V^T), stretching (Σ), and rotation (U).
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "svd_decomposition.png"

# ── config aliases ─────────────────────────────────────────────────────────────
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
LW = _CFG["lines"]["linewidth"]


def draw_vector(ax, end, color, label=None, offset=0.3):
    """Draws a vector and places a label at a calculated offset from the tip."""
    arrow = FancyArrowPatch(
        (0, 0),
        end,
        mutation_scale=12,
        color=color,
        linewidth=LW,
        arrowstyle="-|>",
        zorder=5,
    )
    ax.add_patch(arrow)
    if label:
        norm = np.linalg.norm(end)
        if norm > 0:
            ux, uy = end[0] / norm, end[1] / norm
            lx, ly = end[0] + ux * offset, end[1] + uy * offset
            ax.text(
                lx,
                ly,
                label,
                color=color,
                fontsize=_FS["formula"],
                ha="center",
                va="center",
                fontweight="bold",
            )


def main() -> None:
    plt.rcParams["font.family"] = _CFG["font"]["family"]
    plt.rcParams["font.sans-serif"] = _CFG["font"]["sans_serif"]

    fig, axes = plt.subplots(1, 4, figsize=(16, 4.5), layout="constrained")

    A = np.array([[2, 1], [1, 2]]) / 1.5
    U_mat, S, Vt = np.linalg.svd(A)
    V_mat = Vt.T

    titles = ["Input Space", r"Rotation $V^T$", r"Stretch $\Sigma$", r"Rotation $U$"]
    LIM = 2.5

    theta = np.linspace(0, 2 * np.pi, 100)
    circle = np.array([np.cos(theta), np.sin(theta)])

    # ── Frame 1: Input Space ──────────────────────────────────────────────────
    ax = axes[0]
    ax.plot(circle[0], circle[1], color=BLACK, lw=LW, alpha=0.3)
    draw_vector(ax, V_mat[:, 0], RED, r"$\mathbf{v}_1$")
    draw_vector(ax, V_mat[:, 1], BLUE, r"$\mathbf{v}_2$")

    # ── Frame 2: After V^T ────────────────────────────────────────────────────
    ax = axes[1]
    rotated = Vt @ circle
    ax.plot(rotated[0], rotated[1], color=BLACK, lw=LW, alpha=0.3)
    draw_vector(ax, [1, 0], RED, r"$\mathbf{e}_1$")
    draw_vector(ax, [0, 1], BLUE, r"$\mathbf{e}_2$")

    # ── Frame 3: After Sigma ──────────────────────────────────────────────────
    ax = axes[2]
    stretched = np.diag(S) @ rotated
    ax.plot(stretched[0], stretched[1], color=BLACK, lw=LW, alpha=0.3)
    draw_vector(ax, [S[0], 0], RED, r"$\sigma_1$")
    draw_vector(ax, [0, S[1]], BLUE, r"$\sigma_2$")

    # ── Frame 4: After U ──────────────────────────────────────────────────────
    ax = axes[3]
    final = U_mat @ stretched
    ax.plot(final[0], final[1], color=BLACK, lw=LW, alpha=0.3)
    draw_vector(ax, S[0] * U_mat[:, 0], RED, r"$\sigma_1\mathbf{u}_1$", offset=0.5)
    draw_vector(ax, S[1] * U_mat[:, 1], BLUE, r"$\sigma_2\mathbf{u}_2$", offset=0.5)

    for i, ax in enumerate(axes):
        ax.set_title(titles[i], fontsize=_FS["suptitle"], pad=20, fontweight="black")
        ax.set_aspect("equal")
        ax.set_xlim(-LIM, LIM)
        ax.set_ylim(-LIM, LIM)
        ax.axis("off")
        ax.axhline(0, color=GRAY, lw=0.5)
        ax.axvline(0, color=GRAY, lw=0.5)

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
