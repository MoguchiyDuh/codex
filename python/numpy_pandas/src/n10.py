from shared import *

# E10
# Compute the Euclidean distance matrix for a set of points.
# Given points = np.random.random((5, 2)),
# produce a 5×5 matrix D where D[i,j] = ||points[i] - points[j]||.
# No loops. Hint: use broadcasting and np.sqrt.

points = rng.random((5, 2))

print(points)
print(points[:, np.newaxis, :])
diff = points[:, np.newaxis, :] - points[np.newaxis, :, :]

D = np.sqrt(np.sum(diff**2, axis=-1))
print(D)
