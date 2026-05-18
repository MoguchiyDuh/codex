from shared import *

# ── TRANSFORMATION ────────────────────────────────────────────────────────────
# P07
# Add a column 'tenure_years': number of full years between 'joined' and today.
# Use the .dt accessor and pd.Timestamp.today().
df["tenure_years"] = ((pd.Timestamp.now() - df["joined"]).dt.days // 365.2425).astype(
    int
)
print(df.head())
