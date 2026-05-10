"""Generates resources/pictures/activity_selection.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "activity_selection.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
BLUE = _COL["blue"]
ORANGE = _COL["orange"]
WHITE = _COL["white"]

ACTIVITIES = [
    (0, 3, "a1", True),
    (1, 4, "a2", False),
    (3, 5, "a3", True),
    (4, 7, "a4", False),
    (5, 9, "a5", True),
    (6, 10, "a6", False),
    (9, 11, "a7", True),
]


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(-0.3, 11.7)
    ax.set_ylim(-0.2, 4.2)
    ax.axis("off")
    ax.plot([0, 11], [0.5, 0.5], color=BLACK, linewidth=LW)
    for t in range(12):
        ax.plot([t, t], [0.4, 0.6], color=BLACK, linewidth=LW * 0.6)
        ax.text(t, 0.15, str(t), ha="center", fontsize=_FS["small"], color=GRAY)

    for i, (start, finish, label, chosen) in enumerate(ACTIVITIES):
        y = 3.55 - i * 0.42
        fill = BLUE if chosen else WHITE
        edge = BLACK if chosen else GRAY
        ax.add_patch(
            Rectangle(
                (start, y - 0.14),
                finish - start,
                0.28,
                facecolor=fill,
                edgecolor=edge,
                linewidth=LW,
            )
        )
        ax.text(
            (start + finish) / 2,
            y,
            label,
            ha="center",
            va="center",
            fontsize=_FS["small"],
            color=BLACK,
        )

    ax.text(
        0,
        3.95,
        "sort by finish time, then keep the next compatible interval",
        fontsize=_FS["body"],
        color=BLACK,
    )
    ax.text(7.35, 3.55, "earliest finish leaves", fontsize=_FS["body"], color=ORANGE)
    ax.text(7.35, 3.25, "maximum room", fontsize=_FS["body"], color=ORANGE)
    ax.text(7.35, 2.82, "selected: a1, a3, a5, a7", fontsize=_FS["body"], color=BLACK)


def main() -> None:
    plt.rcParams.update(
        {
            "figure.facecolor": _CFG["figure"]["facecolor"],
            "font.family": _CFG["font"]["family"],
            "font.sans-serif": _CFG["font"]["sans_serif"],
        }
    )
    fig, ax = plt.subplots(figsize=(9, 4.6), layout="constrained")
    fig.suptitle("Activity Selection", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
