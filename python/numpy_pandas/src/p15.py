from shared import *

# ── MATPLOTLIB INTEGRATION ────────────────────────────────────────────────────
# P15
# Create a 2×2 figure with:
#   [0,0] histogram of salary (20 bins)
#   [0,1] scatter of age vs score, colored by department (4 colors, legend)
#   [1,0] horizontal bar chart of mean salary per department, sorted descending
#   [1,1] line chart of monthly headcount (employees joined per month)
# Use the OO Matplotlib interface (fig, axes = plt.subplots(2, 2)).
# Label all axes. Add a figure title.
# Save to resources/pictures/pandas_overview.png if that path exists,
# otherwise just plt.show().
