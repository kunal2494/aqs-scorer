import pandas as pd

social_links_path = "/Users/fincent/Downloads/published_books_author_social_links_july2025_june2026.xlsx"
df_social = pd.read_excel(social_links_path, sheet_name="author_level")

# Print the columns related to social and website links
print("Social Link Columns:")
link_cols = ['cleaned_name', 'linkedin', 'github', 'twitter', 'self_youtube_video', 'website_1', 'website_2']
print(df_social[link_cols].head(10))
