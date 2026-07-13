batch_queries_path = "/Users/fincent/.gemini/antigravity/scratch/aqs-scorer/batch_queries.txt"

with open(batch_queries_path, 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip()]

# Lines 51 to 100 (which corresponds to 0-indexed indices 50 to 99)
target_queries = lines[50:100]

print(f"Loaded {len(target_queries)} queries.")
for idx, q in enumerate(target_queries, 51):
    print(f"{idx}: {q}")
