import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

theta = np.linspace(0, 4 * np.pi, 400)
r = theta**1.2

# 2. Polar plot
plt.figure(figsize=(8, 8))
ax = plt.subplot(projection="polar")
ax.plot(theta, r, color="red")

# 3. Customization
ax.set_title("Spiral: r = θ^1.2", pad=20, fontsize=14)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
