import pandas as pd

pew = pd.read_csv('../data/pew.csv')

# print(pew.iloc[:, 0:6])

pew_long = pd.melt(pew, id_vars='religion', var_name='income', value_name='count')
print(pew_long)
