"""Generates resources/pictures/binomial_pmf.png."""

from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.pyplot as plt

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "binomial_pmf.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GREEN = _COL["green"]

N = 10
P = 0.5
XS = list(range(N + 1))
PROBS = [math.comb(N, k) * P**k * (1 - P) ** (N - k) for k in XS]


def draw(ax: plt.Axes) -> None:
    ax.bar(XS, PROBS, color=GREEN, edgecolor=BLACK, linewidth=LW)
    ax.set_xlabel("successes", fontsize=_FS["label"])
    ax.set_ylabel("probability", fontsize=_FS["label"])
    ax.set_xticks(XS)
    ax.tick_params(labelsize=_FS["body"])
    ax.text(
        7.1,
        0.21,
        r"$X\sim \mathrm{Binomial}(10,0.5)$",
        fontsize=_FS["label"],
        color=BLACK,
    )


def main() -> None:
    plt.rcParams.update(
        {
            "figure.facecolor": _CFG["figure"]["facecolor"],
            "font.family": _CFG["font"]["family"],
            "font.sans-serif": _CFG["font"]["sans_serif"],
        }
    )
    fig, ax = plt.subplots(figsize=(7, 4), layout="constrained")
    fig.suptitle("Binomial PMF", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
