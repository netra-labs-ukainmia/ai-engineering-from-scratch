from datasets import load_dataset
from pyarrow.dataset import ParquetFragmentScanOptions

dataset = load_dataset(
    "wikimedia/wikipedia",
    "20231101.en",
    split="train",
    streaming=True,
    fragment_scan_options=ParquetFragmentScanOptions(pre_buffer=False),
)

iterator = iter(dataset)

try:
    for i in range(5):
        example = next(iterator)
        print(example["title"])
finally:
    iterator.close()

print("Stream closed")