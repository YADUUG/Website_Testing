import requests
import time

def measure_response_time(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()

        response_time = end_time - start_time
        return response_time, response.status_code
    except requests.RequestException as e:
        return None, None

if __name__ == "__main__":
    url = "https://www.chaicode.in"  # Replace with the URL of the website you want to test

    response_time, status_code = measure_response_time(url)

    if response_time is not None:
        print(f"Response Time: {response_time:.2f} seconds")
        print(f"HTTP Status Code: {status_code}")
    else:
        print("Error: Failed to make the request")
