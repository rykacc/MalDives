import pandas as pd

# Assuming your dataset is in a CSV file
df = pd.read_csv('processed_MalMem2022.csv')

# Filter rows where 'Category' column contains 'Trojan'
df = df[df['Category'].str.contains('Trojan')]

# Split the 'Category' column on '-' and take the second part as the family name
df['Category'] = df['Category'].apply(lambda x: x.split('-')[1] if '-' in x else 'Unknown')

# Drop the last column "Class"
df = df.drop(df.columns[-1], axis=1)

# Save the modified dataset to a new CSV file
df.to_csv('MalMem2022_trojan.csv', index=False)
