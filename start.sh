#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

# Set default ports if not provided by Render
FASTAPI_PORT=${FASTAPI_PORT:-8000}
STREAMLIT_PORT=${PORT:-8501}  # Render sets $PORT, fallback to 8501 locally

# Start FastAPI in the background
echo "Starting FastAPI on port $FASTAPI_PORT..."
uvicorn src.api:app --host 0.0.0.0 --port $FASTAPI_PORT &

# Start Streamlit in the foreground so the container doesn't exit
echo "Starting Streamlit on port $STREAMLIT_PORT..."
exec streamlit run frontend/home.py --server.port $STREAMLIT_PORT --server.address 0.0.0.0
