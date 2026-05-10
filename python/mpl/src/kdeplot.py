import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

rng = np.random.default_rng(42)

df = pd.DataFrame(
    {
        "score": np.concatenate(
            [
                rng.normal(65, 12, 200),
                rng.normal(78, 8, 200),
                rng.normal(55, 15, 200),
            ]
        ),
        "group": ["Physics"] * 200 + ["Math"] * 200 + ["History"] * 200,
    }
)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 5), sharey=False)
fig.suptitle("sns.kdeplot() — key parameters", fontsize=14, fontweight="bold")

# --- Left: basic KDE with fill and hue ----------------------------------
# fill=True — shade area under the curve
# hue= — one curve per group, auto colors + legend
# alpha — fill transparency
sns.kdeplot(
    data=df,
    x="score",
    hue="group",
    fill=True,
    alpha=0.4,
    linewidth=2,
    ax=ax1,
)
ax1.set_title("fill=True, hue=")
ax1.set_xlabel("Score")
ax1.set_ylabel("Density")
ax1.grid(True, linestyle="--", alpha=0.4)

# --- Middle: bw_adjust — smoothing control ------------------------------
# bw_adjust scales the bandwidth — higher = smoother, lower = more detail
# default is 1.0
for bw, ls in [(0.3, ":"), (1.0, "-"), (2.0, "--")]:
    sns.kdeplot(
        data=df[df["group"] == "Physics"],
        x="score",
        bw_adjust=bw,
        linestyle=ls,
        label=f"bw_adjust={bw}",
        ax=ax2,
    )
ax2.set_title("bw_adjust — smoothing")
ax2.set_xlabel("Score")
ax2.set_ylabel("Density")
ax2.legend()
ax2.grid(True, linestyle="--", alpha=0.4)

# --- Right: cumulative KDE ----------------------------------------------
# cumulative=True — plots CDF instead of PDF
# useful for reading off percentiles visually
sns.kdeplot(
    data=df,
    x="score",
    hue="group",
    cumulative=True,
    linewidth=2,
    ax=ax3,
)
ax3.set_title("cumulative=True")
ax3.set_xlabel("Score")
ax3.set_ylabel("Cumulative density")
ax3.grid(True, linestyle="--", alpha=0.4)

fig.tight_layout()
plt.show()
