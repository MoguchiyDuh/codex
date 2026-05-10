---
tags: [python, seaborn, matplotlib, visualization, categorical]
status: complete
source: python/mpl/src/violin_box.py
---

# Box and Violin Cheatsheet

> `sns.boxplot()` and `sns.violinplot()` — both axes-level, both show distribution summaries for categorical groups.

![[resources/pictures/mpl/violin_box.png]]

## When to use which

Boxplot shows five-number summary (min, Q1, median, Q3, max) and outliers — compact, precise. Violinplot shows the full distribution shape via KDE — more informative when the distribution is multimodal or skewed, but harder to read exact values from.

## boxplot() arguments

```python
sns.boxplot(
    data=df,
    x="category",       # categorical axis
    y="value",          # numeric axis
    hue="subgroup",     # grouped boxes per category — splits each x position
    palette="Set2",
    width=0.6,          # box width (0–1)
    linewidth=1.5,      # box edge stroke thickness
    flierprops={        # outlier marker styling
        "marker": "o",
        "markersize": 4,
    },
    ax=ax,
)
```

What the box shows: median = center line, IQR = box height, whiskers = 1.5 × IQR, dots beyond whiskers = outliers.

## violinplot() arguments

```python
sns.violinplot(
    data=df,
    x="category",
    y="value",
    hue="subgroup",
    split=True,         # mirror two hue groups inside one violin — requires exactly 2 hue values
    inner="quart",      # marks inside violin: "quart", "box", "point", "stick", None
    palette="Set2",
    linewidth=1.2,
    bw_adjust=1.0,      # KDE smoothing — higher = smoother shape
    ax=ax,
)
```

## inner= options

| Value     | What it draws inside the violin |
| --------- | ------------------------------- |
| `"quart"` | three lines at Q1, median, Q3   |
| `"box"`   | a small embedded boxplot        |
| `"point"` | individual data points          |
| `"stick"` | a stick per data point          |
| `None`    | nothing — clean shape only      |

## split= flag

`split=True` requires exactly 2 `hue=` values. Instead of drawing two separate violins side by side, it mirrors them left/right inside one violin — saves space and makes the comparison more direct.

## sharey

`sharey=True` in `plt.subplots()` links the y-axis scale across all panels — panning or zooming one updates all. Use it when comparing plots of the same variable so the y range is identical and the plots are directly comparable.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
```

## figure-level equivalent

Both are wrapped by `catplot()`:

```python
sns.catplot(data=df, x="category", y="value", hue="subgroup", kind="box")
sns.catplot(data=df, x="category", y="value", hue="subgroup", kind="violin")
```

`catplot` adds `col=`/`row=` faceting. Returns a `FacetGrid`.

## Source files

- `python/mpl/src/violin_box.py` — boxplot and violinplot side by side on the same data with `sharey=True`

## See also

- [[Axes vs Figure Level]]
- [[Index]]
