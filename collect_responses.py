import json
import os
import sys

path = "/Users/fincent/.gemini/antigravity/scratch/aqs-scorer/raw_responses_temp_A.json"

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 collect_responses.py <query> <response>")
        sys.exit(1)
        
    query = sys.argv[1]
    response = sys.argv[2]
    
    data = {}
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except Exception:
                data = {}
                
    data[query] = response
    
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    print(f"Added query: {query}")

if __name__ == "__main__":
    main()
