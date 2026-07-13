import pandas as pd
import json
import os
import time
import profile_scraper
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
social_links_path = "/Users/fincent/Downloads/published_books_author_social_links_july2025_june2026.xlsx"
existing_aqs_path = "/Users/fincent/Downloads/Existing Author AQS.xlsx"
CACHE_FILE = os.path.join(SCRIPT_DIR, "search_cache.json")
PROFILES_CACHE_FILE = os.path.join(SCRIPT_DIR, "scraped_profiles_cache.json")

def load_cache(filepath):
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_cache(cache, filepath):
    with open(filepath, 'w') as f:
        json.dump(cache, f, indent=2)

print("Loading Excel sheets...")
df_social = pd.read_excel(social_links_path, sheet_name="author_level")
df_aqs = pd.read_excel(existing_aqs_path, sheet_name="Export")

# Find common authors
df_joined = pd.merge(df_social, df_aqs, left_on="cleaned_name", right_on="Author Name", how="inner")
df_joined = df_joined.drop_duplicates(subset=["cleaned_name"])
test_authors = df_joined.head(20).copy()

search_cache = load_cache(CACHE_FILE)
profiles_cache = load_cache(PROFILES_CACHE_FILE)

# Helper to resolve social URLs using search cache fallback
def resolve_social_urls(row, search_results):
    linkedin_url = row['linkedin'] if pd.notnull(row['linkedin']) else None
    github_url = row['github'] if pd.notnull(row['github']) else None
    
    if not linkedin_url or linkedin_url == "nan" or linkedin_url == "":
        linkedin_url = None
        for r in search_results:
            url = r['url']
            if "linkedin.com/in/" in url:
                linkedin_url = url
                break
                
    if not github_url or github_url == "nan" or github_url == "":
        github_url = None
        for r in search_results:
            url = r['url']
            if "github.com/" in url and not any(w in url for w in ["/features", "/pricing", "/trending", "/search"]):
                m = re.match(r'https?://github\.com/([^/]+)', url)
                if m:
                    github_url = f"https://github.com/{m.group(1)}"
                    break
                    
    return linkedin_url, github_url

print("=== STARTING SOCIAL SCRAPING & CACHING PIPELINE ===")
for idx, row in test_authors.iterrows():
    name = row['cleaned_name']
    
    # Retrieve search snippets from cache
    search_queries = [
        f'"{name}" Packt book',
        f'"{name}" github OR linkedin',
        f'"{name}"'
    ]
    all_results = []
    for query in search_queries:
        if query in search_cache:
            all_results.extend(search_cache[query])
            
    linkedin_url, github_url = resolve_social_urls(row, all_results)
    
    print(f"\nAuthor: {name}")
    
    # 1. Process LinkedIn
    if linkedin_url:
        # Check if already cached with valid followers (non-zero)
        if linkedin_url in profiles_cache and profiles_cache[linkedin_url].get("followers", 0) > 0:
            print(f"  LinkedIn Followers (Cached): {profiles_cache[linkedin_url]['followers']}")
        else:
            print(f"  LinkedIn URL resolved: {linkedin_url}")
            # Paced requests: sleep 15s to bypass rate limit
            print("  Sleeping 15 seconds before LinkedIn request...")
            time.sleep(15)
            
            # Scrape LinkedIn with retries on 429
            success = False
            for attempt in range(3):
                import urllib.request
                req = urllib.request.Request(
                    linkedin_url,
                    headers={
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                        'Accept-Language': 'en-US,en;q=0.9'
                    }
                )
                try:
                    with urllib.request.urlopen(req, timeout=10) as response:
                        html = response.read().decode('utf-8')
                        m = re.search(r'<span>\s*([\d,.]+k?)\s*followers\s*</span>', html, re.IGNORECASE)
                        if not m:
                            m = re.search(r'text-color-text[^>]*>\s*([\d,.]+k?)\s*followers\s*<', html, re.IGNORECASE)
                        if not m:
                            m = re.search(r'([\d,.]+k?)\s*followers', html, re.IGNORECASE)
                        
                        followers = profile_scraper.parse_number(m.group(1)) if m else 0
                        
                        c = re.search(r'<span>\s*([\d,.]+k?)\s*connections\s*</span>', html, re.IGNORECASE)
                        if not c:
                            c = re.search(r'([\d,.]+k?)\s*connections', html, re.IGNORECASE)
                        connections = profile_scraper.parse_number(c.group(1)) if c else 0
                        
                        li_data = {
                            "followers": followers,
                            "connections": connections,
                            "raw_followers": m.group(1).strip() if m else None,
                            "raw_connections": c.group(1).strip() if c else None
                        }
                        profiles_cache[linkedin_url] = li_data
                        save_cache(profiles_cache, PROFILES_CACHE_FILE)
                        print(f"  LinkedIn Scraped Successfully: {followers} followers, {connections} connections")
                        success = True
                        break
                except Exception as e:
                    is_429 = hasattr(e, 'code') and e.code == 429
                    if is_429:
                        print(f"  [Attempt {attempt+1}/3] LinkedIn Rate Limited (429). Sleeping 45 seconds before retry...")
                        time.sleep(45)
                    else:
                        print(f"  LinkedIn Scraping Failed: {e}")
                        break
            if not success:
                print("  Could not scrape LinkedIn profile.")
                
    # 2. Process GitHub
    if github_url:
        if github_url in profiles_cache and profiles_cache[github_url].get("followers", 0) > 0:
            print(f"  GitHub Followers (Cached): {profiles_cache[github_url]['followers']}")
        else:
            print(f"  GitHub URL resolved: {github_url}")
            gh_data = profile_scraper.scrape_github(github_url)
            if gh_data:
                profiles_cache[github_url] = gh_data
                save_cache(profiles_cache, PROFILES_CACHE_FILE)
                print(f"  GitHub Scraped Successfully: {gh_data['followers']} followers")
            else:
                print("  Could not scrape GitHub profile.")
                
print("\nScraping pipeline completed. Saved profiles to cache.")
