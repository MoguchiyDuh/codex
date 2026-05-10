from shared import *

# E12
# Given a 6×6 matrix of random ints in [0, 10):
# set all values on the main diagonal to 0,
# then set all values above the diagonal to -1,
# using only boolean/fancy indexing (no loops).

matrix = rng.integers(0, 10, (6, 6))

row_indices, col_indices = np.indices(matrix.shape)

matrix[row_indices == col_indices] = 0

matrix[col_indices > row_indices] = -1
print(matrix)
