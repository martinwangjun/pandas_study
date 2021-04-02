# P115
import pandas as pd

ebola = pd.read_csv('../data/country_timeseries.csv')
print(ebola.iloc[:5, [0, 1, 2, 3, 10, 11]])

ebola_long = pd.melt(ebola, id_vars=['Date', 'Day'])
print(ebola_long)
ebola_long.to_excel('../output/ebola.xlsx', index=False)
