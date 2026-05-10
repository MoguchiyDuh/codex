from shared import *

# E14
# Given a (6, 4) matrix, select rows [0, 2, 5] and columns [1, 3]
# simultaneously using fancy indexing to get a (3, 2) submatrix.

matrix = rng.random((6, 4))
rows = [0, 2, 5]
cols = [1, 3]
submatrix = matrix[np.ix_(rows, cols)]

print(submatrix)
