FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the Render port
EXPOSE 8501

# Run the main Streamlit app
CMD ["streamlit", "run", "frontend/streamlit_main.py", "--server.port", "$PORT", "--server.address", "0.0.0.0"]
