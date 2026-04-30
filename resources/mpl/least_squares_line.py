"""Generates resources/pictures/least_squares_line.png.

Illustrates linear regression (least squares) by showing data points,
the best-fit line, and the vertical residuals (errors).
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "least_squares_line.png"

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
    plt.rcParams["text.color"] = BLACK

    fig, ax = plt.subplots(figsize=(6.5, 4.5), layout="constrained")

    t = np.array([1, 2, 3, 4, 5])
    y = np.array([1.2, 1.9, 3.2, 3.8, 5.1])

    A = np.vstack([np.ones(len(t)), t]).T
    c, d = np.linalg.inv(A.T @ A) @ A.T @ y

    t_line = np.linspace(0.5, 5.5, 100)
    y_line = c + d * t_line

    for ti, yi in zip(t, y):
        y_pred = c + d * ti
        ax.plot(
            [ti, ti], [yi, y_pred], color=RED, linestyle="--", lw=LW * 0.8, zorder=1
        )

    ax.plot(t_line, y_line, color=BLUE, lw=LW * 1.5, label="Best-fit line", zorder=2)
    ax.scatter(t, y, color=BLACK, s=60, edgecolors=BLACK, zorder=3, label="Data points")

    ax.set_title("Least Squares Line Fitting", fontsize=_FS["title"], pad=15)
    ax.set_xlabel("time ($t$)", fontsize=_FS["label"])
    ax.set_ylabel("outcome ($y$)", fontsize=_FS["label"])

    ax.text(
        1,
        4.5,
        rf"$y = {c:.2f} + {d:.2f}t$",
        fontsize=_FS["formula"],
        color=BLUE,
        fontweight="bold",
    )
    ax.text(
        3.5,
        2.0,
        r"minimize $\sum (y_i - \hat{y}_i)^2$",
        color=RED,
        fontsize=_FS["body"],
        bbox=dict(facecolor="white", edgecolor="none"),
    )

    ax.spines["top"].set_color("none")
    ax.spines["right"].set_color("none")
    ax.grid(True, linestyle=":", color=GRAY)

    ax.set_xlim(0, 6)
    ax.set_ylim(0, 6)

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
