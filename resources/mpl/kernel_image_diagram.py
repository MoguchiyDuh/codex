"""Generates resources/pictures/kernel_image_diagram.png.

Schematic diagram of kernel (null space) and image (column space).
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, ConnectionPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "kernel_image_diagram.png"

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

    fig, ax = plt.subplots(figsize=(8, 5), layout="constrained")
    ax.set_title(
        "Kernel and Image", fontsize=_FS["suptitle"], fontweight="black", pad=20
    )
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")

    v_ellipse = Ellipse((2.5, 3), 4, 5, fill=False, edgecolor=BLACK, lw=LW)
    ax.add_patch(v_ellipse)
    ax.text(2.5, 5.7, r"Domain $V$", ha="center", fontsize=_FS["title"])

    ker_ellipse = Ellipse(
        (2.5, 3), 1.5, 2, facecolor=GRAY, alpha=0.3, edgecolor=BLACK, linestyle="--"
    )
    ax.add_patch(ker_ellipse)
    ax.text(
        2.5,
        3,
        r"Kernel $N(A)$",
        ha="center",
        va="center",
        fontsize=_FS["label"],
        fontweight="bold",
    )

    w_ellipse = Ellipse((7.5, 3), 4, 5, fill=False, edgecolor=BLACK, lw=LW)
    ax.add_patch(w_ellipse)
    ax.text(7.5, 5.7, r"Codomain $W$", ha="center", fontsize=_FS["title"])

    im_ellipse = Ellipse(
        (7.5, 3), 2.5, 3.5, facecolor=RED, alpha=0.2, edgecolor=RED, lw=LW * 0.8
    )
    ax.add_patch(im_ellipse)
    ax.text(
        7.5,
        3.5,
        r"Image $C(A)$",
        color=RED,
        ha="center",
        va="center",
        fontsize=_FS["label"],
        fontweight="bold",
    )

    ax.scatter(7.5, 1.5, color=BLACK, s=30)
    ax.text(
        7.6,
        1.5,
        r"$\mathbf{0}$",
        ha="left",
        va="center",
        fontsize=_FS["label"],
        fontweight="bold",
    )

    arrow_ker = ConnectionPatch(
        xyA=(2.5, 2.0),
        xyB=(7.4, 1.5),
        coordsA="data",
        coordsB="data",
        arrowstyle="-|>",
        mutation_scale=15,
        color=GRAY,
        lw=LW,
    )
    ax.add_patch(arrow_ker)

    arrow_v = ConnectionPatch(
        xyA=(3.5, 4.5),
        xyB=(6.5, 4.0),
        coordsA="data",
        coordsB="data",
        arrowstyle="-|>",
        mutation_scale=15,
        color=BLACK,
        lw=LW,
    )
    ax.add_patch(arrow_v)
    ax.text(5, 4.5, r"$\mathbf{x} \mapsto A\mathbf{x}$", ha="center")

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
