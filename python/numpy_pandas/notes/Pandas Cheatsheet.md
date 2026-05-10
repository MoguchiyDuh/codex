---
tags: [python, pandas, data-science]
status: complete
---

# Pandas Cheatsheet

> Core reference for Series, DataFrame, selection, cleaning, transformation, aggregation, merging, time series, and Matplotlib integration.

## Core structures

```python
import pandas as pd
import numpy as np
```

**Series** — 1D labeled array. Think of it as a column with an index.

```python
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s['b']        # 2 — label-based access
s[1]          # 2 — positional access (deprecated for non-integer indexes; prefer .iloc)
s.values      # underlying NumPy array
s.index       # Index(['a', 'b', 'c'])
s.dtype       # dtype('int64')
```

**DataFrame** — 2D labeled table. Each column is a Series sharing a common index.

```python
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Carol'],
    'age':  [25, 30, 22],
    'score': [88.5, 92.0, 79.3],
}, index=['r0', 'r1', 'r2'])

df.shape      # (3, 3)
df.columns    # Index(['name', 'age', 'score'])
df.index      # Index(['r0', 'r1', 'r2'])
df.dtypes     # per-column dtypes
df.info()     # summary: dtype, non-null count, memory
df.describe() # stats for numeric columns
df.head(3)
df.tail(3)
```

## I/O

```python
df = pd.read_csv('file.csv')
df = pd.read_csv('file.csv', index_col=0, parse_dates=['date'])
df = pd.read_excel('file.xlsx', sheet_name='Sheet1')
df = pd.read_json('file.json')
df = pd.read_parquet('file.parquet')
df = pd.read_sql('SELECT * FROM t', con=engine)

df.to_csv('out.csv', index=False)
df.to_parquet('out.parquet')
df.to_excel('out.xlsx', index=False)
```

## Selection

### Columns

```python
df['age']           # Series
df[['age', 'name']] # DataFrame (list of cols)
```

### `.loc` — label-based

```python
df.loc['r0']                    # row by label → Series
df.loc['r0', 'age']             # single value
df.loc['r0':'r1', 'age':'score'] # slice (inclusive on both ends)
df.loc[['r0', 'r2'], 'name']    # list of row labels
df.loc[df['age'] > 24]          # boolean mask
df.loc[df['age'] > 24, 'name']  # mask + column
```

### `.iloc` — integer position-based

```python
df.iloc[0]          # first row
df.iloc[0, 1]       # row 0, col 1
df.iloc[:2, 1:]     # first 2 rows, cols from 1 onward
df.iloc[[0, 2], :]  # rows 0 and 2
```

### `.query`

```python
df.query('age > 24 and score > 80')
df.query('name in ["Alice", "Carol"]')
```

### Boolean indexing

```python
df[df['age'] > 24]
df[(df['age'] > 24) & (df['score'] > 85)]  # & not and
df[df['name'].isin(['Alice', 'Bob'])]
df[~df['name'].isin(['Bob'])]
```

## Adding and modifying columns

```python
df['grade'] = df['score'] >= 85          # boolean column
df['score_norm'] = df['score'] / 100
df['label'] = df['name'].str.upper()

# conditional assignment
df['result'] = np.where(df['score'] >= 85, 'pass', 'fail')

# drop columns
df.drop(columns=['grade'], inplace=True)
# or: df = df.drop(columns=['grade'])
```

## Data cleaning

### Missing values

```python
df.isna()               # boolean DataFrame
df.isna().sum()         # count NaN per column
df.dropna()             # drop rows with any NaN
df.dropna(subset=['age'])   # only care about specific cols
df.dropna(thresh=2)         # keep rows with at least 2 non-NaN
df.fillna(0)            # fill all NaN with 0
df.fillna({'age': 0, 'score': df['score'].mean()})  # per-column fill
df.fillna(method='ffill')   # forward fill (propagate last valid)
df.fillna(method='bfill')   # backward fill
```

### Duplicates

```python
df.duplicated()              # boolean Series
df.duplicated(subset=['name'])
df.drop_duplicates()
df.drop_duplicates(subset=['name'], keep='last')
```

### Dtypes and casting

```python
df['age'].astype('float32')
df['date'] = pd.to_datetime(df['date'])
df['cat'] = df['cat'].astype('category')   # memory-efficient
pd.to_numeric(df['col'], errors='coerce')  # invalid → NaN
```

### Renaming

```python
df.rename(columns={'age': 'years', 'score': 'points'}, inplace=True)
df.columns = ['a', 'b', 'c']   # replace all at once
df.index.name = 'id'
```

## Transformation

### `.apply`

```python
df['score'].apply(lambda x: x * 2)         # element-wise on Series
df.apply(lambda col: col.max() - col.min()) # per column (axis=0)
df.apply(lambda row: row['age'] + 1, axis=1) # per row (axis=1)
```

### `.map` (Series only — element-wise)

```python
df['name'].map({'Alice': 1, 'Bob': 2})   # dict lookup
df['score'].map(lambda x: round(x))
```

### String accessor `.str`

```python
df['name'].str.upper()
df['name'].str.contains('li')
df['name'].str.replace('o', '0')
df['name'].str.split(' ', expand=True)   # → DataFrame of parts
df['name'].str.len()
df['name'].str.strip()
```

### Sorting

```python
df.sort_values('score', ascending=False)
df.sort_values(['age', 'score'], ascending=[True, False])
df.sort_index()
```

### Binning

```python
pd.cut(df['score'], bins=[0, 60, 80, 100], labels=['C', 'B', 'A'])
pd.qcut(df['score'], q=4)   # quartile-based bins
```

## Aggregation and groupby

```python
df.groupby('result')['score'].mean()
df.groupby('result').agg({'score': 'mean', 'age': 'max'})
df.groupby('result').agg(
    avg_score=('score', 'mean'),
    max_age=('age', 'max'),
)

# multiple agg functions on one column
df.groupby('result')['score'].agg(['mean', 'std', 'count'])

# transform — returns same-length result (useful for normalizing within groups)
df['score_z'] = df.groupby('result')['score'].transform(
    lambda x: (x - x.mean()) / x.std()
)
```

Common aggregation functions: `mean`, `sum`, `count`, `min`, `max`, `std`, `var`, `median`, `first`, `last`, `nunique`.

## Pivot tables and reshaping

```python
# pivot_table — like Excel pivot
df.pivot_table(values='score', index='result', columns='name', aggfunc='mean')

# pivot — no aggregation (values must be unique per index/column combo)
df.pivot(index='date', columns='name', values='score')

# melt — wide → long
pd.melt(df, id_vars=['name'], value_vars=['score', 'age'],
        var_name='metric', value_name='value')

# stack / unstack — move index levels to/from columns
df.stack()    # columns → innermost index level
df.unstack()  # innermost index level → columns
```

## Combining datasets

### `pd.concat`

```python
pd.concat([df1, df2])               # vertical stack (axis=0)
pd.concat([df1, df2], axis=1)       # horizontal stack
pd.concat([df1, df2], ignore_index=True)  # reset index
```

### `pd.merge`

```python
pd.merge(left, right, on='key')                    # inner join
pd.merge(left, right, on='key', how='left')        # left join
pd.merge(left, right, on='key', how='outer')       # outer join
pd.merge(left, right, left_on='a', right_on='b')  # different key names
pd.merge(left, right, on=['key1', 'key2'])         # composite key
```

| `how`   | Keeps                                     |
| ------- | ----------------------------------------- |
| `inner` | only rows with matches in both (default)  |
| `left`  | all rows from left, NaN for missing right |
| `right` | all rows from right, NaN for missing left |
| `outer` | all rows from both, NaN where no match    |

### `.join`

```python
df1.join(df2, how='left')   # joins on index by default
df1.join(df2.set_index('key'), on='key')  # join on column
```

## Index operations

```python
df.set_index('name')            # use column as index
df.reset_index()                # move index back to column
df.reset_index(drop=True)       # drop index entirely

# reindex — conform to new index, NaN for missing
df.reindex(['r0', 'r3', 'r5'])

# MultiIndex
df.set_index(['year', 'name'])
df.loc[(2020, 'Alice')]
df.xs('Alice', level='name')
```

## Time series

```python
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# .dt accessor (on datetime Series)
df['date'].dt.year
df['date'].dt.month
df['date'].dt.day_name()
df['date'].dt.is_month_end

# resampling
df.resample('M').mean()      # monthly mean
df.resample('W').sum()       # weekly sum
df.resample('Q').agg({'sales': 'sum', 'price': 'mean'})

# shifting
df['lag1'] = df['value'].shift(1)    # previous value
df['lead1'] = df['value'].shift(-1)  # next value
df['pct_change'] = df['value'].pct_change()

# rolling window
df['roll_mean'] = df['value'].rolling(window=7).mean()
df['roll_std']  = df['value'].rolling(window=7).std()
```

## Passing DataFrames to Matplotlib

Pandas integrates with Matplotlib in two ways: the built-in `.plot()` wrapper, and passing columns directly to Matplotlib functions.

### Built-in `.plot()` wrapper

Calls Matplotlib internally — good for quick exploration.

```python
import matplotlib.pyplot as plt

df['score'].plot()                    # line plot
df['score'].plot(kind='hist', bins=10)
df.plot(x='age', y='score', kind='scatter')
df.plot(kind='bar')
df.plot(kind='box')

# returns a Matplotlib Axes object — customize from there
ax = df['score'].plot(kind='hist')
ax.set_xlabel('Score')
ax.set_title('Score distribution')
plt.tight_layout()
plt.show()
```

### Passing columns to Matplotlib directly

Use this when you need full control (OO interface, subplots, seaborn, etc.).

```python
fig, ax = plt.subplots()
ax.scatter(df['age'], df['score'])
ax.set_xlabel('Age')
ax.set_ylabel('Score')

# groupby + color by group
fig, ax = plt.subplots()
for label, group in df.groupby('result'):
    ax.scatter(group['age'], group['score'], label=label)
ax.legend()

# multiple subplots from DataFrame columns
fig, axes = plt.subplots(1, 2)
axes[0].hist(df['age'], bins=5)
axes[1].hist(df['score'], bins=5)
```

### Seaborn — pass DataFrame directly

Seaborn accepts a `data=` DataFrame and column names as strings.

```python
import seaborn as sns
sns.scatterplot(data=df, x='age', y='score', hue='result')
sns.boxplot(data=df, x='result', y='score')
sns.histplot(data=df, x='score', hue='result', kde=True)
```

## Performance notes

- **Avoid row-wise loops** — use vectorized operations, `.apply` only when necessary, `np.where` instead of `apply(lambda)` for conditionals.
- **Use `category` dtype** for low-cardinality string columns — saves memory and speeds up `groupby`.
- **`pd.read_csv` with `dtype=`** — specify dtypes upfront to avoid inference overhead on large files.
- **`inplace=True`** — modifies the object in place; avoids creating a copy. Use carefully — can mask errors and breaks method chaining.
- **Method chaining** — cleaner than intermediate variables:

```python
result = (
    df
    .dropna(subset=['score'])
    .rename(columns={'score': 'points'})
    .query('points > 80')
    .groupby('result')['points']
    .mean()
)
```

## Exercises

`python/numpy_pandas/src/pandas_exercises.py`

| #   | Topic                                               | Difficulty | File         |
| --- | --------------------------------------------------- | ---------- | ------------ |
| P01 | Inspection — shape, dtypes, NaN counts, describe    | easy       | `src/p01.py` |
| P02 | Boolean filtering + column selection                | easy       | `src/p02.py` |
| P03 | `.loc` vs `.iloc` — same slice, compare results     | easy       | `src/p03.py` |
| P04 | Fill NaN salary with per-department median          | medium     | `src/p04.py` |
| P05 | Conditional column with `np.where`/`pd.cut`         | medium     | `src/p05.py` |
| P06 | Rename columns + reset index                        | easy       | `src/p06.py` |
| P07 | Tenure in years from datetime column                | medium     | `src/p07.py` |
| P08 | String accessor — uppercase + truncate              | easy       | `src/p08.py` |
| P09 | Multi-key sort                                      | easy       | `src/p09.py` |
| P10 | groupby multi-aggregation summary table             | medium     | `src/p10.py` |
| P11 | Top earner per department                           | medium     | `src/p11.py` |
| P12 | salary vs dept mean via groupby transform           | medium     | `src/p12.py` |
| P13 | Left merge on department                            | medium     | `src/p13.py` |
| P14 | Resample to quarterly + dual-axis plot              | hard       | `src/p14.py` |
| P15 | 2×2 Matplotlib dashboard — hist, scatter, bar, line | hard       | `src/p15.py` |

## See also

- [[NumPy Cheatsheet]]
- [[Index]]
- [[../../python/mpl/notes/Index|Matplotlib Notes]]
