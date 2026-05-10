from shared import *

# E9
# Given a matrix X of shape (100, 4), normalize each column
# so it has zero mean and unit standard deviation.
# Do it in two lines: one for mean/std, one for the normalization.

matrix = rng.random((100, 4))
m_mean = matrix.mean(axis=0)
m_std = matrix.std(axis=0)
normalized = (matrix - m_mean) / m_std
print(f"mean: {m_mean}; std: {m_std}")
print(normalized)
