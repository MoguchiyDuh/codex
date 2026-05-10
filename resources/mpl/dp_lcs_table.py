"""Generates resources/pictures/dp_lcs_table.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "dp_lcs_table.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
BLUE = _COL["blue"]
GREEN = _COL["green"]
ORANGE = _COL["orange"]
WHITE = _COL["white"]

X = "ABCBDAB"
Y = "BDCABA"


def _lcs_table() -> list[list[int]]:
    dp = [[0] * (len(Y) + 1) for _ in range(len(X) + 1)]
    for i, x in enumerate(X, start=1):
        for j, y in enumerate(Y, start=1):
            if x == y:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp


def draw(ax: plt.Axes) -> None:
    dp = _lcs_table()
    ax.set_xlim(0, 10.4)
    ax.set_ylim(0, 8.0)
    ax.axis("off")
    size = 0.72
    x0, y0 = 1.3, 1.0
    path = {(1, 1), (2, 1), (3, 2), (4, 3), (5, 3), (6, 4), (7, 5), (7, 6)}
    for i in range(len(X) + 1):
        for j in range(len(Y) + 1):
            fill = GREEN if (i, j) in path else WHITE
            ax.add_patch(
                Rectangle(
                    (x0 + j * size, y0 + (len(X) - i) * size),
                    size,
                    size,
                    facecolor=fill,
                    edgecolor=BLACK,
                    linewidth=LW * 0.6,
                )
            )
            ax.text(
                x0 + j * size + size / 2,
                y0 + (len(X) - i) * size + size / 2,
                str(dp[i][j]),
                ha="center",
                va="center",
                fontsize=_FS["small"],
                color=BLACK,
            )
    for j, ch in enumerate(" " + Y):
        ax.text(
            x0 + j * size + size / 2,
            y0 + (len(X) + 1) * size + 0.15,
            ch or "0",
            ha="center",
            fontsize=_FS["body"],
            color=BLUE,
        )
    for i, ch in enumerate(" " + X):
        ax.text(
            x0 - 0.25,
            y0 + (len(X) - i) * size + size / 2,
            ch or "0",
            ha="center",
            va="center",
            fontsize=_FS["body"],
            color=ORANGE,
        )
    ax.text(7.0, 5.7, "match: diagonal + 1", fontsize=_FS["body"], color=BLACK)
    ax.text(7.0, 5.28, "mismatch: max(top, left)", fontsize=_FS["body"], color=BLACK)
    ax.text(7.0, 4.55, "answer = bottom-right = 4", fontsize=_FS["label"], color=BLACK)
    ax.text(
        1.3,
        0.45,
        "dependencies flow from top, left, and diagonal",
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
    fig, ax = plt.subplots(figsize=(9.8, 7.5), layout="constrained")
    fig.suptitle(
        "LCS Dynamic-Programming Table", fontsize=_FS["suptitle"], fontweight="black"
    )
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
