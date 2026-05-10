from shared import *

# E15 (hard)
# Use np.add.at to implement a scatter-add:
# given values = np.array([1.0, 2.0, 3.0, 4.0])
# and indices  = np.array([0, 1, 1, 0]),
# produce an output array of length 3 where:
#   out[0] = values[0] + values[3] = 5.0
#   out[1] = values[1] + values[2] = 5.0
#   out[2] = 0.0
# Show why x[indices] += values would give the wrong answer. there are solutions, read the files first

values = np.array([1.0, 2.0, 3.0, 4.0])
indices = np.array([0, 1, 1, 0])

out = np.zeros(3)

np.add.at(out, indices, values)

print("currect unbuffered indexing: ", out)

wrong = np.zeros(3)
wrong[indices] += values

print("wrong buffered indexing: ", wrong)
