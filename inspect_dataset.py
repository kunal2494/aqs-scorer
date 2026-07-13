import json

path = "/Users/fincent/.gemini/antigravity/scratch/aqs-scorer/search_cache_partA.json"
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total keys in search_cache_partA.json: {len(data)}")
keys = list(data.keys())
print("First key:", repr(keys[0]))
print("First value preview:", json.dumps(data[keys[0]][:2], indent=2))
print("Last key:", repr(keys[-1]))
print("Last value preview:", json.dumps(data[keys[-1]][:2], indent=2))
