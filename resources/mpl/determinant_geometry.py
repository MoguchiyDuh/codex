"""Generates resources/pictures/determinant_geometry.png.

Illustrates the geometric meaning of determinants as area and volume.
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "determinant_geometry.png"

# ── config aliases ─────────────────────────────────────────────────────────────
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
PURPLE = _COL["purple"]
LW = _CFG["lines"]["linewidth"]


def main() -> None:
    plt.rcParams["font.family"] = _CFG["font"]["family"]
    plt.rcParams["font.sans-serif"] = _CFG["font"]["sans_serif"]

    fig = plt.figure(figsize=(12, 5), layout="constrained")

    # ── Frame 1: 2D Area ──────────────────────────────────────────────────────
    ax1 = fig.add_subplot(121)
    ax1.set_title("2D: Signed Area", fontsize=_FS["title"], pad=10)
    ax1.set_aspect("equal")
    ax1.set_xlim(-0.5, 4)
    ax1.set_ylim(-0.5, 4)
    ax1.axis("off")

    u = np.array([3, 1])
    v = np.array([1, 3])

    points = np.array([[0, 0], u, u + v, v])
    poly = Polygon(points, facecolor=BLUE, alpha=0.3, edgecolor=BLUE, lw=LW)
    ax1.add_patch(poly)

    ax1.quiver(
        [0, 0],
        [0, 0],
        [u[0], v[0]],
        [u[1], v[1]],
        color=[BLACK, BLACK],
        angles="xy",
        scale_units="xy",
        scale=1,
        zorder=5,
    )
    ax1.text(u[0], u[1], r"$\mathbf{a}_1$", ha="left", va="top", fontweight="bold")
    ax1.text(v[0], v[1], r"$\mathbf{a}_2$", ha="right", va="bottom", fontweight="bold")

    det = np.linalg.det(np.column_stack([u, v]))
    ax1.text(
        2,
        2,
        f"Area = |det(A)|\n= {abs(det):.0f}",
        ha="center",
        va="center",
        fontsize=_FS["label"],
        fontweight="bold",
        color=BLACK,
    )

    # ── Frame 2: 3D Volume ────────────────────────────────────────────────────
    ax2 = fig.add_subplot(122, projection="3d")
    ax2.set_title("3D: Signed Volume", fontsize=_FS["title"], pad=10)
    ax2.set_axis_off()

    u = np.array([1, 0, 0])
    v = np.array([0.5, 1, 0])
    w = np.array([0, 0.5, 1])

    def draw_edge(p1, p2, color=GRAY, style="-"):
        ax2.plot(
            [p1[0], p2[0]],
            [p1[1], p2[1]],
            [p1[2], p2[2]],
            color=color,
            linestyle=style,
            lw=LW * 0.5,
        )

    draw_edge([0, 0, 0], u)
    draw_edge([0, 0, 0], v)
    draw_edge(u, u + v)
    draw_edge(v, u + v)

    draw_edge(w, w + u)
    draw_edge(w, w + v)
    draw_edge(w + u, w + u + v)
    draw_edge(w + v, w + u + v)

    draw_edge([0, 0, 0], w)
    draw_edge(u, u + w)
    draw_edge(v, v + w)
    draw_edge(u + v, u + v + w)

    ax2.quiver(
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [u[0], v[0], w[0]],
        [u[1], v[1], w[1]],
        [u[2], v[2], w[2]],
        color=BLACK,
        arrow_length_ratio=0.1,
        lw=LW * 1.5,
    )

    ax2.view_init(elev=20, azim=-30)

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
