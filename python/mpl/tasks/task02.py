import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# 1. Simulate 10,000 rolls of two dice
rolls1 = np.random.randint(1, 7, 10000)
rolls2 = np.random.randint(1, 7, 10000)
sums = rolls1 + rolls2

# 2. Plot histogram (discrete bins centered at integers 2-12)
bins = np.arange(1.5, 13.5, 1)  # bins: 1.5-2.5, 2.5-3.5, ..., 11.5-12.5
plt.hist(sums, bins=bins, density=True, alpha=0.7, edgecolor="black", label="Histogram")
# sns.histplot(
#     sums,
#     bins=bins,
#     stat="density",
#     alpha=0.7,
#     edgecolor="black",
#     label="Histogram",
#     kde=True,
# )

# 3. Overlay KDE
sns.kdeplot(sums, color="red", label="KDE")
# kde = gaussian_kde(sums)
# x_smooth = np.linspace(2, 12, 200)
# plt.plot(x_smooth, kde(x_smooth), "r-", linewidth=2, label="KDE")


# 4. Formatting
plt.title("Sum of Two Dice (10,000 Rolls)", fontsize=14)
plt.xlabel("Sum", fontsize=12)
plt.ylabel("Probability Density", fontsize=12)
plt.xticks(np.arange(2, 13, 1))
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

# Optional: Print theoretical probabilities for comparison
theoretical = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36,
}
print("Theoretical peak at 7:", f"{theoretical[7]:.3f}")
print("Simulated peak at 7:", f"{np.sum(sums == 7) / 10000:.3f}")
