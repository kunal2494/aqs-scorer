with open("raw_responses_partA.json", "r") as f:
    content = f.read()

char_pos = 45172
start = max(0, char_pos - 300)
end = min(len(content), char_pos + 300)

print(f"Content around char {char_pos}:")
print("----------------------------------------")
print(content[start:end])
print("----------------------------------------")
