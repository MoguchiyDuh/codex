"""Generates resources/pictures/bst.png.

Illustrates a typical Binary Search Tree (BST) structure where the BST
invariant holds for every node.
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
_OUTPUT = _HERE.parent / "pictures" / "bst.png"

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
_BLUE = _COL["blue"]

NODE_R = 0.45


def _draw_node(ax, x, y, label, color=None, edge_color=_BLACK):
    if color is None:
        color = _BLUE
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

    fig, ax = plt.subplots(figsize=(8, 6), layout="constrained")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")
    ax.set_title("Binary Search Tree", fontsize=_FS_TITLE, pad=20)

    nodes = {
        "root": (5, 5.5, "15"),
        "l": (2.5, 4, "6"),
        "r": (7.5, 4, "18"),
        "ll": (1.2, 2.5, "3"),
        "lr": (3.8, 2.5, "7"),
        "rl": (6.2, 2.5, "17"),
        "rr": (8.8, 2.5, "20"),
        "lrl": (3.0, 1, "4"),
    }

    edges = [
        ("root", "l"),
        ("root", "r"),
        ("l", "ll"),
        ("l", "lr"),
        ("r", "rl"),
        ("r", "rr"),
        ("lr", "lrl"),
    ]

    for p, c in edges:
        x0, y0, _ = nodes[p]
        x1, y1, _ = nodes[c]
        _draw_edge(ax, x0, y0, x1, y1)

    for x, y, label in nodes.values():
        _draw_node(ax, x, y, label)

    ax.text(
        5,
        0.2,
        "for every node: left subtree keys < node key < right subtree keys",
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
