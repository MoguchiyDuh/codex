import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
N = 200
df = pd.DataFrame(
    {
        "name": rng.choice(["Alice", "Bob", "Carol", "Dave"], N),
        "dept": rng.choice(["Eng", "Sales", "HR", "Finance"], N),
        "age": rng.integers(22, 55, N),
        "salary": rng.integers(40000, 120000, N).astype(float),
        "joined": pd.date_range("2015-01-01", periods=N, freq="W"),
        "score": rng.uniform(50, 100, N),
    }
)
# inject some NaNs
df.loc[rng.choice(N, 15, replace=False), "salary"] = np.nan
df.loc[rng.choice(N, 10, replace=False), "score"] = np.nan
