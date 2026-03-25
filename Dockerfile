# Use Python 3.12 slim image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copy application files
COPY app.py .
COPY templates/ ./templates/
COPY Syracuse_Permit_Guide_RAG.json .
COPY Syracuse_Permit_Guide_AI_Optimized.md .

# Set environment variables
ENV PORT=8080
ENV PYTHONUNBUFFERED=True

# Run with gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --timeout 0 app:app
