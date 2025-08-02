FROM python:3.12-slim

# Set environment for reliability and performance
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

WORKDIR /app

# Install system build dependencies and clean up apt artifacts
RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential \
  && rm -rf /var/lib/apt/lists/*

# Copy only necessary files for the main app
COPY ./app ./app
COPY pyproject.toml .
COPY README.md .

# Diagnostics: show files for debugging (optional, remove if you like)
RUN echo "--- ROOT DIR ---" && ls -l /app && echo "--- APP DIR ---" && ls -l /app/app

# Install pip and flit
RUN python -m pip install --no-cache-dir --upgrade pip flit

# Install your package and dependencies using flit (production only)
RUN FLIT_ROOT_INSTALL=1 flit install --deps production --symlink

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
