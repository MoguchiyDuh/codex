from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "set_venn_operations.png"

# ── config aliases ────────────────────────────────────────────────────────────
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
LABEL_FS = _FS["label"]
CAP_FS = _FS["label"]
FORM_FS = _FS["formula"]

# ── layout constants ──────────────────────────────────────────────────────────
W, H = 10.0, 5.5
CX = W / 2

R = 1.55
LEFT_C = (CX - 1.2, H / 2 + 0.25)
RIGHT_C = (CX + 1.2, H / 2 + 0.25)

DISJ_L = (CX - 2.2, H / 2 + 0.25)
DISJ_R = (CX + 2.2, H / 2 + 0.25)

OUTER_C = (CX, H / 2 + 0.35)
OUTER_R = 1.7
INNER_C = (CX - 0.2, H / 2 + 0.05)
INNER_R = 0.85

HATCH = "////"


# ── helpers ───────────────────────────────────────────────────────────────────


def _panel(ax: plt.Axes) -> None:
    """Configure axes: fixed limits, aspect, no spines, rounded border box."""
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.set_aspect("equal")
    ax.axis("off")

    box = FancyBboxPatch(
        (0.15, 0.15),
        W - 0.30,
        H - 0.30,
        boxstyle="round,pad=0.0,rounding_size=0.35",
        linewidth=LW,
        edgecolor=BLACK,
        facecolor="white",
        zorder=0,
    )
    ax.add_patch(box)


def _circle(ax: plt.Axes, center: tuple[float, float], radius: float, **kw) -> Circle:
    defaults = dict(facecolor="white", edgecolor=BLACK, linewidth=LW)
    defaults.update(kw)
    c = Circle(center, radius, **defaults)
    ax.add_patch(c)
    return c


def _hatched_circle(
    ax: plt.Axes,
    center: tuple[float, float],
    radius: float,
    clip_to: Circle | None = None,
) -> None:
    """Draw a hatched filled circle, optionally clipped to another circle."""
    patch = Circle(
        center,
        radius,
        facecolor="white",
        edgecolor=BLACK,
        linewidth=0,
        hatch=HATCH,
        zorder=2,
    )
    if clip_to is not None:
        patch.set_clip_path(clip_to)
    ax.add_patch(patch)


def _ab_labels(ax: plt.Axes, lx: float, rx: float, y: float) -> None:
    kw = dict(fontsize=LABEL_FS, fontweight="bold", ha="center", va="center", zorder=5)
    ax.text(lx, y, "A", **kw)
    ax.text(rx, y, "B", **kw)


def _caption(ax: plt.Axes, formula: str, caption: str) -> None:
    if formula:
        ax.text(
            CX,
            1.05,
            formula,
            fontsize=FORM_FS,
            fontweight="bold",
            ha="center",
            va="center",
            zorder=5,
        )
    ax.text(
        CX,
        0.52,
        caption,
        fontsize=CAP_FS,
        fontweight="bold",
        ha="center",
        va="center",
        zorder=5,
    )


# ── panel drawing functions ───────────────────────────────────────────────────


def draw_disjoint(ax: plt.Axes) -> None:
    _panel(ax)
    _circle(ax, DISJ_L, R)
    _circle(ax, DISJ_R, R)
    _ab_labels(ax, DISJ_L[0], DISJ_R[0], H / 2 + 0.25)
    _caption(ax, "", "Set A and Set B")


def draw_intersection(ax: plt.Axes) -> None:
    _panel(ax)
    _circle(ax, LEFT_C, R)
    _circle(ax, RIGHT_C, R)

    right_outline = Circle(RIGHT_C, R, transform=ax.transData)
    _hatched_circle(ax, LEFT_C, R, clip_to=right_outline)

    _circle(ax, LEFT_C, R, facecolor="none")
    _circle(ax, RIGHT_C, R, facecolor="none")
    _ab_labels(ax, LEFT_C[0] - 1.3, RIGHT_C[0] + 1.3, H / 2 + 0.25)
    _caption(ax, r"$A \cap B$", "The intersection of A and B")


def draw_symmetric_difference(ax: plt.Axes) -> None:
    _panel(ax)
    _hatched_circle(ax, LEFT_C, R)
    _hatched_circle(ax, RIGHT_C, R)

    left_outline = Circle(LEFT_C, R, transform=ax.transData)
    white = Circle(
        RIGHT_C, R, facecolor="white", edgecolor="none", linewidth=0, zorder=3
    )
    white.set_clip_path(left_outline)
    ax.add_patch(white)

    _circle(ax, LEFT_C, R, facecolor="none", zorder=4)
    _circle(ax, RIGHT_C, R, facecolor="none", zorder=4)
    _ab_labels(ax, LEFT_C[0] - 1.3, RIGHT_C[0] + 1.3, H / 2 + 0.25)
    _caption(ax, r"$A \triangle B$", "The symmetric difference of A and B")


def draw_difference(ax: plt.Axes) -> None:
    _panel(ax)
    _hatched_circle(ax, LEFT_C, R)

    left_outline = Circle(LEFT_C, R, transform=ax.transData)
    white = Circle(
        RIGHT_C, R, facecolor="white", edgecolor="none", linewidth=0, zorder=3
    )
    white.set_clip_path(left_outline)
    ax.add_patch(white)

    _circle(ax, LEFT_C, R, facecolor="none", zorder=4)
    _circle(ax, RIGHT_C, R, facecolor="none", zorder=4)
    _ab_labels(ax, LEFT_C[0] - 1.3, RIGHT_C[0] + 1.3, H / 2 + 0.25)
    _caption(ax, r"$A \setminus B$", "The relative complement of B in A")


def draw_subset(ax: plt.Axes) -> None:
    _panel(ax)
    _circle(ax, OUTER_C, OUTER_R)
    _circle(ax, INNER_C, INNER_R)
    ax.text(
        INNER_C[0],
        INNER_C[1],
        "A",
        fontsize=LABEL_FS,
        fontweight="bold",
        ha="center",
        va="center",
        zorder=5,
    )
    ax.text(
        OUTER_C[0] + 0.9,
        OUTER_C[1] + 0.85,
        "B",
        fontsize=LABEL_FS,
        fontweight="bold",
        ha="center",
        va="center",
        zorder=5,
    )
    _caption(ax, r"$A \subseteq B$", "A is a subset of B")


def draw_union(ax: plt.Axes) -> None:
    _panel(ax)
    _hatched_circle(ax, LEFT_C, R)
    _hatched_circle(ax, RIGHT_C, R)
    _circle(ax, LEFT_C, R, facecolor="none", zorder=4)
    _circle(ax, RIGHT_C, R, facecolor="none", zorder=4)
    _ab_labels(ax, LEFT_C[0] - 1.3, RIGHT_C[0] + 1.3, H / 2 + 0.25)
    _caption(ax, r"$A \cup B$", "The union of A and B")


# ── main ──────────────────────────────────────────────────────────────────────


PANELS = [
    draw_disjoint,
    draw_intersection,
    draw_symmetric_difference,
    draw_difference,
    draw_subset,
    draw_union,
]


def main() -> None:
    plt.rcParams.update(
        {
            "figure.facecolor": _CFG["figure"]["facecolor"],
            "font.family": _CFG["font"]["family"],
            "font.sans-serif": _CFG["font"]["sans_serif"],
        }
    )

    fig, axes = plt.subplots(3, 2, figsize=(12, 10), layout="constrained")
    fig.suptitle("SETS BASIC OPERATIONS", fontsize=_FS["suptitle"], fontweight="black")

    for ax, draw_fn in zip(axes.flat, PANELS, strict=True):
        draw_fn(ax)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
