"""Generates resources/pictures/log_inverse.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "log_inverse.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
LW = _CFG["lines"]["linewidth"]

FIG_SIZE = (6, 6)


def main() -> None:
    plt.rcParams["font.family"] = _CFG["font"]["family"]
    plt.rcParams["font.sans-serif"] = _CFG["font"]["sans_serif"]

    fig, ax = plt.subplots(figsize=FIG_SIZE, layout="constrained")

    x1 = np.linspace(-3, 2.3, 200)
    y1 = 2**x1

    x2 = np.linspace(0.125, 5, 200)
    y2 = np.log2(x2)

    x_ref = np.linspace(-3, 5, 100)

    ax.plot(x1, y1, color=RED, linewidth=LW, label="$y = 2^x$")
    ax.plot(x2, y2, color=BLUE, linewidth=LW, label=r"$y = \log_2 x$")
    ax.plot(x_ref, x_ref, color=GRAY, linestyle="-.", linewidth=LW / 2, label="$y = x$")

    p1 = (1, 2)
    p2 = (2, 1)
    ax.scatter([p1[0], p2[0]], [p1[1], p2[1]], color=BLACK, zorder=5)
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=GRAY, linestyle=":", alpha=0.5)
    ax.text(p1[0] - 0.2, p1[1] + 0.2, "$(1, 2)$", ha="right", fontsize=_FS["small"])
    ax.text(p2[0] + 0.2, p2[1] - 0.2, "$(2, 1)$", ha="left", fontsize=_FS["small"])

    ax.set_xlim(-3, 5)
    ax.set_ylim(-3, 5)
    ax.set_aspect("equal")
    ax.axhline(0, color=BLACK, linewidth=0.5)
    ax.axvline(0, color=BLACK, linewidth=0.5)
    ax.grid(True, linestyle=":", alpha=0.3)
    ax.set_title(r"Inverse Relationship: $a^x$ and $\log_a x$", fontsize=_FS["title"])
    ax.legend(fontsize=_FS["body"])

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
