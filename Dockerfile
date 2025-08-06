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
COPY app/requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Stage 3: Final image
FROM python:3.12-slim

WORKDIR /app
COPY --from=backend /app /app
COPY --from=frontend /frontend/build /app/static

RUN pip install "uvicorn[standard]" fastapi

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
