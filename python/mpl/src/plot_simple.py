import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# figsize: (width, height) in inches
plt.figure(figsize=(9, 5))

# --- plot() args ---
# color:      any CSS color name, hex, or 'C0'-'C9' cycle colors
# linewidth:  stroke thickness in points
# linestyle:  '-', '--', '-.', ':'
# marker:     'o', 's', '^', 'D', 'x', '+', etc.
# markersize: diameter in points
# markerfacecolor / markeredgecolor: fill and border of the marker
# alpha:      0.0 (transparent) to 1.0 (opaque)
# label:      string shown in the legend — does nothing without plt.legend()
plt.plot(
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

plt.plot(
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

# --- labels and title ---
plt.xlabel("x (radians)", fontsize=12)
plt.ylabel("Amplitude", fontsize=12)
plt.title("sin(x) and cos(x) — pyplot style", fontsize=14)

# --- axis limits ---
plt.xlim(0, 2 * np.pi)
plt.ylim(-1.3, 1.3)

# --- grid ---
# which='both': major and minor ticks | axis='both'/'x'/'y'
plt.grid(True, which="major", axis="both", linestyle="--", alpha=0.4)

# --- legend ---
# loc: 'best', 'upper right', 'lower left', etc.
# framealpha: legend box transparency
plt.legend(loc="upper right", fontsize=11, framealpha=0.9)

# --- tight_layout: pads everything so labels don't get clipped ---
plt.tight_layout()

plt.show()
