"""Generates resources/pictures/matrix_non_commutativity.png.

Illustrates that AB != BA using rotation and shear.
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "matrix_non_commutativity.png"

# ── config aliases ─────────────────────────────────────────────────────────────
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
LW = _CFG["lines"]["linewidth"]

# ── layout constants ───────────────────────────────────────────────────────────
LIM = 2.5
FIG_SIZE = (12, 8)

A = np.array([[0, -1], [1, 0]])
B = np.array([[1, 1], [0, 1]])


def draw_square(ax, matrix, color, label=None, alpha=1.0):
    pts = np.array([[0, 0], [1.5, 0], [1.5, 1.5], [0, 1.5], [0, 0]]).T
    t_pts = matrix @ pts

    rect_center_x = np.mean(t_pts[0, :-1])
    ghost_center_x = np.mean(pts[0, :-1])

    if np.allclose(matrix, np.eye(2)):
        center_x = rect_center_x
    else:
        center_x = (rect_center_x + ghost_center_x) / 2

    ax.set_xlim(center_x - LIM, center_x + LIM)
    ax.set_ylim(-1.5, 3.5)

    if not np.allclose(matrix, np.eye(2)):
        ax.plot(pts[0, :], pts[1, :], color=GRAY, lw=LW, linestyle="--", alpha=0.3)

    ax.plot(t_pts[0, :], t_pts[1, :], color=color, lw=LW, label=label, alpha=alpha)
    ax.fill(t_pts[0, :], t_pts[1, :], color=color, alpha=0.2 * alpha)


def setup_ax(ax, title):
    ax.set_title(title, fontsize=_FS["title"])
    ax.set_aspect("equal")
    ax.axhline(0, color=BLACK, lw=LW * 0.5, zorder=0)
    ax.axvline(0, color=BLACK, lw=LW * 0.5, zorder=0)
    ax.axis("off")


def main() -> None:
    plt.rcParams["font.family"] = _CFG["font"]["family"]
    plt.rcParams["font.sans-serif"] = _CFG["font"]["sans_serif"]

    fig, axes = plt.subplots(2, 3, figsize=FIG_SIZE, layout="constrained")
    fig.suptitle(
        r"Non-Commutativity: $AB \neq BA$", fontsize=_FS["suptitle"], fontweight="black"
    )

    # ── Row 1: Case AB (B then A) ─────────────────────────────────────────────
    # Frame 1: I
    setup_ax(axes[0, 0], "Start: $I$")
    draw_square(axes[0, 0], np.eye(2), BLACK)

    # Frame 2: B (Shear)
    setup_ax(axes[0, 1], "Step 1: $B$ (Shear)")
    draw_square(axes[0, 1], B, BLUE)

    # Frame 3: AB (Rotate after Shear)
    setup_ax(axes[0, 2], "Step 2: $AB$ (Rotate)")
    draw_square(axes[0, 2], A @ B, BLUE)

    # ── Row 2: Case BA (A then B) ─────────────────────────────────────────────
    # Frame 1: I
    setup_ax(axes[1, 0], "Start: $I$")
    draw_square(axes[1, 0], np.eye(2), BLACK)

    # Frame 2: A (Rotate)
    setup_ax(axes[1, 1], "Step 1: $A$ (Rotate)")
    draw_square(axes[1, 1], A, RED)

    # Frame 3: BA (Shear after Rotate)
    setup_ax(axes[1, 2], "Step 2: $BA$ (Shear)")
    draw_square(axes[1, 2], B @ A, RED)

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
