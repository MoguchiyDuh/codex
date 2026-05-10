import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

rng = np.random.default_rng(42)

# --- Data in wide format ------------------------------------------------
# Wide format: one row per year, one column per city
# This is the natural shape when you build the data manually
years = np.arange(2000, 2021)
wide_df = pd.DataFrame(
    {
        "year": years,
        "London": 12 + 0.05 * (years - 2000) + rng.normal(0, 0.5, len(years)),
        "Paris": 14 + 0.03 * (years - 2000) + rng.normal(0, 0.5, len(years)),
        "Berlin": 10 + 0.04 * (years - 2000) + rng.normal(0, 0.5, len(years)),
    }
)

# --- Reshape to long (tidy) format with melt() --------------------------
# melt() unpivots wide → long:
#   id_vars    = columns to keep as-is (the index / identifier)
#   value_vars = columns to unpivot into rows (default: all non-id_vars columns)
#   var_name   = name of the new column that holds the old column names
#   value_name = name of the new column that holds the values
long_df = wide_df.melt(
    id_vars="year",
    value_vars=["London", "Paris", "Berlin"],
    var_name="city",
    value_name="temperature",
)
# result: 63 rows × 3 cols — year | city | temperature
# seaborn expects this tidy shape to use hue=

# --- Figure --------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle("Wide → Long with melt() + sns.lineplot()", fontsize=14, fontweight="bold")

# --- Left: wide format — manual loop required ---------------------------
# without melt, you must loop and call plot() per column
for city, color in [
    ("London", "steelblue"),
    ("Paris", "crimson"),
    ("Berlin", "seagreen"),
]:
    ax1.plot(wide_df["year"], wide_df[city], label=city, color=color, linewidth=2)
ax1.set_title("Wide format — manual loop")
ax1.set_xlabel("Year")
ax1.set_ylabel("Avg temperature (°C)")
ax1.legend()
ax1.grid(True, linestyle="--", alpha=0.4)

# --- Right: long format — hue= handles everything ----------------------
# sns.lineplot auto-aggregates multiple y values per x per hue group
# and draws CI bands — here each x/hue combo has one value so no aggregation
sns.lineplot(
    data=long_df,
    x="year",
    y="temperature",
    hue="city",
    linewidth=2,
    ax=ax2,
)
ax2.set_title("Long format — sns.lineplot(hue=)")
ax2.set_xlabel("Year")
ax2.set_ylabel("")
ax2.grid(True, linestyle="--", alpha=0.4)

fig.tight_layout()
plt.show()
