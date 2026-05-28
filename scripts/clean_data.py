import pandas as pd

df = pd.read_csv('data/insurance_data.csv')
print("Original size:", len(df))
df.dropna(subset=['TotalPremium'], inplace=True)
df['CustomValueEstimate'] = df['CustomValueEstimate'].fillna(df['CustomValueEstimate'].median())
df.to_csv('data/insurance_data.csv', index=False)
print("Cleaned size:", len(df))
