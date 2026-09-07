import pandas as pd

csv = pd.read_csv("format-output/imdb_train.csv")
json = pd.read_json("format-output/imdb_train.json", lines=True)
parquet = pd.read_parquet("format-output/imdb_train.parquet")

assert len(csv) == len(json) == len(parquet) == 25_000
assert csv["text"].tolist() == json["text"].tolist() == parquet["text"].tolist()
assert csv["label"].tolist() == json["label"].tolist() == parquet["label"].tolist()

print("All three formats preserve the same 25,000 reviews and labels.")