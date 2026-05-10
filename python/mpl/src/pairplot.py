import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

rng = np.random.default_rng(42)

x1 = rng.normal(0, 1, 150)
df = pd.DataFrame(
    {
        "X1": x1,
        "X2": x1 + rng.normal(0, 0.5, 150),  # strongly correlated with X1
        "X3": rng.normal(0, 1, 150),  # independent
        "X4": x1 * 0.5 + rng.normal(0, 1, 150),  # weakly correlated with X1
        "group": rng.choice(["A", "B", "C"], 150),
    }
)

# pairplot returns a PairGrid — not an Axes, not a Figure
# it creates its own figure with nvar×nvar panels automatically
g = sns.pairplot(
    data=df,
    hue="group",  # color all panels by group — auto legend
    vars=["X1", "X2", "X3", "X4"],  # columns to plot (default: all numeric)
    kind="scatter",  # off-diagonal panels: "scatter", "kde", "hist", "reg"
    diag_kind="kde",  # diagonal panels: "kde", "hist", or "auto"
    plot_kws={"alpha": 0.5, "s": 20},  # kwargs for off-diagonal plots
    diag_kws={"fill": True, "alpha": 0.4},  # kwargs for diagonal plots
)

g.figure.suptitle("Pairplot — pairwise relationships", y=1.02, fontsize=13)
plt.show()
