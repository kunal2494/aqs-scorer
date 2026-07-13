import json
import os
import sys

PATH = "/Users/fincent/.gemini/antigravity/scratch/aqs-scorer/raw_responses_partB.json"

def update(new_data):
    if os.path.exists(PATH):
        with open(PATH, 'r') as f:
            try:
                data = json.load(f)
            except Exception:
                data = {}
    else:
        data = {}
    data.update(new_data)
    with open(PATH, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Updated cache with {len(new_data)} keys. Total keys: {len(data)}")

if __name__ == '__main__':
    # read json from stdin
    new_data = json.load(sys.stdin)
    update(new_data)
