import pandas as pd

billboard = pd.read_csv('../data/billboard.csv')

# print(billboard.iloc[0:5, 0:16])

billboard_long = pd.melt(
    billboard, 
    id_vars=['year', 'artist', 'track', 'time', 'date.entered'],
    var_name='Week',
    value_name='Rating')
print(billboard_long.iloc[:, :])
