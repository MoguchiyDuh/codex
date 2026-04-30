"""Generates resources/pictures/graph_of_tangent.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "graph_of_tangent.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
LW = _CFG["lines"]["linewidth"]

FIG_SIZE = (6.0, 4.5)


def f(x: float | np.ndarray) -> float | np.ndarray:
    return 0.5 * x**2 + 1


def f_prime(x: float) -> float:
    return x


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

    ax.set_xticks([])
    ax.set_yticks([])

    x_min, x_max = -0.5, 3.5
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(-0.5, 6.0)

    # Plot curve
    x_vals = np.linspace(-0.2, 3.2, 200)
    ax.plot(x_vals, f(x_vals), color=BLACK, linewidth=LW)

    # Points
    x1 = 1.0
    x2 = 2.5
    y1 = f(x1)
    y2 = f(x2)

    # Secant line
    m_sec = (y2 - y1) / (x2 - x1)
    sec_x = np.array([-0.2, 3.2])
    sec_y = m_sec * (sec_x - x1) + y1
    ax.plot(sec_x, sec_y, color=GRAY, linestyle="--", linewidth=LW)

    # Tangent line
    m_tan = f_prime(x1)
    tan_x = np.array([-0.2, 3.0])
    tan_y = m_tan * (tan_x - x1) + y1
    ax.plot(tan_x, tan_y, color=RED, linewidth=LW)

    # Projections
    ax.plot([x1, x1], [0, y1], color=GRAY, linestyle=":", linewidth=LW * 0.8)
    ax.plot([x2, x2], [0, y2], color=GRAY, linestyle=":", linewidth=LW * 0.8)
    ax.plot([0, x1], [y1, y1], color=GRAY, linestyle=":", linewidth=LW * 0.8)
    ax.plot([0, x2], [y2, y2], color=GRAY, linestyle=":", linewidth=LW * 0.8)

    # Triangle for secant
    ax.plot([x1, x2], [y1, y1], color=GRAY, linestyle="-", linewidth=LW * 0.8)
    ax.plot([x2, x2], [y1, y2], color=GRAY, linestyle="-", linewidth=LW * 0.8)

    # Points
    ax.plot([x1, x2], [y1, y2], marker="o", markersize=6, color=BLACK, linestyle="none")

    # Labels
    ax.text(x1, -0.2, r"$x$", fontsize=_FS["label"], ha="center", va="top")
    ax.text(x2, -0.2, r"$x+h$", fontsize=_FS["label"], ha="center", va="top")
    ax.text(-0.2, y1, r"$f(x)$", fontsize=_FS["label"], ha="right", va="center")
    ax.text(-0.2, y2, r"$f(x+h)$", fontsize=_FS["label"], ha="right", va="center")

    ax.text(
        (x1 + x2) / 2, y1 - 0.15, r"$h$", fontsize=_FS["label"], ha="center", va="top"
    )
    ax.text(
        x2 + 0.1,
        (y1 + y2) / 2,
        r"$f(x+h) - f(x)$",
        fontsize=_FS["label"],
        ha="left",
        va="center",
    )

    # Legend texts
    ax.text(0.5, f(0.5) + 0.5, r"$y = f(x)$", fontsize=_FS["label"], ha="right")
    ax.text(
        1.8, m_tan * (1.8 - x1) + y1 - 0.4, "Tangent", color=RED, fontsize=_FS["label"]
    )
    ax.text(
        3.1, m_sec * (3.1 - x1) + y1 - 0.2, "Secant", color=GRAY, fontsize=_FS["label"]
    )

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
