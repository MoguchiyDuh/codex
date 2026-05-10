from shared import *

# E7
# Use np.add.at to build a histogram manually:
# given x = np.array([0.1, 0.5, 0.5, 0.9, 0.9, 0.9])
# and bins = np.array([0.0, 0.33, 0.66, 1.0]),
# produce counts = [1, 2, 3] without np.histogram.

x = np.array([0.1, 0.5, 0.5, 0.9, 0.9, 0.9])
bins = np.array([0.0, 0.33, 0.66, 1.0])
print("x: ", x)
print("bins: ", bins)

print("indeces:")
indices = np.searchsorted(bins, x, side="right") - 1
print(indices)

counts = np.zeros(len(bins) - 1, dtype=int)
np.add.at(counts, indices, 1)
print("counts: ", counts)
