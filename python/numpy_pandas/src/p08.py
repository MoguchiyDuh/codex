from shared import *

# P08
# Using the .str accessor, add a column 'name_upper' (uppercase name)
# and a column 'dept_short' (first 3 characters of dept, lowercase).
df["name_upper"] = df["name"].str.upper()
df["dept_short"] = df["dept"].str[:3].str.lower()
print(df.head())
