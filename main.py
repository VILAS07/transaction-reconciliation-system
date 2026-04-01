import pandas as pd

# Load CSV files
bank = pd.read_csv("bank.csv")
company = pd.read_csv("company.csv")

# Merge on TransactionID
merged = pd.merge(bank, company, on="TransactionID", how="outer", suffixes=('_bank', '_company'), indicator=True)

# Matched transactions
matched = merged[
    (merged['_merge'] == 'both') &
    (merged['Amount_bank'] == merged['Amount_company']) &
    (merged['Date_bank'] == merged['Date_company'])
]

# Mismatched transactions
mismatched = merged[
    (merged['_merge'] == 'both') &
    (
        (merged['Amount_bank'] != merged['Amount_company']) |
        (merged['Date_bank'] != merged['Date_company'])
    )
]

# Missing transactions
missing = merged[merged['_merge'] != 'both']

# Save outputs
matched.to_csv("matched.csv", index=False)
mismatched.to_csv("mismatched.csv", index=False)
missing.to_csv("missing.csv", index=False)

# Print summary
print("Matched:", len(matched))
print("Mismatched:", len(mismatched))
print("Missing:", len(missing))