import urllib.request
import re

url = "https://github.com/GameDevJourney101"
req = urllib.request.Request(
    url,
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36'}
)
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        print("HTML Length:", len(html))
        # Find followers count
        # In GitHub profile HTML: href="https://github.com/GameDevJourney101?tab=followers"
        # Inside the link there is a span with class "text-bold color-fg-default" or similar containing the count
        # Let's search for "followers" link context
        matches = re.findall(r'href="[^"]+\?tab=followers"[^>]*>.*?<span[^>]*>([^<]+)</span>\s*followers', html, re.DOTALL)
        if matches:
            print("Followers:", matches[0].strip())
        else:
            # Try a broader regex
            m = re.search(r'([\d,]+)\s*followers', html, re.IGNORECASE)
            if m:
                print("Followers (fallback):", m.group(1))
            else:
                print("Followers not found.")
except Exception as e:
    print("Error:", e)
