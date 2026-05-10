from shared import *

# ── MERGING ───────────────────────────────────────────────────────────────────
# P13
# Create a second DataFrame 'dept_budget':
#   dept_budget = pd.DataFrame({
#       'department': ['Eng', 'Sales', 'HR', 'Finance'],
#       'budget_m':   [5.2, 3.1, 1.8, 4.0],
#   })
# Merge it into the main df (after P06 rename) on 'department'.
# Use a left join. Verify no rows were lost.
