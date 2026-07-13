import re
import json

with open("raw_responses_partA.json", "r") as f:
    content = f.read()

# Pattern: find keys and the raw value blocks
# A key looks like: "\"[Author Name]\" site:[site]"
# Followed by: ": "
# And value ends before the next key or at the end of the file.
pattern = r'"(\\"[^"\\]+\\" site:[^"]+)"\s*:\s*"(.*?)(?=(?:"\\"[^"\\]+\\" site:)|(?:"\s*}\s*$))'
matches = re.findall(pattern, content, re.DOTALL)

print(f"Regex found {len(matches)} queries.")
extracted = {}
for q, val in matches:
    # Unescape newlines and backslashes if needed, or clean up
    # Since we want to parse it as a valid string, let's replace double backslashes
    clean_val = val.replace('\\"', '"').replace('\\n', '\n')
    extracted[q.replace('\\"', '"')] = clean_val

print(f"Extracted dictionary has {len(extracted)} entries.")
print("Sample extracted keys:")
for k in list(extracted.keys())[:3]:
    print(" -", k)
