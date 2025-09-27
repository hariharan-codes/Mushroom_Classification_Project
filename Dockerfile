# Base image
FROM python:3.12-slim

# Set workdir
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make start.sh executable
RUN chmod +x start.sh

# Expose ports
EXPOSE 8000 8501

# Start both apps
CMD ["./start.sh"]
