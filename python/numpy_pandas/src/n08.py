from shared import *

# ── BROADCASTING ──────────────────────────────────────────────────────────────
# E8
# Without any loop, produce a 10×10 multiplication table
# (entry [i,j] = (i+1)*(j+1)).
# Use broadcasting only — no np.outer, no np.meshgrid.

a = np.arange(1, 11).reshape(10, 1)
b = np.arange(1, 11).reshape(1, 10)
table = a * b
print(table)
