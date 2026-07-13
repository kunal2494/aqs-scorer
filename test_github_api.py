import urllib.request
import json

url = "https://api.github.com/users/GameDevJourney101"
req = urllib.request.Request(
    url,
    headers={'User-Agent': 'Mozilla/5.0'}
)
try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode('utf-8'))
        print("GitHub Username:", data.get("login"))
        print("GitHub Followers:", data.get("followers"))
        print("GitHub Public Repos:", data.get("public_repos"))
except Exception as e:
    print("Error:", e)
