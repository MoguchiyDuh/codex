"""Generates resources/pictures/discrete_pmf.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "discrete_pmf.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
BLUE = _COL["blue"]

SUMS = list(range(2, 13))
COUNTS = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
PROBS = [c / 36 for c in COUNTS]


def draw(ax: plt.Axes) -> None:
    ax.bar(SUMS, PROBS, color=BLUE, edgecolor=BLACK, linewidth=LW)
    ax.set_xlabel("sum", fontsize=_FS["label"])
    ax.set_ylabel("probability", fontsize=_FS["label"])
    ax.set_xticks(SUMS)
    ax.set_ylim(0, 0.19)
    ax.tick_params(labelsize=_FS["body"])


def main() -> None:
    plt.rcParams.update(
        {
            "figure.facecolor": _CFG["figure"]["facecolor"],
            "font.family": _CFG["font"]["family"],
            "font.sans-serif": _CFG["font"]["sans_serif"],
        }
    )
    fig, ax = plt.subplots(figsize=(7, 4), layout="constrained")
    fig.suptitle("PMF of a Two-Dice Sum", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
