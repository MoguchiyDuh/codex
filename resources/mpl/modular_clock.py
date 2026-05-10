"""Generates resources/pictures/modular_clock.png."""

from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "modular_clock.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
WHITE = _COL["white"]

R = 1.0
TICK_INNER = 0.84
LABEL_R = 0.66


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(-1.35, 1.35)
    ax.set_ylim(-1.55, 1.35)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.add_patch(Circle((0, 0), R, facecolor=WHITE, edgecolor=BLACK, linewidth=LW))
    for k in range(12):
        theta = math.pi / 2 - 2 * math.pi * k / 12
        x, y = math.cos(theta), math.sin(theta)
        ax.plot(
            [TICK_INNER * x, R * x], [TICK_INNER * y, R * y], color=BLACK, linewidth=LW
        )
        ax.text(
            LABEL_R * x,
            LABEL_R * y,
            str(k),
            ha="center",
            va="center",
            fontsize=_FS["label"],
            color=BLACK,
        )
    theta_5 = math.pi / 2 - 2 * math.pi * 5 / 12
    ax.add_patch(
        FancyArrowPatch(
            (0, 0),
            (0.72 * math.cos(theta_5), 0.72 * math.sin(theta_5)),
            arrowstyle="-|>",
            mutation_scale=16,
            linewidth=LW,
            color=RED,
        )
    )
    ax.text(
        0,
        -1.28,
        r"$17 \equiv 5\; (\mathrm{mod}\ 12)$",
        ha="center",
        fontsize=_FS["formula"],
        color=BLACK,
    )
    ax.text(
        0,
        1.18,
        "same remainder, same position",
        ha="center",
        fontsize=_FS["body"],
        color=GRAY,
    )


def main() -> None:
    plt.rcParams.update(
        {
            "figure.facecolor": _CFG["figure"]["facecolor"],
            "font.family": _CFG["font"]["family"],
            "font.sans-serif": _CFG["font"]["sans_serif"],
        }
    )
    fig, ax = plt.subplots(figsize=(5, 5.4), layout="constrained")
    fig.suptitle(
        "Modular Arithmetic Clock", fontsize=_FS["suptitle"], fontweight="black"
    )
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
