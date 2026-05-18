from shared import *

# ── CLEANING ──────────────────────────────────────────────────────────────────
# P04
# Fill missing salary values with the median salary of that employee's department.
# (Each dept gets its own median — not the global median.)
# Verify: no NaN left in 'salary'.
df["salary"] = df["salary"].fillna(df.groupby("dept")["salary"].transform("median"))
print("Should be no NaN: ", df["salary"].isna().sum())
