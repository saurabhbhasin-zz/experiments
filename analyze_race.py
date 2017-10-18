import pandas as pd


df = pd.read_csv('all_entrants.csv')
print(df.head(5))

# print(df.set_index('Age Group'))
# print(df.info())
# print(df.groupby("State").describe())
