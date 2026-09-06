FROM python:3.12-slim

WORKDIR /app

RUN python -m pip install --no-cache-dir numpy
CMD ["python", "-c", "import numpy as np; print(np.array([1, 2, 3]) * 2)"]