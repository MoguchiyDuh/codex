---
tags: [python, seaborn, visualization]
status: complete
source: python/mpl/src/pairplot.py
---

# Pairplot Cheatsheet

> `sns.pairplot()` — figure-level function that plots all pairwise relationships in a dataset. Returns a `PairGrid`, not an `Axes`.

![[resources/pictures/mpl/pairplot.png]]

## pairplot() arguments

```python
g = sns.pairplot(
    data=df,
    hue="group",        # color all panels by a categorical column — auto legend
    vars=["X1", "X2"], # columns to include — default: all numeric columns
    kind="scatter",     # off-diagonal panels: "scatter", "kde", "hist", "reg"
    diag_kind="kde",    # diagonal panels: "kde", "hist", or "auto"
    plot_kws={},        # kwargs forwarded to off-diagonal plot function
    diag_kws={},        # kwargs forwarded to diagonal plot function
    corner=False,       # if True, show only lower triangle — halves the panels
)
# returns PairGrid
```

## kind= options

| Value       | Off-diagonal panels       |
| ----------- | ------------------------- |
| `"scatter"` | scatter plot — default    |
| `"kde"`     | 2D KDE contour            |
| `"hist"`    | 2D histogram              |
| `"reg"`     | scatter + regression line |

## diag_kind= options

| Value    | Diagonal panels                         |
| -------- | --------------------------------------- |
| `"kde"`  | KDE curve per hue group                 |
| `"hist"` | histogram per hue group                 |
| `"auto"` | hist when no hue=, kde when hue= is set |

## PairGrid object

`pairplot` returns a `PairGrid`. Access the figure and axes through it:

```python
g.figure.suptitle("Title", y=1.02)   # overall title — y>1 to clear the panels
g.axes[0, 1]                          # individual axes by row, col index
```

`suptitle` needs `y=1.02` or similar because the panels fill the full figure height — the default `y=0.98` puts the title inside the plot area.

## corner=True

Shows only the lower triangle — halves the number of panels. Useful for large datasets with many variables.

## No ax= parameter

`pairplot` is figure-level — it creates its own figure. You cannot inject it into a subplot grid. Use `PairGrid` directly if you need more control:

```python
g = sns.PairGrid(df, hue="group")
g.map_lower(sns.scatterplot)
g.map_diag(sns.histplot)
g.map_upper(sns.kdeplot)
```

## Source files

- `python/mpl/src/pairplot.py` — 4-variable dataset with controlled correlations, `hue=`, `kind="scatter"`, `diag_kind="kde"`

## See also

- [[Axes vs Figure Level]]
- [[Scatterplot Cheatsheet]]
- [[Index]]
