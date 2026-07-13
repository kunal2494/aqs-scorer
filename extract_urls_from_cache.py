import json
import re
import os

CACHE_FILE = "/Users/fincent/.gemini/antigravity/scratch/aqs-scorer/search_cache.json"

if not os.path.exists(CACHE_FILE):
    print("Search cache does not exist!")
    exit(1)

with open(CACHE_FILE, 'r') as f:
    cache = json.load(f)

# Group queries by author name
# Queries are like: '"Robert Henning" Packt book OR course', '"Robert Henning" linkedin github'
authors = {}
for query, results in cache.items():
    if not results:
        continue
    # Extract author name from query
    m = re.match(r'^"(.*?)"', query)
    if m:
        name = m.group(1)
        if name not in authors:
            authors[name] = []
        authors[name].extend(results)

print("=== RESOLVED SOCIAL URLS FROM CACHED GOOGLE SEARCHES ===")
for name, results in authors.items():
    linkedin_url = None
    github_url = None
    
    for r in results:
        url = r['url']
        if "linkedin.com/in/" in url and not linkedin_url:
            linkedin_url = url
        if "github.com/" in url and not github_url and not any(w in url for w in ["/features", "/pricing", "/trending", "/search"]):
            # Clean github url to base profile
            m_gh = re.match(r'https?://github\.com/([^/]+)', url)
            if m_gh:
                github_url = f"https://github.com/{m_gh.group(1)}"
                
    print(f"\nAuthor: {name}")
    print(f"  LinkedIn: {linkedin_url}")
    print(f"  GitHub: {github_url}")
