# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app
COPY . .

# Make the start script executable
RUN chmod +x start.sh

# Expose default ports (optional; Render will override with $PORT)
EXPOSE 8501 8000

# Use start.sh to launch FastAPI and Streamlit
CMD ["./start.sh"]
