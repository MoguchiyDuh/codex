"""Generates resources/pictures/recursion_tree_merge_sort.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "recursion_tree_merge_sort.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
BLUE = _COL["blue"]
WHITE = _COL["white"]


def _node(ax: plt.Axes, x: float, y: float, text: str) -> None:
    ax.add_patch(
        FancyBboxPatch(
            (x - 0.38, y - 0.2),
            0.76,
            0.4,
            boxstyle="round,pad=0.03,rounding_size=0.08",
            facecolor=WHITE,
            edgecolor=BLACK,
            linewidth=LW,
        )
    )
    ax.text(x, y, text, ha="center", va="center", fontsize=_FS["small"], color=BLACK)


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 8)
    ax.set_ylim(0.3, 5.0)
    ax.axis("off")
    levels = [
        [(4.0, "n")],
        [(2.2, "n/2"), (5.8, "n/2")],
        [(1.3, "n/4"), (3.1, "n/4"), (4.9, "n/4"), (6.7, "n/4")],
        [
            (0.85, "1"),
            (1.75, "1"),
            (2.65, "1"),
            (3.55, "1"),
            (4.45, "1"),
            (5.35, "1"),
            (6.25, "1"),
            (7.15, "1"),
        ],
    ]
    ys = [4.35, 3.25, 2.15, 1.05]
    edges = [
        (0, 0, 1, 0),
        (0, 0, 1, 1),
        (1, 0, 2, 0),
        (1, 0, 2, 1),
        (1, 1, 2, 2),
        (1, 1, 2, 3),
        (2, 0, 3, 0),
        (2, 0, 3, 1),
        (2, 1, 3, 2),
        (2, 1, 3, 3),
        (2, 2, 3, 4),
        (2, 2, 3, 5),
        (2, 3, 3, 6),
        (2, 3, 3, 7),
    ]
    for level_a, idx_a, level_b, idx_b in edges:
        x0 = levels[level_a][idx_a][0]
        x1 = levels[level_b][idx_b][0]
        ax.plot(
            [x0, x1], [ys[level_a] - 0.22, ys[level_b] + 0.22], color=GRAY, linewidth=LW
        )
    for y, level in zip(ys, levels, strict=True):
        for x, text in level:
            _node(ax, x, y, text)
        ax.plot([0.65, 7.35], [y - 0.48, y - 0.48], color=BLUE, linewidth=LW)
        ax.text(
            7.45,
            y - 0.5,
            r"level work $n$",
            va="center",
            fontsize=_FS["small"],
            color=BLACK,
        )
    ax.text(
        0.75,
        0.38,
        r"height $\log_2 n$ times $\Theta(n)$ work per level",
        fontsize=_FS["body"],
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
    fig, ax = plt.subplots(figsize=(8.3, 5.0), layout="constrained")
    fig.suptitle(
        "Merge-Sort Recursion Tree", fontsize=_FS["suptitle"], fontweight="black"
    )
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
