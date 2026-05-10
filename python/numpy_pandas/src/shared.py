import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
N = 200
df = pd.DataFrame(
    {
        "name": np.random.choice(["Alice", "Bob", "Carol", "Dave"], N),
        "dept": np.random.choice(["Eng", "Sales", "HR", "Finance"], N),
        "age": np.random.randint(22, 55, N),
        "salary": np.random.randint(40000, 120000, N).astype(float),
        "joined": pd.date_range("2015-01-01", periods=N, freq="W"),
        "score": np.random.uniform(50, 100, N),
    }
)
# inject some NaNs
df.loc[np.random.choice(N, 15, replace=False), "salary"] = np.nan
df.loc[np.random.choice(N, 10, replace=False), "score"] = np.nan
