"""Generates resources/pictures/dynamic_array_growth.png.

Illustrates dynamic array doubling: array state at each growth step (capacity
1 → 2 → 4 → 8) with copy arrows, plus an amortized-cost bar chart showing
bounded total work.
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "dynamic_array_growth.png"

# ── config aliases ────────────────────────────────────────────────────────────
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
_BLACK = _CFG["colors"]["black"]
_GRAY = _CFG["colors"]["gray"]
_RED = _CFG["colors"]["red"]

# ── layout constants ──────────────────────────────────────────────────────────
_SLOT_W = 0.65
_SLOT_H = 0.55
_SLOT_GAP = 0.08
_ARRAY_PAD = 0.25
_ROW_GAP = 1.6
_X0 = 0.5
_Y_TOP = 7.2
_ARROW_COLOR = _RED
_OCCUPIED_COLOR = _CFG["colors"]["blue"]
_EMPTY_COLOR = _CFG["colors"]["gray"]
_COPY_ALPHA = 0.20

_CHART_X = 5.5
_CHART_Y_BOT = 0.8
_CHART_W = 3.8
_CHART_H = 6.0
_BAR_W = 0.65


def _draw_array(
    ax: plt.Axes,
    capacity: int,
    occupied: int,
    y_center: float,
    x_left: float,
    *,
    highlight_copy: int = 0,
) -> None:
    """Draw one array row: outline, occupied/empty slots, capacity label."""
    total_w = capacity * _SLOT_W + (capacity - 1) * _SLOT_GAP
    x0 = x_left
    y0 = y_center - _SLOT_H / 2

    rect = mpatches.FancyBboxPatch(
        (x0 - _ARRAY_PAD, y0),
        total_w + 2 * _ARRAY_PAD,
        _SLOT_H,
        boxstyle="round,pad=0.04",
        facecolor=_CFG["colors"]["white"],
        edgecolor=_GRAY,
        linewidth=1.0,
        zorder=0,
    )
    ax.add_patch(rect)

    for i in range(capacity):
        sx = x0 + i * (_SLOT_W + _SLOT_GAP)
        filled = i < occupied
        face = _OCCUPIED_COLOR if filled else _EMPTY_COLOR
        slot = mpatches.FancyBboxPatch(
            (sx, y0),
            _SLOT_W,
            _SLOT_H,
            boxstyle="round,pad=0.03",
            facecolor=face,
            edgecolor="none",
            zorder=2,
        )
        ax.add_patch(slot)
        if i < highlight_copy:
            overlay = mpatches.FancyBboxPatch(
                (sx, y0),
                _SLOT_W,
                _SLOT_H,
                boxstyle="round,pad=0.03",
                facecolor=_RED,
                edgecolor="none",
                alpha=_COPY_ALPHA,
                zorder=3,
            )
            ax.add_patch(overlay)

    ax.text(
        x0 - _ARRAY_PAD - 0.25,
        y_center,
        f"{capacity}",
        ha="right",
        va="center",
        fontsize=_FS_BODY,
        fontfamily=_FAMILY,
        color=_BLACK,
    )


def _draw_copy_arrow(
    ax: plt.Axes,
    x_src: float,
    y_src: float,
    x_dst: float,
    y_dst: float,
) -> None:
    """Curved arrow from source array to destination array indicating copy."""
    ax.annotate(
        "",
        xy=(x_dst, y_dst),
        xytext=(x_src, y_src),
        arrowprops=dict(
            arrowstyle="->",
            color=_ARROW_COLOR,
            lw=1.8,
            connectionstyle="arc3,rad=0.35",
        ),
        zorder=1,
    )


def _build_array_rows(ax: plt.Axes) -> None:
    """Draw the four array states: capacity 1, 2, 4, 8."""
    capacities = [1, 2, 4, 8]
    y_positions = [_Y_TOP - i * _ROW_GAP for i in range(4)]

    for idx, cap in enumerate(capacities):
        y = y_positions[idx]
        if idx == 0:
            occupied = 1
            _draw_array(ax, cap, occupied, y, _X0)
        else:
            prev_cap = capacities[idx - 1]
            occupied = prev_cap + 1
            _draw_array(ax, cap, occupied, y, _X0, highlight_copy=prev_cap)

            x_src = _X0 + (prev_cap * _SLOT_W + (prev_cap - 1) * _SLOT_GAP) / 2
            y_src = y_positions[idx - 1] - _SLOT_H / 2 - 0.15
            x_dst = _X0 + (cap * _SLOT_W + (cap - 1) * _SLOT_GAP) / 2
            y_dst = y + _SLOT_H / 2 + 0.15
            _draw_copy_arrow(ax, x_src, y_src, x_dst, y_dst)

    ax.text(
        2.4,
        0.4,
        "arrows indicate 'allocate, copy, free' cycle during growth",
        ha="center",
        va="center",
        fontsize=_FS_BODY,
        fontfamily=_FAMILY,
        color=_GRAY,
        fontstyle="italic",
    )


def _draw_amortized_chart(ax: plt.Axes) -> None:
    """Bar chart: cumulative cost per append for 8 appends."""
    n_appends = 8
    indiv_cost = []
    cumulative = 0
    capacity = 1

    for i in range(1, n_appends + 1):
        if i > capacity:
            cost = capacity + 1
            capacity *= 2
        else:
            cost = 1
        cumulative += cost
        indiv_cost.append(cost)

    indices = np.arange(1, n_appends + 1)
    amortized = np.cumsum(indiv_cost) / indices

    colors_indiv = [_RED if c > 1 else _OCCUPIED_COLOR for c in indiv_cost]
    bars = ax.bar(
        indices,
        indiv_cost,
        width=_BAR_W,
        color=colors_indiv,
        edgecolor="white",
        linewidth=0.5,
        zorder=2,
    )

    ax.plot(
        indices,
        amortized,
        "o-",
        color=_BLACK,
        lw=_LW * 0.8,
        markersize=5,
        zorder=3,
        label="amortized\nper append",
    )

    for i, bar in enumerate(bars):
        c = indiv_cost[i]
        if c > 1:
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.15,
                str(c),
                ha="center",
                va="bottom",
                fontsize=_FS_SMALL,
                fontfamily=_FAMILY,
                color=_RED,
            )

    ax.set_xticks(indices)
    ax.set_xticklabels(
        [str(i) for i in indices], fontsize=_FS_SMALL, fontfamily=_FAMILY
    )
    ax.set_ylim(0, max(indiv_cost) + 1.5)
    ax.set_ylabel("cost", fontsize=_FS_LABEL, fontfamily=_FAMILY)
    ax.set_xlabel("append #", fontsize=_FS_LABEL, fontfamily=_FAMILY)
    ax.legend(
        fontsize=_FS_SMALL,
        frameon=True,
        loc="upper left",
        handlelength=1.2,
    )
    ax.tick_params(labelsize=_FS_SMALL)
    ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))

    ax.axhline(
        y=3,
        color=_GRAY,
        linestyle="--",
        lw=1.0,
        zorder=1,
    )
    ax.text(
        n_appends + 0.4,
        3,
        "~3",
        ha="left",
        va="center",
        fontsize=_FS_SMALL,
        fontfamily=_FAMILY,
        color=_GRAY,
        fontstyle="italic",
    )


def main() -> None:
    plt.rcParams.update(
        {
            "font.family": _FAMILY,
            "font.sans-serif": _SANS,
            "figure.facecolor": _FACE,
            "axes.facecolor": _FACE,
            "text.color": _BLACK,
            "axes.edgecolor": _BLACK,
            "axes.labelcolor": _BLACK,
            "xtick.color": _BLACK,
            "ytick.color": _BLACK,
        }
    )

    fig = plt.figure(figsize=(9.5, 7.5), layout="constrained")
    gs = fig.add_gridspec(1, 2, width_ratios=[1.0, 1.15])

    ax_left = fig.add_subplot(gs[0, 0])
    ax_left.set_xlim(0, 4.8)
    ax_left.set_ylim(0, 8)
    ax_left.axis("off")
    ax_left.set_title(
        "Growth (×2 factor)",
        fontsize=_FS_TITLE,
        fontfamily=_FAMILY,
        pad=12,
    )

    ax_right = fig.add_subplot(gs[0, 1])
    ax_right.set_title(
        "Amortized cost",
        fontsize=_FS_TITLE,
        fontfamily=_FAMILY,
        pad=12,
    )

    _build_array_rows(ax_left)
    _draw_amortized_chart(ax_right)

    fig.savefig(OUTPUT, dpi=_DPI, bbox_inches=_BBOX)
    plt.close(fig)


if __name__ == "__main__":
    main()
