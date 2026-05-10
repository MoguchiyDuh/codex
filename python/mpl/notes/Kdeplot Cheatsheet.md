---
tags: [python, seaborn, matplotlib, visualization, kde]
status: complete
source: python/mpl/src/kdeplot.py
---

# Kdeplot Cheatsheet

> `sns.kdeplot()` — axes-level kernel density estimate. Shows the shape of a distribution as a smooth curve rather than discrete bins.

![[resources/pictures/mpl/kdeplot.png]]

## kdeplot() arguments

```python
sns.kdeplot(
    data=df,
    x="col",            # column name or array
    y="col",            # second variable — produces a 2D bivariate KDE
    hue="group",        # one curve per category — auto colors + legend
    fill=True,          # shade area under the curve
    alpha=0.4,          # fill transparency — has no effect if fill=False
    linewidth=2,        # curve stroke thickness
    linestyle="-",      # "-", "--", "-.", ":"
    bw_adjust=1.0,      # smoothing multiplier — higher = smoother, lower = more detail
    cumulative=False,   # if True, plot CDF instead of PDF
    common_norm=True,   # if True, curves are normalized together — False = each normalized independently
    log_scale=False,    # log scale on x (or both axes for bivariate)
    color="steelblue",  # single color — ignored if hue= is set
    ax=ax,
)
```

## bw_adjust

Controls how smooth the curve is. It scales the automatically chosen bandwidth — it does not set the bandwidth directly.

| Value   | Effect                                               |
| ------- | ---------------------------------------------------- |
| `< 1.0` | undersmoothed — follows data closely, may show noise |
| `1.0`   | default — sensible automatic bandwidth               |
| `> 1.0` | oversmoothed — broader, hides fine structure         |

## fill= vs alpha=

`fill=True` shades the area under the curve. `alpha=` controls how transparent that fill is. `alpha=` has no visual effect when `fill=False` — it does not affect the line itself.

## cumulative=True

Plots the empirical CDF instead of the PDF. Y-axis goes from 0 to 1. Useful for reading off percentiles visually — where the curve crosses y=0.5 is the median.

## common_norm=

When `hue=` is set and groups have different sizes, `common_norm=True` (default) normalizes all curves together so areas sum to 1 across groups. `common_norm=False` normalizes each curve independently so each has area = 1 — better for comparing shape when group sizes differ.

## bivariate KDE

Pass both `x=` and `y=` to get a 2D density estimate — rendered as filled contours.

```python
sns.kdeplot(data=df, x="col_x", y="col_y", fill=True, cmap="Blues", ax=ax)
```

## figure-level equivalent

`sns.displot(kind="kde", ...)` — adds `col=`/`row=` faceting, returns `FacetGrid`.

## Source files

- `python/mpl/src/kdeplot.py` — three panels: `fill=True` with `hue=`, `bw_adjust` comparison, `cumulative=True`

## See also

- [[Histplot Cheatsheet]]
- [[Axes vs Figure Level]]
- [[Index]]
