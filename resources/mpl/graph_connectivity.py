"""Generates resources/pictures/graph_connectivity.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "graph_connectivity.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
BLUE = _COL["blue"]
GREEN = _COL["green"]
WHITE = _COL["white"]

NODE_R = 0.2


def _node(ax: plt.Axes, xy: tuple[float, float], label: str, color: str) -> None:
    ax.add_patch(
        Circle(xy, NODE_R, facecolor=color, edgecolor=BLACK, linewidth=LW, zorder=3)
    )
    ax.text(
        *xy,
        label,
        ha="center",
        va="center",
        fontsize=_FS["small"],
        color=BLACK,
        zorder=4,
    )


def _draw_graph(
    ax: plt.Axes,
    x0: float,
    title: str,
    pts: list[tuple[float, float]],
    edges: list[tuple[int, int]],
    colors: list[str],
) -> None:
    ax.text(x0 + 2.0, 3.25, title, ha="center", fontsize=_FS["label"], color=BLACK)
    shifted = [(x + x0, y) for x, y in pts]
    for i, j in edges:
        ax.plot(
            [shifted[i][0], shifted[j][0]],
            [shifted[i][1], shifted[j][1]],
            color=BLACK,
            linewidth=LW,
            zorder=1,
        )
    for i, p in enumerate(shifted):
        _node(ax, p, str(i + 1), colors[i])


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 9)
    ax.set_ylim(0.4, 3.7)
    ax.set_aspect("equal")
    ax.axis("off")
    pts1 = [(0.8, 2.4), (2.0, 2.9), (3.2, 2.2), (2.2, 1.2)]
    _draw_graph(
        ax,
        0.1,
        "connected",
        pts1,
        [(0, 1), (1, 2), (2, 3), (3, 0), (1, 3)],
        [WHITE] * 4,
    )
    pts2 = [(0.8, 2.5), (1.7, 1.6), (3.0, 2.5), (3.9, 1.5)]
    _draw_graph(
        ax, 4.7, "two components", pts2, [(0, 1), (2, 3)], [BLUE, BLUE, GREEN, GREEN]
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
    fig.suptitle("Graph Connectivity", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
