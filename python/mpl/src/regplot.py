import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

rng = np.random.default_rng(42)

x = rng.normal(50, 10, 200)
df = pd.DataFrame(
    {
        "x": x,
        "linear": 2 * x + rng.normal(0, 15, 200),
        "noisy": 2 * x + rng.normal(0, 40, 200),
        "nonlin": 0.05 * x**2 - x + rng.normal(0, 10, 200),
    }
)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle("sns.regplot() — key parameters", fontsize=14, fontweight="bold")

# --- Left: basic linear regression with CI ------------------------------
# ci=95 — shaded 95% confidence interval band around the regression line
# scatter_kws / line_kws — dicts of kwargs forwarded to scatter and line artists
sns.regplot(
    data=df,
    x="x",
    y="linear",
    ci=95,
    scatter_kws={"alpha": 0.5, "s": 30},
    line_kws={"color": "red", "linewidth": 2},
    ax=ax1,
)
ax1.set_title("Linear regression, ci=95")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.grid(True, linestyle="--", alpha=0.4)

# --- Middle: ci=None — no confidence band -------------------------------
# useful when the band clutters the plot or data is very noisy
sns.regplot(
    data=df,
    x="x",
    y="noisy",
    ci=None,
    scatter_kws={"alpha": 0.4, "s": 30},
    line_kws={"color": "crimson", "linewidth": 2},
    ax=ax2,
)
ax2.set_title("Noisy data, ci=None")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.grid(True, linestyle="--", alpha=0.4)

# --- Right: polynomial regression via order= ----------------------------
# order=2 — fits a degree-2 polynomial instead of a line
# use when the relationship is clearly curved
sns.regplot(
    data=df,
    x="x",
    y="nonlin",
    order=2,
    ci=95,
    scatter_kws={"alpha": 0.5, "s": 30},
    line_kws={"color": "darkorange", "linewidth": 2},
    ax=ax3,
)
ax3.set_title("Polynomial fit, order=2")
ax3.set_xlabel("x")
ax3.set_ylabel("y")
ax3.grid(True, linestyle="--", alpha=0.4)

fig.tight_layout()
plt.show()
