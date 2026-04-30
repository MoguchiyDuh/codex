# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "matplotlib>=3.9",
#   "networkx>=3.0",
# ]
# ///

"""
Generates resources/pictures/scc_condensation_dag.png.
Visualizes a directed graph and its condensation DAG.
"""

import json
from pathlib import Path
import matplotlib.pyplot as plt
import networkx as nx

_HERE = Path(__file__).resolve().parent
_REPO_ROOT = _HERE.parent.parent.parent
_CFG_PATH = _REPO_ROOT / "resources" / "mpl" / "config.json"
_CFG = json.loads(_CFG_PATH.read_text())

OUTPUT = _REPO_ROOT / "resources" / "pictures" / "scc_condensation_dag.png"

# Style aliases
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
ORANGE = "#f59e0b"
GREEN = "#22c55e"
PURPLE = "#a855f7"


def main():
    G = nx.DiGraph()
    G.add_edges_from([(1, 2), (2, 1), (3, 4), (4, 5), (5, 3), (2, 3), (4, 6), (5, 6)])

    sccs = list(nx.strongly_connected_components(G))
    node_to_scc = {}
    for i, scc in enumerate(sccs):
        for node in scc:
            node_to_scc[node] = i
    scc_colors = [ORANGE, GREEN, PURPLE]
    C = nx.condensation(G)

    plt.rcParams.update(
        {
            "font.family": _CFG["font"]["family"],
            "font.sans-serif": _CFG["font"]["sans_serif"],
            "figure.facecolor": "white",
        }
    )

    fig, (ax_orig, ax_cond) = plt.subplots(1, 2, figsize=(12, 6), layout="constrained")
    fig.suptitle("SCC CONDENSATION DAG", fontsize=_FS["suptitle"], fontweight="black")

    pos_orig = {
        1: (0, 1),
        2: (1, 1),
        3: (2.5, 1.5),
        4: (3.5, 1),
        5: (2.5, 0.5),
        6: (5, 1),
    }
    node_colors_orig = [scc_colors[node_to_scc[n]] for n in G.nodes()]
    nx.draw_networkx_nodes(
        G,
        pos_orig,
        ax=ax_orig,
        node_color=node_colors_orig,
        edgecolors=BLACK,
        linewidths=LW,
        node_size=800,
    )
    nx.draw_networkx_labels(
        G,
        pos_orig,
        ax=ax_orig,
        font_size=_FS["label"],
        font_weight="bold",
        font_color="white",
    )
    nx.draw_networkx_edges(
        G,
        pos_orig,
        ax=ax_orig,
        edge_color=GRAY,
        width=LW,
        arrows=True,
        arrowsize=25,
        min_source_margin=15,
        min_target_margin=15,
        arrowstyle="<-",
    )  # Forced inversion to fix environment bug
    ax_orig.set_title(
        "Original Directed Graph with Cycles", fontsize=_FS["title"], fontweight="bold"
    )
    ax_orig.axis("off")

    pos_cond = {0: (0, 0), 1: (1, 0), 2: (2, 0)}
    cond_labels = {i: f"SCC {i + 1}" for i in C.nodes()}
    nx.draw_networkx_nodes(
        C,
        pos_cond,
        ax=ax_cond,
        node_color=scc_colors,
        edgecolors=BLACK,
        linewidths=LW,
        node_size=3000,
    )
    nx.draw_networkx_labels(
        C,
        pos_cond,
        ax=ax_cond,
        labels=cond_labels,
        font_size=_FS["body"],
        font_weight="bold",
        font_color="white",
    )
    nx.draw_networkx_edges(
        C,
        pos_cond,
        ax=ax_cond,
        edge_color=GRAY,
        width=LW * 1.5,
        arrows=True,
        arrowsize=30,
        min_source_margin=40,
        min_target_margin=40,
        arrowstyle="<-",
    )  # Forced inversion to fix environment bug
    ax_cond.set_title(
        "Condensation Graph (always a DAG)", fontsize=_FS["title"], fontweight="bold"
    )
    ax_cond.axis("off")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
