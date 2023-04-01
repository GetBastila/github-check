import os
import re
import sys

search_pattern = os.environ.get("SEARCH_PATTERN", None)
if not search_pattern:
    sys.exit("SEARCH_PATTERN not provided")

results = []
for root, _, files in os.walk("."):
    for file in files:
        file_path = os.path.join(root, file)
        with open(file_path, "r", errors="ignore") as f:
            content = f.read()
            if re.search(search_pattern, content, re.IGNORECASE):
                results.append(file_path)

with open("search-results.txt", "w") as f:
    for result in results:
        f.write(f"{result}\n")

if results:
    print("Search results saved to search-results.txt")
else:
    print("No matches found")
