"""Generates resources/pictures/linear_independence_diagram.png.

Compares linearly independent and dependent vectors.
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "linear_independence_diagram.png"

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

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5), layout="constrained")
    fig.suptitle(
        "Linear Independence vs. Dependence",
        fontsize=_FS["suptitle"],
        fontweight="black",
    )

    # ── Frame 1: Independent ──────────────────────────────────────────────────
    ax1.set_title("Linearly Independent", fontsize=_FS["title"])
    u = np.array([2, 1])
    v = np.array([0.5, 2])

    ax1.quiver(
        [0, 0],
        [0, 0],
        [u[0], v[0]],
        [u[1], v[1]],
        color=[BLUE, RED],
        angles="xy",
        scale_units="xy",
        scale=1,
        zorder=5,
    )
    ax1.text(u[0], u[1], r"$\mathbf{u}$", color=BLUE, ha="left", fontweight="bold")
    ax1.text(v[0], v[1], r"$\mathbf{v}$", color=RED, ha="left", fontweight="bold")
    ax1.text(1, -0.5, "Not on same line", ha="center", fontsize=_FS["small"])

    ax1.set_xlim(-0.5, 3)
    ax1.set_ylim(-0.5, 3)
    ax1.set_aspect("equal")
    ax1.axis("off")

    # ── Frame 2: Dependent ────────────────────────────────────────────────────
    ax2.set_title("Linearly Dependent", fontsize=_FS["title"])
    u = np.array([1, 1])
    v = np.array([2, 2])

    ax2.quiver(
        [0, 0],
        [0, 0],
        [v[0]],
        [v[1]],
        color=RED,
        alpha=0.5,
        angles="xy",
        scale_units="xy",
        scale=1,
        zorder=4,
    )
    ax2.quiver(
        [0, 0],
        [0, 0],
        [u[0]],
        [u[1]],
        color=BLUE,
        angles="xy",
        scale_units="xy",
        scale=1,
        zorder=5,
    )

    ax2.text(
        u[0], u[1], r"$\mathbf{u}$", color=BLUE, ha="right", va="top", fontweight="bold"
    )
    ax2.text(
        v[0],
        v[1],
        r"$\mathbf{v} = 2\mathbf{u}$",
        color=RED,
        ha="left",
        va="bottom",
        fontweight="bold",
    )
    ax2.text(1.5, -0.5, "Collinear", ha="center", fontsize=_FS["small"])

    ax2.set_xlim(-0.5, 3)
    ax2.set_ylim(-0.5, 3)
    ax2.set_aspect("equal")
    ax2.axis("off")

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
