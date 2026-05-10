"""Generates resources/pictures/state_machine_diagram.png.

Two-panel figure:
  Left  — annotated state machine notation
  Right — robot-on-a-grid parity invariant example
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "state_machine_diagram.png"

# ── config aliases ────────────────────────────────────────────────────────────
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

LW = _CFG["lines"]["linewidth"]
CIRCLE_R = 0.38
BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
WHITE = _COL["white"]
FILL_EVEN = _COL["white"]
FILL_ODD = _COL["gray"]

ANNOTATION_FS = _FS["body"]
STATE_FS = _FS["label"]
TITLE_FS = _FS["title"]
GRID_TEXT_FS = _FS["label"]


# ── helpers ───────────────────────────────────────────────────────────────────


def _panel_box(ax: plt.Axes, xlim: tuple, ylim: tuple) -> None:
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.axis("off")
    pad = 0.15
    w = xlim[1] - xlim[0]
    h = ylim[1] - ylim[0]
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


def _state(
    ax: plt.Axes,
    cx: float,
    cy: float,
    label: str,
    terminal: bool = False,
    zorder: int = 3,
) -> None:
    """Draw a state circle with optional double ring for terminal states."""
    c = Circle(
        (cx, cy),
        CIRCLE_R,
        facecolor=WHITE,
        edgecolor=BLACK,
        linewidth=LW,
        zorder=zorder,
    )
    ax.add_patch(c)
    if terminal:
        c2 = Circle(
            (cx, cy),
            CIRCLE_R * 0.72,
            facecolor=WHITE,
            edgecolor=BLACK,
            linewidth=LW,
            zorder=zorder,
        )
        ax.add_patch(c2)
    ax.text(
        cx,
        cy,
        label,
        ha="center",
        va="center",
        fontsize=STATE_FS,
        fontweight="bold",
        zorder=zorder + 1,
    )


def _start_arrow(
    ax: plt.Axes,
    tip_x: float,
    tip_y: float,
    length: float = 0.55,
    angle_deg: float = 0.0,
) -> None:
    """Small filled-dot + arrow indicating the start state."""
    rad = math.radians(angle_deg)
    dot_x = tip_x - (length + 0.08) * math.cos(rad)
    dot_y = tip_y - (length + 0.08) * math.sin(rad)
    tail_x = tip_x - length * math.cos(rad)
    tail_y = tip_y - length * math.sin(rad)
    ax.plot(dot_x, dot_y, "o", color=BLACK, markersize=8, zorder=5, clip_on=False)
    ax.annotate(
        "",
        xy=(tip_x - CIRCLE_R * math.cos(rad), tip_y - CIRCLE_R * math.sin(rad)),
        xytext=(tail_x, tail_y),
        arrowprops=dict(arrowstyle="-|>", color=BLACK, lw=LW, mutation_scale=14),
        zorder=5,
    )


def _arrow(
    ax: plt.Axes,
    x0: float,
    y0: float,
    x1: float,
    y1: float,
    label: str = "",
    label_offset: tuple = (0, 0.18),
    rad: float = 0.0,
) -> None:
    """Straight or curved arrow between two states."""
    dx, dy = x1 - x0, y1 - y0
    dist = math.hypot(dx, dy)
    ux, uy = dx / dist, dy / dist
    sx = x0 + ux * CIRCLE_R
    sy = y0 + uy * CIRCLE_R
    ex = x1 - ux * CIRCLE_R
    ey = y1 - uy * CIRCLE_R
    ax.annotate(
        "",
        xy=(ex, ey),
        xytext=(sx, sy),
        arrowprops=dict(
            arrowstyle="-|>",
            color=BLACK,
            linewidth=LW,
            mutation_scale=14,
            connectionstyle=f"arc3,rad={rad}",
        ),
        zorder=4,
    )
    if label:
        mx = (sx + ex) / 2 + label_offset[0]
        my = (sy + ey) / 2 + label_offset[1]
        ax.text(
            mx, my, label, ha="center", va="center", fontsize=ANNOTATION_FS, color=BLACK
        )


def _self_loop(
    ax: plt.Axes, cx: float, cy: float, label: str, angle_deg: float = 90.0
) -> None:
    """Draw a self-loop arc on a state."""
    r = CIRCLE_R
    loop_r = 0.28
    rad = math.radians(angle_deg)
    lx = cx + (r + loop_r) * math.cos(rad)
    ly = cy + (r + loop_r) * math.sin(rad)
    loop = Circle(
        (lx, ly), loop_r, facecolor="none", edgecolor=BLACK, linewidth=LW, zorder=3
    )
    ax.add_patch(loop)

    arrow_angle = rad - math.pi / 2
    ax_x = lx + loop_r * math.cos(arrow_angle + 0.3)
    ax_y = ly + loop_r * math.sin(arrow_angle + 0.3)
    bx = lx + loop_r * math.cos(arrow_angle + 0.3 + 0.01)
    by = ly + loop_r * math.sin(arrow_angle + 0.3 + 0.01)
    ax.annotate(
        "",
        xy=(ax_x, ax_y),
        xytext=(bx, by),
        arrowprops=dict(arrowstyle="-|>", color=BLACK, lw=LW, mutation_scale=12),
        zorder=4,
    )
    ax.text(
        lx,
        ly + loop_r + 0.14,
        label,
        ha="center",
        va="bottom",
        fontsize=ANNOTATION_FS,
        color=BLACK,
    )


def _annotation(
    ax: plt.Axes, text: str, xy: tuple, xytext: tuple, color: str = GRAY
) -> None:
    ax.annotate(
        text,
        xy=xy,
        xytext=xytext,
        fontsize=ANNOTATION_FS,
        color=color,
        fontstyle="italic",
        ha="center",
        va="center",
        arrowprops=dict(arrowstyle="-", color=color, lw=1.0, linestyle="dashed"),
    )


# ── Panel A: state machine notation ──────────────────────────────────────────


def draw_notation(ax: plt.Axes) -> None:
    _panel_box(ax, (0, 8), (0, 6))

    ax.text(
        4.0,
        5.55,
        "State machine notation",
        ha="center",
        va="center",
        fontsize=TITLE_FS,
        fontweight="bold",
    )

    Q = [(1.7, 3.0), (4.0, 3.0), (6.3, 3.0)]
    labels = ["$q_0$", "$q_1$", "$q_2$"]
    terminals = [False, False, True]
    for (cx, cy), lbl, term in zip(Q, labels, terminals):
        _state(ax, cx, cy, lbl, terminal=term)

    _start_arrow(ax, Q[0][0], Q[0][1], length=0.6, angle_deg=0)

    LABEL_A_Y = 0.22
    LABEL_B_Y = 0.40
    LABEL_C_Y = -0.15

    _arrow(ax, *Q[0], *Q[1], label="$a$", label_offset=(0, LABEL_A_Y))
    _arrow(ax, *Q[1], *Q[2], label="$b$", label_offset=(0, LABEL_B_Y))
    _arrow(ax, *Q[2], *Q[1], label="$c$", label_offset=(0, LABEL_C_Y), rad=0.35)
    _self_loop(ax, *Q[1], label="$d$", angle_deg=90)

    _annotation(ax, "start state", xy=(Q[0][0] - 0.70, Q[0][1]), xytext=(0.6, 1.8))
    _annotation(ax, "state", xy=(Q[0][0], Q[0][1] - CIRCLE_R), xytext=(1.2, 0.75))
    _annotation(
        ax,
        "transition",
        xy=((Q[0][0] + Q[1][0]) / 2, Q[0][1] + 0.22),
        xytext=(2.8, 4.95),
    )
    _annotation(
        ax, "terminal state", xy=(Q[2][0], Q[2][1] - CIRCLE_R), xytext=(6.5, 1.55)
    )
    _annotation(
        ax, "self-loop", xy=(Q[1][0], Q[1][1] + CIRCLE_R + 0.56), xytext=(5.5, 5.1)
    )

    ax.text(
        4.0,
        0.48,
        "Deterministic: at most one successor per state",
        ha="center",
        va="center",
        fontsize=ANNOTATION_FS,
        color=GRAY,
        style="italic",
    )


# ── Panel B: robot-on-a-grid parity invariant ─────────────────────────────────


def draw_robot_grid(ax: plt.Axes) -> None:
    _panel_box(ax, (0, 8), (0, 6))

    ax.text(
        4.0,
        5.55,
        "Parity invariant: robot on a grid",
        ha="center",
        va="center",
        fontsize=TITLE_FS,
        fontweight="bold",
    )

    GRID_N = 5
    CELL = 0.80
    ORIG_X = 0.62
    ORIG_Y = 0.92

    def cell_center(col: int, row: int) -> tuple[float, float]:
        return ORIG_X + col * CELL + CELL / 2, ORIG_Y + row * CELL + CELL / 2

    for row in range(GRID_N):
        for col in range(GRID_N):
            parity = (col + row) % 2
            fc = FILL_EVEN if parity == 0 else FILL_ODD
            rect = mpatches.FancyBboxPatch(
                (ORIG_X + col * CELL, ORIG_Y + row * CELL),
                CELL,
                CELL,
                boxstyle="square,pad=0",
                linewidth=0.8,
                edgecolor=GRAY,
                facecolor=fc,
                zorder=1,
            )
            ax.add_patch(rect)

    total = GRID_N * CELL
    border = mpatches.Rectangle(
        (ORIG_X, ORIG_Y),
        total,
        total,
        linewidth=LW,
        edgecolor=BLACK,
        facecolor="none",
        zorder=2,
    )
    ax.add_patch(border)

    for i in range(GRID_N):
        cx, cy = cell_center(i, 0)
        ax.text(
            cx,
            ORIG_Y - 0.22,
            str(i),
            ha="center",
            va="center",
            fontsize=GRID_TEXT_FS,
            color=BLACK,
        )
        cx2, cy2 = cell_center(0, i)
        ax.text(
            ORIG_X - 0.22,
            cy2,
            str(i),
            ha="center",
            va="center",
            fontsize=GRID_TEXT_FS,
            color=BLACK,
        )

    LABEL_00_DY = -0.17
    LABEL_10_DY = +0.22

    sx, sy = cell_center(0, 0)
    ax.plot(sx, sy, "o", color=BLUE, markersize=10, zorder=5)
    ax.text(
        sx,
        sy + LABEL_00_DY,
        "$(0,0)$",
        ha="center",
        va="top",
        fontsize=GRID_TEXT_FS,
        color=BLACK,
    )

    tx, ty = cell_center(1, 0)
    ax.plot(tx, ty, "x", color=RED, markersize=13, markeredgewidth=2.6, zorder=5)
    ax.text(
        tx,
        ty + LABEL_10_DY,
        "$(1,0)$",
        ha="center",
        va="bottom",
        fontsize=GRID_TEXT_FS,
        color=RED,
    )

    # Legal moves in this example are diagonal, so x+y changes by 0 or +/-2.
    for dcol, drow in [(1, 1)]:
        ex, ey = cell_center(dcol, drow)
        ax.annotate(
            "",
            xy=(ex, ey),
            xytext=(sx, sy),
            arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=LW, mutation_scale=13),
            zorder=4,
        )
    ax.text(
        cell_center(1, 1)[0] + 0.10,
        cell_center(1, 1)[1] + 0.10,
        "legal diagonal move",
        ha="left",
        va="bottom",
        fontsize=ANNOTATION_FS,
        color=BLUE,
    )

    LX = ORIG_X + total + 0.42
    LY_TOP = ORIG_Y + total - 0.35

    def _legend_swatch(y: float, fc: str, label: str) -> None:
        swatch = mpatches.FancyBboxPatch(
            (LX, y - 0.18),
            0.38,
            0.36,
            boxstyle="square,pad=0",
            linewidth=0.8,
            edgecolor=GRAY,
            facecolor=fc,
            zorder=3,
        )
        ax.add_patch(swatch)
        ax.text(
            LX + 0.52,
            y,
            label,
            ha="left",
            va="center",
            fontsize=GRID_TEXT_FS,
            color=BLACK,
        )

    _legend_swatch(LY_TOP, FILL_EVEN, "even parity\n$x+y$ even")
    _legend_swatch(LY_TOP - 0.72, FILL_ODD, "odd parity\n$x+y$ odd")

    INV_X = LX
    INV_Y = ORIG_Y + 1.15
    ax.text(
        INV_X,
        INV_Y + 0.62,
        "Invariant $P$:",
        ha="left",
        va="center",
        fontsize=GRID_TEXT_FS,
        fontweight="bold",
        color=BLACK,
    )
    ax.text(
        INV_X,
        INV_Y + 0.18,
        r"$x + y \equiv 0\ (\mathrm{mod}\ 2)$",
        ha="left",
        va="center",
        fontsize=GRID_TEXT_FS,
        color=BLACK,
    )
    ax.text(
        INV_X,
        INV_Y - 0.28,
        "$(1,0)$ is unreachable\n" r"$1+0=1$ is odd",
        ha="left",
        va="center",
        fontsize=GRID_TEXT_FS,
        color=RED,
    )

    ax.text(
        ORIG_X + total / 2,
        ORIG_Y - 0.48,
        r"Moves: $(\pm1,\pm1)$ — parity is preserved",
        ha="center",
        va="center",
        fontsize=GRID_TEXT_FS,
        color=GRAY,
        style="italic",
    )


# ── main ──────────────────────────────────────────────────────────────────────


def main() -> None:
    plt.rcParams.update(
        {
            "figure.facecolor": _CFG["figure"]["facecolor"],
            "font.family": _CFG["font"]["family"],
            "font.sans-serif": _CFG["font"]["sans_serif"],
        }
    )

    fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(13, 6), layout="constrained")
    fig.suptitle("STATE MACHINES", fontsize=_FS["suptitle"], fontweight="black")

    draw_notation(ax_left)
    draw_robot_grid(ax_right)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
