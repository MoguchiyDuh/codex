from shared import *

# ── BASICS ────────────────────────────────────────────────────────────────────
# E1
# Create a 5×5 identity matrix without using np.eye.
# Hint: start with zeros, then fill the diagonal.

I = np.zeros((5, 5))
np.fill_diagonal(I, 1)

print(I)
