import re

with open("linkedin_sample.html", "r") as f:
    html = f.read()

print("HTML length:", len(html))

# Let's search for followers and connections in the HTML
matches = list(re.finditer(r'follower', html, re.IGNORECASE))
print(f"Found {len(matches)} matches for 'follower'")
for m in matches[:10]:
    start = max(0, m.start() - 100)
    end = min(len(html), m.end() + 100)
    print(f"Context: {html[start:end]}\n")

matches_conn = list(re.finditer(r'connection', html, re.IGNORECASE))
print(f"Found {len(matches_conn)} matches for 'connection'")
for m in matches_conn[:5]:
    start = max(0, m.start() - 100)
    end = min(len(html), m.end() + 100)
    print(f"Context: {html[start:end]}\n")
