import requests
import os

def get_data():
    github_pat = os.environ["GITHUB_PAT"]
    branch = os.environ["COMPARE_BRANCH"]
    owner = os.environ["REPO_OWNER"]
    repo = os.environ["REPO_NAME"]

    try:
        response = requests.post(
            "https://bastilaapi-production.up.railway.app/api/github-check/",
            headers={
                "Content-Type": "application/json",
            },
            data={
                'pat': github_pat,
                'repo': repo,
                'owner': owner,
                'branch': branch
            }
        )

        response.raise_for_status()  # Raise an exception if the response contains an HTTP error status code
    except requests.exceptions.RequestException as e:
        sys.exit(f"Error: {str(e)}")


if __name__ == "__main__":
    data = get_data()



