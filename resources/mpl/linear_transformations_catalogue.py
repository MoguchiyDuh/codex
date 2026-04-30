"""Generates resources/pictures/linear_transformations_catalogue.png.

Grid of panels showing different 2D linear transformations.
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "linear_transformations_catalogue.png"

# ── config aliases ─────────────────────────────────────────────────────────────
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
LW = _CFG["lines"]["linewidth"]


def draw_transformed_square(ax, matrix, title, x_offset=0.0):
    x = np.linspace(0, 1, 5)
    y = np.linspace(0, 1, 5)
    X, Y = np.meshgrid(x, y)

    square_x = np.array([0, 1, 1, 0, 0]) + x_offset
    ax.plot(square_x, [0, 0, 1, 1, 0], color=GRAY, alpha=0.3, linestyle="--", lw=LW)

    pts = np.vstack([X.flatten(), Y.flatten()])
    t_pts = matrix @ pts
    TX = t_pts[0, :].reshape(X.shape) + x_offset
    TY = t_pts[1, :].reshape(Y.shape)

    for i in range(5):
        ax.plot(TX[i, :], TY[i, :], color=BLUE, lw=LW * 0.8)
        ax.plot(TX[:, i], TY[:, i], color=BLUE, lw=LW * 0.8)

    ax.set_title(title, fontsize=_FS["title"])
    ax.set_aspect("equal")
    ax.set_xlim(-0.8, 1.8)
    ax.set_ylim(-0.8, 1.8)
    ax.axis("off")


def main() -> None:
    plt.rcParams["font.family"] = _CFG["font"]["family"]
    plt.rcParams["font.sans-serif"] = _CFG["font"]["sans_serif"]

    fig, axes = plt.subplots(2, 3, figsize=(12, 8), layout="constrained")
    fig.suptitle(
        "2D Linear Transformation Catalogue",
        fontsize=_FS["suptitle"],
        fontweight="black",
    )

    # ── Row 1 ─────────────────────────────────────────────────────────────────
    S = np.array([[1.5, 0], [0, 0.5]])
    draw_transformed_square(axes[0, 0], S, "Scaling")

    theta = np.pi / 4
    R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    draw_transformed_square(axes[0, 1], R, "Rotation")

    H = np.array([[1, 1.5], [0, 1]])
    draw_transformed_square(axes[0, 2], H, "Shear", x_offset=-0.7)

    # ── Row 2 ─────────────────────────────────────────────────────────────────
    Ref = np.array([[-1, 0], [0, 1]])
    draw_transformed_square(axes[1, 0], Ref, "Reflection", x_offset=0.8)

    P = np.array([[1, 0], [0, 0]])
    draw_transformed_square(axes[1, 1], P, "Projection")

    I_mat = np.eye(2)
    draw_transformed_square(axes[1, 2], I_mat, "Identity")

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
