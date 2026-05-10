---
tags: [python, seaborn, matplotlib, visualization, heatmap]
status: complete
source: python/mpl/src/heatmap.py
---

# Heatmap Cheatsheet

> `sns.heatmap()` — no figure-level wrapper. Takes a 2D array or DataFrame directly, not tidy data.

![[resources/pictures/mpl/heatmap.png]]

## heatmap() arguments

```python
sns.heatmap(
    data,               # 2D array or square DataFrame — e.g. df.corr()
    annot=True,         # print values in each cell
    fmt=".2f",          # format string for annotations — ".2f", "d", ".0%", etc.
    cmap="coolwarm",    # colormap — see table below
    vmin=-1, vmax=1,    # pin colorbar range explicitly
    center=0,           # value mapped to the middle of the colormap
    linewidths=0.5,     # separator lines between cells
    linecolor="white",  # color of separator lines
    square=True,        # force square cells
    mask=None,          # boolean array — True = cell is hidden (e.g. upper triangle)
    cbar=True,          # show colorbar
    cbar_kws={},        # kwargs forwarded to the colorbar
    ax=ax,
)
```

## Colormap choices

| cmap                      | Use case                                                   |
| ------------------------- | ---------------------------------------------------------- |
| `"coolwarm"` / `"RdBu_r"` | correlations, diverging data centered at 0                 |
| `"viridis"` / `"plasma"`  | sequential — counts, magnitudes, always positive           |
| `"YlOrRd"`                | sequential, intuitive for heatmaps like confusion matrices |
| `"Blues"`                 | single-hue sequential                                      |

Use `vmin`/`vmax` to pin the colorbar range. Use `center=` to set what value maps to the colormap midpoint.

## Correlation matrix pattern

The most common exam use case — compute with `df.corr()`, plot with `heatmap`.

```python
corr = df.corr()       # square DataFrame, values in [-1, 1]
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1, square=True)
```

## Masking the upper triangle

Correlation matrices are symmetric — masking one triangle avoids redundancy.

```python
import numpy as np
mask = np.triu(np.ones_like(corr, dtype=bool))  # True for upper triangle + diagonal
sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap="coolwarm")
```

## No figure-level equivalent

`heatmap` is axes-level only. There is no `sns.displot`-style wrapper for it. Use `ax=` to place it in a subplot grid.

## Source files

- `python/mpl/src/heatmap.py` — correlation matrix from a synthetic DataFrame

## See also

- [[Scatterplot Cheatsheet]]
- [[Axes vs Figure Level]]
- [[Index]]
