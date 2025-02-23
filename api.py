from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
import time
import random
import os
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response  # For /metrics endpoint

app = FastAPI()

# Prometheus Metrics using Histogram (for min/max/average)
REQUEST_COUNT = Counter("request_count", "Total number of requests received", ["endpoint"])
ERROR_COUNT = Counter("error_count", "Total number of errors occurred", ["endpoint"])  
REQUEST_LATENCY = Histogram("request_latency_seconds", "Latency of requests in seconds", ["endpoint"])

# File Path
FILE_PATH = "employees.txt"

# Generate a dummy file if it doesn't exist
if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w") as f:
        f.write("This is an example file for download.")

@app.get("/health", summary="Health Check API")
def health_check():
    """Returns the health status of the application with a random delay."""
    REQUEST_COUNT.labels(endpoint="/health").inc()
    start_time = time.time()
    delay = random.uniform(0.1, 2.0)
    time.sleep(delay)
    duration = time.time() - start_time

    # Simulating an error condition randomly for demonstration
    if random.random() < 0.1:  # 10% chance of error
        ERROR_COUNT.labels(endpoint="/health").inc()
        raise HTTPException(status_code=500, detail="Simulated error in health check.")

    REQUEST_LATENCY.labels(endpoint="/health").observe(duration)
    return {"status": "healthy", "response_time": f"{duration:.2f} seconds"}

@app.get("/download", summary="File Download API")
def download_file():
    """Allows the user to download a file with a random delay."""
    REQUEST_COUNT.labels(endpoint="/download").inc()
    start_time = time.time()
    delay = random.uniform(0.1, 2.0)
    time.sleep(delay)
    duration = time.time() - start_time

    # Simulating an error condition randomly for demonstration
    if random.random() < 0.1:  # 10% chance of error
        ERROR_COUNT.labels(endpoint="/download").inc()
        raise HTTPException(status_code=500, detail="Simulated error during file download.")

    REQUEST_LATENCY.labels(endpoint="/download").observe(duration)
    return FileResponse(FILE_PATH, media_type="application/octet-stream", filename="employees.txt")

@app.get("/metrics", summary="Prometheus Metrics")
def metrics():
    """Expose Prometheus metrics."""
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/", summary="API Info")
def api_info():
    """Returns information about the available endpoints."""
    return JSONResponse({
        "endpoints": {
            "/health": "Check the health of the application.",
            "/download": "Download the example file.",
            "/metrics": "Expose Prometheus metrics."
        }
    })
