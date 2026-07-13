import pandas as pd

df = pd.read_excel('/Users/fincent/Downloads/published_books_author_social_links_july2025_june2026.xlsx', sheet_name='author_level')
print("Non-empty columns and their counts:")
for col in df.columns:
    non_null_count = df[col].notnull().sum()
    if non_null_count > 0:
        print(f"  {col}: {non_null_count}")
