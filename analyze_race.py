import pandas as pd
import sklearn

# import matplotlib.pyplot as plt

# df = pd.read_csv('all.tar.gz')
df = pd.read_csv('output/Saurabh_Bhasin.csv')
# print(df)
# print(df['Event'])
df = df['Event'].str.split('-',expand=True)
print(df)

# plt.hist(df.Rank)
# plt.show()
