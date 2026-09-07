from datasets import load_dataset

dataset = load_dataset("nyu-mll/glue", "mrpc", split="train")

print(dataset.features)

for example in dataset.select(range(5)):
    print(example)
    print()