FROM python:3.12-slim

WORKDIR /app

# Copy requirements and install Python dependencies
COPY app/requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Copy the rest of your FastAPI application code
COPY app/ ./app/

# Expose the correct port for Railway
EXPOSE 8080

# Start FastAPI app with Uvicorn, pointing to 'app.main:app' (app/main.py)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
