import pandas as pd
# import matplotlib.pyplot as plt

df = pd.read_csv('all_entrants.csv')
df = df[['First Name', 'Last Name', 'Projected Time']]
print(df.head(5))

# print(df.head(5))
# print(df.set_index('Age Group'))
# print(df.info())
# subset = df[['Projected Time', 'Age Group']]
# print(subset.head(5))
