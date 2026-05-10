import matplotlib.pyplot as plt
import numpy as np

# 1. Generate base temps + noise
base_temps = np.array([15, 16, 14, 17, 19, 21, 20])  # °C
noise = np.random.normal(0, 1.5, 7)  # random variation
temps = base_temps + noise

# 2. Plot
days = np.arange(1, 8)
plt.plot(
    days,
    temps,
    "o-",
    markerfacecolor="blue",
    markeredgecolor="darkblue",
    linewidth=2,
    markersize=8,
    color="skyblue",
)

# 3. Formatting
plt.title("Daily Temperatures - 1 Week Forecast", fontsize=14)
plt.xlabel("Day", fontsize=12)
plt.ylabel("Temperature (°C)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
