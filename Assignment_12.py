import pandas as pd

df=pd.read_csv('data.csv')

print("head of data:-\n",df.head())
print("info of data:-",df.tail())
print("null values:\n",df.isnull().sum())