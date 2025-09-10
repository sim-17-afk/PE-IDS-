# Assignment 7: Implementation of Data Operations in Pandas

import pandas as pd

# Create a sample dictionary of data
data = {
    'Name': ['Simran', 'Rohan', 'Aditi', 'Karan', 'Meera'],
    'Age': [21, 22, 20, 23, 21],
    'Department': ['CSE', 'AIML', 'CSE', 'ENTC', 'CSE'],
    'Marks': [88, 75, 90, 60, 95]
}

# Create DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# 1. Selecting Columns
print("\n--- Selecting Columns ---")
print("Names:\n", df['Name'])
print("Ages:\n", df.Age)

# 2. Selecting Rows
print("\n--- Selecting Rows ---")
print("First 3 Rows:\n", df.head(3))
print("Row by Index (loc):\n", df.loc[2])
print("Row by Position (iloc):\n", df.iloc[1])

# 3. Adding a New Column
df['Grade'] = ['A', 'B', 'A', 'C', 'A']
print("\n--- After Adding Grade Column ---\n", df)

# 4. Updating Values
df.at[3, 'Marks'] = 65
print("\n--- After Updating Karan's Marks ---\n", df)

# 5. Deleting a Column
df = df.drop(columns=['Grade'])
print("\n--- After Dropping Grade Column ---\n", df)

# 6. Basic Statistics
print("\n--- Basic Statistics ---")
print("Description:\n", df.describe())
print("Average Age:", df['Age'].mean())
print("Maximum Marks:", df['Marks'].max())
