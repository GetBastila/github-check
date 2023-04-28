import requests
import json
import os
import re
from pathlib import Path
import sys

base_url = "https://bastilaapi-production.up.railway.app"


def fetch_patterns():
    response = requests.get(f"{base_url}/api/standard-changes/")
    response.raise_for_status()
    standards = response.json()

    return standards['results']


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

            patterns_in_file = re.findall(pattern['snippet'].encode(), content)
            snippet_instances += len(patterns_in_file)

        # pattern['previous_count']
        # pattern['previous_count']
        pattern_failed = pattern['previous_count'] and (snippet_instances > pattern['previous_count'])
        results.append({
            'id': pattern['id'],
            'previous_count': pattern['previous_count'],
            'count': snippet_instances,
            'is_successful': not pattern_failed,
            'fix_recommendation': pattern['fix_recommendation']
        })

    return results


def post_results(result):
    response = requests.post(
        f"{base_url}/api/check-results/",
        data=json.dumps(result),
        headers={
            'Content-Type': 'application/json'
        }
    )
    response.raise_for_status()
    return response


def create_check():
    response = requests.post(
        f"{base_url}/api/code-checks/",
        data=json.dumps({}),
        headers={
            'Content-Type': 'application/json'
        }
    )
    response.raise_for_status()
    return response.json()


def main():
    print('Starting')

    try:
        check = create_check()
    except Exception as e:
        sys.exit(e)

    print('Done Check')

    try:
        patterns = fetch_patterns()
    except Exception as e:
        sys.exit(e)

    print('Patterns fetched')
    print(patterns)

    try:
        results = search_files(patterns)
    except Exception as e:
        sys.exit(e)

    print('Code Searched')

    result = {
        "check": check["id"],
        "results": results
    }
    try:
        post_results(result)
    except Exception as e:
        sys.exit(e)

    print('Results Saved')

    is_regression = False
    for result in results:
        if not result['is_successful']:
            print(result['fix_recommendation'])
            is_regression = True

    if is_regression:
        sys.exit(1)


if __name__ == "__main__":
    main()
