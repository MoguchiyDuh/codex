"""Generates resources/pictures/compressed_sparse_row_layout.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "compressed_sparse_row_layout.png"
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
BLUE = _COL["blue"]
GREEN = _COL["green"]
WHITE = _COL["white"]


def _array(ax: plt.Axes, y: float, name: str, vals: list[int], color: str) -> None:
    ax.text(0.7, y + 0.25, name, ha="right", fontsize=_FS["label"], color=BLACK)
    for i, v in enumerate(vals):
        ax.add_patch(
            Rectangle(
                (1.0 + i * 0.6, y),
                0.6,
                0.5,
                facecolor=color,
                edgecolor=BLACK,
                linewidth=LW,
            )
        )
        ax.text(
            1.3 + i * 0.6,
            y + 0.25,
            str(v),
            ha="center",
            va="center",
            fontsize=_FS["body"],
        )


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 8.5)
    ax.set_ylim(0.4, 3.6)
    ax.set_aspect("equal")
    ax.axis("off")
    _array(ax, 2.5, "offsets", [0, 2, 4, 5, 6], BLUE)
    _array(ax, 1.45, "edges", [1, 2, 2, 3, 3, 0], GREEN)
    ax.text(
        4.8,
        0.75,
        "neighbours of v are edges[offset[v] : offset[v+1]]",
        ha="center",
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
    fig, ax = plt.subplots(figsize=(8, 3.8), layout="constrained")
    fig.suptitle("Compressed Sparse Row", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
