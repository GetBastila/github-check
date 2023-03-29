import requests

def get_data():
    try:
        response = requests.get(
            "https://bastilaapi-production.up.railway.app/api/standard-change/",
            headers={
                "Authorization": "",
                "Content-Type": "application/json",
            }
        )

        # Raise an exception if the response contains an HTTP error status code
        response.raise_for_status()

    except requests.exceptions.HTTPError as e:
        print(f"An HTTP error occurred: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"A request error occurred: {e}")
        return None
    else:
        return response.json()

if __name__ == "__main__":
    data = get_data()

    if data is not None:
        print("Data retrieved from the API:")
        print(data)
    else:
        print("Failed to retrieve data from the API.")

