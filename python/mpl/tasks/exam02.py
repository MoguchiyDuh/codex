import matplotlib.pyplot as plt
import seaborn as sns

# --- Data ----------------------------------------------------------------
planets = sns.load_dataset("planets").dropna(subset=["method"])

# count planets per method, take top 5
top5 = planets["method"].value_counts().head(5)

# --- Plot ----------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 5))

ax.barh(top5.index, top5.values, color="orange", edgecolor="black")

ax.set_title("Top 5 Planet Discovery Methods", fontsize=13)
ax.set_xlabel("Number of Planets Discovered")
ax.set_ylabel("")
ax.grid(True, axis="x", linestyle="--", alpha=0.4)

# rotate y-axis tick labels so method names don't overlap
# tick_params is the clean way — no need to touch set_yticklabels at all
ax.tick_params(axis="y", labelrotation=30)

fig.tight_layout()
plt.show()
