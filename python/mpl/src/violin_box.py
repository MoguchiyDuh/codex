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
                rng.normal(72, 9, 200),
                rng.normal(60, 15, 200),
            ]
        ),
        "subject": ["Physics"] * 200 + ["Math"] * 200 + ["History"] * 200,
        "year": (["Year 1"] * 100 + ["Year 2"] * 100) * 3,
    }
)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), sharey=True)
fig.suptitle("Boxplot vs Violinplot", fontsize=14, fontweight="bold")

# --- Left: boxplot -------------------------------------------------------
# shows: median (line), IQR (box), 1.5*IQR whiskers, outliers (dots)
sns.boxplot(
    data=df,
    x="subject",
    y="score",
    hue="year",  # grouped boxes per category
    palette="Set2",
    width=0.6,  # box width
    linewidth=1.5,  # box edge thickness
    flierprops={"marker": "o", "markersize": 4},  # outlier dot style
    ax=ax1,
)
ax1.set_title("sns.boxplot()")
ax1.set_xlabel("")
ax1.set_ylabel("Score")
ax1.grid(True, axis="y", linestyle="--", alpha=0.4)

# --- Right: violinplot ---------------------------------------------------
# shows: full distribution shape (KDE) + embedded boxplot summary
sns.violinplot(
    data=df,
    x="subject",
    y="score",
    hue="year",
    palette="Set2",
    split=True,  # mirror the two hue groups inside one violin — needs exactly 2 hue values
    inner="quart",  # marks inside violin: "quart", "box", "point", "stick", or None
    linewidth=1.2,
    ax=ax2,
)
ax2.set_title("sns.violinplot(split=True, inner='quart')")
ax2.set_xlabel("")
ax2.set_ylabel("")
ax2.grid(True, axis="y", linestyle="--", alpha=0.4)

fig.tight_layout()
plt.show()
