#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

# Start FastAPI in the background, but keep logs
echo "Starting FastAPI on port 8000..."
uvicorn src.api:app --host 0.0.0.0 --port 8000 &  # Runs FastAPI in background (&)

# Start Streamlit in foreground so container doesn't exit
echo "Starting Streamlit on port 8501..."
exec streamlit run frontend/home.py --server.port 8501 --server.address 0.0.0.0
