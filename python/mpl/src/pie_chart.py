import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(42)

labels = ["Python", "JavaScript", "Rust", "Go", "C++"]
sizes = rng.integers(10, 40, len(labels)).astype(float)
sizes = sizes / sizes.sum() * 100  # normalise to sum to 100

# explode the largest slice outward
explode = [0.1 if s == sizes.max() else 0 for s in sizes]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))
fig.suptitle("ax.pie()", fontsize=14, fontweight="bold")

# --- Left: standard pie -------------------------------------------------
# autopct — format string for percentage labels inside slices
# startangle — rotate chart so first slice starts at this angle
# explode — offset per slice (0 = no offset)
# shadow — drop shadow behind chart
wedges, texts, autotexts = ax1.pie(
    sizes,
    labels=labels,
    explode=explode,
    autopct="%1.1f%%",  # show one decimal place inside each slice
    startangle=90,  # start at top (12 o'clock)
    shadow=True,
    colors=plt.cm.tab10.colors[: len(labels)],
)
# style the percentage text
for at in autotexts:
    at.set_fontsize(9)
    at.set_color("white")

ax1.set_title("Standard pie, explode on largest")

# --- Right: donut chart -------------------------------------------------
# donut = pie with a white circle drawn on top
ax2.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",
    startangle=90,
    colors=plt.cm.tab10.colors[: len(labels)],
    wedgeprops={"width": 0.5},  # width < 1 creates the donut hole
)
ax2.set_title("Donut chart (wedgeprops width=0.5)")

fig.tight_layout()
plt.show()
