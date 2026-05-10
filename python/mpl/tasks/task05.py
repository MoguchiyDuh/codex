import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Generate x
np.random.seed(42)
x = np.random.normal(0, 1, 200)  # mean 0, std 1

# 2. Generate y with correlation
noise = np.random.normal(0, 2, 200)  # std=2 gives noticeable spread
y = 3 * x + noise

# 3. DataFrame
df = pd.DataFrame({"x": x, "y": y})

# 4. Scatter plot
sns.scatterplot(data=df, x="x", y="y")

# 5. Labels and title
plt.xlabel("X (standard normal)")
plt.ylabel("Y = 3X + noise")
plt.title("Positive Correlation: y vs x")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
