---
tags: [python, seaborn, matplotlib, visualization, categorical]
status: complete
source: python/mpl/src/barplot.py
---

# Barplot Cheatsheet

> `sns.barplot()` — axes-level bar chart that auto-aggregates data and shows uncertainty via error bars. Not the same as `ax.bar()` — it operates on raw data, not pre-computed values.

![[resources/pictures/mpl/barplot.png]]

## barplot() arguments

```python
sns.barplot(
    data=df,
    x="category",       # categorical axis
    y="value",          # numeric axis — aggregated automatically
    hue="subgroup",     # grouped bars per category
    estimator=np.mean,  # aggregation function — np.mean, np.median, np.sum, etc.
    errorbar="ci",      # error bar type — see table below
    capsize=0.1,        # width of error bar end caps (0–1)
    orient="v",         # "v" vertical (default) or "h" horizontal
    palette="Set2",
    width=0.8,          # bar width
    ax=ax,
)
```

## estimator=

Any callable that reduces an array to a scalar. Default is `np.mean`.

| Value       | Aggregates to               |
| ----------- | --------------------------- |
| `np.mean`   | arithmetic mean — default   |
| `np.median` | median — robust to outliers |
| `np.sum`    | total                       |
| `len`       | count                       |

## errorbar=

Controls what the error bars represent.

| Value  | Meaning                                        |
| ------ | ---------------------------------------------- |
| `"ci"` | bootstrapped 95% confidence interval — default |
| `"sd"` | one standard deviation                         |
| `"se"` | standard error of the mean                     |
| `"pi"` | percentile interval                            |
| `None` | no error bars                                  |

## orient="h"

Swaps the axes — bars grow horizontally. When using `orient="h"`, put the numeric variable in `x=` and the categorical in `y=`.

## vs ax.bar()

`sns.barplot` takes raw data and aggregates. `ax.bar()` takes pre-computed heights. If you already have summary statistics, use `ax.bar()`. If you have raw observations and want mean + CI automatically, use `sns.barplot`.

## figure-level equivalent

`sns.catplot(kind="bar", ...)` — adds `col=`/`row=` faceting, returns `FacetGrid`.

## Source files

- `python/mpl/src/barplot.py` — two panels: grouped bars with `errorbar="ci"`, horizontal with `estimator=np.median` and `errorbar="sd"`

## See also

- [[Box and Violin Cheatsheet]]
- [[Axes vs Figure Level]]
- [[Index]]
