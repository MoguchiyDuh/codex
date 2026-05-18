from shared import *

# P09
# Sort the DataFrame by department ascending, then salary descending.
# Print the top 10 rows.
df_sorted = df.sort_values(by=["dept", "salary"], ascending=[True, False])
print(df_sorted.head(10))
