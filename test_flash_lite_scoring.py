import urllib.request
import json
import os
import math
api_key = os.environ.get("GEMINI_API_KEY", "")
model = "gemini-2.5-flash-lite"
url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"

prompt_path = "/Users/fincent/Downloads/AQS Gen 2 v1 Prompt 1.txt"
with open(prompt_path, 'r') as f:
    aqs_guide_text = f.read()

# Let's test scoring for Fuheng Wu (existing score 153)
system_prompt = f"""You are an expert acquisitions editor. You use the AQS scoring system to assess technical professionals using the DA12 framework.

*** DETAILED SCORING GUIDE (DA12 FRAMEWORK) ***
{aqs_guide_text}

*** MANDATORY SCORING UPDATES (AUG-OCT 2025) ***
1. SCORE FRESHNESS: Score fresh.
2. ISOLATION: Evaluate independently.
3. FOLLOWER EVIDENCE: If follower counts are provided, treat them as validated evidence. Follow thresholds (e.g. D9 Reach: <5k is 20-30%, 5k-20k is 30-40%, 20k-50k is 40-50%, 50k-75k is 50-60%, etc.).

Respond ONLY in JSON format of this structure:
{{
  "dimensions": {{
    "D1": {{"score_percent": <int>, "justification": "..."}},
    ...
    "D12": {{"score_percent": <int>, "justification": "..."}}
  }}
}}
"""

user_content = """Here is the profile for Fuheng Wu:
Name: Fuheng Wu
Title: Clean Architecture in Swift
Bio: iOS Engineer with years of experience.
LinkedIn Followers: 0
GitHub Followers: 70
Udemy Students: 0
YouTube Subscribers: 0
"""

payload = {
    "contents": [{
        "parts": [{"text": system_prompt + "\n\n" + user_content}]
    }],
    "generationConfig": {
        "responseMimeType": "application/json",
        "temperature": 0.1
    }
}

req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={"Content-Type": "application/json"}, method='POST')

try:
    with urllib.request.urlopen(req, timeout=30) as response:
        res_data = response.read().decode('utf-8')
        res_json = json.loads(res_data)
        text_response = res_json["candidates"][0]["content"]["parts"][0]["text"]
        scores_data = json.loads(text_response)
        
        DIM_WEIGHTS = {
            "D1": 41.4, "D2": 33.0, "D3": 27.6, "D4": 27.6, "D5": 27.6, "D6": 21.9,
            "D7": 24.0, "D8": 11.1, "D9": 54.9, "D10": 16.5, "D11": 11.1, "D12": 3.3
        }
        
        total_aqs = 0
        print("\nDimension Scores:")
        for dim, data in scores_data["dimensions"].items():
            pct = data["score_percent"]
            weight = DIM_WEIGHTS[dim]
            pts = math.floor((pct / 100.0) * weight)
            total_aqs += pts
            print(f"  {dim}: Pct={pct}%, Pts={pts} ({data['justification'][:50]}...)")
        print("\nTotal Computed AQS:", total_aqs)
except Exception as e:
    print("Error:", e)
    if hasattr(e, 'read'):
        print(e.read().decode('utf-8'))
