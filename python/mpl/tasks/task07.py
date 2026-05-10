import matplotlib.pyplot as plt
import numpy as np

# Parameters
years = np.arange(0, 21)  # 0 to 20 inclusive
initial = 1000  # dollars
rates = [0.03, 0.05, 0.07]  # 3%, 5%, 7%
labels = ["3% rate", "5% rate", "7% rate"]

plt.figure(figsize=(10, 6))

for rate, label in zip(rates, labels):
    growth = initial * (1 + rate) ** years
    plt.plot(
        years, growth, marker="o", linestyle="-", linewidth=2, markersize=4, label=label
    )

# Formatting
plt.title("Investment Growth Over 20 Years", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Value ($)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()
