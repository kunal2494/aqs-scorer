import urllib.request
import re

url = "https://github.com/marcosecchi"
req = urllib.request.Request(
    url,
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36'}
)
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        print("HTML length:", len(html))
        # Search for 'followers' and 'following'
        matches = list(re.finditer(r'follower', html, re.IGNORECASE))
        print(f"Found {len(matches)} matches for 'follower'")
        for m in matches[:5]:
            start = max(0, m.start() - 100)
            end = min(len(html), m.end() + 100)
            print(f"Context: {html[start:end]}\n")
except Exception as e:
    print("Error:", e)
