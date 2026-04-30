"""Generates resources/pictures/bst_degeneration.png.

Illustrates a degenerate Binary Search Tree (BST) where it has become a
linked-list like structure, leading to O(n) operations.
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
_OUTPUT = _HERE.parent / "pictures" / "bst_degeneration.png"

_DPI = _CFG["output"]["dpi"]
_BBOX = _CFG["output"]["bbox_inches"]
_FACE = _CFG["figure"]["facecolor"]
_FAMILY = _CFG["font"]["family"]
_SANS = _CFG["font"]["sans_serif"]
_FS_TITLE = _CFG["font"]["sizes"]["title"]
_FS_LABEL = _CFG["font"]["sizes"]["label"]
_FS_BODY = _CFG["font"]["sizes"]["body"]
_FS_SMALL = _CFG["font"]["sizes"]["small"]
_LW = _CFG["lines"]["linewidth"]
_COL = _CFG["colors"]
_BLACK = _COL["black"]
_GRAY = _COL["gray"]
_RED = _COL["red"]
_WHITE = _COL["white"]

NODE_R = 0.4


def _draw_node(ax, x, y, label, color=None, edge_color=_BLACK):
    if color is None:
        color = _WHITE
    circle = mpatches.Circle(
        (x, y), NODE_R, facecolor=color, edgecolor=edge_color, lw=_LW, zorder=3
    )
    ax.add_patch(circle)
    ax.text(
        x,
        y,
        label,
        ha="center",
        va="center",
        fontsize=_FS_BODY,
        fontfamily=_FAMILY,
        weight="bold",
    )


def _draw_edge(ax, x0, y0, x1, y1):
    dx, dy = x1 - x0, y1 - y0
    dist = np.sqrt(dx**2 + dy**2)
    ux, uy = dx / dist, dy / dist
    ax.plot(
        [x0 + ux * NODE_R, x1 - ux * NODE_R],
        [y0 + uy * NODE_R, y1 - uy * NODE_R],
        color=_BLACK,
        lw=_LW,
        zorder=1,
    )


def main():
    plt.rcParams.update(
        {
            "font.family": _FAMILY,
            "font.sans-serif": _SANS,
            "figure.facecolor": _FACE,
            "axes.facecolor": _FACE,
        }
    )

    fig, ax = plt.subplots(figsize=(6, 8), layout="constrained")
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 9)
    ax.axis("off")
    ax.set_title("Degenerate BST (Chain)", fontsize=_FS_TITLE, pad=20)

    nodes = [
        (1, 8.0, "1"),
        (2, 6.5, "2"),
        (3, 5.0, "3"),
        (4, 3.5, "4"),
        (5, 2.0, "5"),
    ]

    for i in range(len(nodes) - 1):
        x0, y0, _ = nodes[i]
        x1, y1, _ = nodes[i + 1]
        _draw_edge(ax, x0, y0, x1, y1)

    for x, y, label in nodes:
        _draw_node(ax, x, y, label)

    ax.text(
        3,
        0.5,
        "Sorted insertion into a plain BST\nresults in O(n) search time",
        ha="center",
        va="center",
        fontsize=_FS_BODY,
        color=_GRAY,
        fontstyle="italic",
    )

    fig.savefig(_OUTPUT, dpi=_DPI, bbox_inches=_BBOX)
    plt.close(fig)


if __name__ == "__main__":
    main()
