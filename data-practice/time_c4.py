from time import perf_counter
from datasets import load_dataset

dataset = load_dataset(
    "allenai/c4", "en", split="train", streaming=True
)

count = 0
start = perf_counter()

for example in dataset:
    if perf_counter() - start >= 10:
        break
    count += 1

elapsed = perf_counter() - start
print(f"Examples received within 10 seconds: {count}")
print(f"Actual elapsed time: {elapsed:.2f} seconds")