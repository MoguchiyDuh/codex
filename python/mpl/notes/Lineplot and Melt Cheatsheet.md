---
tags: [python, seaborn, matplotlib, visualization, pandas]
status: complete
source: python/mpl/src/lineplot_melt.py
---

# Lineplot and Melt Cheatsheet

> `sns.lineplot()` expects tidy (long) data. `df.melt()` reshapes wide data into long format so seaborn can use `hue=`, `col=`, and `row=`.

![[resources/pictures/mpl/lineplot_melt.png]]

## Wide vs long format

Wide format has one column per category — natural when building data manually:

```text
year  | London | Paris | Berlin
2000  | 12.1   | 14.3  | 10.2
2001  | 12.4   | 14.1  | 10.5
```

Long (tidy) format has one row per observation — what seaborn expects:

```text
year  | city    | temperature
2000  | London  | 12.1
2000  | Paris   | 14.3
2000  | Berlin  | 10.2
2001  | London  | 12.4
```

## df.melt()

```python
long_df = wide_df.melt(
    id_vars="year",              # columns to keep as-is — the identifier
    value_vars=["London", "Paris", "Berlin"],  # columns to unpivot (default: all non-id_vars)
    var_name="city",             # name for the new column holding old column names
    value_name="temperature",    # name for the new column holding the values
)
```

`id_vars` stays fixed per row. Each `value_vars` column becomes a separate row, with its name going into `var_name` and its value into `value_name`.

## sns.lineplot() arguments

```python
sns.lineplot(
    data=df,
    x="col_x",
    y="col_y",
    hue="category",      # one line per category — auto colors + legend
    style="category",    # line style per category
    size="col",          # line width scales with column value
    markers=True,        # show markers at data points
    dashes=True,         # use dashes to distinguish lines (pairs with style=)
    errorbar="ci",       # show CI band when multiple y per x — "ci", "sd", None
    linewidth=2,
    ax=ax,
)
```

## Without melt — manual loop

When data is wide, you must loop and call `ax.plot()` per column. You lose `hue=` and CI bands.

```python
for city in ["London", "Paris", "Berlin"]:
    ax.plot(df["year"], df[city], label=city)
ax.legend()
```

## figure-level equivalent

`sns.relplot(kind="line", ...)` — adds `col=`/`row=` faceting, returns `FacetGrid`.

## Source files

- `python/mpl/src/lineplot_melt.py` — wide format manual loop vs long format with `melt()` + `sns.lineplot(hue=)` side by side

## See also

- [[Axes vs Figure Level]]
- [[Index]]
