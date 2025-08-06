FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY app/requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./

EXPOSE 8000

# Start FastAPI (adjust main:app if needed)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
