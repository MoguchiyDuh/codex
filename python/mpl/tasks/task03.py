import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# 1. Generate data
x = np.linspace(0, 10, 100)
noise = np.random.normal(0, 1, 100)  # mean 0, std 1
y = 2 * x + noise

# 2. Plot with regression
sns.regplot(x=x, y=y, ci=None, scatter_kws={"alpha": 0.6}, line_kws={"color": "red"})

# 3. Labels and title
plt.xlabel("X (0 to 10)")
plt.ylabel("y = 2x + noise")
plt.title("Noisy Linear Relationship with Regression Line")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
