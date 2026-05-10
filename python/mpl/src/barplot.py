import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

rng = np.random.default_rng(42)

df = pd.DataFrame(
    {
        "subject": rng.choice(["Math", "Physics", "History"], 300),
        "grade": rng.choice(["A", "B", "C"], 300),
        "score": rng.normal(70, 15, 300),
    }
)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle("sns.barplot()", fontsize=14, fontweight="bold")

# --- Left: basic barplot ------------------------------------------------
# barplot auto-aggregates — computes mean of score per subject by default
# errorbar="ci" — bootstrapped 95% CI shown as caps on each bar
# hue= — grouped bars per subject, one color per grade
sns.barplot(
    data=df,
    x="subject",
    y="score",
    hue="grade",
    palette="Set2",
    errorbar="ci",  # "ci", "sd", "se", "pi", or None
    capsize=0.1,  # width of the error bar caps
    ax=ax1,
)
ax1.set_title("Mean score by subject and grade")
ax1.set_xlabel("Subject")
ax1.set_ylabel("Mean score")
ax1.grid(True, axis="y", linestyle="--", alpha=0.4)

# --- Right: horizontal barplot with estimator= --------------------------
# estimator= — any aggregation function, default is np.mean
# orient="h" — horizontal bars, swap x= and y= roles
sns.barplot(
    data=df,
    x="score",
    y="subject",
    hue="grade",
    palette="Set2",
    estimator=np.median,  # use median instead of mean
    errorbar="sd",  # standard deviation instead of CI
    orient="h",
    ax=ax2,
)
ax2.set_title("Median score, errorbar='sd', orient='h'")
ax2.set_xlabel("Median score")
ax2.set_ylabel("")
ax2.grid(True, axis="x", linestyle="--", alpha=0.4)

fig.tight_layout()
plt.show()
