"""Generates resources/pictures/types_of_concavity.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "types_of_concavity.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
LW = _CFG["lines"]["linewidth"]

FIG_SIZE = (7.0, 3.5)


def main() -> None:
    plt.rcParams["font.family"] = _CFG["font"]["family"]
    plt.rcParams["font.sans-serif"] = _CFG["font"]["sans_serif"]
    plt.rcParams["text.color"] = BLACK

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FIG_SIZE, layout="constrained")

    x = np.linspace(-1.5, 1.5, 100)

    # ── Concave Up ────────────────────────────────────────────────────────────
    y_up = x**2
    ax1.plot(x, y_up, color=BLACK, linewidth=LW)

    pts_up = [-1.0, 0.0, 1.0]
    for pt in pts_up:
        m = 2 * pt
        y_pt = pt**2
        t_x = np.array([pt - 0.5, pt + 0.5])
        t_y = m * (t_x - pt) + y_pt
        ax1.plot(t_x, t_y, color=RED, linewidth=LW * 0.8)
        ax1.plot(pt, y_pt, marker="o", markersize=5, color=RED)

    ax1.set_title("Concave Up\n$f''(x) > 0$", fontsize=_FS["title"])
    ax1.text(
        0,
        1.8,
        "Tangents lie below the curve",
        ha="center",
        fontsize=_FS["body"],
        color=GRAY,
    )

    # ── Concave Down ──────────────────────────────────────────────────────────
    y_down = -(x**2)
    ax2.plot(x, y_down, color=BLACK, linewidth=LW)

    pts_down = [-1.0, 0.0, 1.0]
    for pt in pts_down:
        m = -2 * pt
        y_pt = -(pt**2)
        t_x = np.array([pt - 0.5, pt + 0.5])
        t_y = m * (t_x - pt) + y_pt
        ax2.plot(t_x, t_y, color=RED, linewidth=LW * 0.8)
        ax2.plot(pt, y_pt, marker="o", markersize=5, color=RED)

    ax2.set_title("Concave Down\n$f''(x) < 0$", fontsize=_FS["title"])
    ax2.text(
        0,
        -1.8,
        "Tangents lie above the curve",
        ha="center",
        fontsize=_FS["body"],
        color=GRAY,
    )

    for ax in (ax1, ax2):
        ax.set_xticks([])
        ax.set_yticks([])
        ax.spines["top"].set_color("none")
        ax.spines["right"].set_color("none")
        ax.spines["bottom"].set_color("none")
        ax.spines["left"].set_color("none")

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
