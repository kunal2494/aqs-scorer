import urllib.request

url = "https://www.linkedin.com/in/secchimarco/"
req = urllib.request.Request(
    url,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9'
    }
)
try:
    print("Fetching LinkedIn profile...")
    with urllib.request.urlopen(req, timeout=10) as response:
        html = response.read().decode('utf-8')
        print("Success! Status:", response.status)
        print("HTML length:", len(html))
        # Save a snippet of HTML to inspect
        with open("linkedin_sample.html", "w") as f:
            f.write(html)
        print("Saved to linkedin_sample.html")
except Exception as e:
    print("Error:", e)
