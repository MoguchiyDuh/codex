"""Generates resources/pictures/ivt_diagram.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "ivt_diagram.png"

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

    x = np.linspace(0, 4, 100)
    y = 0.5 * (x - 1) ** 3 - 2 * (x - 1) + 2

    ax.plot(x, y, color=BLACK, linewidth=LW)

    a, b = 0.5, 3.5
    fa = 0.5 * (a - 1) ** 3 - 2 * (a - 1) + 2
    fb = 0.5 * (b - 1) ** 3 - 2 * (b - 1) + 2

    N = 2.5
    c = 2.3

    ax.plot([a, a], [0, fa], color=GRAY, linestyle=":")
    ax.plot([b, b], [0, fb], color=GRAY, linestyle=":")
    ax.axhline(N, color=RED, linestyle="--", label="$y = N$")

    ax.plot(c, N, marker="o", color=RED)
    ax.plot([c, c], [0, N], color=RED, linestyle=":")

    ax.set_xticks([a, c, b])
    ax.set_xticklabels(["$a$", "$c$", "$b$"], fontsize=_FS["label"])

    ax.set_yticks([fa, N, fb])
    ax.set_yticklabels(["$f(a)$", "$N$", "$f(b)$"], fontsize=_FS["label"], color=BLACK)

    ax.set_title("Intermediate Value Theorem", fontsize=_FS["title"])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
