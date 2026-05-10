---
tags: [python, matplotlib, visualization, subplots]
status: complete
---

# Subplots Cheatsheet

> `plt.subplots()` — create a figure with a grid of axes in one call.

## Basic signature

```python
fig, ax  = plt.subplots()                        # single axes
fig, axs = plt.subplots(2, 3)                    # 2 rows, 3 cols → axs.shape == (2, 3)
fig, axs = plt.subplots(1, 2, figsize=(12, 5))   # control figure size
```

## plt.subplots() arguments

```python
fig, axs = plt.subplots(
    nrows=2,
    ncols=3,
    figsize=(12, 8),      # (width, height) in inches
    sharex=False,         # share x-axis scale across columns — "col", "row", True, False
    sharey=True,          # share y-axis scale across rows — same options
    squeeze=True,         # if True (default), squeeze out size-1 dimensions
    layout="constrained", # "constrained", "tight", or None — auto spacing
)
```

## Accessing axes

```python
fig, axs = plt.subplots(2, 3)

axs[0, 0]   # row 0, col 0
axs[1, 2]   # row 1, col 2

# single row or column — axs is 1D when nrows=1 or ncols=1 (squeeze=True)
fig, axs = plt.subplots(1, 3)
axs[0]      # first panel

# unpacking — cleaner for small fixed grids
fig, (ax1, ax2) = plt.subplots(1, 2)
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
```

## sharex= / sharey=

Links axis scales across panels. Zooming or setting limits on one updates all linked axes.

| Value   | Effect                   |
| ------- | ------------------------ |
| `True`  | share across all panels  |
| `False` | independent — default    |
| `"col"` | share within each column |
| `"row"` | share within each row    |

Use `sharey=True` when comparing the same variable across panels — ensures y range is identical and plots are directly comparable.

## squeeze= behavior

With `squeeze=True` (default), size-1 dimensions are removed from `axs`:

- `subplots(1, 1)` → `axs` is a single `Axes`, not a 1×1 array
- `subplots(1, 3)` → `axs` is a 1D array of length 3, not shape `(1, 3)`
- `subplots(2, 3)` → `axs` is always 2D — no squeezing

Set `squeeze=False` to always get a 2D array regardless of shape — safer when writing generic code.

## layout=

Controls automatic spacing between panels so labels don't overlap.

| Value           | Behaviour                                                 |
| --------------- | --------------------------------------------------------- |
| `"constrained"` | recommended — precise, handles colorbars                  |
| `"tight"`       | older — calls `tight_layout()` internally                 |
| `None`          | no automatic spacing — call `fig.tight_layout()` manually |

## fig.suptitle()

Overall figure title, above all panels.

```python
fig.suptitle("Overall title", fontsize=14, fontweight="bold", y=1.02)
```

`y=` nudges the title vertically — useful when `layout="constrained"` clips it.

## Injecting seaborn into a subplot

Pass `ax=` to any axes-level seaborn function:

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
sns.histplot(data=df, x="score", hue="group", ax=ax1)
sns.boxplot(data=df, x="group", y="score", ax=ax2)
fig.tight_layout()
```

Figure-level functions (`displot`, `relplot`, `catplot`) cannot be injected this way — they have no `ax=` parameter.

## See also

- [[Axes vs Figure Level]]
- [[Plot Cheatsheet]]
- [[Index]]
