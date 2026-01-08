# -------------------------------
# Base image
# -------------------------------
FROM python:3.12-slim

# -------------------------------
# Environment variables
# -------------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# -------------------------------
# Set working directory
# -------------------------------
WORKDIR /app

# -------------------------------
# System dependencies (optional but recommended)
# -------------------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# -------------------------------
# Copy requirements first (cache optimization)
# -------------------------------
COPY requirements.txt .

# -------------------------------
# Install Python dependencies
# -------------------------------
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install "pydantic[email]"

# -------------------------------
# Copy application code
# -------------------------------
COPY . .

# -------------------------------
# Expose FastAPI port
# -------------------------------
EXPOSE 8000

# -------------------------------
# Start FastAPI app
# -------------------------------
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
