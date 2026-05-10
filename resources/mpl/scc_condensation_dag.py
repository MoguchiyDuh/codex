"""Generates resources/pictures/scc_condensation_dag.png."""

from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, FancyBboxPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "scc_condensation_dag.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
BLUE = _COL["blue"]
GREEN = _COL["green"]
ORANGE = _COL["orange"]
WHITE = _COL["white"]

NODE_R = 0.27
DAG_R = 0.42
ARROW_SCALE = 12

GRAPH_NODES = {
    "a": (1.2, 3.65, BLUE),
    "b": (2.25, 3.65, BLUE),
    "c": (2.25, 2.55, BLUE),
    "d": (1.2, 2.55, BLUE),
    "e": (3.75, 3.65, GREEN),
    "f": (3.75, 2.55, GREEN),
    "g": (5.25, 3.65, ORANGE),
    "h": (5.25, 2.55, ORANGE),
}

INTERNAL_EDGES = [
    ("a", "b", 0.0),
    ("b", "c", 0.0),
    ("c", "d", 0.0),
    ("d", "a", 0.0),
    ("b", "d", 0.18),
    ("e", "f", 0.22),
    ("f", "e", 0.22),
    ("g", "h", 0.22),
    ("h", "g", 0.22),
]

CROSS_EDGES = [("b", "e"), ("d", "g"), ("f", "h")]
COMPONENTS = [(["a", "b", "c", "d"], BLUE), (["e", "f"], GREEN), (["g", "h"], ORANGE)]

DAG_NODES = {
    "C0": (1.2, 2.95, BLUE, "{a,b,c,d}", r"$C_0$"),
    "C1": (3.2, 2.95, GREEN, "{e,f}", r"$C_1$"),
    "C2": (5.2, 2.95, ORANGE, "{g,h}", r"$C_2$"),
}
DAG_EDGES = [("C0", "C1", -0.1), ("C1", "C2", -0.1), ("C0", "C2", -0.32)]


def _setup_panel(ax: plt.Axes, title: str) -> None:
    ax.set_xlim(0, 6.4)
    ax.set_ylim(0.95, 4.95)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.add_patch(
        FancyBboxPatch(
            (0.12, 1.2),
            6.15,
            3.45,
            boxstyle="round,pad=0.0,rounding_size=0.25",
            facecolor=WHITE,
            edgecolor=BLACK,
            linewidth=LW,
            zorder=0,
        )
    )
    ax.text(
        3.2, 4.36, title, ha="center", va="center", fontsize=_FS["title"], color=BLACK
    )


def _arrow(
    ax: plt.Axes,
    start: tuple[float, float],
    end: tuple[float, float],
    color: str,
    rad: float = 0.0,
    linestyle: str = "solid",
    r0: float = NODE_R,
    r1: float = NODE_R,
) -> None:
    x0, y0 = start
    x1, y1 = end
    dx = x1 - x0
    dy = y1 - y0
    dist = math.hypot(dx, dy)
    if dist == 0:
        return
    ux = dx / dist
    uy = dy / dist
    ax.add_patch(
        FancyArrowPatch(
            (x0 + ux * r0, y0 + uy * r0),
            (x1 - ux * r1, y1 - uy * r1),
            arrowstyle="-|>",
            mutation_scale=ARROW_SCALE,
            linewidth=LW,
            color=color,
            linestyle=linestyle,
            connectionstyle=f"arc3,rad={rad}",
            zorder=2,
        )
    )


def _node(
    ax: plt.Axes, x: float, y: float, label: str, fill: str, radius: float = NODE_R
) -> None:
    ax.add_patch(
        Circle((x, y), radius, facecolor=fill, edgecolor=BLACK, linewidth=LW, zorder=3)
    )
    ax.text(
        x,
        y,
        label,
        ha="center",
        va="center",
        fontsize=_FS["body"],
        color=BLACK,
        zorder=4,
    )


def _component_hulls(ax: plt.Axes) -> None:
    for names, color in COMPONENTS:
        xs = [GRAPH_NODES[name][0] for name in names]
        ys = [GRAPH_NODES[name][1] for name in names]
        cx = sum(xs) / len(xs)
        cy = sum(ys) / len(ys)
        width = max(xs) - min(xs) + 1.0
        height = max(ys) - min(ys) + 1.0
        ax.add_patch(
            Ellipse(
                (cx, cy),
                width,
                height,
                facecolor=color,
                edgecolor=BLACK,
                linewidth=LW,
                linestyle="--",
                alpha=0.28,
                zorder=1,
            )
        )


def draw_graph_panel(ax: plt.Axes) -> None:
    _setup_panel(ax, "original directed graph")
    _component_hulls(ax)
    for a, b, rad in INTERNAL_EDGES:
        _arrow(ax, GRAPH_NODES[a][:2], GRAPH_NODES[b][:2], BLACK, rad)
    for a, b in CROSS_EDGES:
        _arrow(ax, GRAPH_NODES[a][:2], GRAPH_NODES[b][:2], GRAY, 0.0, "--")
    for label, (x, y, color) in GRAPH_NODES.items():
        _node(ax, x, y, label, color)
    ax.text(1.72, 1.75, "SCC 0", ha="center", fontsize=_FS["body"], color=BLACK)
    ax.text(3.75, 1.75, "SCC 1", ha="center", fontsize=_FS["body"], color=BLACK)
    ax.text(5.25, 1.75, "SCC 2", ha="center", fontsize=_FS["body"], color=BLACK)
    ax.text(
        3.2,
        1.03,
        "dashed edges cross component boundaries",
        ha="center",
        fontsize=_FS["small"],
        color=GRAY,
    )


def draw_dag_panel(ax: plt.Axes) -> None:
    _setup_panel(ax, "condensation DAG")
    for a, b, rad in DAG_EDGES:
        _arrow(ax, DAG_NODES[a][:2], DAG_NODES[b][:2], BLACK, rad, r0=DAG_R, r1=DAG_R)
    for _, (x, y, color, members, label) in DAG_NODES.items():
        _node(ax, x, y, label, color, DAG_R)
        ax.text(x, y - 0.7, members, ha="center", fontsize=_FS["small"], color=BLACK)
    ax.text(
        3.2,
        3.95,
        "collapse each SCC to one vertex",
        ha="center",
        fontsize=_FS["body"],
        color=GRAY,
    )
    ax.text(
        3.2,
        1.03,
        "cycles disappear; remaining component graph is acyclic",
        ha="center",
        fontsize=_FS["small"],
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
    fig, axes = plt.subplots(1, 2, figsize=(13.5, 6.0), layout="constrained")
    fig.suptitle("SCC Condensation Graph", fontsize=_FS["suptitle"], fontweight="black")
    draw_graph_panel(axes[0])
    draw_dag_panel(axes[1])
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
