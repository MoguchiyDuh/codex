"""Generates resources/pictures/vector_2d_3d.png.

Shows a 2D vector and a 3D vector side-by-side to illustrate coordinate components.
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

OUTPUT = _HERE.parent / "pictures" / "vector_2d_3d.png"

# ── config aliases ─────────────────────────────────────────────────────────────
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
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

    fig = plt.figure(figsize=(12, 6), layout="constrained")

    # ── Frame 1: 2D Panel ─────────────────────────────────────────────────────
    ax1 = fig.add_subplot(121)
    ax1.set_title("2D Vector", fontsize=_FS["suptitle"], fontweight="black", pad=20)
    ax1.set_aspect("equal")
    ax1.set_xlim(-0.5, 4.5)
    ax1.set_ylim(-0.5, 4.5)
    ax1.axis("off")

    ax1.annotate(
        "",
        xy=(4.2, 0),
        xytext=(-0.2, 0),
        arrowprops=dict(arrowstyle="->", color=BLACK, lw=1),
    )
    ax1.annotate(
        "",
        xy=(0, 4.2),
        xytext=(0, -0.2),
        arrowprops=dict(arrowstyle="->", color=BLACK, lw=1),
    )
    ax1.text(
        4.4, 0, "$x$", fontsize=_FS["label"], fontweight="bold", ha="left", va="center"
    )
    ax1.text(
        0,
        4.4,
        "$y$",
        fontsize=_FS["label"],
        fontweight="bold",
        ha="center",
        va="bottom",
    )

    for i in [1, 2, 3, 4]:
        ax1.plot([i, i], [-0.05, 0], color=BLACK, lw=1)
        ax1.text(i, -0.25, str(i), ha="center", va="top", fontsize=_FS["body"])
        ax1.plot([-0.05, 0], [i, i], color=BLACK, lw=1)
        ax1.text(-0.2, i, str(i), ha="right", va="center", fontsize=_FS["body"])

    v2d = np.array([2, 2])
    arrow2d = FancyArrowPatch(
        (0, 0),
        v2d,
        mutation_scale=15,
        color=BLUE,
        linewidth=LW * 1.5,
        arrowstyle="-|>",
        zorder=5,
    )
    ax1.add_patch(arrow2d)
    ax1.text(
        v2d[0] + 0.3,
        v2d[1] + 0.3,
        r"$\mathbf{v} = [2, 2]^T$",
        color=BLUE,
        fontsize=_FS["formula"],
        fontweight="bold",
        ha="left",
        va="bottom",
    )

    ax1.plot([2, 2], [0, 2], color=GRAY, linestyle=":", lw=LW)
    ax1.plot([0, 2], [2, 2], color=GRAY, linestyle=":", lw=LW)

    # ── Frame 2: 3D Panel ─────────────────────────────────────────────────────
    ax2 = fig.add_subplot(122, projection="3d")
    ax2.set_title("3D Vector", fontsize=_FS["suptitle"], fontweight="black", pad=20)
    ax2.set_box_aspect([1, 1, 1])
    ax2.axis("off")

    v3d = [2, 2, 2]

    ax2.plot([2, 2], [0, 2], [0, 0], color=GRAY, linestyle=":", lw=LW * 0.8)
    ax2.plot([0, 2], [2, 2], [0, 0], color=GRAY, linestyle=":", lw=LW * 0.8)
    ax2.plot([2, 2], [2, 2], [0, 2], color=GRAY, linestyle=":", lw=LW * 0.8)
    ax2.plot([2, 2], [0, 0], [0, 2], color=GRAY, linestyle=":", lw=LW * 0.8)
    ax2.plot([0, 0], [2, 2], [0, 2], color=GRAY, linestyle=":", lw=LW * 0.8)
    ax2.plot([0, 2], [2, 2], [2, 2], color=GRAY, linestyle=":", lw=LW * 0.8)
    ax2.plot([2, 2], [0, 2], [2, 2], color=GRAY, linestyle=":", lw=LW * 0.8)
    ax2.plot([0, 2], [0, 0], [2, 2], color=GRAY, linestyle=":", lw=LW * 0.8)
    ax2.plot([0, 0], [0, 2], [2, 2], color=GRAY, linestyle=":", lw=LW * 0.8)

    a3d = Arrow3D(
        [0, v3d[0]],
        [0, v3d[1]],
        [0, v3d[2]],
        mutation_scale=15,
        lw=LW * 1.5,
        arrowstyle="-|>",
        color=RED,
        zorder=5,
    )
    ax2.add_artist(a3d)

    ax2.text(
        v3d[0] + 0.4,
        v3d[1] + 0.4,
        v3d[2] + 0.6,
        r"$\mathbf{u} = [2, 2, 2]^T$",
        color=RED,
        fontsize=_FS["formula"],
        fontweight="bold",
        ha="left",
        va="bottom",
    )

    AX_TIP = 4.2

    def draw_axis_3d(ax, start, end):
        a = Arrow3D(
            [start[0], end[0]],
            [start[1], end[1]],
            [start[2], end[2]],
            mutation_scale=10,
            lw=1,
            arrowstyle="-|>",
            color=BLACK,
        )
        ax.add_artist(a)

    draw_axis_3d(ax2, [0, 0, 0], [AX_TIP, 0, 0])
    draw_axis_3d(ax2, [0, 0, 0], [0, AX_TIP, 0])
    draw_axis_3d(ax2, [0, 0, 0], [0, 0, AX_TIP])

    ax2.text(
        AX_TIP + 0.2,
        0,
        0,
        "$x$",
        fontsize=_FS["label"],
        fontweight="bold",
        ha="left",
        va="center",
    )
    ax2.text(
        0,
        AX_TIP + 0.2,
        0,
        "$y$",
        fontsize=_FS["label"],
        fontweight="bold",
        ha="center",
        va="bottom",
    )
    ax2.text(
        0,
        0,
        AX_TIP + 0.2,
        "$z$",
        fontsize=_FS["label"],
        fontweight="bold",
        ha="center",
        va="bottom",
    )

    for i in [1, 2, 3, 4]:
        ax2.plot([i, i], [-0.08, 0], [0, 0], color=BLACK, lw=0.8)
        ax2.text(i, -0.4, 0, str(i), ha="center", va="top", fontsize=_FS["small"])
        ax2.plot([0, 0], [i, i], [-0.08, 0], color=BLACK, lw=0.8)
        ax2.text(0, i, -0.4, str(i), ha="center", va="top", fontsize=_FS["small"])
        ax2.plot([-0.08, 0], [0, 0], [i, i], color=BLACK, lw=0.8)
        ax2.text(-0.3, 0, i, str(i), ha="right", va="center", fontsize=_FS["small"])

    ax2.view_init(elev=20, azim=30)
    ax2.set_xlim(0, 4.5)
    ax2.set_ylim(0, 4.5)
    ax2.set_zlim(0, 4.5)

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
