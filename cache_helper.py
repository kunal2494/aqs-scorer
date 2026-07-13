import json
import os
import sys

RAW_FILE = "/Users/fincent/.gemini/antigravity/scratch/aqs-scorer/raw_responses_partB.json"

def get_missing_queries():
    batch_queries_path = "/Users/fincent/.gemini/antigravity/scratch/aqs-scorer/batch_queries.txt"
    if not os.path.exists(batch_queries_path):
        print(f"Error: {batch_queries_path} not found")
        sys.exit(1)
        
    with open(batch_queries_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
        
    # Lines 41 to 80 (indices 40 to 79)
    target_queries = lines[40:80]
    
    raw_data = {}
    if os.path.exists(RAW_FILE):
        try:
            with open(RAW_FILE, "r", encoding="utf-8") as f:
                raw_data = json.load(f)
        except Exception as e:
            print(f"Error loading raw responses: {e}")
            raw_data = {}
            
    missing = []
    for q in target_queries:
        if q not in raw_data:
            missing.append(q)
            
    return target_queries, raw_data, missing

def add_response(query, text):
    _, raw_data, _ = get_missing_queries()
    raw_data[query] = text
    with open(RAW_FILE, "w", encoding="utf-8") as f:
        json.dump(raw_data, f, indent=2, ensure_ascii=False)
    print(f"Successfully added response for: {query}")
    print(f"Total responses cached: {len(raw_data)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 cache_helper.py [status | add <query> <response_file>]")
        sys.exit(1)
        
    cmd = sys.argv[1]
    if cmd == "status":
        targets, raw, missing = get_missing_queries()
        print(f"Target queries: {len(targets)}")
        print(f"Cached queries: {len(raw)}")
        print(f"Missing queries: {len(missing)}")
        if missing:
            print("Next missing query:")
            print(missing[0])
    elif cmd == "add":
        query = sys.argv[2]
        resp_file = sys.argv[3]
        with open(resp_file, "r", encoding="utf-8") as f:
            text = f.read()
        add_response(query, text)
