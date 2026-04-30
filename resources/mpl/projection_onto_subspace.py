"""Generates resources/pictures/projection_onto_subspace.png.

Illustrates the projection p of vector b onto a subspace (plane) W,
showing the error vector e = b - p is orthogonal to W.
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "projection_onto_subspace.png"

# ── config aliases ─────────────────────────────────────────────────────────────
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
WHITE = _COL["white"]
LW = _CFG["lines"]["linewidth"]


class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        return np.min(zs)


def main() -> None:
    plt.rcParams["font.family"] = _CFG["font"]["family"]
    plt.rcParams["font.sans-serif"] = _CFG["font"]["sans_serif"]

    fig = plt.figure(figsize=(7, 6))
    ax = fig.add_subplot(111, projection="3d")
    ax.set_box_aspect([1, 1, 0.8])

    u = np.linspace(-1, 1, 10)
    v = np.linspace(-1, 1, 10)
    U, V = np.meshgrid(u, v)
    X = 2 * U + 0.5 * V
    Y = 0.5 * U + 2 * V
    Z = 0.5 * U + 0.5 * V

    ax.plot_surface(X, Y, Z, alpha=0.3, color=BLUE, shade=False, zorder=0)

    for i in [-1, 1]:
        ax.plot(2 * u + 0.5 * i, 0.5 * u + 2 * i, 0.5 * u + 0.5 * i, color=BLUE, lw=1)
        ax.plot(2 * i + 0.5 * v, 0.5 * i + 2 * v, 0.5 * i + 0.5 * v, color=BLUE, lw=1)

    b = np.array([1, 1, 2.5])
    A = np.array([[2, 0.5], [0.5, 2], [0.5, 0.5]])
    P = A @ np.linalg.inv(A.T @ A) @ A.T
    p = P @ b
    e = b - p

    def arrow(start, end, color, lw=LW):
        a = Arrow3D(
            [start[0], end[0]],
            [start[1], end[1]],
            [start[2], end[2]],
            mutation_scale=15,
            lw=lw,
            arrowstyle="-|>",
            color=color,
            zorder=5,
        )
        ax.add_artist(a)

    arrow([0, 0, 0], b, BLACK)
    arrow([0, 0, 0], p, BLUE, lw=LW * 1.5)
    arrow(p, b, RED)

    ax.text(
        b[0],
        b[1],
        b[2] + 0.15,
        r"$\mathbf{b}$",
        fontsize=_FS["label"],
        fontweight="bold",
        ha="center",
    )
    ax.text(
        p[0] + 0.4,
        p[1],
        p[2] - 0.4,
        r"$\mathbf{p} = P\mathbf{b}$",
        color=BLUE,
        fontsize=_FS["label"],
        fontweight="bold",
        ha="left",
    )
    ax.text(
        (b[0] + p[0]) / 2 + 0.3,
        (b[1] + p[1]) / 2 + 0.3,
        (b[2] + p[2]) / 2,
        r"$\mathbf{e} = \mathbf{b} - \mathbf{p}$",
        color=RED,
        fontsize=_FS["label"],
        fontweight="bold",
        ha="left",
    )

    ax.text(
        -2.5,
        2.0,
        0,
        r"$W = C(A)$",
        color=BLUE,
        fontsize=_FS["title"],
        fontweight="bold",
    )

    size = 0.2
    v1 = A[:, 0] / np.linalg.norm(A[:, 0])
    e_n = e / np.linalg.norm(e)
    pt1 = p + size * v1
    pt2 = p + size * e_n
    pt3 = pt1 + size * e_n
    ax.plot(
        [pt1[0], pt3[0], pt2[0]],
        [pt1[1], pt3[1], pt2[1]],
        [pt1[2], pt3[2], pt2[2]],
        color=RED,
        lw=1,
        zorder=4,
    )

    ax.set_xlim(-2, 3)
    ax.set_ylim(-2, 3)
    ax.set_zlim(0, 3)
    ax.axis("off")
    ax.set_facecolor("white")
    ax.view_init(elev=20, azim=-60)

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
