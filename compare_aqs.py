import pandas as pd
import json
import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
results_path = os.path.join(SCRIPT_DIR, "aqs_test_results.json")

# 1. Load our computed results
with open(results_path, 'r') as f:
    computed_data = json.load(f)

print(f"Loaded {len(computed_data)} computed scores from our results file.")

# 2. Extract scores from RL CoP files
colors = ['BLUE', 'GREEN', 'RED']
rl_scores = []

def clean_name(name):
    # Strip titles, leading/trailing whitespace, and normalize spaces
    name = str(name).strip()
    name = re.sub(r'\b(Mr|Ms|Mrs|Dr|Prof|Sr|Jr)\.?\s+', '', name, flags=re.IGNORECASE)
    # Remove extra spaces
    name = ' '.join(name.split())
    return name.lower()

def clean_tokens(name):
    name = str(name).strip().lower()
    name = re.sub(r'\b(mr|ms|mrs|dr|prof|sr|jr)\.?\s+', '', name)
    name = re.sub(r'[^a-z\s]', '', name)
    return set(name.split())

for color in colors:
    path = f'/Users/fincent/Downloads/RL CoP {color} Agenda.xlsx'
    if not os.path.exists(path):
        continue
    
    xl = pd.ExcelFile(path)
    acl_sheets = [s for s in xl.sheet_names if s.startswith('ACL-')]
    
    for sheet in acl_sheets:
        df = pd.read_excel(path, sheet_name=sheet, header=None)
        
        header_row = -1
        name_col = -1
        aqs_col = -1
        
        # Scan first 50 rows for header
        for r_idx in range(min(50, len(df))):
            row_vals = [str(x).strip() for x in df.iloc[r_idx].fillna('')]
            for c_idx, val in enumerate(row_vals):
                val_clean = val.replace('\n', ' ').strip()
                if 'Author/' in val_clean or 'Author Name' in val_clean or 'Lead Name' in val_clean:
                    header_row = r_idx
                    name_col = c_idx
                    break
            if header_row != -1:
                break
        
        if header_row == -1:
            continue
            
        row_vals = [str(x).replace('\n', ' ').strip() for x in df.iloc[header_row].fillna('')]
        for c_idx, val in enumerate(row_vals):
            if val == 'AQS':
                aqs_col = c_idx
                break
                
        if name_col == -1 or aqs_col == -1:
            continue
            
        for r_idx in range(header_row + 1, len(df)):
            row = df.iloc[r_idx]
            name_val = row[name_col]
            aqs_val = row[aqs_col]
            
            if pd.isnull(name_val):
                continue
                
            name_str = str(name_val).strip()
            if not name_str or name_str.lower() in ['nan', '', 'total', 'average']:
                continue
                
            try:
                aqs_score = float(aqs_val)
                if pd.isnull(aqs_score):
                    continue
            except:
                continue
                
            rl_scores.append({
                'raw_name': name_str,
                'clean_name': clean_name(name_str),
                'clean_tokens': clean_tokens(name_str),
                'rl_aqs': aqs_score,
                'rl_name': sheet.replace('ACL-', ''),
                'file_color': color
            })

print(f"Extracted {len(rl_scores)} records from Relationship Lead sheets.")

# 3. Match and compare
matched_pairs = []

# Map our computed data by clean name and clean tokens
our_names_tokens = {}
for r in computed_data:
    if not r.get('success'):
        continue
    our_names_tokens[r['name']] = clean_tokens(r['name'])

# Find matches
for r_score in rl_scores:
    # First try exact cleaned name match
    c_name = r_score['clean_name']
    exact_match = None
    for r in computed_data:
        if not r.get('success'): continue
        if clean_name(r['name']) == c_name:
            exact_match = r
            break
            
    if exact_match:
        our_item = exact_match
        diff = our_item['computed_aqs'] - r_score['rl_aqs']
        matched_pairs.append({
            'author_name': our_item['name'],
            'rl_raw_name': r_score['raw_name'],
            'computed_aqs': our_item['computed_aqs'],
            'rl_aqs': r_score['rl_aqs'],
            'difference': diff,
            'rl_name': r_score['rl_name'],
            'file_color': r_score['file_color']
        })
    else:
        # Fallback to token-based fuzzy match
        rl_tok = r_score['clean_tokens']
        if not rl_tok:
            continue
        best_match = None
        best_intersection = 0
        for our_n, our_tok in our_names_tokens.items():
            intersect = len(rl_tok.intersection(our_tok))
            if intersect >= 2:
                union = len(rl_tok.union(our_tok))
                jaccard = intersect / union
                if jaccard > 0.5:
                    if intersect > best_intersection:
                        best_intersection = intersect
                        best_match = our_n
                        
        if best_match:
            our_item = [x for x in computed_data if x['name'] == best_match][0]
            diff = our_item['computed_aqs'] - r_score['rl_aqs']
            matched_pairs.append({
                'author_name': our_item['name'],
                'rl_raw_name': r_score['raw_name'],
                'computed_aqs': our_item['computed_aqs'],
                'rl_aqs': r_score['rl_aqs'],
                'difference': diff,
                'rl_name': r_score['rl_name'],
                'file_color': r_score['file_color']
            })

print(f"Matched {len(matched_pairs)} unique author records between our file and RL files.")

# Deduplicate matches (if an author appeared multiple times in RL files, take the average or first)
matched_df = pd.DataFrame(matched_pairs)
if not matched_df.empty:
    # Deduplicate by author_name & rl_name & file_color to avoid double-counting
    matched_df = matched_df.drop_duplicates(subset=['author_name', 'rl_name', 'file_color'])
    print(f"Deduplicated to {len(matched_df)} unique matching pairs.")
    
    # Save comparison data to JSON for reference
    comparison_file = os.path.join(SCRIPT_DIR, "aqs_comparison_analysis.json")
    matched_df.to_json(comparison_file, orient='records', indent=2)
    print(f"Saved comparison data to {comparison_file}")
    
    # Print high-level metrics
    print("\nHigh-Level Statistics:")
    print(f"  Mean Difference (Our - RL): {matched_df['difference'].mean():.2f}")
    print(f"  Mean Absolute Difference (MAE): {matched_df['difference'].abs().mean():.2f}")
    print(f"  Median Difference: {matched_df['difference'].median():.2f}")
    print(f"  Min Difference: {matched_df['difference'].min():.2f}")
    print(f"  Max Difference: {matched_df['difference'].max():.2f}")
    
    # Break down by file color
    print("\nBreakdown by RL File Color:")
    for color, group in matched_df.groupby('file_color'):
        print(f"  {color}: count={len(group)}, mean_diff={group['difference'].mean():.2f}, mae={group['difference'].abs().mean():.2f}")
        
    # Top 15 Outliers (highest absolute difference)
    print("\nTop 15 Outliers:")
    outliers = matched_df.reindex(matched_df['difference'].abs().sort_values(ascending=False).index).head(15)
    for idx, row in outliers.iterrows():
         print(f"  {row['author_name']} ({row['file_color']} - {row['rl_name']}): Computed={row['computed_aqs']}, RL={row['rl_aqs']}, Diff={row['difference']:.1f}")
else:
    print("No matches found!")
