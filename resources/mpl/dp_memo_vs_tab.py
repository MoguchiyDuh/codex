"""Generates resources/pictures/dp_memo_vs_tab.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "dp_memo_vs_tab.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
BLUE = _COL["blue"]
GREEN = _COL["green"]
RED = _COL["red"]
WHITE = _COL["white"]

TREE = [
    ("F5", 1.6, 4.2),
    ("F4", 0.9, 3.2),
    ("F3", 2.3, 3.2),
    ("F3", 0.55, 2.2),
    ("F2", 1.25, 2.2),
    ("F2", 1.95, 2.2),
    ("F1", 2.65, 2.2),
]
EDGES = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 8.8)
    ax.set_ylim(0.5, 5.0)
    ax.axis("off")
    ax.text(1.55, 4.72, "memoization", ha="center", fontsize=_FS["title"], color=BLACK)
    ax.text(6.35, 4.72, "tabulation", ha="center", fontsize=_FS["title"], color=BLACK)

    for i, j in EDGES:
        x0, y0 = TREE[i][1], TREE[i][2]
        x1, y1 = TREE[j][1], TREE[j][2]
        ax.plot([x0, x1], [y0, y1], color=GRAY, linewidth=LW)
    seen = set()
    for label, x, y in TREE:
        repeated = label in seen
        seen.add(label)
        ax.add_patch(
            Circle(
                (x, y),
                0.25,
                facecolor=RED if repeated else BLUE,
                edgecolor=BLACK,
                linewidth=LW,
                zorder=2,
            )
        )
        ax.text(
            x,
            y,
            label,
            ha="center",
            va="center",
            fontsize=_FS["small"],
            color=BLACK,
            zorder=3,
        )
    ax.text(0.35, 1.25, "cache cuts repeated calls", fontsize=_FS["body"], color=BLACK)

    values = ["F0", "F1", "F2", "F3", "F4", "F5"]
    for i, value in enumerate(values):
        x = 4.2 + i * 0.62
        ax.add_patch(
            Rectangle(
                (x, 2.55),
                0.58,
                0.5,
                facecolor=GREEN if i >= 2 else WHITE,
                edgecolor=BLACK,
                linewidth=LW,
            )
        )
        ax.text(
            x + 0.29,
            2.8,
            value,
            ha="center",
            va="center",
            fontsize=_FS["small"],
            color=BLACK,
        )
        if i < len(values) - 1:
            ax.add_patch(
                FancyArrowPatch(
                    (x + 0.58, 2.8),
                    (x + 0.65, 2.8),
                    arrowstyle="-|>",
                    mutation_scale=10,
                    linewidth=LW,
                    color=GRAY,
                )
            )
    ax.text(4.2, 1.85, "fill dependency order once", fontsize=_FS["body"], color=BLACK)
    ax.text(
        4.2, 1.48, r"same $\Theta(n)$ subproblems", fontsize=_FS["body"], color=BLACK
    )


def main() -> None:
    plt.rcParams.update(
        {
            "figure.facecolor": _CFG["figure"]["facecolor"],
            "font.family": _CFG["font"]["family"],
            "font.sans-serif": _CFG["font"]["sans_serif"],
        }
    )
    fig, ax = plt.subplots(figsize=(8.8, 5.0), layout="constrained")
    fig.suptitle(
        "Memoization vs Tabulation", fontsize=_FS["suptitle"], fontweight="black"
    )
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
