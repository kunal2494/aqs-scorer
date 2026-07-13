import sys
import json
import os

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 save_subagent_response.py <subagent_id> <query>")
        sys.exit(1)
        
    subagent_id = sys.argv[1]
    query = sys.argv[2]
    
    temp_file = f"/Users/fincent/.gemini/antigravity/scratch/aqs-scorer/temp_{subagent_id}.txt"
    out_file = f"/Users/fincent/.gemini/antigravity/scratch/aqs-scorer/raw_responses_sub{subagent_id}.json"
    
    if not os.path.exists(temp_file):
        print(f"Error: Temp file {temp_file} does not exist.")
        sys.exit(1)
        
    with open(temp_file, "r", encoding="utf-8") as f:
        response_text = f.read()
        
    # Load existing database for this subagent
    data = {}
    if os.path.exists(out_file):
        try:
            with open(out_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            data = {}
            
    data[query] = response_text
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    # Clean up temp file
    try:
        os.remove(temp_file)
    except Exception:
        pass
        
    print(f"Saved response for query: {query} to subagent {subagent_id}. Total count: {len(data)}")

if __name__ == "__main__":
    main()
