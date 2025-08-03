# Use a slim official Python base image
FROM python:3.12-slim

# Set workdir
WORKDIR /app

# Copy only files needed for install first for better caching
COPY pyproject.toml .
COPY README.rst .

# Copy your application code
COPY app/ ./app/

# Install build tools and flit
RUN python -m pip install --no-cache-dir --upgrade pip flit

# Debug: list project root and app dir
RUN echo "---- /app ----" && ls -l /app
RUN echo "---- /app/app ----" && ls -l /app/app
RUN echo "---- /app/app/__init__.py ----" && cat /app/app/__init__.py
RUN echo "---- /app/pyproject.toml ----" && cat /app/pyproject.toml
RUN echo "---- /app/README.rst ----" && cat /app/README.rst

# Flit install (show error log if fails)
RUN FLIT_ROOT_INSTALL=1 flit install --deps production --symlink || (echo "------ FLIT INSTALL ERROR ------" && false)

# Expose port for FastAPI
EXPOSE 8080

# Default command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
