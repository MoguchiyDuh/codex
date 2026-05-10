---
tags: [python, matplotlib, visualization]
status: complete
source: python/mpl/src/fill_between.py
---

# Fill Between Cheatsheet

> `ax.fill_between()` — shade the area between two curves or between a curve and a threshold. Native matplotlib, no seaborn equivalent.

![[resources/pictures/mpl/fill_between.png]]

## fill_between() arguments

```python
ax.fill_between(
    x,                  # x values
    y1,                 # lower bound — curve, scalar, or array
    y2=0,               # upper bound — default is 0 (fills to x-axis)
    where=None,         # boolean array — fill only where True
    alpha=0.3,          # always set — default fill is opaque and heavy
    color="steelblue",
    label="shaded region",
    interpolate=False,  # if True, interpolates crossing points when using where=
)
```

## Three common patterns

**Highlight region above a threshold:**

```python
ax.fill_between(x, y, 0.5, where=(y > 0.5), color="orange", alpha=0.4)
```

**Fill between two curves:**

```python
ax.fill_between(x, y1, y2, alpha=0.2, color="purple")
```

**Confidence band (mean ± std):**

```python
ax.fill_between(x, mean - std, mean + std, alpha=0.3, color="steelblue")
```

## where=

Accepts any boolean array of the same length as `x`. Only regions where `where=True` are filled. Use `interpolate=True` when the condition boundary falls between data points — without it, the fill edge can look jagged at crossings.

## y2 default

`y2` defaults to `0`, so `fill_between(x, y)` fills between the curve and the x-axis. Pass a scalar or array to change the lower/upper bound.

## axhline / axvline

Often paired with `fill_between` to draw the threshold reference line:

```python
ax.axhline(0.5, color="orange", linestyle="--", linewidth=1)  # horizontal line
ax.axvline(3.0, color="gray",   linestyle="--", linewidth=1)  # vertical line
```

## Source files

- `python/mpl/src/fill_between.py` — three panels: threshold highlight, two-curve fill, confidence band

## See also

- [[Plot Cheatsheet]]
- [[Index]]
