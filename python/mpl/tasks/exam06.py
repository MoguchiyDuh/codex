import matplotlib.pyplot as plt
import seaborn as sns

# --- Data ----------------------------------------------------------------
mpg = sns.load_dataset("mpg").dropna(subset=["cylinders", "origin"])

# order= controls bar sequence on x-axis
# value_counts() gives descending frequency — extract index for the order
cylinder_order = mpg["cylinders"].value_counts().index.tolist()

# --- Plot ----------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 6))

# countplot counts observations per category automatically — no aggregation needed
sns.countplot(
    data=mpg,
    x="cylinders",
    hue="origin",
    order=cylinder_order,  # highest frequency first
    palette="Set2",
    ax=ax,
)

ax.set_title("Cylinder Count by Origin — ordered by frequency", fontsize=13)
ax.set_xlabel("Cylinders")
ax.set_ylabel("Count")
ax.legend(title="Origin")
ax.grid(True, axis="y", linestyle="--", alpha=0.4)
fig.tight_layout()
plt.show()
