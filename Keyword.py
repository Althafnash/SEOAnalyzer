import requests
from bs4 import BeautifulSoup
import re

def google_suggestions(keyword):
    url = "https://suggestqueries.google.com/complete/search"
    params = {
        "client": "firefox",
        "q": keyword
    }
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        try:
            suggestions = response.json()[1]
            return suggestions
        except Exception:
            return []
    else:
        return []

def get_result_count(keyword):
    url = f"https://www.google.com/search"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9"
    }
    params = {"q": keyword}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return "Blocked or Failed"

    soup = BeautifulSoup(response.text, 'html.parser')
    result_stats = soup.find("div", id="result-stats")

    if not result_stats:
        return "No data"

    match = re.search(r'About ([\d,]+) results', result_stats.text)
    if match:
        return match.group(1)
    else:
        return "Not Found"

# keyword = input("Enter the keyword: ").strip()
# suggestions = google_suggestions(keyword)
# results_count = get_result_count(keyword)

# print(f"\nKeyword Suggestions for '{keyword}':")
# for s in suggestions:
#     print(f"- {s}")

# print(f"\nSearch Results Count for '{keyword}': {results_count}")
