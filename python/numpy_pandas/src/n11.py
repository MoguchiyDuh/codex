from shared import *

# ── BOOLEAN MASKS ─────────────────────────────────────────────────────────────
# E11
# Given x = np.random.normal(0, 1, 1000):
# (a) count how many values fall outside [-2, 2]
# (b) replace all values outside [-2, 2] with the boundary value
#     (clip to [-2, 2]) — use boolean indexing, not np.clip

x = rng.normal(0, 1, 1000)


def count_outside():
    outside_mask = (x < -2) | (x > 2)
    count = np.sum(outside_mask)
    return count


print(count_outside())

x[x < -2] = -2
x[x > 2] = 2
print(count_outside())
