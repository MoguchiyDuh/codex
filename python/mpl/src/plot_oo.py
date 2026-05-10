import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# plt.subplots() returns (Figure, Axes) — or (Figure, ndarray of Axes) for grids
# figsize: same as before, set on the Figure
# fig, ax = plt.subplots(X, Y) - where X - num of dimentions, Y - num of elements in each, defaults to 1,1
fig, ax = plt.subplots(figsize=(9, 5))

# --- ax.plot() takes identical args to plt.plot() ---
ax.plot(
    x,
    y1,
    color="royalblue",
    linewidth=2,
    linestyle="-",
    marker="o",
    markersize=4,
    markerfacecolor="white",
    markeredgecolor="royalblue",
    alpha=0.9,
    label="sin(x)",
)

ax.plot(
    x,
    y2,
    color="crimson",
    linewidth=2,
    linestyle="--",
    marker="s",
    markersize=4,
    markerfacecolor="crimson",
    markeredgecolor="darkred",
    alpha=0.9,
    label="cos(x)",
)

# --- OO equivalents: set_* methods instead of plt.* functions ---
ax.set_xlabel("x (radians)", fontsize=12)
ax.set_ylabel("Amplitude", fontsize=12)
ax.set_title("sin(x) and cos(x) — OO style", fontsize=14)

# set_xlim / set_ylim instead of plt.xlim / plt.ylim
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.3, 1.3)

# grid: same signature as pyplot
ax.grid(True, which="major", axis="both", linestyle="--", alpha=0.4)

# legend: same signature as pyplot
ax.legend(loc="upper right", fontsize=11, framealpha=0.9)

# tight_layout is called on the Figure, not the Axes
# (plt.tight_layout() works too — it operates on the current figure)
fig.tight_layout()

plt.show()
