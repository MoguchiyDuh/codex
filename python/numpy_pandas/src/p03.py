from shared import *

# P03
# Using .loc, select rows 10 through 20 (by position, not label),
# and only the 'name', 'dept', 'salary' columns.
# Then do the same with .iloc.
# Are the results identical? Why or why not?
print("--- Label-based ---")
print(df.loc[10:21, ["name", "dept", "salary"]])
print("--- Position-based ---")
print(df.iloc[10:21, [0, 1, 3]])

df_label_pos_diff = pd.DataFrame(
    {
        "name": ["Alice", "Bob", "Charlie"],
        "dept": ["Eng", "Eng", "HR"],
        "salary": [90000, 70000, 60000],
    },
    index=[10, 20, 30],
)
print("--- Diff Example (indices [10, 20, 30]) ---")
print("--- Label-based (0 items) ---")
print(df_label_pos_diff.loc[:2])
print("--- Position-based (2 items) ---")
print(df_label_pos_diff.iloc[:2])
