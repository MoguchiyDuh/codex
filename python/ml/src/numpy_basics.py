# NumPy — core patterns and ML-relevant usage
# See: ../notes/numpy.md

import numpy as np

# ── Array Creation ────────────────────────────────────────────────────────────

a = np.array([1, 2, 3, 4, 5], dtype=np.float32)
b = np.zeros((3, 4))
c = np.ones((2, 3), dtype=np.int32)
d = np.arange(0, 10, 2)  # [0 2 4 6 8]
e = np.linspace(0, 1, 5)  # [0. .25 .5 .75 1.]
f = np.random.randn(4, 4)  # standard normal


# ── Shape & Reshaping ────────────────────────────────────────────────────────

arr = np.arange(24)
print(arr.shape)  # (24,)
arr2d = arr.reshape(4, 6)
print(arr2d.shape)  # (4, 6)

col = arr[:8].reshape(-1, 1)  # (8, 1) — column vector
row = arr[:8].reshape(1, -1)  # (1, 8) — row vector

arr3d = arr.reshape(2, 3, 4)
print(arr3d.shape)  # (2, 3, 4)

flat = arr3d.ravel()  # view if contiguous
flat2 = arr3d.flatten()  # always copy


# ── Indexing ──────────────────────────────────────────────────────────────────

m = np.arange(12).reshape(3, 4)

print(m[0])  # first row
print(m[0, 2])  # element at (0, 2)
print(m[:, 1])  # column 1
print(m[1:3, 0:2])  # submatrix — VIEW

# Fancy indexing (COPY)
rows = m[[0, 2], :]
print(rows)

# Boolean mask (COPY)
mask = m > 5
print(m[mask])  # 1D array of elements > 5
m[m < 3] = 0  # in-place masked assignment

# np.where
result = np.where(m > 6, m, -1)  # keep values > 6, else -1


# ── Broadcasting ──────────────────────────────────────────────────────────────

a = np.ones((3, 4))
b = np.array([1, 2, 3, 4])  # (4,) → broadcasts to (3, 4)
print(a + b)

# Subtract row mean — keepdims prevents shape mismatch
row_means = a.mean(axis=1, keepdims=True)  # (3, 1)
centered = a - row_means  # (3, 4) - (3, 1) → (3, 4)


# ── Vectorized Ops ────────────────────────────────────────────────────────────

x = np.array([1.0, 4.0, 9.0, 16.0])
print(np.sqrt(x))  # [1. 2. 3. 4.]
print(np.log(x))
print(np.clip(x, 2, 10))  # [2. 4. 9. 10.]

# Avoid Python loops
arr = np.random.randn(100_000)
result = arr**2 + 2 * arr + 1  # vectorized — fast
# result = np.array([(x**2 + 2*x + 1) for x in arr])  # slow


# ── Aggregations ──────────────────────────────────────────────────────────────

m = np.random.randint(0, 100, (5, 4))
print(m.sum())  # total
print(m.sum(axis=0))  # column sums — shape (4,)
print(m.sum(axis=1))  # row sums — shape (5,)
print(m.sum(axis=1, keepdims=True))  # shape (5, 1)
print(m.argmax(axis=1))  # col index of max in each row
print(np.percentile(m, [25, 50, 75]))


# ── Linear Algebra ───────────────────────────────────────────────────────────

A = np.random.randn(3, 3)
b = np.array([1.0, 2.0, 3.0])

print(A @ A.T)  # matmul
print(np.linalg.det(A))
print(np.linalg.norm(b))  # L2 norm = sqrt(1+4+9)
x = np.linalg.solve(A, b)  # Ax = b
print(np.allclose(A @ x, b))  # True


# ── Views vs Copies ───────────────────────────────────────────────────────────

original = np.arange(6).reshape(2, 3)

view = original[0:1, :]  # slice → view
view[0, 0] = 99
print(original[0, 0])  # 99 — original changed

copy = original[[0], :]  # fancy index → copy
copy[0, 0] = 0
print(original[0, 0])  # 99 — original unchanged

print(np.shares_memory(original, view))  # True
print(np.shares_memory(original, copy))  # False


# ── Common ML Patterns ───────────────────────────────────────────────────────

X = np.random.randn(1000, 20).astype(np.float32)
y = np.random.randint(0, 10, 1000)

# Normalize features
X = (X - X.mean(axis=0)) / X.std(axis=0)

# One-hot encode labels
num_classes = 10
y_onehot = np.eye(num_classes, dtype=np.float32)[y]  # (1000, 10)

# Shuffle in sync
idx = np.random.permutation(len(X))
X, y = X[idx], y[idx]

# Train/val split (80/20)
split = int(0.8 * len(X))
X_train, X_val = X[:split], X[split:]
y_train, y_val = y[:split], y[split:]

print(X_train.shape, X_val.shape)  # (800, 20) (200, 20)

# Batch iteration
batch_size = 32
for i in range(0, len(X_train), batch_size):
    X_batch = X_train[i : i + batch_size]
    y_batch = y_train[i : i + batch_size]
    # ... forward pass ...


if __name__ == "__main__":
    print("shapes:", X_train.shape, y_onehot.shape)
