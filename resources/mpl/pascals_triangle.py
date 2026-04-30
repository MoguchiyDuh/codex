"""Generates resources/pictures/pascals_triangle.png."""

from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "pascals_triangle.png"

# ── config aliases ─────────────────────────────────────────────────────────────
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]

# ── layout ────────────────────────────────────────────────────────────────────
ROWS = 9
HEX_SIZE = 0.50
LW = 1.6
ENTRY_FS = _FS["body"]
ROW_SUM_FS = _FS["small"]


def _triangle(n: int) -> list[list[int]]:
    rows = [[1]]
    for i in range(1, n):
        prev = rows[-1]
        rows.append([1] + [prev[j] + prev[j + 1] for j in range(len(prev) - 1)] + [1])
    return rows


def _hex_vertices(cx: float, cy: float, size: float) -> list[tuple[float, float]]:
    """Flat-top hexagon vertices (first vertex at top-right)."""
    return [
        (
            cx + size * math.cos(math.radians(30 + 60 * i)),
            cy + size * math.sin(math.radians(30 + 60 * i)),
        )
        for i in range(6)
    ]


def draw(ax: plt.Axes) -> None:
    T = _triangle(ROWS)

    col_step = 2 * HEX_SIZE
    row_step = math.sqrt(3) * HEX_SIZE

    fig_w = (ROWS - 1) * col_step + 2.6
    fig_h = ROWS * row_step + 0.8

    ax.set_xlim(0, fig_w)
    ax.set_ylim(0, fig_h)
    ax.set_aspect("equal")
    ax.axis("off")

    cx = fig_w / 2

    for r, row in enumerate(T):
        y = fig_h - 0.55 - r * row_step
        n_cells = len(row)
        x0 = cx - (n_cells - 1) * col_step / 2

        for k, val in enumerate(row):
            x = x0 + k * col_step
            verts = _hex_vertices(x, y, HEX_SIZE)
            hex_patch = Polygon(
                verts,
                closed=True,
                facecolor="white",
                edgecolor=BLACK,
                linewidth=LW,
                zorder=2,
            )
            ax.add_patch(hex_patch)

            fs = ENTRY_FS if val < 100 else ENTRY_FS - 1.5
            ax.text(
                x,
                y,
                str(val),
                ha="center",
                va="center",
                fontsize=fs,
                fontweight="bold",
                color=BLACK,
                zorder=3,
            )

        label_x = cx + (n_cells - 1) * col_step / 2 + HEX_SIZE + 0.18
        ax.text(
            label_x,
            y,
            f"= $2^{{{r}}}$",
            ha="left",
            va="center",
            fontsize=ROW_SUM_FS,
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

    fig, ax = plt.subplots(figsize=(7, 7), layout="constrained")
    fig.suptitle("Pascal's Triangle", fontsize=_FS["suptitle"], fontweight="black")

    draw(ax)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
