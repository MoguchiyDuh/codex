import matplotlib.pyplot as plt
import seaborn as sns

# --- Data ----------------------------------------------------------------
flights = sns.load_dataset("flights")

# pivot_table reshapes long → wide (matrix form required by heatmap)
# index = rows, columns = cols, values = cell values, aggfunc = how to aggregate
pivot = flights.pivot_table(index="month", columns="year", values="passengers")

# --- Plot ----------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 6))

sns.heatmap(
    pivot,
    annot=True,  # show passenger count inside each cell
    fmt=".0f",  # no decimals — pivot_table returns floats so "d" fails
    cmap="YlGnBu",
    cbar=False,  # remove the colorbar
    linewidths=0.5,
    ax=ax,
)

ax.set_title("Flights — Passengers per Month and Year", fontsize=13)
ax.set_xlabel("Year")
ax.set_ylabel("Month")
fig.tight_layout()
plt.show()
