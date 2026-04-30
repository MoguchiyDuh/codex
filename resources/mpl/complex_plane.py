"""Generates resources/pictures/complex_plane.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "complex_plane.png"

# ── config aliases ─────────────────────────────────────────────────────────────
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
LW = _CFG["lines"]["linewidth"]

# ── layout constants ──────────────────────────────────────────────────────────
FIG_SIZE = (5.5, 4.5)
Z_A = 3.0
Z_B = 2.0
AX_LIM = 4.0
OFFSET_TEXT = 0.2


def main() -> None:
    plt.rcParams["font.family"] = _CFG["font"]["family"]
    plt.rcParams["font.sans-serif"] = _CFG["font"]["sans_serif"]
    plt.rcParams["text.color"] = BLACK
    plt.rcParams["axes.labelcolor"] = BLACK
    plt.rcParams["xtick.color"] = BLACK
    plt.rcParams["ytick.color"] = BLACK

    fig, ax = plt.subplots(figsize=FIG_SIZE, layout="constrained")

    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")

    ax.set_xlim(-AX_LIM / 2, AX_LIM)
    ax.set_ylim(-AX_LIM, AX_LIM)

    x_ticks = np.arange(-1, int(AX_LIM) + 1, 1)
    y_ticks = np.arange(-int(AX_LIM) + 1, int(AX_LIM) + 1, 1)

    ax.set_xticks([x for x in x_ticks if x != 0])
    ax.set_xticklabels([str(x) for x in x_ticks if x != 0], fontsize=_FS["body"])

    ax.set_yticks([y for y in y_ticks if y != 0])
    y_labels = []
    for y in y_ticks:
        if y == 0:
            continue
        elif y == 1:
            y_labels.append(r"$i$")
        elif y == -1:
            y_labels.append(r"$-i$")
        else:
            y_labels.append(rf"${y}i$")
    ax.set_yticklabels(y_labels, fontsize=_FS["body"])

    ax.text(-OFFSET_TEXT, -OFFSET_TEXT, "0", fontsize=_FS["body"], ha="right", va="top")

    ax.text(
        AX_LIM,
        0.2,
        "Re",
        ha="right",
        va="bottom",
        fontsize=_FS["title"],
        style="italic",
    )
    ax.text(
        0.2, AX_LIM, "Im", ha="left", va="top", fontsize=_FS["title"], style="italic"
    )

    # ── z = a + bi ────────────────────────────────────────────────────────────
    arrow_z = FancyArrowPatch(
        (0, 0), (Z_A, Z_B), mutation_scale=15, color=RED, linewidth=LW
    )
    ax.add_patch(arrow_z)

    ax.plot([Z_A, Z_A], [0, Z_B], color=GRAY, linestyle="--", linewidth=LW * 0.8)
    ax.plot([0, Z_A], [Z_B, Z_B], color=GRAY, linestyle="--", linewidth=LW * 0.8)

    ax.plot(Z_A, Z_B, marker="o", markersize=6, color=RED)
    ax.text(
        Z_A + OFFSET_TEXT,
        Z_B + OFFSET_TEXT,
        r"$z = 3 + 2i$",
        fontsize=_FS["label"],
        color=RED,
        va="bottom",
        ha="left",
    )

    mid_x, mid_y = Z_A / 2, Z_B / 2
    ax.text(
        mid_x - 0.2,
        mid_y + 0.2,
        r"$|z|$",
        fontsize=_FS["formula"],
        color=RED,
        ha="right",
        va="bottom",
    )

    # ── conjugate z_bar = a - bi ──────────────────────────────────────────────
    arrow_z_bar = FancyArrowPatch(
        (0, 0), (Z_A, -Z_B), mutation_scale=15, color=BLUE, linewidth=LW
    )
    ax.add_patch(arrow_z_bar)

    ax.plot([Z_A, Z_A], [0, -Z_B], color=GRAY, linestyle="--", linewidth=LW * 0.8)
    ax.plot([0, Z_A], [-Z_B, -Z_B], color=GRAY, linestyle="--", linewidth=LW * 0.8)

    ax.plot(Z_A, -Z_B, marker="o", markersize=6, color=BLUE)
    ax.text(
        Z_A + OFFSET_TEXT,
        -Z_B - OFFSET_TEXT,
        r"$\overline{z} = 3 - 2i$",
        fontsize=_FS["label"],
        color=BLUE,
        va="top",
        ha="left",
    )

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
