"""Generates resources/pictures/parabola_components.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "parabola_components.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
LW = _CFG["lines"]["linewidth"]

FIG_SIZE = (6.5, 4.5)


def main() -> None:
    plt.rcParams["font.family"] = _CFG["font"]["family"]
    plt.rcParams["font.sans-serif"] = _CFG["font"]["sans_serif"]
    plt.rcParams["text.color"] = BLACK

    fig, ax = plt.subplots(figsize=FIG_SIZE, layout="constrained")

    ax.spines["top"].set_color("none")
    ax.spines["right"].set_color("none")
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.set_xticks([])
    ax.set_yticks([])

    ax.set_xlim(-0.5, 6.5)
    ax.set_ylim(-0.5, 5.5)

    x_vals = np.linspace(0, 6, 100)
    y_vals = 0.25 * (x_vals - 2) ** 2 + 2
    ax.plot(x_vals, y_vals, color=BLACK, linewidth=LW)

    h, k = 2.0, 2.0
    focus_y = 3.0
    dir_y = 1.0

    ax.plot([h, h], [0, 5.5], color=GRAY, linestyle="-.", linewidth=LW * 0.8)
    ax.text(
        h - 0.2,
        5.3,
        "Axis of\nsymmetry",
        ha="right",
        va="top",
        fontsize=_FS["body"],
        color=GRAY,
    )

    ax.plot([-0.5, 6.5], [dir_y, dir_y], color=RED, linestyle="--", linewidth=LW * 0.8)
    ax.text(
        6.0,
        dir_y - 0.2,
        "Directrix",
        ha="right",
        va="top",
        fontsize=_FS["body"],
        color=RED,
    )

    ax.plot([h], [k], marker="o", markersize=6, color=BLACK)
    ax.text(h + 0.2, k - 0.1, "Vertex", ha="left", va="top", fontsize=_FS["label"])

    ax.plot([h], [focus_y], marker="o", markersize=6, color=RED)
    ax.text(
        h - 0.2,
        focus_y,
        "Focus",
        ha="right",
        va="center",
        fontsize=_FS["label"],
        color=RED,
    )

    px = 5.0
    py = 4.25

    ax.plot([px], [py], marker="o", markersize=5, color=BLACK)
    ax.text(px + 0.1, py - 0.25, "$P(x,y)$", ha="left", va="top", fontsize=_FS["label"])

    ax.plot([h, px], [focus_y, py], color=RED, linestyle="-", linewidth=LW * 0.8)

    ax.plot([px, px], [dir_y, py], color=RED, linestyle="-", linewidth=LW * 0.8)
    ax.plot([px], [dir_y], marker="s", markersize=5, color=RED)

    m_size = 0.15
    ax.plot(
        [px - m_size, px - m_size],
        [dir_y, dir_y + m_size],
        color=RED,
        linewidth=LW * 0.6,
    )
    ax.plot(
        [px - m_size, px],
        [dir_y + m_size, dir_y + m_size],
        color=RED,
        linewidth=LW * 0.6,
    )

    mid_fx = (h + px) / 2
    mid_fy = (focus_y + py) / 2
    dx = px - h
    dy = py - focus_y
    length = np.sqrt(dx**2 + dy**2)
    nx = -dy / length * 0.15
    ny = dx / length * 0.15

    ax.plot(
        [mid_fx - nx, mid_fx + nx], [mid_fy - ny, mid_fy + ny], color=RED, linewidth=LW
    )

    mid_dx = px
    mid_dy = (py + dir_y) / 2
    ax.plot([mid_dx - 0.15, mid_dx + 0.15], [mid_dy, mid_dy], color=RED, linewidth=LW)

    bbox_white = dict(facecolor="white", edgecolor="none", pad=1)
    ax.text(
        3.7,
        3.9,
        "$d_1$",
        color=RED,
        fontsize=_FS["label"],
        ha="right",
        va="bottom",
        bbox=bbox_white,
    )
    ax.text(
        5.2,
        2.0,
        "$d_2$",
        color=RED,
        fontsize=_FS["label"],
        ha="left",
        va="center",
        bbox=bbox_white,
    )

    ax.text(
        3.0,
        5.0,
        "$d_1 = d_2$",
        color=RED,
        fontsize=_FS["formula"],
        ha="left",
        va="center",
    )

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
