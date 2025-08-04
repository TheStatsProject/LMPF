# ---- Build stage ----
FROM python:3.12-slim AS build

WORKDIR /app

# Copy metadata and app code
COPY pyproject.toml .
COPY README.rst .
COPY app/ ./app/

# Install pip and flit
RUN python -m pip install --no-cache-dir --upgrade pip flit

# Optional: show what got copied (for debugging, comment out in production)
# RUN echo "---- /app ----" && ls -l /app
# RUN echo "---- /app/app ----" && ls -l /app/app
# RUN echo "---- /app/app/__init__.py ----" && cat /app/app/__init__.py
# RUN echo "---- /app/pyproject.toml ----" && cat /app/pyproject.toml
# RUN echo "---- /app/README.rst ----" && cat /app/README.rst

# Install project dependencies into the image
RUN FLIT_ROOT_INSTALL=1 flit install --deps production --symlink || (echo "------ FLIT INSTALL ERROR ------" && false)

# ---- Production stage ----
FROM python:3.12-slim

WORKDIR /app

# Copy installed packages from build stage
COPY --from=build /usr/local/lib/python3.12 /usr/local/lib/python3.12
COPY --from=build /usr/local/bin /usr/local/bin

# Copy app source
COPY app/ ./app/

# Copy entrypoint files
COPY --from=build /app/pyproject.toml .
COPY --from=build /app/README.rst .

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
