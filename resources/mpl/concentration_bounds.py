"""Generates resources/pictures/concentration_bounds.png."""

from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.pyplot as plt

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "concentration_bounds.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
PURPLE = _COL["purple"]

X_MIN = 1.0
X_MAX = 6.0
N = 240


def draw(ax: plt.Axes) -> None:
    xs = [X_MIN + (X_MAX - X_MIN) * i / (N - 1) for i in range(N)]
    markov = [1 / x for x in xs]
    chebyshev = [1 / (x * x) for x in xs]
    chernoff_shape = [math.exp(-(x - 1)) for x in xs]
    ax.plot(xs, markov, color=RED, linewidth=LW, label="Markov")
    ax.plot(xs, chebyshev, color=BLUE, linewidth=LW, label="Chebyshev")
    ax.plot(xs, chernoff_shape, color=PURPLE, linewidth=LW, label="Chernoff shape")
    ax.set_ylim(0, 1.05)
    ax.set_xlabel("deviation scale", fontsize=_FS["label"])
    ax.set_ylabel("upper bound", fontsize=_FS["label"])
    ax.grid(color=GRAY, linestyle=":", linewidth=0.8)
    ax.legend(frameon=False, fontsize=_FS["body"])


def main() -> None:
    plt.rcParams.update(
        {
            "figure.facecolor": _CFG["figure"]["facecolor"],
            "font.family": _CFG["font"]["family"],
            "font.sans-serif": _CFG["font"]["sans_serif"],
        }
    )
    fig, ax = plt.subplots(figsize=(7, 4.2), layout="constrained")
    fig.suptitle("Concentration Bounds", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
