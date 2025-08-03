# ---- Build stage ----
FROM python:3.12-slim AS build

WORKDIR /app

# Copy metadata and app code
COPY pyproject.toml .
COPY README.rst .
COPY app/ ./app/
# Optionally copy railway.toml if you have one, but it's not required for Flit
# COPY railway.toml .

# Install pip and flit
RUN python -m pip install --no-cache-dir --upgrade pip flit

# Debug: show what got copied (can comment out for production)
RUN echo "---- /app ----" && ls -l /app
RUN echo "---- /app/app ----" && ls -l /app/app
RUN echo "---- /app/app/__init__.py ----" && cat /app/app/__init__.py
RUN echo "---- /app/pyproject.toml ----" && cat /app/pyproject.toml
RUN echo "---- /app/README.rst ----" && cat /app/README.rst

# Install project dependencies into a virtual environment (symlink keeps edits live, optional)
RUN FLIT_ROOT_INSTALL=1 flit install --deps production --symlink || (echo "------ FLIT INSTALL ERROR ------" && false)

# ---- Production stage ----
FROM python:3.12-slim

WORKDIR /app

# Copy installed packages from build stage (optional for smaller images)
COPY --from=build /usr/local/lib/python3.12 /usr/local/lib/python3.12
COPY --from=build /usr/local/bin /usr/local/bin

# Copy app source (for symlink installs)
COPY app/ ./app/

# Copy entrypoint files
COPY --from=build /app/pyproject.toml .
COPY --from=build /app/README.rst .

# Expose FastAPI port
EXPOSE 8080

# Launch with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
