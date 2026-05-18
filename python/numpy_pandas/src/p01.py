from shared import *

# ── BASICS & INSPECTION ───────────────────────────────────────────────────────
# P01
# Print: shape, column dtypes, count of NaN per column, and descriptive stats.

print("--- SHAPE ---")
print(df.shape)
print("--- DTYPES ---")
print(df.dtypes)
print("--- NaN COUNT ---")
print(df.isna().sum(axis=0))
print("--- DESCRIBE ---")
print(df.describe(include="all"))
