from shared import *

# ── AGGREGATION ───────────────────────────────────────────────────────────────
# P10
# For each department, compute:
#   - headcount
#   - mean salary (rounded to 2dp)
#   - max score
#   - % of employees with score_grade == 'A'  (requires P05)
# Return a clean summary DataFrame.

# p05.py
df = df.dropna(subset=["score"])
conditions = [df["score"] >= 85, df["score"] >= 70]
choices = ["A", "B"]
df["score_grade"] = np.select(conditions, choices, default="C")


df_dept = (
    df.groupby("dept")
    .agg(
        headcount=("name", "count"),
        mean_salary=("salary", lambda x: x.mean().round(2)),
        max_score=("score", "max"),
        pct_grade_A=("score_grade", lambda x: (x == "A").mean() * 100),
    )
    .reset_index()
)
print(df_dept)
