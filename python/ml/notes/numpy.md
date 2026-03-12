---
tags: [ml, numpy, foundations]
status: complete
---

# NumPy

> N-dimensional array library. The foundation of the entire Python ML stack — pandas, TensorFlow, PyTorch all sit on top of it.

**Code:** `../src/numpy_basics.py`

---

## Core Concept

NumPy's power is the **ndarray** — a typed, contiguous block of memory with shape metadata. Operations run in C/Fortran, not Python. Avoid Python loops over arrays entirely.

```python
import numpy as np
```

---

## Array Creation

```python
np.array([1, 2, 3])              # from list — infers dtype
np.array([[1, 2], [3, 4]])       # 2D from nested lists
np.zeros((3, 4))                 # float64 zeros
np.ones((2, 3), dtype=np.int32)
np.full((3, 3), 7)               # filled with constant
np.eye(4)                        # identity matrix
np.arange(0, 10, 2)             # [0, 2, 4, 6, 8] — like range()
np.linspace(0, 1, 5)            # [0, .25, .5, .75, 1] — n evenly spaced
np.empty((3, 3))                 # uninitialized — fastest, use when you'll fill it

# Random
np.random.rand(3, 4)            # uniform [0, 1)
np.random.randn(3, 4)           # standard normal (mean=0, std=1)
np.random.randint(0, 10, (3,4)) # random ints
np.random.seed(42)              # reproducibility
```

---

## Data Types

```python
np.int8 / int16 / int32 / int64
np.uint8 / uint16 / uint32 / uint64
np.float16 / float32 / float64
np.complex64 / complex128
np.bool_
np.str_, np.bytes_, np.object_
np.datetime64, np.timedelta64

arr.dtype                        # inspect
arr.astype(np.float32)          # cast — always returns copy
```

**float32 vs float64:** float64 is default. Use float32 for ML — half the memory, faster on GPU, sufficient precision.
**uint8:** standard for image pixel data (0–255).

---

## Shape & Reshaping

```python
arr.shape                        # tuple: (rows, cols, ...)
arr.ndim                         # number of dimensions
arr.size                         # total element count
arr.nbytes                       # memory in bytes

arr.reshape(2, 6)               # new shape — must be compatible, returns view
arr.reshape(-1)                  # flatten, infer size
arr.reshape(-1, 1)              # (n,) → (n, 1) column vector
arr.ravel()                      # flatten to 1D — view if contiguous
arr.flatten()                    # flatten — always copy
arr.T                            # transpose (view)
arr.swapaxes(0, 1)              # swap two axes

# Adding/removing dimensions
arr[:, np.newaxis]              # (n,) → (n, 1)
arr[np.newaxis, :]              # (n,) → (1, n)
np.expand_dims(arr, axis=0)    # same as newaxis
arr.squeeze()                   # remove all size-1 dimensions
```

---

## Indexing & Slicing

```python
arr[0]                           # first row (2D → 1D)
arr[0, 2]                        # row 0, col 2
arr[-1]                          # last row
arr[:, 1]                        # all rows, col 1
arr[1:3, 0:2]                   # slice — returns VIEW

# Fancy indexing — returns COPY
arr[[0, 2], :]                  # rows 0 and 2
arr[:, [1, 3]]                  # cols 1 and 3
arr[[0, 1], [2, 3]]             # elements (0,2) and (1,3)

# Boolean masking — returns COPY
mask = arr > 5
arr[mask]                        # 1D array of matching elements
arr[arr > 5] = 0                # in-place masked assignment

# np.where
np.where(arr > 5, arr, 0)      # ternary: if > 5 keep, else 0
np.where(arr > 5)               # returns indices where True
```

---

## Vectorized Operations

No Python loops. Operations broadcast element-wise and run in C.

```python
a + b                            # elementwise add
a * b                            # elementwise multiply (NOT matmul)
a ** 2
a / b
np.sqrt(a)
np.exp(a)
np.log(a)                        # natural log
np.abs(a)
np.sin(a), np.cos(a)
np.clip(a, 0, 1)                # clamp values to [0, 1]

# Comparison → bool array
a > 3
np.logical_and(a > 0, a < 10)
np.logical_or(a < 0, a > 10)
```

---

## Broadcasting

Shapes are compared element-wise from the right. A dimension of 1 stretches to match. Missing leading dimensions are treated as 1.

```
(3, 4) + (4,)      → (3, 4)   ✓  — (4,) broadcasts over 3 rows
(3, 1) + (1, 4)    → (3, 4)   ✓  — both stretch
(3, 4) + (3,)      → ERROR    ✗  — rightmost dims don't match
(3, 4) + (1, 4)    → (3, 4)   ✓
```

```python
a = np.ones((3, 4))
b = np.array([1, 2, 3, 4])     # (4,) → adds to every row
a + b

# Subtract row mean — keepdims prevents shape mismatch
a - a.mean(axis=1, keepdims=True)  # (3, 4) - (3, 1) → (3, 4)
```

---

## Aggregations

```python
arr.sum()                        # scalar
arr.sum(axis=0)                  # collapse rows → column sums
arr.sum(axis=1)                  # collapse cols → row sums
arr.sum(axis=1, keepdims=True)  # keeps shape (rows, 1) — useful for broadcasting

arr.mean(), arr.std(), arr.var()
arr.min(), arr.max()
arr.argmin(), arr.argmax()       # flat index of min/max
arr.argmin(axis=0)              # index of min along axis

np.cumsum(arr)
np.sort(arr, axis=-1)
np.argsort(arr)
np.unique(arr)
np.unique(arr, return_counts=True)
np.percentile(arr, [25, 50, 75])
```

---

## Linear Algebra

```python
np.dot(a, b)                     # dot product (1D) or matmul (2D)
a @ b                            # matmul — preferred

np.linalg.inv(A)                # matrix inverse
np.linalg.det(A)                # determinant
np.linalg.norm(v)               # L2 norm
np.linalg.norm(v, ord=1)        # L1 norm
np.linalg.norm(A, axis=1)       # row-wise norms
np.linalg.eig(A)                # eigenvalues + eigenvectors
np.linalg.svd(A)                # singular value decomposition
np.linalg.solve(A, b)          # solve Ax = b — better than inv(A) @ b
np.trace(A)                      # sum of diagonal
np.diag(A)                       # extract diagonal / create diagonal matrix
```

---

## Views vs Copies

Critical — silent bugs come from modifying a view and affecting the original.

```python
# Slices → VIEW
b = a[1:3, :]
b[0, 0] = 99       # a is modified

# Fancy indexing → COPY
b = a[[0, 1], :]
b[0, 0] = 99       # a unchanged

# Boolean mask → COPY
b = a[a > 5]

a.copy()                         # explicit copy
np.shares_memory(a, b)         # True if sharing
b.base is a                      # True if b is a view of a
```

**Rule:** reshape, transpose, slice → view. Fancy index, boolean mask, astype → copy.

---

## Stacking & Splitting

```python
np.concatenate([a, b], axis=0)
np.vstack([a, b])               # vertical (axis=0)
np.hstack([a, b])               # horizontal (axis=1)
np.stack([a, b], axis=0)       # new axis

np.split(arr, 3, axis=0)
np.split(arr, [2, 5], axis=0)  # split at indices 2 and 5
np.vsplit(arr, 3)
np.hsplit(arr, 3)
```

---

## I/O

```python
np.save("arr.npy", arr)
arr = np.load("arr.npy")

np.savez("data.npz", x=arr1, y=arr2)
data = np.load("data.npz")
data["x"], data["y"]

np.savetxt("arr.csv", arr, delimiter=",", fmt="%.4f")
arr = np.loadtxt("arr.csv", delimiter=",")
```

---

## Performance

```python
# Always vectorize — no Python loops over arrays
result = arr ** 2                # fast
result = np.array([x**2 for x in arr])  # slow

# In-place avoids allocation
arr += 1          # in-place
arr = arr + 1     # allocates new array

# float32 for ML
arr = arr.astype(np.float32)

# Contiguous memory = better cache
arr = np.ascontiguousarray(arr)
arr.flags["C_CONTIGUOUS"]

# Preallocate instead of appending
out = np.empty(len(data))
for i, x in enumerate(data):
    out[i] = f(x)
```

---

## Common ML Patterns

```python
# Normalize to [0, 1]
arr = (arr - arr.min()) / (arr.max() - arr.min())

# Standardize (zero mean, unit variance)
arr = (arr - arr.mean(axis=0)) / arr.std(axis=0)

# One-hot encode labels
y_onehot = np.eye(num_classes, dtype=np.float32)[y]   # (n, C)

# Shuffle dataset in sync
idx = np.random.permutation(len(X))
X, y = X[idx], y[idx]

# Train/val split
split = int(0.8 * len(X))
X_train, X_val = X[:split], X[split:]

# Batch iteration
for i in range(0, len(X_train), batch_size):
    X_batch = X_train[i:i + batch_size]
    y_batch = y_train[i:i + batch_size]
```
