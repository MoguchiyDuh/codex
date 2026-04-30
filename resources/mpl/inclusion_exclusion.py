"""Generates resources/pictures/inclusion_exclusion.png.

Two-panel Venn diagram illustrating inclusion-exclusion for 2 and 3 sets.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "inclusion_exclusion.png"

# ── config aliases ─────────────────────────────────────────────────────────────
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]

BLACK = _COL["black"]
GRAY = _COL["gray"]
LW = _CFG["lines"]["linewidth"]
HATCH = "////"

# ── layout constants ──────────────────────────────────────────────────────────
S = 10.0
CX = S / 2
CY = S / 2

R = 1.65
ALPHA = 0.30

COL_A = _COL["red"]
COL_B = _COL["blue"]
COL_C = _COL["green"]

_sep2 = R * 0.75
A2 = (CX - _sep2, CY + 0.5)
B2 = (CX + _sep2, CY + 0.5)

_side = R * 1.5
_h3 = _side * math.sqrt(3) / 2
_cy3 = CY + 0.2
A3 = (CX, _cy3 + _h3 * 2 / 3)
B3 = (CX - _side / 2, _cy3 - _h3 / 3)
C3 = (CX + _side / 2, _cy3 - _h3 / 3)

TITLE_FS = _FS["title"]
LABEL_FS = _FS["label"]
FORM_FS = _FS["body"]
SMALL_FS = _FS["small"]


# ── helpers ───────────────────────────────────────────────────────────────────


def _panel_box(ax: plt.Axes) -> None:
    ax.set_xlim(0, S)
    ax.set_ylim(0, S)
    ax.set_aspect("equal")
    ax.axis("off")
    pad = 0.18
    ax.add_patch(
        FancyBboxPatch(
            (pad, pad),
            S - 2 * pad,
            S - 2 * pad,
            boxstyle="round,pad=0.0,rounding_size=0.3",
            linewidth=LW,
            edgecolor=BLACK,
            facecolor="white",
            zorder=0,
        )
    )


def _outline(ax: plt.Axes, c: tuple, r: float = R, zorder: int = 4) -> None:
    ax.add_patch(
        Circle(c, r, facecolor="none", edgecolor=BLACK, linewidth=LW, zorder=zorder)
    )


def _filled(
    ax: plt.Axes,
    c: tuple,
    r: float = R,
    fc: str = "white",
    hatch: str | None = None,
    clip_c: tuple | None = None,
    zorder: int = 2,
) -> None:
    """Solid or hatched circle, optionally clipped to another circle."""
    ec = BLACK if hatch else "none"
    patch = Circle(
        c, r, facecolor=fc, edgecolor=ec, linewidth=0, hatch=hatch, zorder=zorder
    )
    if clip_c is not None:
        patch.set_clip_path(Circle(clip_c, r, transform=ax.transData))
    ax.add_patch(patch)


def _label(
    ax: plt.Axes, x: float, y: float, text: str, fs: float = 0, color: str = BLACK
) -> None:
    ax.text(
        x,
        y,
        text,
        ha="center",
        va="center",
        fontsize=fs or LABEL_FS,
        fontweight="bold",
        color=color,
        zorder=6,
    )


def _point_along(
    c_from: tuple[float, float], c_to: tuple[float, float], distance: float
) -> tuple[float, float]:
    """Point starting at c_from and moving toward c_to by distance."""
    dx = c_to[0] - c_from[0]
    dy = c_to[1] - c_from[1]
    norm = math.hypot(dx, dy)
    if norm == 0:
        return c_from
    ux = dx / norm
    uy = dy / norm
    return (c_from[0] + ux * distance, c_from[1] + uy * distance)


# ── Frame A: two sets ─────────────────────────────────────────────────────────


def draw_two_sets(ax: plt.Axes) -> None:
    _panel_box(ax)
    ax.text(
        CX,
        S - 0.52,
        "Two sets",
        ha="center",
        va="center",
        fontsize=TITLE_FS,
        fontweight="bold",
    )

    ax.add_patch(
        Circle(A2, R, facecolor=COL_A, edgecolor="none", alpha=ALPHA, zorder=2)
    )
    ax.add_patch(
        Circle(B2, R, facecolor=COL_B, edgecolor="none", alpha=ALPHA, zorder=2)
    )

    ax.add_patch(
        Circle(A2, R, facecolor="none", edgecolor=COL_A, linewidth=LW + 0.4, zorder=4)
    )
    ax.add_patch(
        Circle(B2, R, facecolor="none", edgecolor=COL_B, linewidth=LW + 0.4, zorder=4)
    )

    overlap2 = ((A2[0] + B2[0]) / 2, (A2[1] + B2[1]) / 2)
    label_A2 = _point_along(overlap2, A2, 1.4 * R)
    label_B2 = _point_along(overlap2, B2, 1.4 * R)
    _label(ax, *label_A2, "A", fs=21, color=COL_A)
    _label(ax, *label_B2, "B", fs=21, color=COL_B)

    ax.text(
        CX,
        A2[1],
        r"$A{\cap}B$",
        ha="center",
        va="center",
        fontsize=SMALL_FS,
        color=BLACK,
        zorder=6,
        fontweight="bold",
    )

    ax.text(
        CX,
        1.1,
        r"$|A \cup B| = |A| + |B| - |A \cap B|$",
        ha="center",
        va="center",
        fontsize=FORM_FS,
        color=BLACK,
    )


# ── Frame B: three sets ───────────────────────────────────────────────────────


def draw_three_sets(ax: plt.Axes) -> None:
    _panel_box(ax)
    ax.text(
        CX,
        S - 0.52,
        "Three sets",
        ha="center",
        va="center",
        fontsize=TITLE_FS,
        fontweight="bold",
    )

    for c, col in ((A3, COL_A), (B3, COL_B), (C3, COL_C)):
        ax.add_patch(
            Circle(c, R, facecolor=col, edgecolor="none", alpha=ALPHA, zorder=2)
        )

    for c, col in ((A3, COL_A), (B3, COL_B), (C3, COL_C)):
        ax.add_patch(
            Circle(c, R, facecolor="none", edgecolor=col, linewidth=LW + 0.4, zorder=4)
        )

    mid_AC = [(A3[0] + C3[0]) / 2, (A3[1] + C3[1]) / 2]
    mid_BC = [(B3[0] + C3[0]) / 2, (B3[1] + C3[1]) / 2]
    mid_AB = [(A3[0] + B3[0]) / 2, (A3[1] + B3[1]) / 2]
    mid_ABC = ((A3[0] + B3[0] + C3[0]) / 3, (A3[1] + B3[1] + C3[1]) / 3)

    label_A3 = _point_along(mid_ABC, A3, 1.5 * R)
    label_B3 = _point_along(mid_ABC, B3, 1.5 * R)
    label_C3 = _point_along(mid_ABC, C3, 1.5 * R)
    _label(ax, *label_A3, "A", fs=21, color=COL_A)
    _label(ax, *label_B3, "B", fs=21, color=COL_B)
    _label(ax, *label_C3, "C", fs=21, color=COL_C)

    def _push_from_centroid(
        pt: list[float], factor: float = 0.32
    ) -> tuple[float, float]:
        dx = pt[0] - mid_ABC[0]
        dy = pt[1] - mid_ABC[1]
        return (pt[0] + factor * dx, pt[1] + factor * dy)

    mid_AC = _push_from_centroid(mid_AC)
    mid_BC = _push_from_centroid(mid_BC)
    mid_AB = _push_from_centroid(mid_AB)

    kw = dict(ha="center", va="center", fontsize=SMALL_FS, fontweight="bold", zorder=5)
    ax.text(*mid_AC, r"$A{\cap}C$", color=BLACK, **kw)
    ax.text(*mid_BC, r"$B{\cap}C$", color=BLACK, **kw)
    ax.text(*mid_AB, r"$A{\cap}B$", color=BLACK, **kw)
    ax.text(
        *mid_ABC,
        r"$A{\cap}B{\cap}C$",
        color=BLACK,
        ha="center",
        va="center",
        fontsize=SMALL_FS,
        fontweight="bold",
        zorder=5,
    )

    ax.text(
        CX,
        1.4,
        r"$|A \cup B \cup C| = |A|+|B|+|C|$",
        ha="center",
        va="center",
        fontsize=FORM_FS,
        color=BLACK,
    )
    ax.text(
        CX,
        0.85,
        r"$-\,|A\cap B|-|A\cap C|-|B\cap C|+|A\cap B\cap C|$",
        ha="center",
        va="center",
        fontsize=FORM_FS,
        color=BLACK,
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

    fig, (ax_left, ax_right) = plt.subplots(
        1, 2, figsize=(12, 6.5), layout="constrained"
    )
    fig.suptitle(
        "Inclusion-Exclusion Principle", fontsize=_FS["suptitle"], fontweight="black"
    )

    draw_two_sets(ax_left)
    draw_three_sets(ax_right)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
