# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "matplotlib>=3.9",
#   "networkx>=3.0",
# ]
# ///

"""
Generates resources/pictures/bfs_dfs_traversal.png.
Visualizes BFS vs DFS traversal order on the same graph.
"""

import json
from pathlib import Path
import matplotlib.pyplot as plt
import networkx as nx

_HERE = Path(__file__).resolve().parent
_REPO_ROOT = _HERE.parent.parent.parent
_CFG_PATH = _REPO_ROOT / "resources" / "mpl" / "config.json"
_CFG = json.loads(_CFG_PATH.read_text())

OUTPUT = _REPO_ROOT / "resources" / "pictures" / "bfs_dfs_traversal.png"

# Style aliases
_FS = _CFG["font"]["sizes"]
_COL = _CFG["colors"]
LW = _CFG["lines"]["linewidth"]
BLACK = _COL["black"]
GRAY = _COL["gray"]
RED = _COL.get("red", "#cc0000")


def get_traversal_orders(G, start_node):
    bfs_order = list(nx.bfs_tree(G, start_node).nodes())
    dfs_order = list(nx.dfs_tree(G, start_node).nodes())
    return bfs_order, dfs_order


def draw_graph_with_order(ax, G, pos, order, title):
    # Draw edges with larger arrows
    nx.draw_networkx_edges(
        G,
        pos,
        ax=ax,
        edge_color="#666666",
        width=LW,
        arrows=True,
        arrowsize=25,
        min_source_margin=15,
        min_target_margin=15,
    )

    # Draw nodes
    nx.draw_networkx_nodes(
        G,
        pos,
        ax=ax,
        node_color="white",
        edgecolors=BLACK,
        linewidths=LW,
        node_size=1000,
    )

    # Draw labels (Node IDs)
    nx.draw_networkx_labels(
        G,
        pos,
        ax=ax,
        font_size=_FS["label"],
        font_family="sans-serif",
        font_weight="bold",
    )

    # Annotate with order - placed slightly further out
    order_map = {node: i + 1 for i, node in enumerate(order)}
    for node, (x, y) in pos.items():
        visit_num = order_map[node]
        ax.text(
            x + 0.18,
            y + 0.18,
            str(visit_num),
            color=RED,
            fontsize=_FS["label"],
            fontweight="black",
            ha="center",
            va="center",
        )

    ax.set_title(title, fontsize=_FS["title"], fontweight="bold", pad=20)
    ax.set_xlim(-2.0, 1.8)
    ax.set_ylim(-1.5, 1.5)
    ax.axis("off")


def main():
    # Define a simple DAG for traversal
    G = nx.DiGraph()
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (4, 5)]
    G.add_edges_from(edges)

    # Manual position for consistency
    pos = {0: (0, 1), 1: (-1, 0), 2: (1, 0), 3: (-1.5, -1), 4: (-0.5, -1), 5: (0.5, -1)}

    bfs_order, dfs_order = get_traversal_orders(G, 0)

    # Set up figure
    plt.rcParams.update(
        {
            "font.family": _CFG["font"]["family"],
            "font.sans-serif": _CFG["font"]["sans_serif"],
            "figure.facecolor": "white",
        }
    )

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), layout="constrained")
    fig.suptitle(
        "GRAPH TRAVERSAL: BFS VS DFS",
        fontsize=_FS["suptitle"],
        fontweight="black",
        y=0.95,
    )

    draw_graph_with_order(ax1, G, pos, bfs_order, "Breadth-First Search (Layered)")
    draw_graph_with_order(ax2, G, pos, dfs_order, "Depth-First Search (Deep)")

    # Legend for the red numbers - moved to avoid overlap
    fig.text(
        0.5,
        0.02,
        "Red numbers indicate visit order",
        ha="center",
        fontsize=_FS["body"],
        color=GRAY,
        style="italic",
    )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT, dpi=_CFG["output"]["dpi"], bbox_inches=_CFG["output"]["bbox_inches"]
    )
    plt.close(fig)
    print(f"Generated {OUTPUT}")


if __name__ == "__main__":
    main()
