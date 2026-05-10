"""Generates resources/pictures/dynamic_array_amortized.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())
OUTPUT = _HERE.parent / "pictures" / "dynamic_array_amortized.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL["red"]
BLUE = _COL["blue"]


def draw(ax: plt.Axes) -> None:
    n = list(range(1, 17))
    costs = []
    capacity = 0
    size = 0
    for _ in n:
        if size == capacity:
            costs.append(size + 1)
            capacity = 1 if capacity == 0 else capacity * 2
        else:
            costs.append(1)
        size += 1
    ax.bar(
        n,
        costs,
        color=[RED if c > 1 else BLUE for c in costs],
        edgecolor=BLACK,
        linewidth=LW * 0.5,
    )
    ax.plot([0.5, 16.5], [3, 3], color=GRAY, linewidth=LW, linestyle="--")
    ax.text(16.6, 3, "charge 3", va="center", fontsize=_FS["body"], color=GRAY)
    ax.set_xlim(0.5, 17.5)
    ax.set_ylim(0, 18)
    ax.set_xlabel("push number", fontsize=_FS["body"], color=BLACK)
    ax.set_ylabel("actual cost", fontsize=_FS["body"], color=BLACK)
    ax.set_title("rare resize spikes, linear total", fontsize=_FS["title"], color=BLACK)
    ax.tick_params(colors=BLACK)
    for spine in ax.spines.values():
        spine.set_color(BLACK)
    ax.grid(axis="y", color=GRAY, linestyle=":", linewidth=LW * 0.5)
    ax.text(
        2.2,
        15.0,
        r"$1 + 2 + 4 + \cdots \leq 2m$ copied items",
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
    fig, ax = plt.subplots(figsize=(8.4, 5.0), layout="constrained")
    fig.suptitle(
        "Dynamic Array Amortized Push", fontsize=_FS["suptitle"], fontweight="black"
    )
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
