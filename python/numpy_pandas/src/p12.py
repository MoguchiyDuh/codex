from shared import *

# P12
# Add a column 'salary_vs_dept_mean': each employee's salary minus
# their department's mean salary.
# Use groupby + transform — no merge required.

df["salary_vs_dept_mean"] = df["salary"] - df.groupby("dept")["salary"].transform(
    "mean"
)
print(df.head())
