---
tags: [ml, pandas, foundations]
status: complete
---

# Pandas

> DataFrame library built on NumPy. Primary tool for tabular data — loading, cleaning, transforming, and exploring datasets before feeding them to a model.

**Code:** `../src/pandas_basics.py`

---

## Core Structures

**Series** — 1D labeled array. Like a column.
**DataFrame** — 2D table of Series. Like a spreadsheet or SQL table.
**Index** — labels for rows (or columns). Can be integers, strings, datetimes.

```python
import pandas as pd
import numpy as np
```

---

## Creating DataFrames

```python
# From dict — keys become column names
df = pd.DataFrame({
    "name": ["alice", "bob", "carol"],
    "age":  [25, 30, 22],
    "score": [88.5, 72.0, 95.0],
})

# From list of dicts
df = pd.DataFrame([
    {"name": "alice", "age": 25},
    {"name": "bob",   "age": 30},
])

# From numpy array
df = pd.DataFrame(np.random.randn(5, 3), columns=["a", "b", "c"])

# From CSV / other sources
df = pd.read_csv("data.csv")
df = pd.read_csv("data.csv", index_col=0, parse_dates=["date"])
df = pd.read_json("data.json")
df = pd.read_parquet("data.parquet")   # preferred for large data

# Series
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
```

---

## Inspection

```python
df.shape                         # (rows, cols)
df.dtypes                        # dtype per column
df.info()                        # dtypes + memory + null counts
df.describe()                    # stats: count, mean, std, min, max, quartiles
df.head(5)                       # first 5 rows
df.tail(5)                       # last 5 rows
df.sample(5)                     # random 5
df.columns.tolist()
df.index
df.values                        # underlying numpy array
df.nunique()                     # unique count per column
df.value_counts()                # frequency of each value (Series)
df["col"].value_counts()
```

---

## Selecting Data

```python
# Column(s)
df["age"]                        # Series
df[["name", "age"]]             # DataFrame

# Rows by label — .loc (inclusive on both ends)
df.loc[0]                        # row with index label 0
df.loc[0:2]                      # rows 0, 1, 2
df.loc[0:2, "name":"age"]       # rows and columns by label

# Rows by position — .iloc (exclusive end, like Python slicing)
df.iloc[0]                       # first row
df.iloc[0:3]                     # rows 0, 1, 2
df.iloc[0:3, 0:2]               # rows and cols by position
df.iloc[-1]                      # last row

# Boolean filtering
df[df["age"] > 25]
df[(df["age"] > 25) & (df["score"] > 80)]   # use & not 'and'
df[df["name"].isin(["alice", "bob"])]
df[df["age"].between(20, 30)]
df.query("age > 25 and score > 80")          # string query — convenient
```

---

## Adding & Modifying

```python
df["grade"] = df["score"].apply(lambda x: "A" if x >= 90 else "B")
df["age_norm"] = (df["age"] - df["age"].mean()) / df["age"].std()

# Rename columns
df.rename(columns={"name": "full_name"}, inplace=True)

# Drop
df.drop(columns=["grade"])                   # drop column — returns copy
df.drop(index=[0, 2])                        # drop rows by label
df.drop_duplicates()
df.drop_duplicates(subset=["name"])

# Set/reset index
df.set_index("name", inplace=True)
df.reset_index(inplace=True)

# Type casting
df["age"] = df["age"].astype(np.int32)
df["date"] = pd.to_datetime(df["date"])
```

---

## Missing Data

```python
df.isnull()                      # bool DataFrame
df.isnull().sum()                # null count per column
df.isnull().sum() / len(df)     # null fraction per column
df.notnull()

# Drop
df.dropna()                      # drop rows with ANY null
df.dropna(subset=["age"])        # drop rows where 'age' is null
df.dropna(axis=1)                # drop columns with ANY null
df.dropna(thresh=3)              # keep rows with at least 3 non-null

# Fill
df.fillna(0)
df.fillna(df.mean())            # fill with column mean
df["age"].fillna(df["age"].median(), inplace=True)
df.ffill()                       # forward fill
df.bfill()                       # backward fill
```

---

## Sorting & Ranking

```python
df.sort_values("score", ascending=False)
df.sort_values(["age", "score"], ascending=[True, False])
df.sort_index()

df["score"].rank()               # rank within series
df["score"].rank(pct=True)      # percentile rank
```

---

## Apply & Map

```python
# Apply function to each element
df["name"].str.upper()           # string methods via .str accessor
df["score"].apply(lambda x: round(x))

# Apply function to each row or column
df.apply(lambda col: col.max() - col.min(), axis=0)   # per column
df.apply(lambda row: row["age"] + row["score"], axis=1)  # per row

# Map (Series only) — element-wise substitution
df["grade"].map({"A": 4.0, "B": 3.0})

# applymap (element-wise on entire DataFrame) — deprecated in 2.x, use map
df.map(lambda x: round(x, 2) if isinstance(x, float) else x)
```

---

## Grouping & Aggregation

```python
g = df.groupby("grade")
g["score"].mean()                # mean score per grade
g["score"].agg(["mean", "std", "count"])
g.agg({"score": "mean", "age": "max"})

# Multiple groups
df.groupby(["grade", "dept"])["score"].mean()

# Transform — keeps original index, broadcasts result back
df["score_norm"] = df.groupby("grade")["score"].transform(
    lambda x: (x - x.mean()) / x.std()
)

# Filter — keep groups satisfying condition
df.groupby("grade").filter(lambda g: len(g) > 2)
```

---

## Merging & Joining

```python
# Merge (like SQL JOIN)
pd.merge(df1, df2, on="id")                   # inner join
pd.merge(df1, df2, on="id", how="left")       # left join
pd.merge(df1, df2, on="id", how="outer")      # outer join
pd.merge(df1, df2, left_on="user_id", right_on="id")

# Concat — stack DataFrames
pd.concat([df1, df2], axis=0, ignore_index=True)  # stack rows
pd.concat([df1, df2], axis=1)                      # stack columns

# Join — merge on index
df1.join(df2, how="left")
```

---

## Pivot & Reshape

```python
# Pivot table
df.pivot_table(values="score", index="grade", columns="dept", aggfunc="mean")

# Melt — wide to long
pd.melt(df, id_vars=["name"], value_vars=["math", "science"],
        var_name="subject", value_name="score")

# Stack / unstack
df.stack()                       # columns → rows (wide to long)
df.unstack()                     # rows → columns (long to wide)
```

---

## String Operations

```python
df["name"].str.lower()
df["name"].str.upper()
df["name"].str.strip()
df["name"].str.contains("ali")          # bool Series
df["name"].str.startswith("a")
df["name"].str.replace("old", "new")
df["name"].str.split(",", expand=True)  # split into columns
df["name"].str.len()
df["name"].str.extract(r"(\w+)")        # regex capture group
```

---

## DateTime

```python
df["date"] = pd.to_datetime(df["date"])

df["date"].dt.year
df["date"].dt.month
df["date"].dt.day
df["date"].dt.dayofweek          # 0=Monday
df["date"].dt.hour
df["date"].dt.floor("H")         # floor to hour

# Time-based filtering
df[df["date"] > "2024-01-01"]
df.set_index("date").loc["2024-01"]   # all rows in Jan 2024

# Resample (requires datetime index)
df.set_index("date").resample("D")["value"].mean()   # daily mean
df.set_index("date").resample("W")["value"].sum()    # weekly sum
```

---

## I/O

```python
df.to_csv("out.csv", index=False)
df.to_parquet("out.parquet")         # fast, compressed, preserves dtypes
df.to_json("out.json", orient="records")
df.to_excel("out.xlsx", index=False)

pd.read_csv("data.csv", usecols=["a", "b"], dtype={"a": np.float32})
pd.read_csv("data.csv", chunksize=10000)  # iterate large files
```

---

## Performance

```python
# Check memory
df.memory_usage(deep=True).sum()

# Downcast numerics
df["age"] = pd.to_numeric(df["age"], downcast="integer")
df["score"] = pd.to_numeric(df["score"], downcast="float")

# Use category for low-cardinality strings (massive memory saving)
df["grade"] = df["grade"].astype("category")

# Avoid chained indexing — always use .loc/.iloc for assignment
# BAD — may or may not modify original (SettingWithCopyWarning)
df[df["age"] > 25]["score"] = 0
# GOOD
df.loc[df["age"] > 25, "score"] = 0

# eval / query for large DataFrames
df.eval("score_sq = score ** 2", inplace=True)
df.query("age > 25 and score > 80")
```

---

## Common ML Patterns

```python
# Drop target, keep features
X = df.drop(columns=["label"])
y = df["label"]

# Encode categoricals
dummies = pd.get_dummies(df["grade"], prefix="grade", drop_first=True)
df = pd.concat([df, dummies], axis=1).drop(columns=["grade"])

# Convert to numpy for sklearn/torch
X_np = X.values.astype(np.float32)

# Shuffle
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Train/val split
split = int(0.8 * len(df))
train_df = df.iloc[:split]
val_df   = df.iloc[split:]

# Correlation matrix
df.corr()
df.corr()["label"].sort_values(ascending=False)  # feature correlation with target
```
