"""Generates resources/pictures/hasse_diagram.png."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

_HERE = Path(__file__).resolve().parent
_CFG = json.loads((_HERE / "config.json").read_text())

OUTPUT = _HERE.parent / "pictures" / "hasse_diagram.png"

_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
WHITE = _COL["white"]

NODE_R = 0.43
NODES = {"{}": (3.0, 0.8), "{1}": (1.55, 2.3), "{2}": (4.45, 2.3), "{1,2}": (3.0, 3.9)}
EDGES = [("{}", "{1}"), ("{}", "{2}"), ("{1}", "{1,2}"), ("{2}", "{1,2}")]


def draw(ax: plt.Axes) -> None:
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 5.25)
    ax.set_aspect("equal")
    ax.axis("off")
    for a, b in EDGES:
        x0, y0 = NODES[a]
        x1, y1 = NODES[b]
        ax.plot([x0, x1], [y0, y1], color=BLACK, linewidth=LW, zorder=1)
    for label, (x, y) in NODES.items():
        ax.add_patch(
            Circle(
                (x, y), NODE_R, facecolor=WHITE, edgecolor=BLACK, linewidth=LW, zorder=2
            )
        )
        ax.text(
            x,
            y,
            label,
            ha="center",
            va="center",
            fontsize=_FS["label"],
            color=BLACK,
            zorder=3,
        )
    ax.text(
        3,
        4.85,
        r"$(\mathcal{P}(\{1,2\}), \subseteq)$",
        ha="center",
        fontsize=_FS["formula"],
        color=BLACK,
    )
    ax.text(
        3,
        0.2,
        "transitive edges are omitted",
        ha="center",
        fontsize=_FS["body"],
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
    fig, ax = plt.subplots(figsize=(5.8, 5.2), layout="constrained")
    fig.suptitle("Hasse Diagram", fontsize=_FS["suptitle"], fontweight="black")
    draw(ax)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
