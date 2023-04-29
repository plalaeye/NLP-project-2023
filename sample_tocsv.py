import pandas as pd

df = pd.read_csv('./data/train.csv')

df = df[df["label"] == 0]

df.sample(frac=0)

df = df[117:130]

df.to_csv('./data/sample_train.csv', index=False)