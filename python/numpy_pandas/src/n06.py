from shared import *

# E6
# Given a 4×5 matrix of random floats:
# (a) find the max value in each row
# (b) find the index of the min value in each column
# (c) compute the column-wise mean, then subtract it from the matrix (in-place)

matrix = rng.random((4, 5))
print("init array")
print(matrix)
print("max per row")
print(matrix.max(axis=1))
print("argmin per row")
print(matrix.argmin(axis=0))
print("mean per col and sub")
mean_per_col = matrix.mean(axis=0)
matrix -= mean_per_col
print("mean per col: ", mean_per_col)
print(matrix)
