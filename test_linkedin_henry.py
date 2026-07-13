import urllib.request

url = "https://www.linkedin.com/in/henrywoo/"
req = urllib.request.Request(
    url,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9'
    }
)
try:
    print("Fetching Henry Woo LinkedIn profile...")
    with urllib.request.urlopen(req, timeout=10) as response:
        html = response.read().decode('utf-8')
        print("Success! Status:", response.status)
        import re
        m = re.search(r'([\d,.]+k?)\s*followers', html, re.IGNORECASE)
        if m:
            print("Followers found:", m.group(1))
        else:
            print("Followers not found in HTML. Saving to henry.html to debug...")
            with open("henry.html", "w") as f:
                f.write(html)
except Exception as e:
    print("Error:", e)
