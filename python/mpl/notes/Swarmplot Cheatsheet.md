---
tags: [python, seaborn, matplotlib, visualization, categorical]
status: complete
source: python/mpl/src/swarmplot.py
---

# Swarmplot Cheatsheet

> `sns.swarmplot()` — axes-level categorical scatter that shows every individual point without overlap by jittering along the categorical axis.

![[resources/pictures/mpl/swarmplot.png]]

## swarmplot() arguments

```python
sns.swarmplot(
    data=df,
    x="category",       # categorical axis
    y="value",          # numeric axis
    hue="subgroup",     # color by category — auto legend
    palette="Set2",
    size=5,             # marker diameter in points
    orient="v",         # "v" vertical (default) or "h" horizontal
    dodge=True,         # separate points by hue= group — needed when overlaying on grouped plots
    legend="auto",      # "auto", "brief", "full", or False
    ax=ax,
)
```

## When to use

Swarmplot is best for small to medium datasets — up to roughly 300–500 points. Beyond that, the algorithm that avoids overlap becomes slow and the plot gets crowded. For large datasets, use `boxplot` or `violinplot` instead.

## dodge=

When `hue=` is set and the swarmplot is overlaid on a grouped `boxplot` or `violinplot`, set `dodge=True` to align the swarm points with their respective hue groups. Without it, all points stack in the center of each category.

## Overlay pattern

The most common use of swarmplot is layered on top of a boxplot or violinplot — the summary plot gives statistics, the swarm shows the raw data.

```python
sns.boxplot(data=df, x="cat", y="val", hue="group", ax=ax)
sns.swarmplot(data=df, x="cat", y="val", hue="group",
              dodge=True, legend=False, size=3,
              palette="dark:black", ax=ax)
```

Use `legend=False` on the swarmplot — the boxplot already owns the legend. Use a dark neutral palette on the swarm so points are visible over colored boxes.

## figure-level equivalent

`sns.catplot(kind="swarm", ...)` — adds `col=`/`row=` faceting, returns `FacetGrid`.

## Source files

- `python/mpl/src/swarmplot.py` — two panels: standalone swarmplot with `hue=`, swarmplot overlaid on grouped boxplot with `dodge=True`

## See also

- [[Box and Violin Cheatsheet]]
- [[Barplot Cheatsheet]]
- [[Axes vs Figure Level]]
- [[Index]]
