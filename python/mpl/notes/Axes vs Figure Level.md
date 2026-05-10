---
tags: [python, seaborn, matplotlib, visualization]
status: complete
source: python/mpl/src/hist_vs_histplot.py, python/mpl/src/displot.py
---

# Axes vs Figure Level

> Seaborn has two API tiers — axes-level functions draw on one `Axes` you control, figure-level functions create their own figure and support faceting across a grid of panels.

## The split

Every seaborn plot type exists at both levels. The axes-level function does the drawing. The figure-level wrapper adds faceting and manages the figure around it.

| Axes-level                                                   | Figure-level | Domain                  |
| ------------------------------------------------------------ | ------------ | ----------------------- |
| `histplot`, `kdeplot`, `ecdfplot`                            | `displot`    | distributions           |
| `scatterplot`, `lineplot`                                    | `relplot`    | relationships           |
| `boxplot`, `violinplot`, `barplot`, `stripplot`, `swarmplot` | `catplot`    | categorical             |
| `heatmap`, `regplot`                                         | —            | no figure-level wrapper |

## Axes-level

Draws onto a single `Axes`. Returns that `Axes`. Accepts `ax=` so you can place it inside a subplot grid you built with `plt.subplots()`.

![[resources/pictures/mpl/hist_vs_histplot.png]]

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
sns.histplot(data=df, x="score", hue="group", kde=True, ax=ax1)
sns.kdeplot(data=df, x="score", hue="group", ax=ax2)
```

Use axes-level when you need the plot as one panel among others, or when you need fine-grained control over the figure layout.

## Figure-level

Creates its own `Figure` and one or more `Axes` internally. Returns a `FacetGrid` object, not an `Axes`. Has no `ax=` parameter — passing it raises an error.

![[resources/pictures/mpl/displot.png]]

```python
g = sns.displot(data=df, x="score", col="group", hue="year", kind="hist", kde=True)
# g is a FacetGrid
```

The only reason to use figure-level over axes-level is `col=` and `row=` faceting — splitting the data across a grid of panels in one call.

## FacetGrid object

Figure-level functions return a `FacetGrid`. Customisation goes through the grid, not through `ax` directly.

```python
g.set_axis_labels("Score", "Density")   # labels on all panels
g.set_titles(col_template="{col_name}") # panel titles from col= values
g.figure.suptitle("Overall title", y=1.03)

# access individual axes:
g.axes[0, 0]   # row 0, col 0
g.ax            # only valid when there is exactly one panel
```

## Decision rule

| Situation                                        | Use                                       |
| ------------------------------------------------ | ----------------------------------------- |
| One plot, or composing with `plt.subplots()`     | axes-level + `ax=`                        |
| Need `col=` / `row=` faceting                    | figure-level                              |
| Need fine mpl customisation after plotting       | axes-level — returns `Axes` directly      |
| Need to combine two different seaborn plot types | axes-level — call each with its own `ax=` |

## Source files

- `python/mpl/src/hist_vs_histplot.py` — axes-level `histplot` injected via `ax=` into `plt.subplots()`
- `python/mpl/src/displot.py` — figure-level `displot` with `col=` and `hue=` faceting

## See also

- [[Histplot Cheatsheet]]
- [[Matplotlib vs Seaborn]]
- [[Index]]
