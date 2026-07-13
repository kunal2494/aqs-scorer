import urllib.request
import re
import urllib.parse
import os
import requests

# Common headers to mimic a browser
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9'
}

def parse_number(num_str):
    if not num_str:
        return 0
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

def scrape_linkedin(url):
    if not url or "linkedin.com/in/" not in url:
        return None
    
    # Ensure correct protocol
    if not url.startswith("http"):
        url = "https://" + url
        
    # Check for authenticated session cookie
    cookie_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "linkedin_cookie.txt")
    session_headers = HEADERS.copy()
    if os.path.exists(cookie_path):
        with open(cookie_path, 'r') as f:
            cookie = f.read().strip()
            if cookie:
                session_headers['Cookie'] = f"li_at={cookie}"
                print("  [LinkedIn Scraper] Loading session cookie for authenticated scrape.")
                
    try:
        # Use requests with cookies
        response = requests.get(url, headers=session_headers, timeout=15)
        if response.status_code == 999:
            print("  [LinkedIn Scraper Warning] HTTP 999 Blocked. Session cookie is likely expired or invalid.")
            return None
        elif response.status_code != 200:
            print(f"  [LinkedIn Scraper Warning] HTTP {response.status_code} for {url}")
            return None
            
        html = response.text
        
        follower_count = 0
        connections = 0
        raw_followers = None
        raw_connections = None
        
        # 1. Search for followerCount/numberOfFollowers in embedded JSON payloads
        m_fc = re.search(r'"followerCount":\s*(\d+)', html)
        if m_fc:
            follower_count = int(m_fc.group(1))
            raw_followers = str(follower_count)
            
        if not follower_count:
            m_nof = re.search(r'"numberOfFollowers":\s*(\d+)', html)
            if m_nof:
                follower_count = int(m_nof.group(1))
                raw_followers = str(follower_count)
                
        # 2. Text-based HTML regex fallbacks
        if not follower_count:
            m = re.search(r'<span>\s*([\d,.]+k?)\s*followers\s*</span>', html, re.IGNORECASE)
            if not m:
                m = re.search(r'text-color-text[^>]*>\s*([\d,.]+k?)\s*followers\s*<', html, re.IGNORECASE)
            if not m:
                m = re.search(r'([\d,.]+k?)\s*followers', html, re.IGNORECASE)
            
            if m:
                follower_count = parse_number(m.group(1))
                raw_followers = m.group(1).strip()
                
        c = re.search(r'<span>\s*([\d,.]+k?)\s*connections\s*</span>', html, re.IGNORECASE)
        if not c:
            c = re.search(r'([\d,.]+k?)\s*connections', html, re.IGNORECASE)
        if c:
            connections = parse_number(c.group(1))
            raw_connections = c.group(1).strip()
            
        return {
            "followers": follower_count,
            "connections": connections,
            "raw_followers": raw_followers,
            "raw_connections": raw_connections
        }
    except Exception as e:
        print(f"  [LinkedIn Scraper Warning] Failed to scrape {url}: {e}")
        return None

def scrape_github(url):
    if not url or "github.com/" not in url:
        return None
        
    if not url.startswith("http"):
        url = "https://" + url
        
    # Remove trailing slash or tab refs
    url = url.split("?")[0].rstrip("/")
    
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8')
            # <span class="text-bold color-fg-default">78</span> followers
            m = re.search(r'class="text-bold color-fg-default">([^<]+)</span>\s*followers', html, re.IGNORECASE)
            if not m:
                m = re.search(r'href="[^"]+\?tab=followers"[^>]*>.*?<span[^>]*>([^<]+)</span>\s*followers', html, re.DOTALL)
            if not m:
                m = re.search(r'([\d,.]+k?)\s*followers', html, re.IGNORECASE)
                
            followers = parse_number(m.group(1)) if m else 0
            
            # Check repos count
            r = re.search(r'Counter">([^<]+)</span>\s*<span[^>]*>Repositories', html, re.IGNORECASE)
            repos = parse_number(r.group(1)) if r else 0
            
            return {
                "followers": followers,
                "repos": repos,
                "raw_followers": m.group(1).strip() if m else None
            }
    except Exception as e:
        print(f"  [GitHub Scraper Warning] Failed to scrape {url}: {e}")
        return None

# Test the scrapers
if __name__ == "__main__":
    print("Testing LinkedIn scraper on Marco Secchi:")
    li = scrape_linkedin("https://www.linkedin.com/in/secchimarco/")
    print("Result:", li)
    
    print("\nTesting GitHub scraper on Marco Secchi:")
    gh = scrape_github("https://github.com/marcosecchi")
    print("Result:", gh)
