import pandas as pd

df = pd.read_csv('all_entrants.csv')
# print(df.info())
stat = df.groupby(["AG"]).describe()
print(stat)
