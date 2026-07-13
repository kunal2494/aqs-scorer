import pandas as pd

social_links_path = "/Users/fincent/Downloads/published_books_author_social_links_july2025_june2026.xlsx"
existing_aqs_path = "/Users/fincent/Downloads/Existing Author AQS.xlsx"

df_social = pd.read_excel(social_links_path, sheet_name="author_level")
df_aqs = pd.read_excel(existing_aqs_path, sheet_name="Export")

# Join on cleaned_name vs Author Name
df_joined = pd.merge(df_social, df_aqs, left_on="cleaned_name", right_on="Author Name", how="inner")
df_joined = df_joined.drop_duplicates(subset=["cleaned_name"])

test_authors = df_joined.head(20)

queries = []
for idx, row in test_authors.iterrows():
    name = row['cleaned_name']
    queries.append(f'"{name}" Packt book OR course')
    queries.append(f'"{name}" linkedin github')

print("Total queries to run:", len(queries))
for q in queries[:10]:
    print(" -", q)
