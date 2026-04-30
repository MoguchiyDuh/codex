"""Generates resources/pictures/geometric_convergence.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "geometric_convergence.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
LW = _CFG["lines"]["linewidth"]

FIG_SIZE = (6, 4)


def main() -> None:
    plt.rcParams["font.family"] = _CFG["font"]["family"]
    plt.rcParams["font.sans-serif"] = _CFG["font"]["sans_serif"]

    fig, ax = plt.subplots(figsize=FIG_SIZE, layout="constrained")

    n = np.arange(1, 9)
    sums = 1 * (1 - 0.5**n) / (1 - 0.5)

    ax.step(n, sums, where="post", color=RED, linewidth=LW, label="Partial Sum $S_n$")
    ax.scatter(n, sums, color=RED, zorder=3)

    ax.axhline(
        2, color=BLACK, linestyle="--", linewidth=LW, label=r"Asymptote $S_\infty = 2$"
    )

    ax.set_xlim(0.5, 8.5)
    ax.set_ylim(0, 2.5)
    ax.set_xlabel("Term number $n$", fontsize=_FS["label"])
    ax.set_ylabel("Sum $S_n$", fontsize=_FS["label"])
    ax.set_title("Convergent Geometric Series ($r=0.5$)", fontsize=_FS["title"])
    ax.legend(fontsize=_FS["body"])

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(True, linestyle=":", alpha=0.6)

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
