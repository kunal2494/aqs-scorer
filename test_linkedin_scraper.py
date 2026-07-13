import os
import re
import requests

def get_cookie():
    cookie_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "linkedin_cookie.txt")
    if not os.path.exists(cookie_path):
        print("\n[!] 'linkedin_cookie.txt' not found!")
        print("To scrape LinkedIn accurately, you need to provide your session cookie ('li_at').")
        print("\nHow to get your 'li_at' cookie:")
        print("1. Open LinkedIn.com in Chrome or Safari and log in.")
        print("2. Right-click anywhere and select 'Inspect' (or press Cmd+Option+I) to open Developer Tools.")
        print("3. Go to the 'Application' tab (Chrome) or 'Storage' tab (Safari).")
        print("4. Under 'Cookies' in the left menu, select 'https://www.linkedin.com'.")
        print("5. Search for the name 'li_at' and copy its Value (a long string of characters).")
        print("6. Paste that string into a new file named 'linkedin_cookie.txt' in this folder and save it.\n")
        return None
        
    with open(cookie_path, 'r') as f:
        cookie = f.read().strip()
        if not cookie:
            print("[!] 'linkedin_cookie.txt' is empty. Please paste your 'li_at' cookie value.")
            return None
        return cookie

def test_scrape(url):
    cookie = get_cookie()
    if not cookie:
        return
        
    print(f"\n[*] Target Profile: {url}")
    print("[*] Loading cookie...")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': f'li_at={cookie}'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        print(f"[*] Response Status Code: {response.status_code}")
        
        if response.status_code == 999:
            print("[!] LinkedIn returned status 999 (Request Blocked). The session cookie might be invalid or expired.")
            return
            
        html = response.text
        
        # Save html for debugging
        debug_path = "linkedin_debug.html"
        with open(debug_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"[*] Saved raw HTML response to '{debug_path}' for layout auditing.")
        
        # 1. Search for followerCount in embedded JSON-LD or script blocks
        follower_count = None
        
        # Look for "followerCount":12345
        m_fc = re.search(r'"followerCount":\s*(\d+)', html)
        if m_fc:
            follower_count = int(m_fc.group(1))
            print(f"[+] Found 'followerCount' in JSON payload: {follower_count}")
            
        # Look for "numberOfFollowers":12345
        if not follower_count:
            m_nof = re.search(r'"numberOfFollowers":\s*(\d+)', html)
            if m_nof:
                follower_count = int(m_nof.group(1))
                print(f"[+] Found 'numberOfFollowers' in JSON payload: {follower_count}")
                
        # 2. Regular expression fallbacks for front-end text matching
        if not follower_count:
            text_matches = re.findall(r'([\d,.]+k?)\s*followers', html, re.IGNORECASE)
            if text_matches:
                print(f"[*] Found follower text matches: {text_matches}")
                # Use the helper parser logic
                from profile_scraper import parse_number
                follower_count = parse_number(text_matches[0])
                print(f"[+] Parsed follower count from text: {follower_count}")
                
        if follower_count is not None:
            print(f"\n[SUCCESS] Extracted Follower Count: {follower_count}")
        else:
            print("\n[!] Failed to extract follower count. Check 'linkedin_debug.html' to see if you were logged in correctly.")
            
    except Exception as e:
        print(f"[!] Error occurred: {e}")

if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "https://www.linkedin.com/in/cloudanum"
    test_scrape(target)
