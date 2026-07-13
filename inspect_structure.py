with open("raw_responses_partA.json", "r") as f:
    content = f.read()

print("First 1500 chars:")
print(content[:1500])
print("\nLast 1500 chars:")
print(content[-1500:])
