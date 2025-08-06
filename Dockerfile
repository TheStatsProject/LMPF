# Stage 1: Build React frontend
FROM node:20-alpine as frontend

WORKDIR /frontend
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Stage 2: Build Python backend
FROM python:3.12-slim as backend

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install Python dependencies first for better caching
COPY app/requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend code
COPY app/ ./

# (Optional) Stage 2.5: Build Sphinx docs if needed
# RUN pip install --no-cache-dir sphinx
# COPY docs/ ./docs/
# RUN sphinx-build -b html docs/source docs/build/html

# Stage 3: Final image
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy backend (app code + installed dependencies)
COPY --from=backend /app /app

# Copy built frontend (static files) to backend
COPY --from=frontend /frontend/build /app/static

# (Optional) Copy built docs
# COPY --from=backend /app/docs/build/html /app/docs

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
