---
tags: [python, matplotlib, visualization, plotting]
status: complete
source: python/mpl/tasks/plot_simple.py, python/mpl/tasks/plot_oo.py
---

# Plot Cheatsheet

> `plt.plot()` — every common argument, and the full pyplot vs OO style mapping.

![[resources/pictures/mpl/plot_simple.png]]

![[resources/pictures/mpl/plot_oo.png]]

## pyplot vs OO style

pyplot uses module-level functions that operate on an implicit "current axes". OO style creates the figure and axes explicitly and calls methods on them. Both call identical `plot()` arguments — the difference is only in setup and formatting calls.

| Action        | pyplot                      | OO                                      |
| ------------- | --------------------------- | --------------------------------------- |
| Create figure | `plt.figure(figsize=(...))` | `fig, ax = plt.subplots(figsize=(...))` |
| Plot          | `plt.plot(x, y, ...)`       | `ax.plot(x, y, ...)`                    |
| Title         | `plt.title("t")`            | `ax.set_title("t")`                     |
| x label       | `plt.xlabel("x")`           | `ax.set_xlabel("x")`                    |
| y label       | `plt.ylabel("y")`           | `ax.set_ylabel("y")`                    |
| x limits      | `plt.xlim(0, 10)`           | `ax.set_xlim(0, 10)`                    |
| y limits      | `plt.ylim(-1, 1)`           | `ax.set_ylim(-1, 1)`                    |
| Grid          | `plt.grid(True, ...)`       | `ax.grid(True, ...)`                    |
| Legend        | `plt.legend(...)`           | `ax.legend(...)`                        |
| Tight layout  | `plt.tight_layout()`        | `fig.tight_layout()`                    |

`legend()` and `grid()` are exceptions — they have no `set_` prefix. Every other axes-level formatter uses `set_*`.

## plot() arguments

```python
ax.plot(
    x, y,
    color="royalblue",        # any CSS name, hex '#1f77b4', or cycle 'C0'–'C9'
    linewidth=2,              # stroke thickness in points (alias: lw)
    linestyle="-",            # '-'  '--'  '-.'  ':'  (alias: ls)
    marker="o",               # glyph at each data point — see marker table below
    markersize=6,             # diameter in points (alias: ms)
    markerfacecolor="white",  # fill color of the marker (alias: mfc)
    markeredgecolor="navy",   # border color of the marker (alias: mec)
    alpha=0.9,                # 0.0 transparent → 1.0 opaque
    label="sin(x)",           # legend entry — does nothing without legend()
)
```

A format string like `'ro--'` is shorthand for color + marker + linestyle in one positional argument, in the order `[color][marker][linestyle]`.

## Linestyles

| String | Alias       | Appearance           |
| ------ | ----------- | -------------------- |
| `"-"`  | `"solid"`   | continuous line      |
| `"--"` | `"dashed"`  | evenly spaced dashes |
| `"-."` | `"dashdot"` | dash-dot alternating |
| `":"`  | `"dotted"`  | small dots           |

## Markers

| String           | Shape                  |
| ---------------- | ---------------------- |
| `"o"`            | circle                 |
| `"s"`            | square                 |
| `"^"` / `"v"`    | triangle up / down     |
| `"D"`            | diamond                |
| `"x"` / `"+"`    | cross / plus (no fill) |
| `"*"`            | star                   |
| `"."`            | small dot              |
| `""` or `"None"` | no marker              |

## grid() and legend()

```python
ax.grid(
    True,
    which="major",    # "major", "minor", or "both"
    axis="both",      # "both", "x", or "y"
    linestyle="--",
    alpha=0.5,
    color="gray",
)
```

```python
ax.legend(
    loc="upper right",  # "best", "upper left", "lower right", etc.
    fontsize=11,
    framealpha=0.9,     # legend box background opacity
    title="Series",     # optional legend title
)
```

## Source files

- `python/mpl/tasks/plot_simple.py` — pyplot style, every arg annotated
- `python/mpl/tasks/plot_oo.py` — OO style, every arg annotated, same data

## See also

- [[Index]]
