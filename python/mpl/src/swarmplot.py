import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

rng = np.random.default_rng(42)

df = pd.DataFrame(
    {
        "subject": rng.choice(["Math", "Physics", "History"], 150),
        "grade": rng.choice(["A", "B", "C"], 150),
        "score": rng.normal(70, 15, 150),
    }
)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), sharey=True)
fig.suptitle("sns.swarmplot()", fontsize=14, fontweight="bold")

# --- Left: basic swarmplot ----------------------------------------------
# swarmplot shows every individual point — no overlap, points are jittered
# along the categorical axis to avoid overplotting
# best for small-medium datasets (< 500 points) — gets slow and crowded beyond that
sns.swarmplot(
    data=df,
    x="subject",
    y="score",
    hue="grade",
    palette="Set2",
    size=5,  # marker diameter in points
    ax=ax1,
)
ax1.set_title("swarmplot — every point visible")
ax1.set_xlabel("Subject")
ax1.set_ylabel("Score")
ax1.grid(True, axis="y", linestyle="--", alpha=0.4)

# --- Right: swarmplot overlaid on boxplot -------------------------------
# common pattern — boxplot shows summary, swarmplot shows raw data on top
# dodge=True on swarmplot aligns points with grouped boxplot bars
sns.boxplot(
    data=df,
    x="subject",
    y="score",
    hue="grade",
    palette="Set2",
    width=0.6,
    flierprops={"marker": ""},  # hide boxplot outlier dots — swarm shows them
    ax=ax2,
)
sns.swarmplot(
    data=df,
    x="subject",
    y="score",
    hue="grade",
    palette="dark:black",  # dark points so they stand out over colored boxes
    size=3,
    dodge=True,  # align with hue= groups in the boxplot
    legend=False,  # boxplot already has the legend
    ax=ax2,
)
ax2.set_title("swarmplot over boxplot")
ax2.set_xlabel("Subject")
ax2.set_ylabel("")
ax2.grid(True, axis="y", linestyle="--", alpha=0.4)

fig.tight_layout()
plt.show()
