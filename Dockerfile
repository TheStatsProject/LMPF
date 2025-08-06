FROM python:3.12-slim

WORKDIR /app

# Install system dependencies (curl for healthcheck)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Copy only pyproject.toml first to leverage Docker cache for dependencies
COPY app/pyproject.toml ./

# Upgrade pip, install Flit, and install only production dependencies
RUN pip install --no-cache-dir --upgrade pip && pip install flit && flit install --deps production

# Copy the rest of the application code
COPY app/ ./app/

# Expose the port expected by Railway
EXPOSE 8080



# Start FastAPI app with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
