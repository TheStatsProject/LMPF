FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install build dependencies and cleanup in one layer
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential gcc \
    && pip install --no-cache-dir --upgrade pip flit \
    && rm -rf /var/lib/apt/lists/*

# Copy source code and metadata
COPY app/ ./
COPY pyproject.toml .
COPY README.rst .

# Debug: List files and show the __init__.py before Flit install
RUN ls -l /app && cat /app/__init__.py

# Install Python package and dependencies using Flit
RUN FLIT_ROOT_INSTALL=1 flit install --deps production --symlink

EXPOSE 8080

# Optional: Healthcheck for FastAPI/Uvicorn
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl --fail http://localhost:8080/docs || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

# --- Optional: If you want a minimal runtime image, use multi-stage builds
# FROM python:3.12-slim as runtime
# WORKDIR /app
# COPY --from=0 /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
# COPY app/ ./
# EXPOSE 8080
# HEALTHCHECK ... (same as above)
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
