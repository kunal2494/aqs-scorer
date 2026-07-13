import json
import os

QUERIES_FILE = "/Users/fincent/.gemini/antigravity/scratch/aqs-scorer/batch_queries.txt"
RAW_FILE = "/Users/fincent/.gemini/antigravity/scratch/aqs-scorer/raw_responses_partB.json"

def main():
    # Read lines 51 to 100 (1-based index)
    with open(QUERIES_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    # lines are 0-indexed in python, so line 51 is lines[50], line 100 is lines[99]
    target_queries = [line.strip() for line in lines[50:100]]
    
    # Load raw responses
    raw_responses = {}
    if os.path.exists(RAW_FILE):
        try:
            with open(RAW_FILE, 'r', encoding='utf-8') as f:
                raw_responses = json.load(f)
        except Exception:
            pass
            
    print(f"Total target queries: {len(target_queries)}")
    print(f"Successfully fetched raw responses: {len(raw_responses)}")
    
    completed = []
    missing = []
    for q in target_queries:
        if q in raw_responses:
            completed.append(q)
        else:
            missing.append(q)
            
    print(f"Completed: {len(completed)}")
    print(f"Missing: {len(missing)}")
    for i, q in enumerate(missing[:5]):
        print(f"  Missing {i+1}: {q}")
        
if __name__ == "__main__":
    main()
