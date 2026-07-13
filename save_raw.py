import sys
import json
import os

RAW_FILE = "/Users/fincent/.gemini/antigravity/scratch/aqs-scorer/raw_responses_partB.json"

def main():
    try:
        data = json.load(sys.stdin)
    except Exception as e:
        print(f"Error parsing stdin: {e}", file=sys.stderr)
        sys.exit(1)
        
    query = data.get("query")
    response = data.get("response")
    
    if not query:
        print("Error: query is required", file=sys.stderr)
        sys.exit(1)
        
    # Load existing responses
    raw_responses = {}
    if os.path.exists(RAW_FILE):
        try:
            with open(RAW_FILE, 'r', encoding='utf-8') as f:
                raw_responses = json.load(f)
        except Exception as e:
            print(f"Warning: could not load existing raw file: {e}", file=sys.stderr)
            
    raw_responses[query] = response
    
    # Save back
    with open(RAW_FILE, 'w', encoding='utf-8') as f:
        json.dump(raw_responses, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully saved query: {query}. Total: {len(raw_responses)}")

if __name__ == "__main__":
    main()
