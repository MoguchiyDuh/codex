from shared import *

# P02
# Select all employees in the 'Eng' department with salary > 80000.
# Show only: name, age, salary.
print(df.loc[(df["dept"] == "Eng") & (df["salary"] > 80000), ("name", "age", "salary")])
