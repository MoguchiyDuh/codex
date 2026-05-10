---
tags: [python, matplotlib, visualization]
status: complete
source: python/mpl/src/pie_chart.py
---

# Pie Chart Cheatsheet

> `ax.pie()` — native matplotlib, no seaborn equivalent. Takes pre-computed sizes, not raw data.

![[resources/pictures/mpl/pie_chart.png]]

## pie() arguments

```python
wedges, texts, autotexts = ax.pie(
    sizes,                  # array of values — automatically normalized to sum to 1
    labels=labels,          # slice labels
    explode=explode,        # array of offsets per slice — 0=none, 0.1=slight pop-out
    autopct="%1.1f%%",      # format string for percentage inside each slice — None to hide
    startangle=90,          # angle of first slice — 90 = starts at 12 o'clock
    shadow=False,           # drop shadow behind the chart
    colors=None,            # list of colors — defaults to current color cycle
    wedgeprops={},          # kwargs forwarded to each wedge patch
    counterclock=True,      # slice direction — False = clockwise
)
# returns: (wedges, label texts, autopct texts)
```

## explode

Array of the same length as `sizes`. Each value is the fractional radius to offset that slice outward. Typically `0` for all slices except the one you want to highlight.

```python
explode = [0.1 if s == max(sizes) else 0 for s in sizes]
```

## autopct format strings

| String      | Output     |
| ----------- | ---------- |
| `"%1.1f%%"` | `"23.4%"`  |
| `"%1.0f%%"` | `"23%"`    |
| `"%.2f%%"`  | `"23.45%"` |

The double `%%` is a literal `%` in Python format strings.

## Donut chart

Set `wedgeprops={"width": 0.5}` — values between 0 and 1 control the ring thickness. `width=1` is a full pie, `width=0` is invisible.

```python
ax.pie(sizes, wedgeprops={"width": 0.5})
```

## Styling the autopct text

`ax.pie()` returns `(wedges, texts, autotexts)`. Iterate `autotexts` to restyle percentage labels:

```python
for at in autotexts:
    at.set_fontsize(9)
    at.set_color("white")
```

## Sizes are normalized automatically

You do not need to convert to percentages. `ax.pie([10, 20, 30])` is identical to `ax.pie([100, 200, 300])`. Normalize manually only if you want to display the raw percentages in labels or `autopct`.

## Source files

- `python/mpl/src/pie_chart.py` — standard pie with `explode` and shadow, donut with `wedgeprops`

## See also

- [[Plot Cheatsheet]]
- [[Index]]
