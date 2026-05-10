import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 200)
y = np.sin(x)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle("ax.fill_between()", fontsize=14, fontweight="bold")

# --- Left: highlight region where y > 0.5 --------------------------------
# fill_between(x, y1, y2) fills the area between two curves
# where= restricts fill to a boolean condition on x
# alpha — fill transparency, always set this or it looks heavy
ax1.plot(x, y, color="steelblue", linewidth=2)
ax1.fill_between(
    x,
    y,
    0.5,  # fill between the curve and the threshold line y=0.5
    where=(y > 0.5),  # only fill where condition is True
    color="orange",
    alpha=0.4,
    label="y > 0.5",
)
ax1.axhline(0.5, color="orange", linestyle="--", linewidth=1)  # reference line
ax1.set_title("fill where y > 0.5")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.legend()
ax1.grid(True, linestyle="--", alpha=0.4)

# --- Middle: fill between two curves ------------------------------------
y2 = np.cos(x)
ax2.plot(x, y, color="steelblue", linewidth=2, label="sin(x)")
ax2.plot(x, y2, color="crimson", linewidth=2, label="cos(x)")
ax2.fill_between(x, y, y2, alpha=0.2, color="purple", label="difference")
ax2.set_title("fill between two curves")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.legend()
ax2.grid(True, linestyle="--", alpha=0.4)

# --- Right: confidence band (mean ± std) ---------------------------------
rng = np.random.default_rng(42)
samples = rng.normal(loc=y[:, None], scale=0.3, size=(200, 50))
mean = samples.mean(axis=1)
std = samples.std(axis=1)

ax3.plot(x, mean, color="steelblue", linewidth=2, label="mean")
ax3.fill_between(
    x,
    mean - std,  # lower bound
    mean + std,  # upper bound
    alpha=0.3,
    color="steelblue",
    label="± 1 std",
)
ax3.set_title("confidence band (mean ± std)")
ax3.set_xlabel("x")
ax3.set_ylabel("y")
ax3.legend()
ax3.grid(True, linestyle="--", alpha=0.4)

fig.tight_layout()
plt.show()
