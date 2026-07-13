import pandas as pd

social_links_path = "/Users/fincent/Downloads/published_books_author_social_links_july2025_june2026.xlsx"
existing_aqs_path = "/Users/fincent/Downloads/Existing Author AQS.xlsx"

df_social = pd.read_excel(social_links_path, sheet_name="author_level")
df_aqs = pd.read_excel(existing_aqs_path, sheet_name="Export")

# Join on cleaned_name vs Author Name
df_joined = pd.merge(df_social, df_aqs, left_on="cleaned_name", right_on="Author Name", how="inner")
df_joined = df_joined.drop_duplicates(subset=["cleaned_name"])

print(f"Total merged: {len(df_joined)}")
for idx, row in df_joined.head(30).iterrows():
    print(f"- {row['cleaned_name']} (AQS: {row['AQS']}, Product ID: {row['pid']})")
