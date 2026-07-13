import os
import urllib.request
import json

api_key = os.environ.get("GEMINI_API_KEY", "")
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"

try:
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode('utf-8'))
        print("Supported Models:")
        for model in data.get("models", []):
            print(f"  Name: {model['name']} - {model.get('displayName')}")
except Exception as e:
    print("Error:", e)
