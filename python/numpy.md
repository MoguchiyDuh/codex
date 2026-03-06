# NumPy

## Import

```python
import numpy as np
```

---

## Array Creation

```python
np.array([1, 2, 3])              # from list
np.zeros((3, 4))                 # float64 zeros
np.ones((2, 3), dtype=np.int32)
np.full((3, 3), 7)
np.eye(4)                        # identity
np.arange(0, 10, 2)             # like range()
np.linspace(0, 1, 50)           # evenly spaced
np.random.rand(3, 4)            # uniform [0,1)
np.random.randn(3, 4)           # standard normal
np.random.randint(0, 10, (3,4))
np.empty((3, 3))                 # uninitialized (fast)
```

---

## Data Types

```python
# Integers
np.int8, np.int16, np.int32, np.int64
np.uint8, np.uint16, np.uint32, np.uint64

# Floats
np.float16, np.float32, np.float64

# Other
np.complex64, np.complex128
np.bool_
np.str_, np.bytes_, np.object_
np.datetime64, np.timedelta64

arr.dtype                        # check dtype
arr.astype(np.float32)          # cast (returns copy)
```

---

## Shape & Indexing

```python
arr.shape                        # (rows, cols, ...)
arr.ndim                         # number of dims
arr.size                         # total elements
arr.reshape(2, 6)               # new shape, same data
arr.ravel()                      # flatten to 1D (view if possible)
arr.flatten()                    # flatten (always copy)
arr.T                            # transpose

# Indexing
arr[0]                           # first row
arr[0, 2]                        # row 0, col 2
arr[:, 1]                        # all rows, col 1
arr[1:3, 0:2]                   # slicing
arr[[0, 2], :]                  # fancy indexing (copy)
arr[arr > 5]                    # boolean mask

# np.newaxis / expand_dims
arr[:, np.newaxis]              # (n,) -> (n, 1)
np.expand_dims(arr, axis=0)
```

---

## Vectorized Ops

```python
a + b                            # elementwise (no loop needed)
a * b
a ** 2
np.sqrt(a)
np.exp(a)
np.log(a)
np.abs(a)
np.sin(a), np.cos(a)

# Comparison -> bool array
a > 3
np.where(a > 3, a, 0)          # conditional select
```

---

## Broadcasting

Rules: dims are compared right-to-left; a dim of 1 stretches to match.

```python
# (3, 4) + (4,)   -> (3, 4)   OK
# (3, 1) + (1, 4) -> (3, 4)   OK
# (3, 4) + (3,)   -> ERROR

a = np.ones((3, 4))
b = np.array([1, 2, 3, 4])     # (4,) broadcasts over rows
a + b
```

---

## Aggregations

```python
arr.sum()
arr.sum(axis=0)                  # column sums
arr.sum(axis=1)                  # row sums
arr.mean(), arr.std(), arr.var()
arr.min(), arr.max()
arr.argmin(), arr.argmax()       # index of min/max
np.cumsum(arr)
np.sort(arr, axis=-1)
np.argsort(arr)
np.unique(arr)
np.percentile(arr, 75)
```

---

## Linear Algebra

```python
np.dot(a, b)                     # dot product / matmul for 1D
a @ b                            # matmul (preferred)
np.linalg.inv(a)                # inverse
np.linalg.det(a)                # determinant
np.linalg.norm(a)               # L2 norm
np.linalg.eig(a)                # eigenvalues/vectors
np.linalg.solve(A, b)          # solve Ax = b
U, S, Vh = np.linalg.svd(a)   # SVD
```

---

## Views vs Copies

```python
# Slices are VIEWS — modifying changes original
b = a[1:3]
b[0] = 99                        # a is modified

# Fancy indexing returns COPY
b = a[[0, 1]]
b[0] = 99                        # a is NOT modified

a.copy()                         # explicit copy
np.shares_memory(a, b)         # check if sharing
```

---

## Stacking & Splitting

```python
np.concatenate([a, b], axis=0)
np.vstack([a, b])               # vertical (row-wise)
np.hstack([a, b])               # horizontal (col-wise)
np.stack([a, b], axis=0)       # new axis

np.split(arr, 3, axis=0)
np.vsplit(arr, 3)
np.hsplit(arr, 3)
```

---

## I/O

```python
np.save("arr.npy", arr)
arr = np.load("arr.npy")

np.savetxt("arr.csv", arr, delimiter=",")
arr = np.loadtxt("arr.csv", delimiter=",")

np.savez("multi.npz", a=arr1, b=arr2)
data = np.load("multi.npz")
data["a"], data["b"]
```

---

## Performance

```python
# Bad — Python loop
result = [x**2 for x in arr]

# Good — vectorized
result = arr ** 2

# Use float32 over float64 when precision allows (2x memory, faster on GPU)
arr = arr.astype(np.float32)

# Avoid unnecessary copies — prefer in-place ops
arr += 1                         # in-place
arr = arr + 1                   # copy

# Contiguous memory matters for cache
arr = np.ascontiguousarray(arr)
arr.flags['C_CONTIGUOUS']
```
