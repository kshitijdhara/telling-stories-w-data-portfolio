import pandas as pd

# Load the CSV file
df = pd.read_csv('NYC_baby_names.csv')

# Standardize the 'NM' column to lowercase
df['NM'] = df['NM'].str.lower()

# Group by all columns except 'CNT', sum the counts
df = df.groupby(['BRTH_YR', 'GNDR', 'ETHCTY', 'NM', 'RNK'], as_index=False)['CNT'].sum()

# Save the modified DataFrame to a new CSV file
df.to_csv('modified_NYC_baby_names.csv', index=False)
