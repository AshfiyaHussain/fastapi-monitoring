# Using a lightweight Python image
FROM python:3.10-slim

# Setting the working directory inside the container
WORKDIR /app

# Copying and installing dependencies first (optimized for caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Now copying the rest of the application files
COPY . .

# Exposing port 8000
EXPOSE 8000

# Runing FastAPI application with Uvicorn
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]