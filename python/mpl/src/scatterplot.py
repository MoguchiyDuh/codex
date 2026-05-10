import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

rng = np.random.default_rng(42)

df = pd.DataFrame(
    {
        "height": rng.normal(170, 10, 300),
        "weight": rng.normal(70, 15, 300),
        "age": rng.integers(18, 60, 300),
        "group": rng.choice(["A", "B", "C"], 300),
    }
)

fig, ax = plt.subplots(figsize=(8, 6))

sns.scatterplot(
    data=df,
    x="height",
    y="weight",
    hue="group",  # color by category — auto legend
    size="age",  # marker area scales with age value
    style="group",  # marker shape per group
    alpha=0.7,
    ax=ax,
)

ax.set_title("Height vs Weight")
ax.set_xlabel("Height (cm)")
ax.set_ylabel("Weight (kg)")
ax.grid(True, linestyle="--", alpha=0.4)
fig.tight_layout()
plt.show()
