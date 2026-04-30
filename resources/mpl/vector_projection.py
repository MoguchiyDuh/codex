"""Generates resources/pictures/vector_projection.png.

Illustrates vector projection of u onto v.
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "vector_projection.png"

# ── config aliases ─────────────────────────────────────────────────────────────
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
PURPLE = _COL["purple"]
LW = _CFG["lines"]["linewidth"]


def draw_vector(
    ax,
    start,
    end,
    color,
    label=None,
    offset=(0.1, 0.1),
    fs="formula",
    alpha=1.0,
    zorder=5,
):
    arrow = FancyArrowPatch(
        start,
        end,
        mutation_scale=15,
        color=color,
        linewidth=LW * 1.5,
        arrowstyle="-|>",
        zorder=zorder,
        alpha=alpha,
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
            alpha=alpha,
        )


def main() -> None:
    plt.rcParams["font.family"] = _CFG["font"]["family"]
    plt.rcParams["font.sans-serif"] = _CFG["font"]["sans_serif"]

    fig, ax = plt.subplots(figsize=(6, 5), layout="constrained")
    ax.set_title(
        "Vector Projection", fontsize=_FS["suptitle"], fontweight="black", pad=20
    )
    ax.set_aspect("equal")
    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(-0.5, 3.5)
    ax.axis("off")

    U = np.array([1.5, 2.5])
    V = np.array([4.0, 1.0])

    v_norm_sq = np.dot(V, V)
    proj_u_v = (np.dot(U, V) / v_norm_sq) * V
    orth_u_v = U - proj_u_v

    for i in range(5):
        ax.axhline(i, color=GRAY, lw=0.5, zorder=0, alpha=0.3)
        ax.axvline(i, color=GRAY, lw=0.5, zorder=0, alpha=0.3)

    ax.plot(
        [-0.5, 5], [-0.5 / 4 * 1, 5 / 4 * 1], color=GRAY, linestyle=":", lw=LW, zorder=1
    )

    draw_vector(ax, (0, 0), V, BLACK, r"$\mathbf{v}$", (0.2, -0.2))
    draw_vector(ax, (0, 0), U, BLUE, r"$\mathbf{u}$", (-0.1, 0.3))
    draw_vector(
        ax,
        (0, 0),
        proj_u_v,
        PURPLE,
        r"$\text{proj}_{\mathbf{v}} \mathbf{u}$",
        (0.2, -0.4),
    )

    ax.plot(
        [U[0], proj_u_v[0]],
        [U[1], proj_u_v[1]],
        color=RED,
        linestyle="--",
        lw=LW,
        zorder=2,
    )

    v_dir = V / np.linalg.norm(V)
    orth_dir = orth_u_v / np.linalg.norm(orth_u_v)
    S = 0.2
    p1 = proj_u_v + orth_dir * S
    p2 = p1 - v_dir * S
    p3 = proj_u_v - v_dir * S
    ax.plot(
        [p1[0], p2[0], p3[0]], [p1[1], p2[1], p3[1]], color=GRAY, lw=LW * 0.7, zorder=2
    )

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
