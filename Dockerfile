FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y gcc && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application code
COPY . .

# Run the application
CMD ["python", "src/main.py"]



# N/B for me: Do not inlude sqlite3 as a db command, it is included with the python image: It is a python standard library.
# Do not use Uvicorn as it is for FastAPI web server APIs only.
