# Dockerfile
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy project files
COPY . .
COPY data/ data/


# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose both APIs
EXPOSE 8001
EXPOSE 8501

# Start both FastAPI and Streamlit (optional for local)
CMD ["bash", "-c", "uvicorn api.app:app --host 0.0.0.0 --port 8001 & streamlit run streamlit_app.py --server.port 8501"]
