"""Generates resources/pictures/subspace_examples.png.

Illustrates valid subspaces vs non-subspaces.
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "subspace_examples.png"

# ── config aliases ─────────────────────────────────────────────────────────────
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
LW = _CFG["lines"]["linewidth"]


def main() -> None:
    plt.rcParams["font.family"] = _CFG["font"]["family"]
    plt.rcParams["font.sans-serif"] = _CFG["font"]["sans_serif"]

    fig = plt.figure(figsize=(10, 5), layout="constrained")
    fig.suptitle(
        r"Subspaces in $\mathbb{R}^3$", fontsize=_FS["suptitle"], fontweight="black"
    )

    # ── Subspace (Plane through origin) ───────────────────────────────────────
    ax1 = fig.add_subplot(121, projection="3d")
    ax1.set_title("Subspace: Through Origin", color=BLUE, fontsize=_FS["title"])

    xx, yy = np.meshgrid(range(-2, 3), range(-2, 3))
    zz = 0.5 * xx + 0.2 * yy
    ax1.plot_surface(xx, yy, zz, alpha=0.3, color=BLUE)

    ax1.scatter([0], [0], [0], color=BLACK, s=50, zorder=10)
    ax1.text(0, 0, 0.5, r"$\mathbf{0}$", ha="center", fontweight="bold")

    ax1.set_axis_off()

    # ── Non-subspace (Shifted plane) ──────────────────────────────────────────
    ax2 = fig.add_subplot(122, projection="3d")
    ax2.set_title("Not a Subspace: Shifted", color=RED, fontsize=_FS["title"])

    zz_shifted = zz + 1.5
    ax2.plot_surface(xx, yy, zz_shifted, alpha=0.3, color=RED)

    ax2.scatter([0], [0], [0], color=BLACK, s=50, zorder=10)
    ax2.text(
        0, 0, 0.5, r"$\mathbf{0} \notin W$", ha="center", fontweight="bold", color=RED
    )

    ax2.set_axis_off()

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
