FROM python:3.12-slim

WORKDIR /app

# Install system dependencies (curl for healthcheck, optional)
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

# Copy only pyproject.toml for dependency caching
COPY pyproject.toml ./

# Install Flit and your production dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install flit && \
    flit install --deps production

# Copy the backend code (everything from app/) into the container workdir
COPY app/ ./

# Expose the port expected by Railway or your PaaS
EXPOSE 8080

# Optional: Healthcheck (requires you to implement `/health` in FastAPI)
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1

# Start FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
