import requests

def call_api():
    url = "https://94ce-2001-569-7ed1-e000-f5bb-205c-9c3b-7de.ngrok.io/api/standard-change/"
    response = requests.get(url)

    if response.status_code == 200:
        print("GET request was successful.")
        print("Response data:", response.json())
    else:
        print(f"GET request failed with status code {response.status_code}.")

if __name__ == "__main__":
    call_api()
