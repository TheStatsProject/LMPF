FROM python:3.12-slim

WORKDIR /app

# Install system dependencies (curl for healthcheck, optional)
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt first for dependency caching
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code (everything from app/) into the container workdir
COPY app/ ./

# Expose the port expected by Railway or your PaaS
EXPOSE 8080

# Start FastAPI app with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
