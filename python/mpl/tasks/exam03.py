import matplotlib.pyplot as plt
import numpy as np

# --- Data ----------------------------------------------------------------
x = np.linspace(0, 4 * np.pi, 200)
y1 = np.sin(x)
y2 = np.cos(x)

# --- Find intersections -------------------------------------------------
# sin(x) = cos(x) where their difference changes sign
# np.diff(np.sign(y1 - y2)) is non-zero at sign changes
# np.where returns the indices just before each crossing
idx = np.where(np.diff(np.sign(y1 - y2)))[0]

# interpolate the exact x crossing between idx and idx+1
# linear interpolation: x_cross = x[i] - diff[i] * (x[i+1]-x[i]) / (diff[i+1]-diff[i])
diff = y1 - y2
x_cross = x[idx] - diff[idx] * (x[idx + 1] - x[idx]) / (diff[idx + 1] - diff[idx])
y_cross = np.sin(x_cross)

# --- Plot ----------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(x, y1, label="sin(x)", linewidth=2, color="steelblue")
ax.plot(x, y2, label="cos(x)", linewidth=2, color="crimson")

# red markers at intersection points
ax.scatter(
    x_cross,
    y_cross,
    color="red",
    zorder=5,
    s=80,
    label="intersections",
    edgecolors="darkred",
    linewidths=0.5,
)

ax.set_title("sin(x) and cos(x) — intersection points highlighted", fontsize=13)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.4)
fig.tight_layout()
plt.show()
