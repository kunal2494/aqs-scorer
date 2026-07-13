import json

cache_path = "/Users/fincent/.gemini/antigravity/scratch/aqs-scorer/search_cache_partA.json"
with open(cache_path, 'r', encoding='utf-8') as f:
    cache = json.load(f)

print("Total keys in cache:", len(cache))
print("Is dict:", isinstance(cache, dict))
for i, (k, v) in enumerate(cache.items()):
    if i < 3:
        print(f"Key {i+1}: {k}")
        print(f"Val {i+1} type: {type(v)}, length: {len(v)}")
        if v:
            print(f"Example result: {v[0]}")
