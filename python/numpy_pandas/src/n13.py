from shared import *

# ── FANCY INDEXING ────────────────────────────────────────────────────────────
# E13
# Given x = np.array([10, 20, 30, 40, 50]):
# use fancy indexing to produce [50, 10, 30] (indices [4, 0, 2]).
# Then assign 99 to those same three positions.
# Show the result.

x = np.array([10, 20, 30, 40, 50])
indices = [4, 0, 2]

print(x[indices])

x[indices] = 99
print(x)
