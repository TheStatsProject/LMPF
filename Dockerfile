FROM python:3.12-slim

# Set environment for reliability and performance
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

WORKDIR /app

# Install system build dependencies and clean up
RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential \
  && rm -rf /var/lib/apt/lists/*

# Copy only necessary files for the main app
COPY ./app ./app
COPY pyproject.toml .
COPY README.rst .

# Diagnostics: show files for debugging (optional)
RUN ls -l /app && ls -l /app/app && cat /app/pyproject.toml

# Install pip and flit
RUN python -m pip install --no-cache-dir --upgrade pip flit

# Install your package and dependencies using flit (production only)
RUN FLIT_ROOT_INSTALL=1 flit install --deps production --symlink

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
