import json
import re
import os

# Load search cache
CACHE_FILE = "/Users/fincent/.gemini/antigravity/scratch/aqs-scorer/search_cache.json"

if not os.path.exists(CACHE_FILE):
    print("Search cache does not exist!")
    exit(1)

with open(CACHE_FILE, 'r') as f:
    cache = json.load(f)

# Helper to parse numbers like "15.4k", "15,400", "500+"
def parse_number(num_str):
    num_str = num_str.lower().replace(',', '').replace('+', '').strip()
    if 'k' in num_str:
        try:
            return int(float(num_str.replace('k', '').strip()) * 1000)
        except ValueError:
            return 0
    if 'm' in num_str:
        try:
            return int(float(num_str.replace('m', '').strip()) * 1000000)
        except ValueError:
            return 0
    try:
        return int(num_str)
    except ValueError:
        return 0

# Extract metrics from cache for each query
print("=== EXTRACTED REACH METRICS FROM GOOGLE SNIPPETS ===")
for query, results in cache.items():
    if not results:
        continue
    
    # We look for patterns in the snippet or title
    for r in results:
        text = r['title'] + " " + r['snippet']
        
        # 1. LinkedIn Followers / Connections
        # Matches "15,324 followers", "15k followers", "15.4k followers"
        li_followers = re.findall(r'([\d,.]+k?)\s*followers', text, re.IGNORECASE)
        li_connections = re.findall(r'([\d,.]+k?)\s*connections', text, re.IGNORECASE)
        
        # 2. Udemy Students
        ud_students = re.findall(r'([\d,.]+k?)\s*students', text, re.IGNORECASE)
        
        # 3. YouTube subscribers
        yt_subs = re.findall(r'([\d,.]+k?)\s*subscribers', text, re.IGNORECASE)
        
        # 4. GitHub followers (if in snippet)
        gh_followers = re.findall(r'([\d,.]+k?)\s*followers', text, re.IGNORECASE) if 'github' in r['url'] else []
        
        metrics = []
        if li_followers:
            metrics.append(f"LinkedIn Followers: {li_followers[0]} ({parse_number(li_followers[0])})")
        if li_connections:
            metrics.append(f"LinkedIn Connections: {li_connections[0]} ({parse_number(li_connections[0])})")
        if ud_students:
            metrics.append(f"Udemy Students: {ud_students[0]} ({parse_number(ud_students[0])})")
        if yt_subs:
            metrics.append(f"YouTube Subs: {yt_subs[0]} ({parse_number(yt_subs[0])})")
            
        if metrics:
            print(f"\nQuery: {query}")
            print(f"  URL: {r['url']}")
            print(f"  Matches: {', '.join(metrics)}")
            print(f"  Snippet snippet: {r['snippet'][:120]}...")
