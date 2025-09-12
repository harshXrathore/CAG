# Use official Python image
FROM python:3.11-slim

# Install dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY . .

# Default entrypoint (CLI mode)
ENTRYPOINT ["python", "-m", "artgen.cli"]
