import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs

# 1. Generate clustered data
X, y = make_blobs(
    n_samples=300, centers=3, n_features=2, cluster_std=1.0, random_state=42
)

# 2. Create DataFrame
df = pd.DataFrame({"x": X[:, 0], "y": X[:, 1], "cluster": y})

# 3. Plot scatter plot
plt.figure(figsize=(8, 6))
scatter = plt.scatter(
    df["x"],
    df["y"],
    c=df["cluster"],
    cmap="viridis",
    s=50,
    alpha=0.7,
    edgecolors="black",
    linewidth=0.5,
)

# 4. Customization
plt.title("Clustered Data: 3 Synthetic Blobs", fontsize=14)
plt.xlabel("Feature X", fontsize=12)
plt.ylabel("Feature Y", fontsize=12)
plt.colorbar(scatter, label="Cluster ID")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
