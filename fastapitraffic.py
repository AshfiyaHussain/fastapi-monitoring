import requests
import time
import random

# Define the endpoints
HEALTH_CHECK_URL = "http://localhost:8000/health"  # Change if necessary
DOWNLOAD_URL = "http://localhost:8000/download"  # Change if necessary

# Set the duration for traffic simulation (in seconds)
DURATION = 3600  # 1 hour
END_TIME = time.time() + DURATION

# Initialize counters for successful and error responses
success_count = 0
error_count = 0

while time.time() < END_TIME:
    # Randomly decide to hit health check or download endpoint or introduce an error
    endpoint_choice = random.choice(["health", "download", "error"])

    if endpoint_choice == "health":
        try:
            response = requests.get(HEALTH_CHECK_URL)
            if response.status_code == 200:
                success_count += 1
            else:
                error_count += 1
        except Exception as e:
            error_count += 1
            print(f"Error during request: {e}")

    elif endpoint_choice == "download":
        try:
            response = requests.get(DOWNLOAD_URL)
            if response.status_code == 200:
                success_count += 1
            else:
                error_count += 1
        except Exception as e:
            error_count += 1
            print(f"Error during request: {e}")

    elif endpoint_choice == "error":
        # Simulate an error by hitting an invalid endpoint
        try:
            response = requests.get("http://localhost:8000/invalid-endpoint")  # Change if necessary
            error_count += 1  # Should always return an error
        except Exception as e:
            error_count += 1
            print(f"Error during request: {e}")

    # Wait for a random time between 0.5 to 2 seconds before the next request
    time.sleep(random.uniform(0.5, 2))

# Print the results after the simulation
print(f"Total successful requests: {success_count}")
print(f"Total error responses: {error_count}")

