import urllib.request
import json
import os

api_key = os.environ.get("GEMINI_API_KEY", "")

models = [
    "gemini-2.5-flash-lite",
    "gemini-flash-latest",
    "gemini-flash-lite-latest",
    "gemini-2.0-flash-lite"
]

for model in models:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    payload = {
        "contents": [{
            "parts": [{"text": "Write a 3-word greeting."}]
        }]
    }
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='POST')
    
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            res_data = response.read().decode('utf-8')
            res_json = json.loads(res_data)
            greeting = res_json["candidates"][0]["content"]["parts"][0]["text"].strip()
            print(f"Model: {model} -> SUCCESS: {greeting}")
    except Exception as e:
        print(f"Model: {model} -> FAILED: {e}")
