# Stage 1: Build React frontend
FROM node:20-alpine as frontend

WORKDIR /frontend
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Stage 2: Build Python backend
FROM python:3.12-slim as backend

WORKDIR /app
COPY app/ ./

# Install Python dependencies

COPY app/requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Stage 3: Final image with frontend and backend
FROM python:3.12-slim

# Copy backend from previous stage
WORKDIR /app
COPY --from=backend /app /app

# Copy built frontend from frontend build
COPY --from=frontend /frontend/build /app/static

# Install a minimal static server for the frontend, e.g. 'pip install fastapi staticfiles'
RUN pip install "uvicorn[standard]" fastapi

# Expose port (adjust as needed)
EXPOSE 8000

# Start FastAPI app (serving static files from /app/static)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
