import matplotlib.pyplot as plt
import seaborn as sns

# --- Data ----------------------------------------------------------------
mpg = sns.load_dataset("mpg").dropna(subset=["origin", "weight", "mpg"])

# dictionary-based color mapping — map each origin string to a color
# then pass the resulting Series as c= to scatter()
color_map = {"usa": "steelblue", "japan": "crimson", "europe": "seagreen"}
colors = mpg["origin"].map(color_map)

# --- Plot ----------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 6))

# scatter each group separately so each gets a legend entry
for origin, color in color_map.items():
    subset = mpg[mpg["origin"] == origin]
    ax.scatter(
        subset["weight"],
        subset["mpg"],
        color=color,
        label=origin.capitalize(),
        alpha=0.7,
        edgecolors="k",
        linewidths=0.3,
        s=40,
    )

ax.set_title("Vehicle Weight vs Fuel Efficiency by Origin", fontsize=13)
ax.set_xlabel("Vehicle Weight (lbs)")
ax.set_ylabel("Miles Per Gallon")
ax.legend(title="Origin")
ax.grid(True, linestyle="--", alpha=0.4)
fig.tight_layout()
plt.show()
