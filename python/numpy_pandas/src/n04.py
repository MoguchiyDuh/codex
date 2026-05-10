from shared import *

# ── VIEWS VS COPIES ───────────────────────────────────────────────────────────
# E4
# Demonstrate that slices are views:
# create an array, take a slice, modify an element in the slice,
# and print both to show the original changed.
# Then make a copy and show that modifying it leaves the original intact.

a = np.array([1, 2, 3])
s1 = a[:1]
print("init array and slice: ", a, s1)
s1 += 1
print("slice + 1 (view): ", a, s1)

s2 = a[:1].copy()
s2 += 1
print("slice + 1 (copy)", a, s2)
