import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import gaussian_kde

# --- Data ----------------------------------------------------------------
# Isolated RNG — reproducible without polluting global numpy state
rng = np.random.default_rng(42)
physics = rng.normal(loc=65, scale=12, size=200)
math = rng.normal(loc=72, scale=9, size=200)

# Seaborn expects a tidy DataFrame: one row per observation, one column per variable
df = pd.DataFrame(
    {
        "Score": np.concatenate([physics, math]),
        "Group": ["Physics"] * 200 + ["Math"] * 200,
    }
)

# --- Figure --------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle("Native ax.hist() vs sns.histplot()", fontsize=14, fontweight="bold")

# --- Left: matplotlib native hist() -------------------------------------
# density=True: y-axis is probability density, not counts (area under = 1)
# colors set explicitly — mpl default cycle may clash between two overlaid hists
ax1.hist(physics, bins=20, density=True, alpha=0.5, color="steelblue", label="Physics")
ax1.hist(math, bins=20, density=True, alpha=0.5, color="orange", label="Math")

# KDE must be added manually in native mpl — scipy fits the kernel, we evaluate it
# over a smooth x range and plot the resulting curve
for data, color in [(physics, "steelblue"), (math, "orange")]:
    kde = gaussian_kde(data)
    x_range = np.linspace(data.min() - 5, data.max() + 5, 300)
    ax1.plot(x_range, kde(x_range), color=color, linewidth=2)

ax1.set_title("Native ax.hist() + scipy KDE")
# legend must be called manually — hist() has no hue= equivalent
ax1.legend()

# --- Right: seaborn histplot() ------------------------------------------
# hue= splits by the Group column — colors, legend, and KDE all handled automatically
# kde=True overlays a KDE curve per group (no separate kdeplot() call needed)
# stat="density" matches ax.hist(density=True) so both plots are comparable
# ax=ax2 injects into our subplot — figure-level displot() cannot do this
sns.histplot(
    data=df,
    x="Score",
    hue="Group",
    kde=True,
    stat="density",
    alpha=0.5,
    element="bars",
    ax=ax2,
)
ax2.set_title("sns.histplot(kde=True, hue=)")

# --- Shared formatting ---------------------------------------------------
for ax in (ax1, ax2):
    ax.set_xlabel("Score", fontsize=11)
    ax.set_ylabel("Density", fontsize=11)
    ax.grid(True, linestyle="--", alpha=0.4)

fig.tight_layout()
plt.show()
