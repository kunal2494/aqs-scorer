import urllib.request
import json
import os

api_key = os.environ.get("GEMINI_API_KEY", "")
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemma-4-31b-it:generateContent?key={api_key}"

payload = {
    "contents": [{
        "parts": [{"text": "Hello, write a short 3-word greeting."}]
    }]
}

headers = {"Content-Type": "application/json"}
req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='POST')

try:
    print("Testing gemma-4-31b-it...")
    with urllib.request.urlopen(req, timeout=10) as response:
        res_data = response.read().decode('utf-8')
        res_json = json.loads(res_data)
        print("Success!", res_json["candidates"][0]["content"]["parts"][0]["text"])
except Exception as e:
    print("Error:", e)
