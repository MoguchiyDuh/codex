---
tags: [python, numpy, data-science]
status: complete
---

# NumPy Cheatsheet

> Core reference for array creation, indexing, ufuncs, aggregations, broadcasting, and boolean masking.

## Why NumPy

Python lists store objects — each element carries a type tag, reference count, and pointer overhead. A NumPy `ndarray` stores a single contiguous block of typed data. The consequence: operations on arrays run in compiled C rather than interpreted Python, which is orders of magnitude faster at scale.

```python
import numpy as np
```

## Array creation

| Expression                             | Shape    | Notes                              |
| -------------------------------------- | -------- | ---------------------------------- |
| `np.array([1, 2, 3])`                  | `(3,)`   | from list; dtype inferred          |
| `np.array([1, 2, 3], dtype='float32')` | `(3,)`   | explicit dtype                     |
| `np.zeros((3, 4))`                     | `(3, 4)` | float64 by default                 |
| `np.ones((3, 4))`                      | `(3, 4)` |                                    |
| `np.full((3, 4), 3.14)`                | `(3, 4)` | constant fill                      |
| `np.eye(3)`                            | `(3, 3)` | identity matrix                    |
| `np.arange(0, 20, 2)`                  | `(10,)`  | like `range`, returns array        |
| `np.linspace(0, 1, 5)`                 | `(5,)`   | 5 evenly spaced points in [0,1]    |
| `np.random.random((3, 3))`             | `(3, 3)` | uniform [0, 1)                     |
| `np.random.normal(0, 1, (3, 3))`       | `(3, 3)` | standard normal                    |
| `np.random.randint(0, 10, (3, 3))`     | `(3, 3)` | random ints                        |
| `np.empty(3)`                          | `(3,)`   | uninitialized — values are garbage |

Mixed types in a list upcast silently: `np.array([3.14, 4, 2])` → `float64`.

## Array attributes

```python
x = np.random.randint(10, size=(3, 4, 5))
x.ndim    # 3
x.shape   # (3, 4, 5)
x.size    # 60
x.dtype   # dtype('int64')
x.itemsize  # 8  (bytes per element)
x.nbytes    # 480 (= size × itemsize)
```

## Indexing and slicing

```python
x = np.arange(10)       # [0 1 2 3 4 5 6 7 8 9]
x[0]                    # 0
x[-1]                   # 9
x[2:7]                  # [2 3 4 5 6]
x[::2]                  # [0 2 4 6 8]
x[::-1]                 # reversed

# 2D: [row, col]
M = np.array([[1,2,3],[4,5,6],[7,8,9]])
M[0, 0]      # 1
M[:, 0]      # first column → [1 4 7]
M[0, :]      # first row    → [1 2 3]
M[:2, :2]    # top-left 2×2 subarray
```

**Slices are views, not copies.** Modifying a slice modifies the original array.

```python
sub = M[:2, :2]
sub[0, 0] = 99   # M is also changed

copy = M[:2, :2].copy()   # explicit copy — safe to modify
```

## Reshaping

```python
np.arange(1, 10).reshape((3, 3))   # 1D → 3×3 grid

x = np.array([1, 2, 3])
x.reshape((1, 3))       # row vector shape (1, 3)
x[np.newaxis, :]        # same, via newaxis
x[:, np.newaxis]        # column vector shape (3, 1)
```

## Concatenation and splitting

```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
np.concatenate([x, y])        # [1 2 3 4 5 6]

# 2D
np.vstack([x, y])             # stack rows
np.hstack([x[:, None], y[:, None]])   # stack columns

# split at indices
x1, x2, x3 = np.split(np.arange(8), [3, 5])
# x1=[0 1 2]  x2=[3 4]  x3=[5 6 7]
np.vsplit(M, [2])   # split rows at row 2
np.hsplit(M, [2])   # split cols at col 2
```

## Ufuncs (vectorized operations)

Ufuncs apply compiled operations element-wise — no Python loop needed.

```python
x = np.arange(4)
x + 5          # np.add(x, 5)
x - 5          # np.subtract
x * 2          # np.multiply
x / 2          # np.divide
x // 2         # np.floor_divide
x ** 2         # np.power
x % 3          # np.mod
np.abs(x)

np.sin(x); np.cos(x); np.tan(x)
np.exp(x); np.log(x); np.log2(x); np.log10(x)
np.expm1(x)    # exp(x)-1, more precise near 0
np.log1p(x)    # log(1+x), more precise near 0
```

**Advanced ufunc methods:**

```python
np.add.reduce(x)       # sum all elements
np.multiply.reduce(x)  # product of all elements
np.add.accumulate(x)   # running sum (like cumsum)
np.multiply.outer(x, x)   # outer product / multiplication table
np.add.at(x, [2, 3, 3], 1)  # unbuffered in-place add at indices
```

## Aggregations

```python
x.sum()           # np.sum(x)
x.min(); x.max()
x.mean()
x.std(); x.var()
x.argmin(); x.argmax()   # index of min/max
np.median(x)
np.percentile(x, 75)
```

**Along an axis:**

```python
M = np.random.random((3, 4))
M.sum(axis=0)    # sum each column — collapses rows → shape (4,)
M.sum(axis=1)    # sum each row    — collapses cols → shape (3,)
M.min(axis=0)
M.max(axis=1)
```

`axis` specifies the dimension that gets **collapsed**, not the one returned.

**NaN-safe versions:** `np.nansum`, `np.nanmean`, `np.nanmin`, `np.nanmax`, `np.nanmedian`, etc.

| Function    | NaN-safe       | Description        |
| ----------- | -------------- | ------------------ |
| `np.sum`    | `np.nansum`    | sum                |
| `np.prod`   | `np.nanprod`   | product            |
| `np.mean`   | `np.nanmean`   | mean               |
| `np.std`    | `np.nanstd`    | standard deviation |
| `np.min`    | `np.nanmin`    | minimum            |
| `np.max`    | `np.nanmax`    | maximum            |
| `np.argmin` | `np.nanargmin` | index of minimum   |
| `np.argmax` | `np.nanargmax` | index of maximum   |
| `np.median` | `np.nanmedian` | median             |
| `np.any`    | —              | any True           |
| `np.all`    | —              | all True           |

## Broadcasting

Broadcasting lets NumPy apply binary operations on arrays of **different shapes** without copying data. NumPy resolves shape mismatches through three rules, applied left to right:

**Rule 1** — If arrays differ in number of dimensions, pad the smaller shape with 1s on the **left**.

**Rule 2** — Any dimension with size 1 is **stretched** to match the other array.

**Rule 3** — If sizes disagree in any dimension and neither is 1, raise a `ValueError`.

```python
# scalar + 1D
a = np.array([0, 1, 2])   # shape (3,)
a + 5                      # shape () → (1,) → (3,)  result: [5 6 7]

# 2D + 1D
M = np.ones((2, 3))       # shape (2, 3)
a = np.arange(3)          # shape (3,) → rule 1 → (1, 3) → rule 2 → (2, 3)
M + a                     # shape (2, 3)

# both arrays broadcast
a = np.arange(3)               # shape (3,)  → (1, 3)
b = np.arange(3)[:, np.newaxis]  # shape (3, 1)
a + b                          # both → (3, 3): addition table

# incompatible shapes
M = np.ones((3, 2))
a = np.arange(3)       # (3,) → (1, 3) → (3, 3) — clashes with (3, 2) → ValueError
# fix: reshape a
M + a[:, np.newaxis]   # a → (3, 1) → (3, 2) ✓
```

**Practical pattern — centering a dataset:**

```python
X = np.random.random((10, 3))   # 10 observations, 3 features
X_centered = X - X.mean(axis=0)  # mean shape (3,) broadcasts over 10 rows
```

## Boolean masks

Comparison operators return boolean arrays and act as ufuncs:

```python
x = np.array([1, 2, 3, 4, 5])
x < 3       # [True True False False False]
x == 3      # [False False True False False]
(2 * x) == (x ** 2)

np.count_nonzero(x < 3)   # 2
np.sum(x < 3)              # 2 (False=0, True=1)
np.sum(x < 3, axis=1)     # per-row count (for 2D)
np.any(x > 4)              # True
np.all(x < 10)             # True
```

**Compound conditions — use `&` `|` `~`, not `and` `or` `not`:**

```python
np.sum((x > 1) & (x < 4))   # 2
np.sum(~(x <= 1))            # 4
```

`and`/`or` evaluate the truth of the entire array object — always a `ValueError` on arrays with more than one element.

**Boolean array as mask:**

```python
x[x < 3]           # [1 2] — 1D array of matching values
x[(x > 1) & (x < 5)]
```

## Fancy indexing

Pass an array of indices to access multiple elements at once.

```python
x = np.array([51, 92, 14, 71, 60])
x[[3, 0, 2]]        # [71 51 14]

ind = np.array([[3, 0], [1, 2]])
x[ind]              # shape (2, 2): [[71 51], [92 14]]

# 2D fancy indexing
X = np.arange(12).reshape((3, 4))
row = np.array([0, 1, 2])
col = np.array([2, 1, 3])
X[row, col]         # [X[0,2], X[1,1], X[2,3]] = [2, 5, 11]

# combine with broadcasting
X[row[:, np.newaxis], col]   # 3×3 result
```

**Modifying values with fancy indexing:**

```python
x[np.array([2, 1, 4])] = 99

# repeated indices: assignment, not accumulation
x[[0, 0]] = [4, 6]   # x[0] ends up as 6, not 10
x[i] += 1             # same trap — use np.add.at for true accumulation
np.add.at(x, i, 1)   # unbuffered: each repeat counts
```

## Standard dtypes

| dtype            | Description                             |
| ---------------- | --------------------------------------- |
| `bool_`          | boolean                                 |
| `int8/16/32/64`  | signed integer                          |
| `uint8/16/32/64` | unsigned integer                        |
| `float16/32/64`  | floating point                          |
| `complex64/128`  | complex                                 |
| `int_`           | default int (C `long`, usually `int64`) |
| `float_`         | alias for `float64`                     |

Specify as string `dtype='float32'` or object `dtype=np.float32`.

## Exercises

| #   | Topic                                                       | Difficulty | File         |
| --- | ----------------------------------------------------------- | ---------- | ------------ |
| E1  | Array creation — identity without `np.eye`                  | easy       | `src/e01.py` |
| E2  | Reshape + slice bottom-right corner                         | easy       | `src/e02.py` |
| E3  | Reverse 2D array along both axes                            | easy       | `src/e03.py` |
| E4  | Views vs copies — demonstrate in-place mutation             | easy       | `src/e04.py` |
| E5  | Sum of squares 1..100 without a loop                        | easy       | `src/e05.py` |
| E6  | Axis aggregations — row max, col argmin, col-mean centering | medium     | `src/e06.py` |
| E7  | Manual histogram with `np.add.at`                           | medium     | `src/e07.py` |
| E8  | 10×10 multiplication table via broadcasting only            | medium     | `src/e08.py` |
| E9  | Column-wise z-score normalization                           | medium     | `src/e09.py` |
| E10 | Euclidean distance matrix without loops                     | hard       | `src/e10.py` |
| E11 | Boolean mask — count and clip outliers                      | medium     | `src/e11.py` |
| E12 | Mask diagonal and upper triangle                            | medium     | `src/e12.py` |
| E13 | Fancy indexing — select and assign                          | easy       | `src/e13.py` |
| E14 | Fancy indexing — row + col simultaneously                   | medium     | `src/e14.py` |
| E15 | `np.add.at` scatter-add vs `+=` trap                        | hard       | `src/e15.py` |

## See also

- [[Index]]
- [[../../python/mpl/notes/Index|Matplotlib Notes]]
