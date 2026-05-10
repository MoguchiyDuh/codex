from shared import *

# ── UFUNCS & AGGREGATIONS ─────────────────────────────────────────────────────
# E5
# Without using any loop, compute the sum of squares of integers 1..100.
# Expected: 338350

a = np.arange(1, 101)
print(np.sum(a**2))
