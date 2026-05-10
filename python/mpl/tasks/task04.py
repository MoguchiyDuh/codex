import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Simulate times (minutes)
np.random.seed(42)
male_times = np.random.normal(240, 15, 200)  # mean 240 min (4h), std 15
female_times = np.random.normal(260, 18, 200)  # mean 260 min (4h20m), std 18

# 2. Build DataFrame
df = pd.DataFrame(
    {
        "Gender": ["Male"] * 200 + ["Female"] * 200,
        "FinishTime": np.concatenate([male_times, female_times]),
    }
)

# 3. Boxplot
sns.boxplot(
    x="Gender",
    y="FinishTime",
    data=df,
    palette={"Male": "#0080FF", "Female": "#FF8000"},
)

# 4. Customize
plt.title("Marathon Finish Times by Gender")
plt.xlabel("")
plt.ylabel("Finish Time (minutes)")
plt.grid(True, axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
