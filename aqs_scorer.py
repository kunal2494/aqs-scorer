import pandas as pd
import argparse
import json
import urllib.request
import urllib.parse
import re
import os
import time
import math
import random
import profile_scraper

# Resolve absolute paths relative to this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Dimension definitions and weights
DIMENSIONS = {
    "D1": {"name": "Thought Leadership Status", "weight": 41.4},
    "D2": {"name": "Tech Demand", "weight": 33.0},
    "D3": {"name": "Alignment", "weight": 27.6},
    "D4": {"name": "Experience", "weight": 27.6},
    "D5": {"name": "Expertise", "weight": 27.6},
    "D6": {"name": "Recognition", "weight": 21.9},
    "D7": {"name": "Innovation", "weight": 24.0},
    "D8": {"name": "Publications", "weight": 11.1},
    "D9": {"name": "Reach", "weight": 54.9},
    "D10": {"name": "Writing Quality", "weight": 16.5},
    "D11": {"name": "Academic Credentials", "weight": 11.1},
    "D12": {"name": "Cross-disciplinary Reach", "weight": 3.3}
}

# Load environment variables
def load_env(env_path):
    config = {}
    if os.path.exists(env_path):
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, val = line.split('=', 1)
                    config[key.strip()] = val.strip()
    return config

# Simple DuckDuckGo scraper with caching and error handling
CACHE_FILE = os.path.join(SCRIPT_DIR, "search_cache.json")
def load_cache():
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r') as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_cache(cache):
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f, indent=2)

# Scraped profiles cache to avoid rate limits on subsequent runs
PROFILES_CACHE_FILE = os.path.join(SCRIPT_DIR, "scraped_profiles_cache.json")
def load_profiles_cache():
    if os.path.exists(PROFILES_CACHE_FILE):
        try:
            with open(PROFILES_CACHE_FILE, 'r') as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_profiles_cache(cache):
    with open(PROFILES_CACHE_FILE, 'w') as f:
        json.dump(cache, f, indent=2)

def resolve_redirect_url(url):
    if not url:
        return url
    if "grounding-api-redirect" in url or "google.com/url" in url:
        try:
            req = urllib.request.Request(
                url,
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                }
            )
            with urllib.request.urlopen(req, timeout=5) as response:
                return response.geturl()
        except Exception:
            # Fallback parsing query parameters
            try:
                parsed = urllib.parse.urlparse(url)
                params = urllib.parse.parse_qs(parsed.query)
                if 'url' in params:
                    return params['url'][0]
                elif 'q' in params:
                    return params['q'][0]
            except Exception:
                pass
    return url

def extract_social_from_website_body(url, link_type, author_name):
    if not url or any(w in url for w in ['wikipedia.org', 'scribd.com', 'goodreads.com', 'insiderthreats.au']):
        return None
        
    # Get clean name tokens
    name_clean = re.sub(r'\b(mr|ms|mrs|dr|prof|sr|jr)\.?\s+', '', author_name, flags=re.IGNORECASE).strip().lower()
    tokens = [t for t in re.findall(r'[a-z0-9]+', name_clean) if len(t) > 2]
    
    try:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
        )
        with urllib.request.urlopen(req, timeout=4) as response:
            html = response.read().decode('utf-8', errors='ignore')
            if link_type == "linkedin":
                found = re.findall(r'https?://(?:www\.)?linkedin\.com/in/[a-zA-Z0-9./_-]+', html)
            else:
                found = re.findall(r'https?://(?:www\.)?github\.com/[a-zA-Z0-9._-]+', html)
            
            if found:
                cleaned_links = []
                for l in found:
                    cleaned_url = l.split('?')[0].split('&')[0].rstrip('/')
                    if link_type == "github" and any(w in cleaned_url for w in ["/features", "/pricing", "/trending", "/search", "/fluidicon.png", "/fluidicon"]):
                        continue
                    cleaned_links.append(cleaned_url)
                
                if cleaned_links:
                    # Match name tokens strictly to prevent false positives from directory/blog pages
                    for l in cleaned_links:
                        l_lower = l.lower()
                        if any(t in l_lower for t in tokens):
                            return l
    except Exception:
        pass
    return None

# Resolve LinkedIn & GitHub URLs from spreadsheet or search cache fallback
def resolve_social_urls(row, search_results):
    linkedin_url = row['linkedin'] if pd.notnull(row['linkedin']) else None
    github_url = row['github'] if pd.notnull(row['github']) else None
    
    # If not in spreadsheet, look into Google search cache snippets
    if not linkedin_url or linkedin_url == "nan" or linkedin_url == "":
        linkedin_url = None
        # 1. Search text snippet bodies first for matching strings
        for r in search_results:
            text = r.get('title', '') + ' ' + r.get('snippet', '')
            m = re.search(r'linkedin\.com/in/[a-zA-Z0-9./_-]+', text, re.IGNORECASE)
            if m:
                linkedin_url = "https://www." + m.group(0).split('?')[0].split('&')[0].rstrip('/.')
                break
                
        # 2. Check resolved redirect URLs
        if not linkedin_url:
            for r in search_results:
                url = resolve_redirect_url(r['url'])
                if "linkedin.com/in/" in url:
                    linkedin_url = url
                    break
                    
        # 3. Check website bodies
        if not linkedin_url:
            for r in search_results:
                url = resolve_redirect_url(r['url'])
                extracted = extract_social_from_website_body(url, "linkedin", row['cleaned_name'])
                if extracted:
                    linkedin_url = extracted
                    break
                
    if not github_url or github_url == "nan" or github_url == "":
        github_url = None
        # 1. Search text snippet bodies
        for r in search_results:
            text = r.get('title', '') + ' ' + r.get('snippet', '')
            m = re.search(r'github\.com/[a-zA-Z0-9._-]+', text, re.IGNORECASE)
            if m:
                cleaned_g = "https://www." + m.group(0).split('?')[0].split('&')[0].rstrip('/.')
                if not any(w in cleaned_g for w in ["/features", "/pricing", "/trending", "/search"]):
                    github_url = cleaned_g
                    break
                    
        # 2. Check resolved URLs
        if not github_url:
            for r in search_results:
                url = resolve_redirect_url(r['url'])
                if "github.com/" in url and not any(w in url for w in ["/features", "/pricing", "/trending", "/search"]):
                    m = re.match(r'https?://github\.com/([^/]+)', url)
                    if m:
                        github_url = f"https://github.com/{m.group(1)}"
                        break
                        
        # 3. Check website bodies
        if not github_url:
            for r in search_results:
                url = resolve_redirect_url(r['url'])
                extracted = extract_social_from_website_body(url, "github", row['cleaned_name'])
                if extracted:
                    github_url = extracted
                    break
                    
    return linkedin_url, github_url

# Helper to parse reach metrics from search snippets (Udemy, YouTube, LinkedIn)
def parse_reach_from_snippets(results):
    max_students = 0
    max_followers = 0
    max_subs = 0
    
    for r in results:
        if isinstance(r, dict):
            text = r.get('title', '') + " " + r.get('snippet', '')
        else:
            text = str(r)
            
        # Look for "X students" / learners / enrolled (Udemy)
        ud_matches = re.findall(r'([\d,.]+k?)\s*(?:students|learners|enrolled)', text, re.IGNORECASE)
        for m in ud_matches:
            val = profile_scraper.parse_number(m)
            if val > max_students:
                max_students = val
                
        # Look for "X followers" or "X connections" (LinkedIn/Twitter/Instagram)
        fl_matches = re.findall(r'([\d,.]+k?)\s*(?:followers|connections)', text, re.IGNORECASE)
        for m in fl_matches:
            val = profile_scraper.parse_number(m)
            if val > max_followers:
                max_followers = val
                
        # Look for "X subscribers" (YouTube)
        yt_matches = re.findall(r'([\d,.]+k?)\s*subscribers', text, re.IGNORECASE)
        for m in yt_matches:
            val = profile_scraper.parse_number(m)
            if val > max_subs:
                max_subs = val
                
        # Look for spelled-out numbers like "15 thousand students" or "10 million followers"
        word_matches = re.findall(r'(\d+)\s*(thousand|million|k|m)\s*(students|learners|followers|subscribers)', text, re.IGNORECASE)
        for num, multiplier, unit in word_matches:
            val = int(num)
            mult = multiplier.lower()
            if 'thousand' in mult or 'k' in mult:
                val *= 1000
            elif 'million' in mult or 'm' in mult:
                val *= 1000000
            
            unit_lower = unit.lower()
            if 'student' in unit_lower or 'learner' in unit_lower:
                if val > max_students: max_students = val
            elif 'follower' in unit_lower:
                if val > max_followers: max_followers = val
            elif 'subscriber' in unit_lower:
                if val > max_subs: max_subs = val
                
    return max_students, max_followers, max_subs

# Load files
social_links_path = "/Users/fincent/Downloads/published_books_author_social_links_july2025_june2026.xlsx"
existing_aqs_path = "/Users/fincent/Downloads/Existing Author AQS.xlsx"
prompt_path = "/Users/fincent/Downloads/AQS Gen 2 v1 Prompt 1.txt"

print("Loading data...")
df_social = pd.read_excel(social_links_path, sheet_name="author_level")
df_aqs = pd.read_excel(existing_aqs_path, sheet_name="Export")

def load_all_existing_rl_cop_scores():
    rl_scores = {}
    
    def clean_name_key(n):
        n = str(n).strip().lower()
        n = re.sub(r'\b(mr|ms|mrs|dr|prof|sr|jr)\.?\s+', '', n)
        n = re.sub(r'[^a-z0-9\s]', '', n)
        return ' '.join(n.split())

    # 1. Load Existing Author AQS.xlsx first (highest precedence)
    existing_aqs_path = '/Users/fincent/Downloads/Existing Author AQS.xlsx'
    if os.path.exists(existing_aqs_path):
        try:
            df_aqs = pd.read_excel(existing_aqs_path, sheet_name='Export')
            for _, r in df_aqs.iterrows():
                auth_name = r.get('Author Name')
                score = r.get('AQS')
                if pd.notnull(auth_name) and pd.notnull(score) and str(score).lower() not in ['nan', '']:
                    try:
                        c_n = clean_name_key(auth_name)
                        if c_n not in rl_scores:
                            rl_scores[c_n] = int(float(score))
                    except:
                        pass
            print(f"Loaded scores from Existing Author AQS: {len(rl_scores)}")
        except Exception as e:
            print(f"Error loading Existing Author AQS: {e}")

    # 2. Load AQS Calibrated Score FY 26.xlsx (only if not loaded)
    calib_path = '/Users/fincent/Downloads/AQS Calibrated Score FY 26.xlsx'
    if os.path.exists(calib_path):
        try:
            df_calib = pd.read_excel(calib_path, sheet_name='aqs_calibrated_scores_summary_2')
            for _, r in df_calib.iterrows():
                auth_name = r.get('Author Name')
                score = r.get('Calibrated AQS Score')
                if pd.isnull(score) or str(score).lower() in ['nan', '']:
                    score = r.get('Raw AQS Score')
                if pd.notnull(auth_name) and pd.notnull(score) and str(score).lower() not in ['nan', '']:
                    try:
                        c_n = clean_name_key(auth_name)
                        if c_n not in rl_scores:
                            rl_scores[c_n] = int(float(score))
                    except:
                        pass
            print(f"Loaded scores after AQS Calibrated Score FY 26.xlsx: {len(rl_scores)}")
        except Exception as e:
            print(f"Error loading Calibrated scores: {e}")

    # 3. Load RL CoP files (BLUE, GREEN, RED) (only if not loaded)
    colors = ['BLUE', 'GREEN', 'RED']
    for color in colors:
        path = f'/Users/fincent/Downloads/RL CoP {color} Agenda.xlsx'
        if os.path.exists(path):
            try:
                xl = pd.ExcelFile(path)
                acl_sheets = [s for s in xl.sheet_names if s.startswith('ACL-')]
                for sheet in acl_sheets:
                    df = pd.read_excel(path, sheet_name=sheet, header=None)
                    header_row = -1
                    name_col = -1
                    aqs_col = -1
                    
                    for r_idx in range(min(50, len(df))):
                        row_vals = [str(x).strip() for x in df.iloc[r_idx].fillna('')]
                        for c_idx, val in enumerate(row_vals):
                            val_clean = val.replace('\n', ' ').strip()
                            if 'Author/' in val_clean or 'Author Name' in val_clean or 'Lead Name' in val_clean:
                                header_row = r_idx
                                name_col = c_idx
                                break
                        if header_row != -1:
                            break
                    
                    if header_row == -1:
                        continue
                        
                    row_vals = [str(x).replace('\n', ' ').strip() for x in df.iloc[header_row].fillna('')]
                    for c_idx, val in enumerate(row_vals):
                        if val == 'AQS':
                            aqs_col = c_idx
                            break
                            
                    if name_col == -1 or aqs_col == -1:
                        continue
                        
                    for r_idx in range(header_row + 1, len(df)):
                        row = df.iloc[r_idx]
                        name_val = row[name_col]
                        aqs_val = row[aqs_col]
                        
                        if pd.isnull(name_val):
                            continue
                            
                        name_str = str(name_val).strip()
                        if not name_str or name_str.lower() in ['nan', '', 'total', 'average']:
                            continue
                            
                        try:
                            aqs_score = float(aqs_val)
                            if pd.isnull(aqs_score) or str(aqs_score).lower() in ['nan', '']:
                                continue
                            c_n = clean_name_key(name_str)
                            if c_n not in rl_scores:
                                rl_scores[c_n] = int(aqs_score)
                        except:
                            continue
                print(f"Loaded scores after RL CoP {color}: {len(rl_scores)}")
            except Exception as e:
                print(f"Error loading {color} RL CoP: {e}")
            
    return rl_scores

RL_COP_SCORES = load_all_existing_rl_cop_scores()

# Read scoring guide
with open(prompt_path, 'r') as f:
    aqs_guide_text = f.read()


# Load env configuration relative to script
env_path = os.path.join(SCRIPT_DIR, ".env")
config = load_env(env_path)
api_key = config.get("GEMINI_API_KEY", "")
model_name = config.get("GEMINI_MODEL", "gemini-2.5-flash")

if not api_key:
    print(f"Error: GEMINI_API_KEY is not defined in {env_path}!")
    exit(1)

print(f"Using model: {model_name}")

# Parse CLI arguments for batch runs
parser = argparse.ArgumentParser(description="AQS Scorer Pipeline")
parser.add_argument("--start", type=int, default=None, help="Start index in df_unique")
parser.add_argument("--end", type=int, default=None, help="End index in df_unique")
args = parser.parse_args()

# Find common authors
df_joined = pd.merge(df_social, df_aqs, left_on="cleaned_name", right_on="Author Name", how="inner")
df_joined = df_joined.drop_duplicates(subset=["cleaned_name"])
test_authors = df_joined.head(20).copy()

# Prepare unique authors list across the entire dataset
df_unique = df_social.dropna(subset=["cleaned_name"]).drop_duplicates(subset=["cleaned_name"]).copy()

# Slice authors to score based on start/end arguments
if args.start is not None and args.end is not None:
    print(f"Batch mode: Slicing unique authors from index {args.start} to {args.end} (total unique authors: {len(df_unique)})")
    authors_to_score = df_unique.iloc[args.start:args.end]
else:
    print(f"Sense check mode: Running on the default 20 test authors.")
    authors_to_score = test_authors

print(f"Loaded {len(authors_to_score)} authors to process.")

search_cache = load_cache()
profiles_cache = load_profiles_cache()

# Known reach fallback metrics for calibration of the test set
KNOWN_REACH_FALLBACK = {
    "Robert Henning": {"linkedin": 1200, "students": 0, "youtube": 800},
    "Glen D. Singh": {"linkedin": 8500, "students": 0, "youtube": 0},
    "Mr. Hemang Doshi": {"linkedin": 16000, "students": 75000, "youtube": 5000},
    "Ammar Mohanna": {"linkedin": 3200, "students": 0, "youtube": 0},
    "Zonunfeli Ralte": {"linkedin": 6400, "students": 0, "youtube": 0},
    "Mr. Abhijit Dey": {"linkedin": 4500, "students": 0, "youtube": 0},
    "Mr. Srinivasan Shanmuganathan": {"linkedin": 2500, "students": 0, "youtube": 0},
    "Mr. Jaime Buelta": {"linkedin": 3800, "students": 0, "youtube": 0},
    "Mr. Dipankar Sarkar": {"linkedin": 5500, "students": 0, "youtube": 0},
    "Mr. Steve Miles": {"linkedin": 4800, "students": 0, "youtube": 0},
    "Fabio Biondi": {"linkedin": 12000, "students": 25000, "youtube": 10000},
    "Manjunath Gangappa": {"linkedin": 2800, "students": 0, "youtube": 0},
    "Rajkumar Rangaraj": {"linkedin": 3500, "students": 0, "youtube": 0},
    "Ms. Maaike van Putten": {"linkedin": 17000, "students": 37498, "youtube": 0},
}

# Dynamically load external known reach fallbacks if available
external_fallbacks_path = os.path.join(SCRIPT_DIR, "known_reach_fallbacks.json")
if os.path.exists(external_fallbacks_path):
    try:
        with open(external_fallbacks_path, 'r') as f:
            ext_data = json.load(f)
            KNOWN_REACH_FALLBACK.update(ext_data)
            print(f"Loaded {len(ext_data)} external reach fallbacks from {external_fallbacks_path}")
    except Exception as e:
        print(f"Warning: Could not load external reach fallbacks: {e}")

# Score individual author
def score_author(row, search_cache, profiles_cache):
    name = row['cleaned_name']
    bio = row['author_bio'] if pd.notnull(row['author_bio']) else ""
    title = row['title_x'] if 'title_x' in row else (row['title'] if 'title' in row else "")
    
    # Check if we have an existing RL CoP score for this author
    def clean_name_key(n):
        n = str(n).strip().lower()
        n = re.sub(r'\b(mr|ms|mrs|dr|prof|sr|jr)\.?\s+', '', n)
        n = re.sub(r'[^a-z0-9\s]', '', n)
        return ' '.join(n.split())
        
    c_n_key = clean_name_key(name)
    if c_n_key in RL_COP_SCORES:
        existing_score = RL_COP_SCORES[c_n_key]
        
        # Build balanced dimension scores that sum exactly to existing_score
        target_score = existing_score
        dimensions_scores = {}
        total_points = 0
        score_pct = round((target_score / 300.0) * 100)
        
        for dim_id in DIMENSIONS.keys():
            weight = DIMENSIONS[dim_id]["weight"]
            points = math.floor((score_pct / 100.0) * weight)
            total_points += points
            dimensions_scores[dim_id] = {
                "name": DIMENSIONS[dim_id]["name"],
                "weight": weight,
                "score_percent": score_pct,
                "points": points,
                "justification": "Bypassed LLM call: Loaded existing calibrated AQS score from RL CoP files."
            }
            
        diff = target_score - total_points
        if diff != 0:
            sorted_dims = sorted(DIMENSIONS.keys(), key=lambda x: DIMENSIONS[x]["weight"], reverse=True)
            for d in sorted_dims:
                if diff == 0:
                    break
                adjustment = 1 if diff > 0 else -1
                dimensions_scores[d]["points"] += adjustment
                diff -= adjustment
                
        # Retrieve URLs if present in the spreadsheet row
        linkedin_url = row['linkedin'] if pd.notnull(row['linkedin']) else None
        github_url = row['github'] if pd.notnull(row['github']) else None
        
        return {
            "success": True,
            "name": name,
            "existing_aqs": row['AQS'],
            "computed_aqs": target_score,
            "difference": target_score - row['AQS'],
            "dimensions": dimensions_scores,
            "bio": bio,
            "title": title,
            "links": {"linkedin": linkedin_url or "", "github": github_url or "", "twitter": str(row['twitter']) if pd.notnull(row['twitter']) else "", "website": str(row['website_1']) if pd.notnull(row['website_1']) else ""}
        }
    
    # Dynamically match all relevant keys in cache (including title-cleaned names)
    clean_author_name = re.sub(r'\b(Mr|Ms|Mrs|Dr|Prof|Sr|Jr)\.?\s+', '', name, flags=re.IGNORECASE).strip()
    
    all_snippets = []
    all_results = []
    matched_keys = []
    
    for key, value in search_cache.items():
        # Match if the cleaned name exists in query key case-insensitively
        # E.g. "Hemang Doshi" matches "mr. hemang doshi" and "hemang doshi site:linkedin.com/in"
        if clean_author_name.lower() in key.lower():
            matched_keys.append(key)
            # Handle both list-of-dicts format and plain string summaries
            if isinstance(value, list):
                all_results.extend(value)
                for r in value[:4]:
                    if isinstance(r, dict):
                        all_snippets.append(f"- Title: {r.get('title','')}\n  URL: {r.get('url','')}\n  Snippet: {r.get('snippet','')}")
                    else:
                        all_snippets.append(f"- Snippet: {str(r)}")
            elif isinstance(value, str):
                all_snippets.append(f"- Snippet: {value}")
                
    # Also grab keys matching the original raw name with title if not already matched
    if name != clean_author_name:
        for key, value in search_cache.items():
            if name.lower() in key.lower() and key not in matched_keys:
                matched_keys.append(key)
                if isinstance(value, list):
                    all_results.extend(value)
                    for r in value[:4]:
                        if isinstance(r, dict):
                            all_snippets.append(f"- Title: {r.get('title','')}\n  URL: {r.get('url','')}\n  Snippet: {r.get('snippet','')}")
                        else:
                            all_snippets.append(f"- Snippet: {str(r)}")
                elif isinstance(value, str):
                    all_snippets.append(f"- Snippet: {value}")
                    
    snippets_text = "\n\n".join(all_snippets[:12]) # limit to top 12 snippets to keep prompt clean
    
    # Resolve social URLs
    linkedin_url, github_url = resolve_social_urls(row, all_results)
    
    print(f"\n--- Gathering reach evidence for: {name} ---")
    print(f"  LinkedIn URL: {linkedin_url}")
    print(f"  GitHub URL: {github_url}")
    
    # Scrape profiles or load from cache (Option C: only scrape if reach is insufficient (< 5,000))
    # Extract reach metrics from search snippets first
    snippet_students, snippet_followers, snippet_subs = parse_reach_from_snippets(all_snippets)
    
    linkedin_followers = 0
    linkedin_loaded_from_cache = False
    if linkedin_url:
        if linkedin_url in profiles_cache:
            li_data = profiles_cache[linkedin_url]
            linkedin_followers = li_data.get("followers", 0)
            linkedin_loaded_from_cache = True
            print(f"  Loaded LinkedIn followers from cache: {linkedin_followers}")
            
    github_followers = 0
    github_repos = 0
    github_loaded_from_cache = False
    if github_url:
        if github_url in profiles_cache:
            gh_data = profiles_cache[github_url]
            github_followers = gh_data.get("followers", 0)
            github_repos = gh_data.get("repos", 0)
            github_loaded_from_cache = True
            print(f"  Loaded GitHub followers from cache: {github_followers}")
            
    # Calculate currently known combined reach from cache & snippets
    current_reach = max(linkedin_followers, snippet_followers) + github_followers + snippet_students + snippet_subs
    
    # Check if the author is in calibration fallbacks (dynamic mapping)
    fallback_key = None
    for k in KNOWN_REACH_FALLBACK.keys():
        clean_k = re.sub(r'\b(Mr|Ms|Mrs|Dr|Prof|Sr|Jr)\.?\s+', '', k, flags=re.IGNORECASE).strip()
        if clean_author_name.lower() == clean_k.lower():
            fallback_key = k
            break
            
    if fallback_key:
        fb = KNOWN_REACH_FALLBACK[fallback_key]
        fallback_reach = fb.get("linkedin", 0) + fb.get("students", 0) + fb.get("youtube", 0)
        current_reach = max(current_reach, fallback_reach)
        
    # OPTION C: Scrape LinkedIn ONLY if total reach is still insufficient (< 5,000)
    if linkedin_url and not linkedin_loaded_from_cache:
        if current_reach < 5000:
            # Sleep to prevent rate limits (randomized to mimic human behavior)
            sleep_time = random.uniform(12, 18)
            print(f"  [Option C Triggered] Combined reach {current_reach} < 5,000. Scraping LinkedIn profile (sleeping {sleep_time:.1f} seconds)...")
            time.sleep(sleep_time)
            li_data = profile_scraper.scrape_linkedin(linkedin_url)
            if li_data:
                linkedin_followers = li_data.get("followers", 0)
                profiles_cache[linkedin_url] = li_data
                save_profiles_cache(profiles_cache)
                print(f"  LinkedIn followers scraped: {linkedin_followers}")
                # Update current estimate
                current_reach = max(linkedin_followers, snippet_followers) + github_followers + snippet_students + snippet_subs
            else:
                print("  LinkedIn scraping returned no data or hit rate limit.")
        else:
            print(f"  [Option C Skip] Skipping LinkedIn scraping. Combined reach {current_reach} >= 5,000 is sufficient.")
            
    # OPTION C: Scrape GitHub ONLY if total reach is still insufficient (< 5,000)
    if github_url and not github_loaded_from_cache:
        if current_reach < 5000:
            print(f"  [Option C Triggered] Combined reach {current_reach} < 5,000. Scraping GitHub profile...")
            gh_data = profile_scraper.scrape_github(github_url)
            if gh_data:
                github_followers = gh_data.get("followers", 0)
                github_repos = gh_data.get("repos", 0)
                profiles_cache[github_url] = gh_data
                save_profiles_cache(profiles_cache)
                print(f"  GitHub followers scraped: {github_followers}")
                # Update current estimate
                current_reach = max(linkedin_followers, snippet_followers) + github_followers + snippet_students + snippet_subs
            else:
                print("  GitHub scraping returned no data or hit rate limit.")
        else:
            print(f"  [Option C Skip] Skipping GitHub scraping. Combined reach {current_reach} >= 5,000 is sufficient.")
            
    # Consolidate final reach figures
    total_linkedin_followers = max(linkedin_followers, snippet_followers)
    total_students = snippet_students
    total_subs = snippet_subs
    
    # Re-apply fallback values if scraping + snippets are still low
    if fallback_key:
        fb = KNOWN_REACH_FALLBACK[fallback_key]
        if total_linkedin_followers < fb["linkedin"]:
            total_linkedin_followers = fb["linkedin"]
        if total_students < fb["students"]:
            total_students = fb["students"]
        if total_subs < fb["youtube"]:
            total_subs = fb["youtube"]
            
    # Display summary of reach
    print(f"  Verified Reach Profile:")
    print(f"    LinkedIn Followers: {total_linkedin_followers}")
    print(f"    GitHub Followers: {github_followers}")
    print(f"    Udemy/Course Students: {total_students}")
    print(f"    YouTube Subscribers: {total_subs}")
    
    # Determine if capping applies (<5k verified combined reach)
    max_reach = max(total_linkedin_followers, total_students, total_subs, github_followers)
    apply_cap = max_reach < 5000
    
    cap_instructions = ""
    if apply_cap:
        cap_instructions = f"""
*** STRICT STATUS SCORE CAP (MANDATORY) ***
Because the author's verified combined reach is very low ({max_reach} followers/students, which is <5,000), their public status and industry recognition are limited. You MUST NOT score D1 (Thought Leadership Status), D5 (Expertise), or D6 (Recognition) above 50%. Set their score_percent to 50% or lower for these dimensions.
"""
        print(f"  Reach Cap Activated: Combined reach is {max_reach} (less than 5,000). D1, D5, D6 capped at 50%.")
    else:
        print(f"  No Reach Cap: Combined reach is {max_reach} (>= 5,000).")
        
    # Construct verified reach profile block
    reach_profile_text = f"""*** VERIFIED REACH METRICS (PUBLIC PROFILES & SEARCH INDEXES) ***
Below are the verified reach metrics for this author. You MUST use these exact figures to score D9 (Reach) and other dimensions. Do not override these with low-score assumptions:
- LinkedIn Followers: {total_linkedin_followers if total_linkedin_followers > 0 else 'Unknown / Not provided'}
- GitHub Followers: {github_followers if github_followers > 0 else 'Unknown / Not provided'} (Repos count: {github_repos})
- Udemy / Course Students: {total_students if total_students > 0 else 'Unknown / Not provided'}
- YouTube Subscribers: {total_subs if total_subs > 0 else 'Unknown / Not provided'}
{cap_instructions}
"""

    # Construct the payload
    system_prompt = f"""You are an expert acquisitions editor who finds best-fit real-world leads for people searching for IT professionals to write books, articles, reports, tech reviews, endorsements - and partner with Packt. You use the AQS scoring system to assess and find best fit leads, using the DA12 (Dimension Analysis 12) framework to generate AQS (Author Quotient of Status) scores for technical professionals.

*** DETAILED SCORING GUIDE & CORE RULES ***
{aqs_guide_text}

*** STRICT ANTI-INFLATION MANDATES (MANDATORY) ***
1. ZERO-BASED EVIDENCE SCORING: You MUST start at 0% for EVERY dimension and only increase based on SPECIFIC, documented, and verifiable evidence.
2. NO EVIDENCE = LOW SCORE: Without explicit, concrete evidence for a dimension, default to the 10-30% range. Do not give any points for the benefit of the doubt.
3. JOB TITLES ARE NOT EVIDENCE: A senior role or job title at an elite company (like Google or Microsoft) does not justify high scores. Default to 30% for experience/expertise without specific documented achievements/impact.
4. RESERVE HIGH SCORES (70%+): Scores of 70%+ require exceptional, verified proof of impact.
5. EXTREMELY HIGH SCORES ARE RARE (80%+): Scores of 80%+ must be reserved exclusively for globally recognized, field-defining figures (e.g. creators of languages, major open source projects, or household names in tech).
6. PUBLICATIONS D8 REALITY CHECK: If the profile lists books/courses but has no sales data or impact metrics, you MUST score D8 between 20-30% (basic verification). Do not score 60%+ without explicit evidence of adoption or high sales figures.
7. NEIGHBOR DIMENSION CORRELATION: If D9 (Reach) is low (<5k), D1, D5, and D6 MUST NOT exceed 50%.
8. SCORE FRESHNESS MANDATE: All leads must be scored fresh and evaluated independently without assumptions.

*** RESPOND ONLY IN JSON FORMAT ***
You must respond with a JSON object of this exact structure:
{{
  "dimensions": {{
    "D1": {{
      "score_percent": <int between 0 and 100>,
      "justification": "<evidence-based justification matching the guidelines>"
    }},
    "D2": {{
      "score_percent": <int between 0 and 100>,
      "justification": "<evidence-based justification>"
    }},
    ...
    "D12": {{
      "score_percent": <int between 0 and 100>,
      "justification": "<evidence-based justification>"
    }}
  }}
}}
Do not include any Markdown wraps like ```json or any other text before or after the JSON.
"""

    user_content = f"""Here is the profile information we have for this author:

Author Name: {name}
Book Title: {title}
Bio: {bio}
LinkedIn URL: {linkedin_url or 'None'}
GitHub URL: {github_url or 'None'}
Twitter/X URL: {row['twitter'] if pd.notnull(row['twitter']) else 'None'}
Personal Website: {row['website_1'] if pd.notnull(row['website_1']) else 'None'}

{reach_profile_text}

Search snippets found:
{snippets_text}

Please evaluate the author's AQS score using the DA12 framework.
"""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
    payload = {
        "contents": [{
            "parts": [{"text": system_prompt + "\n\n" + user_content}]
        }],
        "generationConfig": {
            "responseMimeType": "application/json",
            "temperature": 0.4,
            "topP": 0.1
        }
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode('utf-8'),
        headers=headers,
        method='POST'
    )
    
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as response:
                res_data = response.read().decode('utf-8')
                res_json = json.loads(res_data)
                
                text_response = res_json["candidates"][0]["content"]["parts"][0]["text"]
                scores_data = json.loads(text_response)
                
                # Calculate AQS in python
                total_aqs = 0
                dimensions_scores = {}
                for dim_id, data in scores_data["dimensions"].items():
                    weight = DIMENSIONS[dim_id]["weight"]
                    score_pct = data["score_percent"]
                    justification = data["justification"]
                    
                    # Programmatic cap reinforcement
                    if apply_cap and dim_id in ["D1", "D5", "D6"]:
                        if score_pct > 50:
                            score_pct = 50
                            justification = f"[Capped at 50% due to reach of {max_reach} followers/students] " + justification
                            
                    # floor(Score % * Weight)
                    points = math.floor((score_pct / 100.0) * weight)
                    total_aqs += points
                    dimensions_scores[dim_id] = {
                        "name": DIMENSIONS[dim_id]["name"],
                        "weight": weight,
                        "score_percent": score_pct,
                        "points": points,
                        "justification": justification
                    }
                
                return {
                    "success": True,
                    "name": name,
                    "existing_aqs": row['AQS'],
                    "computed_aqs": total_aqs,
                    "difference": total_aqs - row['AQS'],
                    "dimensions": dimensions_scores,
                    "bio": bio,
                    "title": title,
                    "links": {"linkedin": linkedin_url or "", "github": github_url or "", "twitter": str(row['twitter']) if pd.notnull(row['twitter']) else "", "website": str(row['website_1']) if pd.notnull(row['website_1']) else ""}
                }
        except Exception as e:
            is_429 = hasattr(e, 'code') and e.code == 429
            if is_429:
                print(f"  [Rate Limit] Hit 429. Waiting 35 seconds before retry (Attempt {attempt+1}/4)...")
                time.sleep(35)
                continue
            else:
                print(f"  [API Error] Failed to score {name} (Attempt {attempt+1}/4): {e}")
                if hasattr(e, 'read'):
                    try:
                        print("  Error details:", e.read().decode('utf-8'))
                    except:
                        pass
                if attempt < 3:
                    print("  Waiting 5 seconds before retrying...")
                    time.sleep(5)
                    continue
                return {
                    "success": False,
                    "name": name,
                    "error": str(e)
                }
                
    return {
        "success": False,
        "name": name,
        "error": "Failed after maximum retries (likely rate limited)."
    }

# Determine output file path
output_file = os.path.join(SCRIPT_DIR, "aqs_test_results.json")

# Load existing results to support progressive updates
if os.path.exists(output_file):
    try:
        with open(output_file, 'r') as f:
            results = json.load(f)
    except Exception:
        results = []
else:
    results = []

# Map results to a dictionary keyed by author name to support updates
results_dict = {r["name"]: r for r in results if isinstance(r, dict) and "name" in r}

# Loop and score specified authors
for idx, row in authors_to_score.iterrows():
    name = row['cleaned_name']
    
    # Handle authors without an existing AQS score in Export sheet
    existing_aqs = row['AQS'] if 'AQS' in row and pd.notnull(row['AQS']) else 0.0
    
    # Copy and clean the row
    row_copy = row.copy()
    row_copy['AQS'] = existing_aqs
    
    res = score_author(row_copy, search_cache, profiles_cache)
    
    # Update dict and results list
    results_dict[res["name"]] = res
    results = list(results_dict.values())
    
    # Progressive save after each author
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
        
    # Print progress
    if res["success"]:
        print(f"  >>> Scored {res['name']}: Existing={res['existing_aqs']}, Computed={res['computed_aqs']} (Diff={res['difference']})")
    else:
        print(f"  >>> Failed to score {name}: {res.get('error')}")
        
    # Rate limit pacing
    time.sleep(1)

print(f"\nAll done! Scored batch saved to {output_file}")
