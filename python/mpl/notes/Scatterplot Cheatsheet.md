---
tags: [python, seaborn, matplotlib, visualization, scatter]
status: complete
source: python/mpl/src/scatterplot.py
---

# Scatterplot Cheatsheet

> `sns.scatterplot()` — axes-level scatter with categorical splitting via `hue=`, `size=`, and `style=`.

![[resources/pictures/mpl/scatterplot.png]]

## scatterplot() arguments

```python
sns.scatterplot(
    data=df,
    x="col_x",         # column name or array
    y="col_y",
    hue="category",    # color by column — categorical or numeric
    size="col",        # marker area scales with column values
    style="category",  # marker shape per category value
    palette="tab10",   # color palette when hue= is set
    sizes=(20, 200),   # (min, max) marker area range when size= is set
    alpha=0.7,
    edgecolor="k",     # marker edge color
    linewidth=0.5,     # marker edge width
    legend="auto",     # "auto", "brief", "full", or False
    ax=ax,
)
```

## hue= behavior

When `hue=` is a categorical column, each category gets a distinct color and a legend entry. When `hue=` is a numeric column, seaborn uses a continuous colormap instead and shows a colorbar legend.

## size= behavior

`size=` maps column values to marker area. The range is controlled by `sizes=(min_area, max_area)`. Without `sizes=`, seaborn picks a default range.

## style= behavior

`style=` maps category values to different marker shapes. Combine with `hue=` on the same column to double-encode the grouping — useful for colorblind-friendly plots.

## figure-level equivalent

`sns.relplot(kind="scatter", ...)` — adds `col=`/`row=` faceting. No `ax=` parameter.

## Source files

- `python/mpl/src/scatterplot.py` — `hue=`, `size=`, `style=` all active on the same plot

## See also

- [[Heatmap Cheatsheet]]
- [[Axes vs Figure Level]]
- [[Index]]
