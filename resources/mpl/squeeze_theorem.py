"""Generates resources/pictures/squeeze_theorem.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "squeeze_theorem.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
LW = _CFG["lines"]["linewidth"]

FIG_SIZE = (6, 4)


def main() -> None:
    plt.rcParams["font.family"] = _CFG["font"]["family"]
    plt.rcParams["font.sans-serif"] = _CFG["font"]["sans_serif"]

    fig, ax = plt.subplots(figsize=FIG_SIZE, layout="constrained")

    x = np.linspace(-0.5, 0.5, 400)
    # Avoid div by zero
    x_small = x[np.abs(x) > 0.01]

    upper = x**2
    lower = -(x**2)
    f = x_small**2 * np.sin(1 / x_small)

    ax.plot(x, upper, color=GRAY, linestyle="--", label="$h(x) = x^2$")
    ax.plot(x, lower, color=GRAY, linestyle="--", label="$g(x) = -x^2$")
    ax.plot(x_small, f, color=RED, linewidth=LW, label=r"$f(x) = x^2 \sin(1/x)$")

    ax.plot(0, 0, marker="o", color=BLACK, markersize=6)

    ax.set_title("Squeeze Theorem", fontsize=_FS["title"])
    ax.legend(fontsize=_FS["body"])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.axhline(0, color=BLACK, linewidth=0.5)
    ax.axvline(0, color=BLACK, linewidth=0.5)

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
