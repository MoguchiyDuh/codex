"""Generates resources/pictures/gauss_pairing.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "gauss_pairing.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
LW = _CFG["lines"]["linewidth"]

FIG_SIZE = (6, 2.5)
TERMS = [1, 2, 3, 4, 5, 6]
Y_START = 0.12
RAD_34 = 0.30
RAD_25 = 0.30
RAD_16 = 0.30
Y_7_34 = 0.22
Y_7_25 = 0.38
Y_7_16 = 0.55


def main() -> None:
    plt.rcParams["font.family"] = _CFG["font"]["family"]
    plt.rcParams["font.sans-serif"] = _CFG["font"]["sans_serif"]

    fig, ax = plt.subplots(figsize=FIG_SIZE, layout="constrained")

    n = len(TERMS)

    for i, val in enumerate(TERMS):
        ax.text(
            i,
            0,
            str(val),
            ha="center",
            va="center",
            fontsize=_FS["formula"],
            fontweight="bold",
        )

    ax.annotate(
        "",
        xy=(2, Y_START),
        xycoords="data",
        xytext=(3, Y_START),
        textcoords="data",
        arrowprops=dict(
            arrowstyle="-",
            connectionstyle=f"arc3,rad={RAD_34}",
            color=RED,
            linewidth=LW,
        ),
    )

    ax.annotate(
        "",
        xy=(1, Y_START),
        xycoords="data",
        xytext=(4, Y_START),
        textcoords="data",
        arrowprops=dict(
            arrowstyle="-",
            connectionstyle=f"arc3,rad={RAD_25}",
            color=RED,
            linewidth=LW,
        ),
    )

    ax.annotate(
        "",
        xy=(0, Y_START),
        xycoords="data",
        xytext=(5, Y_START),
        textcoords="data",
        arrowprops=dict(
            arrowstyle="-",
            connectionstyle=f"arc3,rad={RAD_16}",
            color=RED,
            linewidth=LW,
        ),
    )

    ax.text(
        2.5, Y_7_34, "7", color=BLACK, ha="center", va="bottom", fontsize=_FS["label"]
    )
    ax.text(
        2.5, Y_7_25, "7", color=BLACK, ha="center", va="bottom", fontsize=_FS["label"]
    )
    ax.text(
        2.5, Y_7_16, "7", color=BLACK, ha="center", va="bottom", fontsize=_FS["label"]
    )

    ax.set_xlim(-0.5, n - 0.5)
    ax.set_ylim(-0.2, 1.0)
    ax.axis("off")
    ax.set_title("Gauss's Pairing Trick (Sum of 1 to 6)", fontsize=_FS["title"], pad=10)

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
