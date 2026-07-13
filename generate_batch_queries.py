import pandas as pd
import argparse
import re
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
social_links_path = "/Users/fincent/Downloads/published_books_author_social_links_july2025_june2026.xlsx"

parser = argparse.ArgumentParser(description="Generate search queries for a batch of authors")
parser.add_argument("--start", type=int, required=True, help="Start index in df_unique")
parser.add_argument("--end", type=int, required=True, help="End index in df_unique")
args = parser.parse_args()

print("Loading dataset...")
df_social = pd.read_excel(social_links_path, sheet_name="author_level")
df_unique = df_social.dropna(subset=["cleaned_name"]).drop_duplicates(subset=["cleaned_name"]).copy()

batch = df_unique.iloc[args.start:args.end]
print(f"Batch sliced: {len(batch)} authors (from index {args.start} to {args.end})")

def clean_name(name):
    # Remove titles
    cleaned = re.sub(r'\b(Mr|Ms|Mrs|Dr|Prof|Sr|Jr)\.?\s+', '', name, flags=re.IGNORECASE)
    return cleaned.strip()

queries = []
authors_list = []

for idx, row in batch.iterrows():
    raw_name = row['cleaned_name']
    cleaned = clean_name(raw_name)
    authors_list.append(raw_name)
    
    # 4 targeted queries per author to build comprehensive reach profiles
    queries.append(f'"{cleaned}" site:linkedin.com/in')
    queries.append(f'"{cleaned}" site:github.com OR site:udemy.com/user OR site:medium.com')
    queries.append(f'"{cleaned}" \"students\" site:udemy.com')
    queries.append(f'"{cleaned}" \"subscribers\" site:youtube.com')

# Print details
print("\nAuthors in this batch:")
for i, name in enumerate(authors_list, 1):
    print(f"  {i}. {name}")

# Write queries to a temporary text file
queries_file = os.path.join(SCRIPT_DIR, "batch_queries.txt")
with open(queries_file, 'w') as f:
    for q in queries:
        f.write(q + "\n")

print(f"\nGenerated {len(queries)} search queries and saved to {queries_file}")
