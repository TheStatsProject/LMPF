FROM python:3.12-slim

WORKDIR /app

# Install system dependencies (e.g., curl for healthcheck)
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

# Copy only pyproject.toml and requirements.txt for dependency caching
COPY app/pyproject.toml ./app/requirements.txt ./

# Upgrade pip, install flit, and install only production dependencies
RUN pip install --no-cache-dir --upgrade pip && pip install flit && flit install --deps production

# Copy the whole backend application (app), including templates and routes
COPY app/ ./app/

# Optionally, copy docs if you want them served or built-in (remove if not needed)
# COPY docs/ ./docs/

# Expose the port expected by Railway/platform
EXPOSE 8080


# Start FastAPI app with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
