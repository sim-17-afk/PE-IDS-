# implementation of dataset opration on pandas
import pandas as pd

df=pd.read_csv('data.csv')

print("head of data:-\n",df.head())
print("info of data:-",df.tail())
print("null values:\n",df.isnull().sum())

print("Name Column:\n", df['Name'])
print("Multiple Columns:\n", df[['Name', 'Age']])
print("Sorted by Age:\n", df.sort_values('Age'))
print("older than 25:\n", df[df['Age'] > 21])