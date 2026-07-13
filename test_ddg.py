import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import json
import os
import time
import re
import sys

# Define authors list
AUTHORS = [
    "Robert Henning",
    "Glen D. Singh",
    "Mr. Hemang Doshi",
    "Ammar Mohanna",
    "Zonunfeli Ralte",
    "Mr. Abhijit Dey",
    "Mr. Srinivasan Shanmuganathan",
    "Mr. Jaime Buelta",
    "Mr. Dipankar Sarkar",
    "Mr. Steve Miles",
    "Fabio Biondi",
    "Manjunath Gangappa",
    "Rajkumar Rangaraj"
]

CACHE_FILE = "/Users/fincent/.gemini/antigravity/scratch/aqs-scorer/search_cache.json"

def clean_name(name):
    cleaned = re.sub(r'^(Mr\.|Dr\.|Mrs\.|Ms\.)\s+', '', name)
    return cleaned.strip()

def search_ddg(query):
    url = "https://html.duckduckgo.com/html/?" + urllib.parse.urlencode({'q': query})
    req = urllib.request.Request(
        url,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
        }
    )
    try:
        time.sleep(2)
        with urllib.request.urlopen(req, timeout=15) as response:
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            results = []
            for result in soup.find_all('div', class_='result'):
                title_a = result.find('a', class_='result__url')
                snippet_div = result.find('a', class_='result__snippet')
                if title_a:
                    title = title_a.get_text(strip=True)
                    href = title_a['href']
                    parsed_url = urllib.parse.urlparse(href)
                    actual_url = href
                    if parsed_url.netloc == 'duckduckgo.com' and parsed_url.path == '/l/':
                        qs = urllib.parse.parse_qs(parsed_url.query)
                        if 'uddg' in qs:
                            actual_url = qs['uddg'][0]
                    snippet = snippet_div.get_text(strip=True) if snippet_div else ""
                    results.append({
                        'title': title,
                        'url': actual_url,
                        'snippet': snippet
                    })
            return results
    except Exception as e:
        print(f"Error searching for query [{query}]: {e}", file=sys.stderr)
        return []

def main():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f:
            try:
                cache = json.load(f)
            except Exception as e:
                print(f"Error loading cache: {e}")
                cache = {}
    else:
        cache = {}

    print(f"Loaded existing cache with {len(cache)} keys.")

    total_queries = 0
    successful_queries = 0

    for author in AUTHORS:
        name = clean_name(author)
        print(f"\nProcessing author: {author} (cleaned: {name})")
        
        q1 = f'"{name}" site:linkedin.com/in'
        print(f"  Searching: {q1}")
        res1 = search_ddg(q1)
        cache[q1] = res1
        print(f"    Found {len(res1)} results.")
        total_queries += 1
        if res1:
            successful_queries += 1
            
        q2 = f'"{name}" site:github.com OR site:udemy.com/user OR site:medium.com'
        print(f"  Searching: {q2}")
        res2 = search_ddg(q2)
        cache[q2] = res2
        print(f"    Found {len(res2)} results.")
        total_queries += 1
        if res2:
            successful_queries += 1

    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f, indent=2)
        
    print("\n==========================================")
    print(f"Search and Cache Update Completed.")
    print(f"Total queries run: {total_queries}")
    print(f"Queries with results: {successful_queries}")
    print(f"Total keys in cache now: {len(cache)}")
    print("==========================================")

if __name__ == '__main__':
    main()
