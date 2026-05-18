from shared import *

# P06
# Rename columns: 'name' → 'employee', 'dept' → 'department'.
# Reset the index to a clean 0-based integer range after dropping NaN rows.

df = df.dropna(subset=["score"])
df = df.rename(columns={"name": "employee", "dept": "department"})
df = df.reset_index(drop=True)
print(df.head())
print("Nan score: ", df["score"].isna().sum())
