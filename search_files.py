import requests
import json
import os
import re
from pathlib import Path
import sys

snippets_url = "https://9970-2001-569-7ed1-e000-c7a1-5b1-7f8d-9677.ngrok.io/api/snippets/"
checks_url = "https://bastilaapi-production.up.railway.app/api/checks/"


def fetch_patterns(url):
    response = requests.get(url)
    response.raise_for_status()
    snippets = response.json()

    print(snippets)

    return snippets['results']


def search_files(patterns):
    results = []

    # Loop over every pattern
    for pattern in patterns:
        # Loop over every file
        snippet_instances = 0
        for path in Path('.').glob('**/*'):
            if path.is_dir():
                continue

            with open(path, 'rb') as f:
                content = f.read()

            snippet_instances += re.findall(pattern['old_snippet'].encode(), content)

        pattern_failed = pattern['previous_count'] and (snippet_instances > pattern['previous_count'])
        results.append({
            'id': pattern['id'],
            'previous_count': pattern['previous_count'],
            'count': snippet_instances,
            'is_successful': not pattern_failed
        })

    return results


def post_results(result):
    esponse = requests.post(
        "https://bastilaapi-production.up.railway.app/api/results/",
        data=json.dumps(result),
        headers={
            'Content-Type': 'application/json'
        }
    )
    response.raise_for_status()
    return response


def create_check():
    response = requests.post(
        "https://bastilaapi-production.up.railway.app/api/checks/",
        data=json.dumps({}),
        headers={
            'Content-Type': 'application/json'
        }
    )
    response.raise_for_status()
    return response


def main():
    try:
        check = create_check()
    except Exception as e:
        sys.exit(1)

    try:
        patterns = fetch_patterns(snippets_url)
    except Exception as e:
        sys.exit(1)

    try:
        results = search_files(patterns)
    except Exception as e:
        sys.exit(1)

    result = {
        "check": check["id"]
        "results": results
    }
    try:
        post_results(result)
    except Exception as e:
        sys.exit(1)

    failures = [r for r in results if not r['is_successful']]
    if len(failures) > 1:
        sys.exit(1)


if __name__ == "__main__":
    main()
