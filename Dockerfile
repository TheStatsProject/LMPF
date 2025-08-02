FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy the CONTENTS of app/ into /app/ (not to /app/app!)
COPY app/ ./
COPY pyproject.toml .
COPY README.rst .

RUN ls -l /app

RUN python -m pip install --no-cache-dir --upgrade pip flit

RUN FLIT_ROOT_INSTALL=1 flit install --deps production --symlink

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
