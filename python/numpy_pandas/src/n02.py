from shared import *

# E2
# Given a 1D array of 12 random integers in [0, 50),
# reshape it into a 3×4 matrix, then extract a 2×2 subarray
# from the bottom-right corner.

a = rng.integers(0, 50, size=12)
a = a.reshape((3, 4))

print(a)

sub = a[-2:, -2:]
print(sub)
