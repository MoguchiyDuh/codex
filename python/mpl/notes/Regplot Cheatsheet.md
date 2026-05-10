---
tags: [python, seaborn, matplotlib, visualization, regression]
status: complete
source: python/mpl/src/regplot.py
---

# Regplot Cheatsheet

> `sns.regplot()` — axes-level scatter plot with an automatic regression line and optional confidence interval band. No `hue=` support — use `lmplot()` for grouped regression.

![[resources/pictures/mpl/regplot.png]]

## regplot() arguments

```python
sns.regplot(
    data=df,
    x="col_x",              # column name or array
    y="col_y",
    ci=95,                  # confidence interval width (0–100), or None to hide
    order=1,                # polynomial degree — 1=linear, 2=quadratic, etc.
    logistic=False,         # fit a logistic regression — y must be binary (0/1)
    lowess=False,           # fit a locally weighted smoother instead of OLS
    robust=False,           # use robust regression — less sensitive to outliers
    scatter=True,           # set False to draw the line only, no points
    scatter_kws={           # kwargs forwarded to the scatter plot
        "alpha": 0.5,
        "s": 30,
        "color": "steelblue",
    },
    line_kws={              # kwargs forwarded to the regression line
        "color": "red",
        "linewidth": 2,
        "linestyle": "--",
    },
    ax=ax,
)
```

## ci=

The shaded band around the regression line represents a bootstrapped confidence interval. `ci=95` is standard. Set `ci=None` to remove it — useful when data is very noisy and the band obscures the line.

## order=

Fits a polynomial of the given degree via OLS. `order=1` is a straight line. `order=2` fits a parabola. Use when a scatter plot clearly shows a curved relationship.

## logistic=

Fits a logistic curve. Requires `y` to be binary (0 or 1). Use for classification boundary visualization, not for continuous `y`.

## lowess=

Fits a locally weighted scatterplot smoother — non-parametric, follows the data shape without assuming linearity. No confidence interval is drawn when `lowess=True`.

## scatter_kws and line_kws

Neither `scatter_kws` nor `line_kws` accept `label=` — `regplot` has no legend support. If you need a legend, add it manually with `ax.legend()` after adding proxy artists.

## no hue= — use lmplot() instead

`regplot` draws one regression per call and has no `hue=` parameter. To draw separate regression lines per category, use the figure-level `lmplot()`:

```python
sns.lmplot(data=df, x="col_x", y="col_y", hue="category", col="category")
```

`lmplot` returns a `FacetGrid`, not an `Axes`.

## Source files

- `python/mpl/src/regplot.py` — three panels: linear with CI, noisy data with `ci=None`, polynomial `order=2`

## See also

- [[Scatterplot Cheatsheet]]
- [[Axes vs Figure Level]]
- [[Index]]
