"""Generates resources/pictures/random_walk_1d.png."""

from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.pyplot as plt

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "random_walk_1d.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
BLUE = _COL["blue"]

STEPS = [1, -1, 1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, 1]


def draw(ax: plt.Axes) -> None:
    xs = list(range(len(STEPS) + 1))
    ys = [0]
    for step in STEPS:
        ys.append(ys[-1] + step)
    upper = [math.sqrt(x) for x in xs]
    lower = [-math.sqrt(x) for x in xs]
    ax.fill_between(xs, lower, upper, color=GRAY, alpha=0.25)
    ax.step(xs, ys, where="post", color=BLUE, linewidth=LW)
    ax.axhline(0, color=BLACK, linewidth=LW)
    ax.set_xlabel("step", fontsize=_FS["label"])
    ax.set_ylabel("position", fontsize=_FS["label"])
    ax.text(
        8.0,
        3.25,
        r"typical scale $\Theta(\sqrt{n})$",
        ha="center",
        fontsize=_FS["label"],
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
    fig, ax = plt.subplots(figsize=(7, 4), layout="constrained")
    fig.suptitle(
        "One-Dimensional Random Walk", fontsize=_FS["suptitle"], fontweight="black"
    )
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
