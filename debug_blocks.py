import urllib.request
import urllib.parse
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote('Greg Lim Packt books')}"
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        
        matches = list(re.finditer(r'<div class="[^"]*result[^"]*"', html))
        if matches:
            print(f"Found {len(matches)} results. Printing first result snippet:")
            print(html[matches[0].start():matches[0].start() + 1500])
        else:
            print("No matches for result div found.")
except Exception as e:
    print("Error:", e)
