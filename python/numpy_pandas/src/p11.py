from shared import *

# P11
# Find the top-earning employee in each department.
# Output: department, employee name, salary.
# Hint: groupby + idxmax, or sort + groupby first.

# V1
print("--- .sort_values ---")
top_earners = df.sort_values("salary", ascending=False).drop_duplicates("dept")

print(top_earners[["dept", "name", "salary"]].sort_values("dept"))

# V2
print("--- .loc(groupby.idxmax()) ---")
top_earners = df.loc[df.groupby("dept")["salary"].idxmax(), ["dept", "name", "salary"]]
print(top_earners.sort_values("dept"))
