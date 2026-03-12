import pandas as pd

df = pd.read_csv("C:/Users/anvit/college/experience/cyber_ml_project/data/traffic.csv.csv")

print(df.shape)
print(df.columns)
print(df["Label"].value_counts())
print(df.head())

df = df.dropna()
df["Label"] = df["Label"].apply(lambda x: 0 if x == "BENIGN" else 1)

print(df["Label"].value_counts())

