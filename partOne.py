import pandas as pd
df = pd.read_csv('prompts.csv')

print('Про промты')
print(df.head())

print(df.info())

print(df.describe())

df = pd.read_csv('Wine dataset.csv')

print ('Про вино')

print(df.head())

print(df.info())

print(df.describe())



