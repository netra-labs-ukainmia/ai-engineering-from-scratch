# Wikipedia streaming compatibility test

2026-09-07: the original `stream_wikipedia.py` prints five titles, then crashes
during Python shutdown in `ai-dev-cpu` (Python 3.12.14, datasets 5.0.1,
PyArrow 25.0.1). The original script and image are preserved.

## Findings

- The same failure occurs in an isolated environment without PyTorch.
- Disabling Parquet pre-buffering, closing the Python iterator, and testing
  PyArrow 24.0.0 did not resolve it.
- A diagnostic, in-memory change to disable Arrow scanner worker threads
  exited successfully. No installed library files were patched.
- A compatibility environment using datasets 3.1.0 and PyArrow 25.0.1 also
  exited successfully. This changes transitive dependencies too, so it does
  not isolate a single upstream defective version or prove a universal fix.
- `course-data-streaming` was built with `Dockerfile.streaming`; the saved
  `stream_wikipedia_compat.py` streams five titles without shutdown overrides.
- Its dependency check (`python -m pip check`) passed.

This is a scoped course workaround, not a recommendation to downgrade other
projects. Package pins cover the three direct packages, not every transitive
dependency. The Wikipedia configuration is `20231101.en`; the lesson's
`20220301.en` is unavailable for this dataset.

## Run from this folder (PowerShell)

```powershell
docker build -t course-data-streaming -f Dockerfile.streaming .
docker run --rm --mount "type=bind,source=$($PWD.Path),target=/workspace,readonly" --mount "type=volume,source=course-hf-cache,target=/root/.cache/huggingface" course-data-streaming
$LASTEXITCODE
```

Expected titles: Anarchism, Albedo, A, Alabama, Achilles. Expected exit code: 0.
The cache persists in the existing named volume. No course files are copied
into the image; the script is supplied by the read-only bind mount.
