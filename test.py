import pandas as pd

data = [
    ["1", "2"],
    ["2", "1"],
    ["3", "2"]
]

df = pd.DataFrame(data, columns=["data", "weight"], dtype=float)

somme = df["weight"].sum()
moyenne = (df["data"]*df["weight"]).sum() / somme
mode = df["data"][df["weight"].idxmax()]
df["cumsum"] = df["weight"].cumsum()
Q1 = df["data"][df["cumsum"] >= (somme*0.25)].iloc[0]
Q2 = df["data"][df["cumsum"] >= (somme*0.50)].iloc[0]
Q3 = df["data"][df["cumsum"] >= (somme*0.75)].iloc[0]