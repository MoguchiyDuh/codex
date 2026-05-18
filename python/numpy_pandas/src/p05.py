from shared import *

# P05
# Add a column 'score_grade': 'A' if score >= 85, 'B' if >= 70, else 'C'.
# Use np.where or pd.cut — no loops.
# Then drop all rows where score is NaN.

df = df.dropna(subset=["score"])

conditions = [df["score"] >= 85, df["score"] >= 70]
choices = ["A", "B"]
df["score_grade"] = np.select(conditions, choices, default="C")
print("--- Head ---")
print(df.head())
print("NaN score: ", df["score"].isna().sum())
