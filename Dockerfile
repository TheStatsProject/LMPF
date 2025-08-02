FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy the CONTENTS of app/ into /app/
COPY app/ ./
COPY pyproject.toml .
COPY README.rst .

# Debug: List files and show the __init__.py before Flit install
RUN ls -l /app
RUN cat /app/__init__.py

RUN python -m pip install --no-cache-dir --upgrade pip flit

RUN FLIT_ROOT_INSTALL=1 flit install --deps production --symlink

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
