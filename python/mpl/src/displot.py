import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

rng = np.random.default_rng(42)

df = pd.DataFrame(
    {
        "Score": np.concatenate(
            [
                rng.normal(65, 12, 200),  # Physics
                rng.normal(72, 9, 200),  # Math
                rng.normal(60, 15, 200),  # History
            ]
        ),
        "Group": ["Physics"] * 200 + ["Math"] * 200 + ["History"] * 200,
        "Year": (["Year 1"] * 100 + ["Year 2"] * 100) * 3,
    }
)

# col= creates one panel per Group value — this is the only reason to use displot
# over histplot. displot manages the figure itself; no plt.subplots() needed.
g = sns.displot(
    data=df,
    x="Score",
    col="Group",  # one panel per group
    hue="Year",  # split within each panel by Year
    kind="hist",  # "hist", "kde", or "ecdf"
    kde=True,
    stat="density",
    alpha=0.5,
    height=4,  # height of each panel in inches
    aspect=1,  # width = height * aspect
)

# FacetGrid returned — customise via the grid object, not ax directly
g.set_axis_labels("Score", "Density")
g.set_titles(col_template="{col_name}")  # panel title from col value
g.tight_layout()

# to access individual axes:
# g.axes[0, 0]  — row 0, col 0
# g.ax          — only works when there is a single panel

plt.show()
