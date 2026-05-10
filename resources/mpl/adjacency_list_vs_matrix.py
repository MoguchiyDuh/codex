"""Generates resources/pictures/adjacency_list_vs_matrix.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "adjacency_list_vs_matrix.png"
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
BLUE = _COL["blue"]
GREEN = _COL["green"]
WHITE = _COL["white"]


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.5)
    ax.set_aspect("equal")
    ax.axis("off")
    pts = [(1.4, 2.8), (2.8, 3.2), (2.4, 1.7), (1.0, 1.5)]
    edges = [(0, 1), (0, 2), (1, 2), (2, 3)]
    ax.text(2, 4.0, "list: O(n + m)", ha="center", fontsize=_FS["label"])
    for i, j in edges:
        ax.plot(
            [pts[i][0], pts[j][0]], [pts[i][1], pts[j][1]], color=BLACK, linewidth=LW
        )
    for i, p in enumerate(pts):
        ax.add_patch(Circle(p, 0.2, facecolor=BLUE, edgecolor=BLACK, linewidth=LW))
        ax.text(*p, str(i), ha="center", va="center", fontsize=_FS["body"])
    ax.text(7.2, 4.0, "matrix: O(n^2)", ha="center", fontsize=_FS["label"])
    mat_edges = set(edges + [(j, i) for i, j in edges])
    for r in range(4):
        for c in range(4):
            color = GREEN if (r, c) in mat_edges else WHITE
            ax.add_patch(
                Rectangle(
                    (5.7 + c * 0.55, 2.6 - r * 0.55),
                    0.55,
                    0.55,
                    facecolor=color,
                    edgecolor=BLACK,
                    linewidth=1.0,
                )
            )
            ax.text(
                5.975 + c * 0.55,
                2.875 - r * 0.55,
                "1" if (r, c) in mat_edges else "0",
                ha="center",
                va="center",
                fontsize=_FS["small"],
                color=BLACK if (r, c) in mat_edges else GRAY,
            )
    ax.text(
        5,
        0.35,
        "lists scale with edges; matrices give O(1) edge tests",
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
    fig, ax = plt.subplots(figsize=(9, 4.4), layout="constrained")
    fig.suptitle(
        "Adjacency List vs Matrix", fontsize=_FS["suptitle"], fontweight="black"
    )
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
