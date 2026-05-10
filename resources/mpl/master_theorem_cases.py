"""Generates resources/pictures/master_theorem_cases.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "master_theorem_cases.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]
PURPLE = _COL["purple"]


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 6.2)
    ax.set_ylim(0, 4.4)
    ax.axis("off")
    xs = [0.8, 1.8, 2.8, 3.8, 4.8]
    cases = [
        ("Case 1", "leaves dominate", [0.2, 0.35, 0.65, 1.15, 2.0], BLUE),
        ("Case 2", "all levels equal", [1.0, 1.0, 1.0, 1.0, 1.0], PURPLE),
        ("Case 3", "root dominates", [2.0, 1.15, 0.65, 0.35, 0.2], RED),
    ]
    for r, (title, caption, heights, color) in enumerate(cases):
        y0 = 3.35 - r * 1.25
        ax.text(0.15, y0 + 0.28, title, fontsize=_FS["label"], color=BLACK)
        ax.text(0.15, y0 - 0.05, caption, fontsize=_FS["small"], color=GRAY)
        for x, h in zip(xs, heights, strict=True):
            ax.plot(
                [x, x], [y0 - 0.35, y0 - 0.35 + h * 0.36], color=color, linewidth=LW * 4
            )
        ax.text(
            5.25,
            y0,
            [r"$f(n)$ smaller", r"$f(n)$ matches", r"$f(n)$ larger"][r],
            fontsize=_FS["body"],
            color=BLACK,
        )
    ax.text(
        2.8,
        0.25,
        r"compare combine work $f(n)$ to watershed $n^{\log_b a}$",
        ha="center",
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
    fig, ax = plt.subplots(figsize=(8.4, 5.1), layout="constrained")
    fig.suptitle("Master Theorem Cases", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
