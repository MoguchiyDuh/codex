"""Generates resources/pictures/polar_representation.png."""

from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Arc

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "polar_representation.png"

# ── config aliases ─────────────────────────────────────────────────────────────
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
LW = _CFG["lines"]["linewidth"]

# ── layout constants ──────────────────────────────────────────────────────────
FIG_SIZE = (5.5, 4.5)
R = 3.5
THETA_DEG = 40
THETA_RAD = math.radians(THETA_DEG)
Z_A = R * math.cos(THETA_RAD)
Z_B = R * math.sin(THETA_RAD)
AX_LIM = 4.5
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

    ax.set_xlim(-AX_LIM / 4, AX_LIM)
    ax.set_ylim(-AX_LIM / 4, AX_LIM)

    x_ticks = np.arange(-1, int(AX_LIM) + 1, 1)
    y_ticks = np.arange(-1, int(AX_LIM) + 1, 1)

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

    theta_vals = np.linspace(0, np.pi / 2, 100)
    ax.plot(
        R * np.cos(theta_vals),
        R * np.sin(theta_vals),
        color=GRAY,
        linestyle=":",
        linewidth=LW * 0.8,
    )

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
        r"$z = re^{i\theta}$",
        fontsize=_FS["label"],
        color=RED,
        va="bottom",
        ha="left",
    )

    ax.text(
        Z_A,
        -OFFSET_TEXT,
        r"$r\cos\theta$",
        fontsize=_FS["label"],
        ha="center",
        va="top",
    )
    ax.text(
        -OFFSET_TEXT,
        Z_B,
        r"$r\sin\theta$",
        fontsize=_FS["label"],
        ha="right",
        va="center",
    )

    mid_x, mid_y = Z_A / 2, Z_B / 2
    ax.text(
        mid_x - 0.15,
        mid_y + 0.15,
        r"$r$",
        fontsize=_FS["formula"],
        color=RED,
        ha="right",
        va="bottom",
    )

    arc_radius = 1.0
    arc = Arc(
        (0, 0),
        arc_radius * 2,
        arc_radius * 2,
        angle=0,
        theta1=0,
        theta2=THETA_DEG,
        color=BLACK,
        linewidth=LW,
    )
    ax.add_patch(arc)

    theta_label_x = (arc_radius + 0.3) * math.cos(THETA_RAD / 2)
    theta_label_y = (arc_radius + 0.3) * math.sin(THETA_RAD / 2)
    ax.text(
        theta_label_x,
        theta_label_y,
        r"$\theta$",
        fontsize=_FS["formula"],
        color=BLACK,
        ha="center",
        va="center",
    )

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
