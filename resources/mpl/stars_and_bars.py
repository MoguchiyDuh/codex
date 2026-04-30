"""Generates resources/pictures/stars_and_bars.png.

Illustrates the stars-and-bars bijection from Counting.md:
  n=6 stars, k=4 bins → k-1=3 bars
  Example sequence: ★★ | ★ | | ★★★  →  bins (2, 1, 0, 3)
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "stars_and_bars.png"

# ── config aliases ─────────────────────────────────────────────────────────────
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
LW = _CFG["lines"]["linewidth"]

# ── layout ────────────────────────────────────────────────────────────────────
SEQUENCE = [
    True,
    True,
    False,
    True,
    False,
    False,
    True,
    True,
    True,
]
N_STARS = sum(SEQUENCE)
N_BARS = sum(not x for x in SEQUENCE)
K = N_BARS + 1

SYMBOL_W = 0.72
STAR_R = 0.18
STAR_FS = 55
BAR_LW = 2.2

BRACE_DY = -0.38

FORMULA_Y = -1.20
SEQ_Y = 0.0


def _star(ax: plt.Axes, x: float, y: float) -> None:
    ax.text(
        x,
        y,
        r"$\bigstar$",
        ha="center",
        va="center",
        fontsize=STAR_FS,
        color=BLACK,
        zorder=3,
    )


def _bar(ax: plt.Axes, x: float, y: float) -> None:
    """Thin vertical line acting as a bin divider."""
    ax.plot(
        [x, x],
        [y - STAR_R * 1.6, y + STAR_R * 1.6],
        color=BLACK,
        lw=BAR_LW,
        solid_capstyle="butt",
        zorder=3,
    )


def _upbrace(ax: plt.Axes, x_left: float, x_right: float, y: float, label: str) -> None:
    """Bracket opening upward: horizontal base at y, ticks pointing up, label below base."""
    mid = (x_left + x_right) / 2
    tick = 0.10
    ax.plot([x_left, x_right], [y, y], color=GRAY, lw=1.2, zorder=2)
    ax.plot([x_left, x_left], [y, y + tick], color=GRAY, lw=1.2, zorder=2)
    ax.plot([x_right, x_right], [y, y + tick], color=GRAY, lw=1.2, zorder=2)
    ax.text(
        mid, y - 0.08, label, ha="center", va="top", fontsize=_FS["small"], color=GRAY
    )


def draw(ax: plt.Axes) -> None:
    total = len(SEQUENCE)
    fig_w = total * SYMBOL_W + 1.0

    ax.set_xlim(-0.5, fig_w - 0.5)
    ax.set_ylim(FORMULA_Y - 0.25, SEQ_Y + 0.75)
    ax.set_aspect("equal")
    ax.axis("off")

    # ── draw sequence ─────────────────────────────────────────────────────────
    xs = [0.4 + i * SYMBOL_W for i in range(total)]

    for x, is_star in zip(xs, SEQUENCE):
        if is_star:
            _star(ax, x, SEQ_Y)
        else:
            _bar(ax, x, SEQ_Y)

    # ── upward brackets per bin ───────────────────────────────────────────────
    bins: list[list[float]] = []
    current: list[float] = []
    for x, is_star in zip(xs, SEQUENCE):
        if is_star:
            current.append(x)
        else:
            bins.append(current)
            current = []
    bins.append(current)

    bin_labels = ["2", "1", "0", "3"]
    bar_xs = [x for x, is_star in zip(xs, SEQUENCE) if not is_star]

    brace_y = SEQ_Y + BRACE_DY
    left_bound = xs[0] - SYMBOL_W / 2

    for b, (bin_xs, label) in enumerate(zip(bins, bin_labels)):
        right_bound = (
            bar_xs[b] - SYMBOL_W / 2 if b < len(bar_xs) else xs[-1] + SYMBOL_W / 2
        )
        span_cx = (left_bound + right_bound) / 2

        if bin_xs:
            _upbrace(
                ax,
                bin_xs[0] - STAR_R - 0.05,
                bin_xs[-1] + STAR_R + 0.05,
                brace_y,
                label,
            )
        else:
            ax.text(
                span_cx,
                brace_y - 0.08,
                "0",
                ha="center",
                va="top",
                fontsize=_FS["small"],
                color=GRAY,
            )

        ax.text(
            span_cx,
            SEQ_Y + 0.48,
            f"bin {b + 1}",
            ha="center",
            va="bottom",
            fontsize=_FS["small"] - 0.5,
            color=GRAY,
            style="italic",
        )

        left_bound = right_bound + SYMBOL_W

    # ── formula rows (below sequence) ─────────────────────────────────────────
    cx = (xs[0] + xs[-1]) / 2
    ax.text(
        cx,
        FORMULA_Y + 0.18,
        r"$n = 6$ stars,  $k = 4$ bins  $\Rightarrow$  $k - 1 = 3$ bars",
        ha="center",
        va="center",
        fontsize=_FS["body"],
        color=BLACK,
    )
    ax.text(
        cx,
        FORMULA_Y - 0.18,
        r"positions: $n + k - 1 = 9$,  choose $k - 1 = 3$ for bars"
        r"  $\Rightarrow$  $\binom{9}{3} = 84$",
        ha="center",
        va="center",
        fontsize=_FS["body"],
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

    fig, ax = plt.subplots(figsize=(9, 3.8), layout="constrained")
    fig.suptitle("Stars and Bars", fontsize=_FS["suptitle"], fontweight="black")

    draw(ax)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
