with open("batch_queries.txt", "r") as f:
    lines = f.readlines()

print("Missing queries (lines 41 to 50):")
for idx in range(40, 50):
    print(f"  {idx+1}: {lines[idx].strip()}")
