"""Generates resources/pictures/svd_ellipsoid.png.

Illustrates how SVD transforms a unit ball into an ellipsoid.
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "svd_ellipsoid.png"

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

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5), layout="constrained")
    fig.suptitle(
        "SVD: Unit Ball to Ellipsoid", fontsize=_FS["suptitle"], fontweight="black"
    )

    # ── Frame 1: Unit Ball ────────────────────────────────────────────────────
    ax1.set_title("Unit Circle (Input Space)", fontsize=_FS["title"])
    circle = plt.Circle((0, 0), 1, fill=False, edgecolor=BLUE, lw=LW)
    ax1.add_patch(circle)

    theta = np.pi / 6
    v1 = np.array([np.cos(theta), np.sin(theta)])
    v2 = np.array([-np.sin(theta), np.cos(theta)])

    ax1.quiver(
        [0, 0],
        [0, 0],
        [v1[0], v2[0]],
        [v1[1], v2[1]],
        color=BLACK,
        angles="xy",
        scale_units="xy",
        scale=1,
        zorder=5,
    )
    ax1.text(v1[0], v1[1], r"$\mathbf{v}_1$", ha="left", va="bottom")
    ax1.text(v2[0], v2[1], r"$\mathbf{v}_2$", ha="right", va="bottom")

    ax1.set_xlim(-1.5, 1.5)
    ax1.set_ylim(-1.5, 1.5)
    ax1.set_aspect("equal")
    ax1.axis("off")

    # ── Frame 2: Ellipsoid ────────────────────────────────────────────────────
    ax2.set_title("Ellipsoid (Output Space)", fontsize=_FS["title"])

    sigma1, sigma2 = 2.0, 0.8
    phi = np.pi / 4

    ellipse = Ellipse(
        (0, 0),
        2 * sigma1,
        2 * sigma2,
        angle=np.degrees(phi),
        fill=False,
        edgecolor=RED,
        lw=LW,
    )
    ax2.add_patch(ellipse)

    u1 = np.array([np.cos(phi), np.sin(phi)])
    u2 = np.array([-np.sin(phi), np.cos(phi)])

    ax2.quiver(
        [0, 0],
        [0, 0],
        [sigma1 * u1[0], sigma2 * u2[0]],
        [sigma1 * u1[1], sigma2 * u2[1]],
        color=BLACK,
        angles="xy",
        scale_units="xy",
        scale=1,
        zorder=5,
    )
    ax2.text(
        sigma1 * u1[0],
        sigma1 * u1[1],
        r"$\sigma_1 \mathbf{u}_1$",
        ha="left",
        va="bottom",
    )
    ax2.text(
        sigma2 * u2[0], sigma2 * u2[1], r"$\sigma_2 \mathbf{u}_2$", ha="right", va="top"
    )

    ax2.set_xlim(-2.5, 2.5)
    ax2.set_ylim(-2.5, 2.5)
    ax2.set_aspect("equal")
    ax2.axis("off")

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
