from pathlib import Path
from datasets import load_dataset

output = Path("format-output")
output.mkdir(exist_ok=False)

dataset = load_dataset("stanfordnlp/imdb", split="train")

dataset.to_csv(output / "imdb_train.csv")
dataset.to_json(output / "imdb_train.json")
dataset.to_parquet(output / "imdb_train.parquet")

for path in sorted(output.iterdir()):
    print(f"{path.name}: {path.stat().st_size / 1_000_000:.2f} MB")