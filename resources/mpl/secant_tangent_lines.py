"""Generates resources/pictures/secant_tangent_lines.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "secant_tangent_lines.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
LW = _CFG["lines"]["linewidth"]

FIG_SIZE = (5.5, 4.0)


def f(x: float | np.ndarray) -> float | np.ndarray:
    return -(x**2) + 4 * x


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

    x_min, x_max = -0.2, 3.8
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(-0.2, 4.5)

    x_vals = np.linspace(0, 3.5, 100)
    ax.plot(x_vals, f(x_vals), color=BLACK, linewidth=LW)

    a = 0.5
    b = 3.0
    fa = f(a)
    fb = f(b)

    c = 1.75
    fc = f(c)

    m_sec = (fb - fa) / (b - a)
    sec_x = np.array([-0.2, 3.5])
    sec_y = m_sec * (sec_x - a) + fa
    ax.plot(sec_x, sec_y, color=GRAY, linestyle="--", linewidth=LW)

    tan_x = np.array([0.5, 3.0])
    tan_y = m_sec * (tan_x - c) + fc
    ax.plot(tan_x, tan_y, color=RED, linewidth=LW)

    ax.plot([a, b, c], [fa, fb, fc], "ko", markersize=6)

    ax.plot([a, a], [0, fa], color=GRAY, linestyle=":", linewidth=LW * 0.8)
    ax.plot([b, b], [0, fb], color=GRAY, linestyle=":", linewidth=LW * 0.8)
    ax.plot([c, c], [0, fc], color=GRAY, linestyle=":", linewidth=LW * 0.8)

    ax.text(a, -0.1, "$a$", ha="center", va="top", fontsize=_FS["label"])
    ax.text(b, -0.1, "$b$", ha="center", va="top", fontsize=_FS["label"])
    ax.text(c, -0.1, "$c$", ha="center", va="top", fontsize=_FS["label"], color=RED)

    ax.text(a - 0.1, fa, "$(a, f(a))$", ha="right", va="center", fontsize=_FS["body"])
    ax.text(b + 0.1, fb, "$(b, f(b))$", ha="left", va="center", fontsize=_FS["body"])

    ax.text(
        0.2,
        4.3,
        "Tangent slope = Secant slope",
        fontsize=_FS["label"],
        color=RED,
        ha="left",
        va="center",
    )

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
