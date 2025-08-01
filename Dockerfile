FROM python:3.12-slim

# Set working directory in the container
WORKDIR /app

# Install build tools (optional, for some Python packages)
RUN apt-get update && apt-get install -y build-essential

# Copy all project files and folders (including app/, pyproject.toml, requirements.txt, .env, docs/, etc.)
COPY . /app

# Install flit (build system)
RUN pip install --upgrade pip flit

# Install your package and dependencies, using flit (from pyproject.toml at /app)
RUN flit install --deps production --symlink

# Expose the port your FastAPI app will run on
EXPOSE 8000

# Start FastAPI using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
