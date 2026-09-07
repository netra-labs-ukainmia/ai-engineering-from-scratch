from datasets import load_dataset

dataset = load_dataset("stanfordnlp/imdb", split="train")

def make_splits():
    first = dataset.train_test_split(test_size=0.30, seed=42)
    remaining = first["test"].train_test_split(test_size=0.50, seed=42)
    return first["train"], remaining["train"], remaining["test"]

train_ds, val_ds, test_ds = make_splits()

print(f"Train: {len(train_ds)}, Val: {len(val_ds)}, Test: {len(test_ds)}")

assert (len(train_ds), len(val_ds), len(test_ds)) == (17500, 3750, 3750)

repeat_train, repeat_val, repeat_test = make_splits()

for original, repeated in zip(
    (train_ds, val_ds, test_ds),
    (repeat_train, repeat_val, repeat_test),
):
    assert original["text"] == repeated["text"]
    assert original["label"] == repeated["label"]

print("All three splits have the expected sizes and reproduce exactly.")