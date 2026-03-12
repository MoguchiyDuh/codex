# Pandas — core patterns and ML-relevant usage
# See: ../notes/pandas.md

import numpy as np
import pandas as pd

# ── Creating DataFrames ───────────────────────────────────────────────────────

df = pd.DataFrame(
    {
        "name": ["alice", "bob", "carol", "dave", "eve"],
        "age": [25, 30, 22, 35, 28],
        "score": [88.5, 72.0, 95.0, 61.5, 83.0],
        "grade": ["B", "C", "A", "D", "B"],
        "dept": ["eng", "eng", "sci", "sci", "eng"],
    }
)

print(df.head())
print(df.dtypes)
print(df.describe())


# ── Selecting ────────────────────────────────────────────────────────────────

# Column
print(df["score"])  # Series
print(df[["name", "score"]])  # DataFrame

# .loc — label-based (inclusive)
print(df.loc[0:2, "name":"score"])

# .iloc — position-based (exclusive end)
print(df.iloc[0:3, 0:3])

# Boolean filter
high_scorers = df[df["score"] > 80]
eng_high = df[(df["dept"] == "eng") & (df["score"] > 75)]

# query — clean syntax for complex filters
result = df.query("age > 25 and score > 70")


# ── Adding / Modifying ────────────────────────────────────────────────────────

df["pass"] = df["score"] >= 70
df["score_norm"] = (df["score"] - df["score"].mean()) / df["score"].std()

# Safe assignment — always use .loc
df.loc[df["score"] < 65, "grade"] = "F"

# Apply
df["grade_upper"] = df["grade"].apply(str.upper)
df["label"] = df["score"].apply(lambda x: 1 if x >= 80 else 0)


# ── Missing Data ──────────────────────────────────────────────────────────────

dirty = pd.DataFrame(
    {
        "a": [1.0, np.nan, 3.0, np.nan],
        "b": [np.nan, 2.0, np.nan, 4.0],
        "c": [1.0, 2.0, 3.0, 4.0],
    }
)

print(dirty.isnull().sum())  # null count per column

clean1 = dirty.dropna()  # drop rows with any null
clean2 = dirty.fillna(dirty.mean())  # fill with column mean
clean3 = dirty.ffill()  # forward fill

print(clean2)


# ── Grouping & Aggregation ────────────────────────────────────────────────────

# Mean score per dept
print(df.groupby("dept")["score"].mean())

# Multiple aggregations
print(
    df.groupby("grade").agg(
        mean_score=("score", "mean"),
        count=("score", "count"),
        max_age=("age", "max"),
    )
)

# Transform — broadcast group stats back to original index
df["dept_mean_score"] = df.groupby("dept")["score"].transform("mean")
df["score_vs_dept"] = df["score"] - df["dept_mean_score"]


# ── Merging ───────────────────────────────────────────────────────────────────

info = pd.DataFrame(
    {
        "name": ["alice", "bob", "carol", "dave", "eve"],
        "city": ["NYC", "LA", "NYC", "SF", "LA"],
    }
)

merged = pd.merge(df, info, on="name", how="left")
print(merged[["name", "score", "city"]])


# ── String Operations ─────────────────────────────────────────────────────────

merged["name_upper"] = merged["name"].str.upper()
merged["city_ny"] = merged["city"].str.contains("NY")
merged["initials"] = merged["name"].str[0].str.upper()


# ── Sorting & Ranking ─────────────────────────────────────────────────────────

top = df.sort_values("score", ascending=False).head(3)
print(top[["name", "score"]])

df["rank"] = df["score"].rank(ascending=False, method="min").astype(int)


# ── Pivot ─────────────────────────────────────────────────────────────────────

pivot = df.pivot_table(
    values="score",
    index="dept",
    columns="grade",
    aggfunc="mean",
    fill_value=0,
)
print(pivot)


# ── Common ML Patterns ────────────────────────────────────────────────────────

# Separate features and target
X = df.drop(
    columns=[
        "name",
        "label",
        "grade",
        "grade_upper",
        "pass",
        "score_norm",
        "dept_mean_score",
        "score_vs_dept",
        "rank",
    ]
)
y = df["label"]

# One-hot encode categoricals
X_encoded = pd.get_dummies(X, columns=["dept"], drop_first=True)
print(X_encoded.dtypes)

# Downcast to save memory
for col in X_encoded.select_dtypes("float64").columns:
    X_encoded[col] = X_encoded[col].astype(np.float32)

# Convert to numpy for sklearn/torch
X_np = X_encoded.values.astype(np.float32)
y_np = y.values

# Shuffle
df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Train/val split
split = int(0.8 * len(df))
train_df = df.iloc[:split].copy()
val_df = df.iloc[split:].copy()

# Correlation with target
print(df[["age", "score", "label"]].corr()["label"].sort_values(ascending=False))


if __name__ == "__main__":
    print(f"\nDataFrame shape: {df.shape}")
    print(f"X_np shape: {X_np.shape}, dtype: {X_np.dtype}")
