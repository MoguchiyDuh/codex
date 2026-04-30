"""Generates resources/pictures/scc_condensation_dag.png.

Two-panel figure:
  Left  — directed graph with three SCCs highlighted in distinct colors
  Right — condensation DAG (one node per SCC)
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "scc_condensation_dag.png"

# ── config aliases ─────────────────────────────────────────────────────────────
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]

NODE_R = 0.36
TITLE_FS = _FS["title"]
LABEL_FS = _FS["label"]
SMALL_FS = _FS["small"]
BODY_FS = _FS["body"]

ARROW_SCALE = 13

SCC_FILL = [_COL["blue"], _COL["green"], _COL["orange"]]
SCC_EDGE = [BLACK, BLACK, BLACK]

# ── Graph definition ──────────────────────────────────────────────────────────
NODES: dict[str, tuple[float, float, int]] = {
    "a": (2.0, 6.5, 0),
    "b": (3.5, 6.5, 0),
    "c": (3.5, 5.0, 0),
    "d": (2.0, 5.0, 0),
    "e": (5.5, 7.0, 1),
    "f": (5.5, 5.5, 1),
    "g": (7.5, 6.5, 2),
    "h": (7.5, 5.0, 2),
}

EDGES: list[tuple[str, str, float]] = [
    ("a", "b", 0.0),
    ("b", "c", 0.0),
    ("c", "d", 0.0),
    ("d", "a", 0.0),
    ("b", "d", 0.2),
    ("e", "f", 0.25),
    ("f", "e", 0.25),
    ("g", "h", 0.25),
    ("h", "g", 0.25),
    ("a", "e", 0.0),
    ("d", "g", 0.0),
    ("f", "h", 0.0),
]

# ── Condensation DAG ──────────────────────────────────────────────────────────
COND_NODES: dict[str, tuple[float, float, int]] = {
    "C\u2080": (2.0, 5.75, 0),
    "C\u2081": (5.0, 5.75, 1),
    "C\u2082": (8.0, 5.75, 2),
}

COND_CONTENTS: dict[str, str] = {
    "C\u2080": "{a, b, c, d}",
    "C\u2081": "{e, f}",
    "C\u2082": "{g, h}",
}

COND_EDGES: list[tuple[str, str, float]] = [
    ("C\u2080", "C\u2081", -0.15),
    ("C\u2080", "C\u2082", -0.28),
    ("C\u2081", "C\u2082", -0.15),
]

COND_R = 0.62


# ── helpers ───────────────────────────────────────────────────────────────────


def _panel_box(
    ax: plt.Axes, xlim: tuple[float, float], ylim: tuple[float, float]
) -> None:
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.axis("off")
    w = xlim[1] - xlim[0]
    h = ylim[1] - ylim[0]
    pad = 0.18
    ax.add_patch(
        FancyBboxPatch(
            (xlim[0] + pad, ylim[0] + pad),
            w - 2 * pad,
            h - 2 * pad,
            boxstyle="round,pad=0.0,rounding_size=0.35",
            linewidth=LW,
            edgecolor=BLACK,
            facecolor="white",
            zorder=0,
        )
    )


def _node(
    ax: plt.Axes,
    cx: float,
    cy: float,
    label: str,
    scc: int,
    r: float = NODE_R,
    fs: float = 0.0,
) -> None:
    fc = SCC_FILL[scc]
    ec = SCC_EDGE[scc]
    ax.add_patch(
        mpatches.Circle(
            (cx, cy),
            r,
            facecolor=fc,
            edgecolor=ec,
            linewidth=LW,
            zorder=3,
        )
    )
    ax.text(
        cx,
        cy,
        label,
        ha="center",
        va="center",
        fontsize=fs or LABEL_FS,
        fontweight="bold",
        zorder=4,
    )


def _arrow(
    ax: plt.Axes,
    x0: float,
    y0: float,
    x1: float,
    y1: float,
    rad: float = 0.0,
    color: str = BLACK,
    r0: float = NODE_R,
    r1: float = NODE_R,
    lw: float = 0.0,
) -> None:
    dx, dy = x1 - x0, y1 - y0
    dist = math.hypot(dx, dy)
    if dist < 1e-9:
        return
    ux, uy = dx / dist, dy / dist
    sx = x0 + ux * r0
    sy = y0 + uy * r0
    ex = x1 - ux * r1
    ey = y1 - uy * r1
    ax.annotate(
        "",
        xy=(ex, ey),
        xytext=(sx, sy),
        arrowprops=dict(
            arrowstyle="-|>",
            color=color,
            lw=lw or LW,
            mutation_scale=ARROW_SCALE,
            connectionstyle=f"arc3,rad={rad}",
        ),
        zorder=2,
    )


def _scc_hull(ax: plt.Axes, centers: list[tuple[float, float]], scc: int) -> None:
    """Draw a soft rounded bounding ellipse around the SCC's nodes."""
    xs = [c[0] for c in centers]
    ys = [c[1] for c in centers]
    cx = sum(xs) / len(xs)
    cy = sum(ys) / len(ys)
    hw = max(abs(x - cx) for x in xs) + NODE_R + 0.25
    hh = max(abs(y - cy) for y in ys) + NODE_R + 0.25
    hw = max(hw, 0.7)
    hh = max(hh, 0.7)
    ellipse = mpatches.Ellipse(
        (cx, cy),
        2 * hw,
        2 * hh,
        facecolor=SCC_FILL[scc],
        edgecolor=SCC_EDGE[scc],
        linewidth=LW,
        linestyle="--",
        alpha=0.35,
        zorder=1,
    )
    ax.add_patch(ellipse)


# ── Panel A: original directed graph ──────────────────────────────────────────


def draw_graph(ax: plt.Axes) -> None:
    _panel_box(ax, (0.5, 9.5), (3.5, 8.5))

    ax.text(
        5.0,
        8.1,
        "Directed graph — SCCs highlighted",
        ha="center",
        va="center",
        fontsize=TITLE_FS,
        fontweight="bold",
    )

    scc_centers: dict[int, list[tuple[float, float]]] = {0: [], 1: [], 2: []}
    for name, (cx, cy, scc) in NODES.items():
        scc_centers[scc].append((cx, cy))

    for scc_i, centers in scc_centers.items():
        _scc_hull(ax, centers, scc_i)

    cross = {(s, d) for s, d, _ in EDGES if NODES[s][2] != NODES[d][2]}
    for src, dst, rad in EDGES:
        if (src, dst) in cross:
            sx, sy, _ = NODES[src]
            dx, dy, _ = NODES[dst]
            _arrow(ax, sx, sy, dx, dy, rad=rad, color=GRAY, lw=1.2)

    for src, dst, rad in EDGES:
        if (src, dst) not in cross:
            sx, sy, scc = NODES[src]
            dx, dy, _ = NODES[dst]
            _arrow(ax, sx, sy, dx, dy, rad=rad, color=SCC_EDGE[scc])

    for name, (cx, cy, scc) in NODES.items():
        _node(ax, cx, cy, name, scc)

    HULL_LABELS = [
        (2.75, 4.2, "SCC 0", 0),
        (5.5, 4.2, "SCC 1", 1),
        (7.5, 4.2, "SCC 2", 2),
    ]
    for lx, ly, lt, scc in HULL_LABELS:
        ax.text(
            lx,
            ly,
            lt,
            ha="center",
            va="center",
            fontsize=SMALL_FS,
            color=SCC_EDGE[scc],
            fontweight="bold",
        )

    ax.text(
        5.0,
        4.0,
        "Dashed gray arrows are cross-SCC edges",
        ha="center",
        va="center",
        fontsize=SMALL_FS,
        color=GRAY,
        style="italic",
    )


# ── Panel B: condensation DAG ─────────────────────────────────────────────────


def draw_condensation(ax: plt.Axes) -> None:
    _panel_box(ax, (0.5, 9.5), (3.5, 8.5))

    ax.text(
        5.0,
        8.1,
        "Condensation DAG",
        ha="center",
        va="center",
        fontsize=TITLE_FS,
        fontweight="bold",
    )

    for src, dst, rad in COND_EDGES:
        sx, sy, scc_s = COND_NODES[src]
        dx, dy, scc_d = COND_NODES[dst]
        _arrow(ax, sx, sy, dx, dy, rad=rad, color=BLACK, r0=COND_R, r1=COND_R)

    for name, (cx, cy, scc) in COND_NODES.items():
        _node(ax, cx, cy, name, scc, r=COND_R, fs=LABEL_FS + 1)
        ax.text(
            cx,
            cy - COND_R - 0.28,
            COND_CONTENTS[name],
            ha="center",
            va="top",
            fontsize=SMALL_FS,
            color=SCC_EDGE[scc],
        )

    ax.text(
        5.0,
        7.55,
        "Each SCC collapses to one vertex — result is always a DAG",
        ha="center",
        va="center",
        fontsize=SMALL_FS,
        color=GRAY,
        style="italic",
    )

    ax.text(
        5.0,
        4.0,
        "Condensation enables reasoning about component-level dependencies",
        ha="center",
        va="center",
        fontsize=SMALL_FS,
        color=GRAY,
        style="italic",
    )


# ── main ──────────────────────────────────────────────────────────────────────


def main() -> None:
    rc: dict = {
        "figure.facecolor": _CFG["figure"]["facecolor"],
        "font.family": _CFG["font"]["family"],
        "font.sans-serif": _CFG["font"]["sans_serif"],
    }
    plt.rcParams.update(rc)

    fig, (ax_left, ax_right) = plt.subplots(
        1, 2, figsize=(13, 6.5), layout="constrained"
    )
    fig.suptitle(
        "STRONGLY CONNECTED COMPONENTS", fontsize=_FS["suptitle"], fontweight="black"
    )

    for ax in (ax_left, ax_right):
        ax.set_anchor("N")

    draw_graph(ax_left)
    draw_condensation(ax_right)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
