"""Generates resources/pictures/quantifier_scope.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "quantifier_scope.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
BLUE = _COL["blue"]
RED = _COL["red"]
WHITE = _COL["white"]

PANEL_W = 4.2
PANEL_H = 2.9
PANEL_Y = 0.75
LEFT_X = 0.55
RIGHT_X = 5.25


def _panel(
    ax: plt.Axes, x: float, title: str, body: str, verdict: str, color: str
) -> None:
    ax.add_patch(
        FancyBboxPatch(
            (x, PANEL_Y),
            PANEL_W,
            PANEL_H,
            boxstyle="round,pad=0.08,rounding_size=0.22",
            facecolor=WHITE,
            edgecolor=BLACK,
            linewidth=LW,
        )
    )
    cx = x + PANEL_W / 2
    ax.text(
        cx, 3.25, title, ha="center", va="center", fontsize=_FS["formula"], color=BLACK
    )
    ax.text(cx, 2.25, body, ha="center", va="center", fontsize=_FS["body"], color=BLACK)
    ax.text(
        cx, 1.20, verdict, ha="center", va="center", fontsize=_FS["label"], color=color
    )


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.4)
    ax.set_aspect("equal")
    ax.axis("off")
    _panel(
        ax,
        LEFT_X,
        r"$\forall x\;\exists y:\; y>x$",
        "each x may choose\na different y",
        "true in Z",
        BLUE,
    )
    _panel(
        ax,
        RIGHT_X,
        r"$\exists y\;\forall x:\; y>x$",
        "one y must work\nfor every x",
        "false in Z",
        RED,
    )
    ax.text(
        5.0,
        0.25,
        "Mixed quantifiers do not commute",
        ha="center",
        fontsize=_FS["label"],
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
    fig, ax = plt.subplots(figsize=(8, 4), layout="constrained")
    fig.suptitle("Quantifier Scope", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
