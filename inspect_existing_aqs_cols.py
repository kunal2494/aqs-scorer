import pandas as pd

existing_aqs_path = "/Users/fincent/Downloads/Existing Author AQS.xlsx"
df = pd.read_excel(existing_aqs_path, sheet_name="Export")

print("Columns in Excel:")
print(list(df.columns))

print("\nRow for Ken Huang:")
print(df[df['Author Name'].str.contains('Ken Huang', na=False, case=False)])

print("\nRow for Hemang Doshi:")
print(df[df['Author Name'].str.contains('Hemang Doshi', na=False, case=False)])
