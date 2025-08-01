FROM python:3.12-slim

WORKDIR /app

# Install build tools (optional)
RUN apt-get update && apt-get install -y build-essential

# Copy your project files (app/, pyproject.toml, etc.)
COPY . /app

# Install flit
RUN pip install --upgrade pip flit

# Install your package and dependencies using flit and allow root install
RUN FLIT_ROOT_INSTALL=1 flit install --deps production --symlink

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
