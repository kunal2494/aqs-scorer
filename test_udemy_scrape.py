import urllib.request
import re

url = "https://www.udemy.com/user/hemang-doshi/"
req = urllib.request.Request(
    url,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9'
    }
)
try:
    print("Fetching Udemy profile...")
    with urllib.request.urlopen(req, timeout=10) as response:
        html = response.read().decode('utf-8')
        print("Success! HTML Length:", len(html))
        # Look for student counts
        matches = list(re.finditer(r'student', html, re.IGNORECASE))
        print(f"Found {len(matches)} matches for 'student'")
        for m in matches[:10]:
            start = max(0, m.start() - 100)
            end = min(len(html), m.end() + 100)
            print(f"Context: {html[start:end]}\n")
except Exception as e:
    print("Error:", e)
