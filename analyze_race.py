import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('athlete.csv')

plt.hist(df.Rank)
plt.show()
# print(df.head(5))
# print(df.set_index('Age Group'))
# print(df.info())
# subset = df[['Projected Time', 'Age Group']]
# print(subset.head(5))
