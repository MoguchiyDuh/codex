---
tags: [python, seaborn, matplotlib, visualization, histogram]
status: complete
source: python/mpl/src/hist_vs_histplot.py
---

# Histplot Cheatsheet

> `sns.histplot()` — axes-level seaborn histogram with optional KDE, hue splitting, and flexible y-axis statistics.

![[resources/pictures/mpl/hist_vs_histplot.png]]

## axes-level vs figure-level

`histplot` is axes-level — it draws onto one `Axes` and returns it. Pass `ax=` to place it inside your own subplot grid. The figure-level equivalent is `displot(kind="hist")`, which creates its own figure and supports `col=`/`row=` faceting but has no `ax=` parameter.

## histplot() arguments

```python
sns.histplot(
    data=df,              # DataFrame, array, or Series
    x="col",              # column name for x-axis (or pass array directly)
    y="col",              # use instead of x for horizontal orientation
    hue="group_col",      # split and color by a categorical column — auto legend
    bins=30,              # int = number of bins, or array of explicit bin edges
    stat="count",         # y-axis statistic — see stat table below
    kde=True,             # overlay a KDE curve per group (no separate kdeplot needed)
    cumulative=False,     # if True, plot cumulative distribution
    element="bars",       # "bars", "step", or "poly" (line connecting bar tops)
    fill=True,            # fill bars — set False with element="step" for outline only
    multiple="layer",     # how groups overlap — see multiple table below
    palette="tab10",      # color palette when hue= is set
    color="steelblue",    # single color — ignored if hue= is set
    alpha=0.5,            # bar transparency
    linewidth=0.5,        # bar edge stroke width
    edgecolor="black",    # bar edge color (alias: ec)
    log_scale=False,      # True or (True, False) for (x, y) log scaling
    ax=ax,                # inject into an existing Axes — key for subplots
)
```

## stat= options

| Value           | y-axis meaning                                   |
| --------------- | ------------------------------------------------ |
| `"count"`       | raw observation count per bin (default)          |
| `"density"`     | probability density — area of all bars sums to 1 |
| `"probability"` | probability mass — bar heights sum to 1          |
| `"percent"`     | like probability but scaled to 100               |
| `"frequency"`   | count divided by bin width                       |

`"density"` matches `ax.hist(density=True)`. Bar heights can exceed 1 — it is density, not probability.

## multiple= options

Controls what happens when `hue=` produces overlapping groups.

| Value     | Behaviour                                      |
| --------- | ---------------------------------------------- |
| `"layer"` | transparent overlap — default                  |
| `"dodge"` | side-by-side bars per bin                      |
| `"stack"` | bars stacked vertically                        |
| `"fill"`  | stacked and normalized to 1 — shows proportion |

## element= options

| Value    | Appearance                     |
| -------- | ------------------------------ |
| `"bars"` | standard filled bars — default |
| `"step"` | unfilled step outline          |
| `"poly"` | line connecting bar midpoints  |

`element="step"` with `fill=False` is useful for overlaying multiple groups without alpha clutter.

## kde overlay

`kde=True` fits and draws a KDE curve for each group automatically. The KDE is scaled to match the chosen `stat=` — so a density histogram and its KDE curve share the same y-axis. No separate `kdeplot()` call needed.

## Source files

- `python/mpl/src/hist_vs_histplot.py` — `ax.hist()` and `sns.histplot()` side by side on the same data, with `ax=` injection into a subplot grid

## See also

- [[Matplotlib vs Seaborn]]
- [[Plot Cheatsheet]]
- [[Index]]
