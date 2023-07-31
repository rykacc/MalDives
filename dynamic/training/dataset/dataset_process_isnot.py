import pandas as pd

# Assuming your dataset is in a CSV file
df = pd.read_csv('processed_MalMem2022.csv')

# Modify the strings in the first column
df['Category'] = df['Category'].apply(lambda x: 'Benign' if x == 'Benign' else 'Malicious')

# Drop the last column "Class"
df = df.drop(df.columns[-1], axis=1)

# Save the modified dataset to a new CSV file
df.to_csv('MalMem2022_isnot.csv', index=False)
