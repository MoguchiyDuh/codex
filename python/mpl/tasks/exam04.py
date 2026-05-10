import matplotlib.pyplot as plt
import seaborn as sns

# --- Data ----------------------------------------------------------------
penguins = sns.load_dataset("penguins").dropna(subset=["species", "sex", "body_mass_g"])

# --- Plot ----------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 6))

sns.boxplot(
    data=penguins,
    x="species",
    y="body_mass_g",
    hue="sex",
    palette="Set2",
    ax=ax,
)

ax.set_title("Penguin Body Mass by Species and Sex", fontsize=13)
ax.set_xlabel("Species")
ax.set_ylabel("Body Mass (g)")
# move legend to upper left
ax.legend(title="Sex", loc="upper left")
ax.grid(True, axis="y", linestyle="--", alpha=0.4)
fig.tight_layout()
plt.show()
