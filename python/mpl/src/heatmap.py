import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

rng = np.random.default_rng(42)

df = pd.DataFrame(
    {
        "height": rng.normal(170, 10, 300),
        "weight": rng.normal(70, 15, 300),
        "age": rng.normal(35, 10, 300),
        "income": rng.normal(50, 20, 300),
        "score": rng.normal(75, 12, 300),
    }
)

# df.corr() produces a square DataFrame of pairwise Pearson correlations
corr = df.corr()

# mask upper triangle — correlation matrices are symmetric, no need to show both halves
# np.ones_like produces a boolean array of same shape, np.triu keeps upper triangle as True
mask = np.triu(np.ones_like(corr, dtype=bool))

fig, ax = plt.subplots(figsize=(7, 6))

sns.heatmap(
    corr,
    mask=mask,  # cells where True are hidden
    annot=True,  # print correlation value in each cell
    fmt=".2f",  # 2 decimal places
    cmap="coolwarm",  # diverging — red=positive, blue=negative
    vmin=-1,
    vmax=1,  # pin colorbar to correlation range
    linewidths=0.5,  # separator lines between cells
    square=True,  # force square cells
    ax=ax,
)

ax.set_title("Correlation matrix")
fig.tight_layout()
plt.show()
