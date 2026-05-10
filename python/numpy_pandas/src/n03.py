from shared import *

# E3
# Reverse a 2D array along both axes in a single expression.
# Input:  [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[9,8,7],[6,5,4],[3,2,1]]

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
a = a[::-1, ::-1]

print(a)
