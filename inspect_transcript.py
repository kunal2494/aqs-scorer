import os
import json

transcript_path = "/Users/fincent/.gemini/antigravity/brain/80b7d530-1fc7-4dba-8722-8f85551b070a/.system_generated/logs/transcript.jsonl"
transcript_full_path = "/Users/fincent/.gemini/antigravity/brain/80b7d530-1fc7-4dba-8722-8f85551b070a/.system_generated/logs/transcript_full.jsonl"

print("transcript.jsonl exists:", os.path.exists(transcript_path))
print("transcript_full.jsonl exists:", os.path.exists(transcript_full_path))

# Check the contents of transcript if it exists
if os.path.exists(transcript_path):
    print("Size of transcript.jsonl:", os.path.getsize(transcript_path))
    with open(transcript_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        print("Total steps in transcript:", len(lines))
        for idx, line in enumerate(lines):
            try:
                data = json.loads(line)
                print(f"Step {idx}: source={data.get('source')}, type={data.get('type')}, status={data.get('status')}")
            except Exception as e:
                print(f"Error parsing line {idx}: {e}")
