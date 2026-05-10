---
tags: [python, matplotlib, seaborn, visualization]
status: complete
---

# Matplotlib vs Seaborn

> Seaborn is a wrapper around matplotlib — it calls mpl underneath and returns mpl objects. The difference is defaults, statistical features, and DataFrame awareness.

## What seaborn adds

Matplotlib plots whatever numbers you pass. Seaborn adds three things on top:

**Statistical aggregation.** `sns.barplot()` computes mean and confidence intervals from raw data automatically. `ax.bar()` plots whatever values you give it — aggregation is your responsibility.

**Faceting by category.** `hue=`, `col=`, and `row=` split a plot by a categorical variable in a single call. In matplotlib you write a loop, manage colors manually, and build the legend yourself.

**DataFrame-aware API.** Pass `data=df, x="col_name", y="other_col"` instead of `df["col_name"]` everywhere. Column names become axis labels automatically.

The tradeoff: seaborn is less flexible for precise customization. When defaults aren't enough, you drop down to the matplotlib `Axes` object that every seaborn function returns.

## Function-level comparison

| Task              | matplotlib                          | seaborn                                        |
| ----------------- | ----------------------------------- | ---------------------------------------------- |
| Histogram         | `ax.hist()`                         | `sns.histplot()`                               |
| KDE curve         | `scipy.stats.gaussian_kde` manually | `sns.kdeplot()`                                |
| Scatter           | `ax.scatter()`                      | `sns.scatterplot()`                            |
| Line              | `ax.plot()`                         | `sns.lineplot()` — adds CI bands               |
| Bar (categorical) | `ax.bar()`                          | `sns.barplot()` — auto-aggregates + error bars |
| Box plot          | `ax.boxplot()`                      | `sns.boxplot()` — cleaner API, hue support     |
| Regression        | manual                              | `sns.regplot()` / `sns.lmplot()`               |
| Heatmap           | `ax.imshow()` + manual colorbar     | `sns.heatmap()` — annotations built in         |

## hist() vs histplot()

![[resources/pictures/mpl/hist_vs_histplot.png]]

|                | `ax.hist()`                    | `sns.histplot()`                                               |
| -------------- | ------------------------------ | -------------------------------------------------------------- |
| Default y-axis | counts                         | counts                                                         |
| KDE overlay    | no — separate `kdeplot()` call | `kde=True`                                                     |
| y-axis control | `density=True` only            | `stat=` — `"count"`, `"density"`, `"probability"`, `"percent"` |
| Input          | array or list                  | array, Series, or DataFrame column name                        |
| Returns        | `(counts, bin_edges, patches)` | `Axes`                                                         |

`density=True` in mpl and `stat="density"` in seaborn produce the same y-axis. With density, bar heights can exceed 1 — the y-axis is density, not probability.

## Customization flow

Seaborn functions return the matplotlib `Axes` (or a `FacetGrid` for figure-level functions like `displot`, `catplot`). Fine-grained tweaks always go through matplotlib after the seaborn call:

```python
ax = sns.histplot(data=df, x="col", kde=True)
ax.set_title("My title")        # standard mpl call on the returned Axes
ax.set_xlim(0, 100)
```

For figure-level functions, access the underlying axes via `.axes` or `.ax` on the returned grid object.

## See also

- [[Plot Cheatsheet]]
- [[Index]]
