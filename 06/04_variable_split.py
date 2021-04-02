import pandas as pd

ebola = pd.read_csv('../data/country_timeseries.csv')
ebola_long = pd.melt(ebola, id_vars=['Date', 'Day'])
# print(ebola_long)
# variable_split = ebola_long.variable.str.split('_')
# status_values = variable_split.str.get(0)
# country_values = variable_split.str.get(1)

# ebola_long['status'] = status_values
# ebola_long['country'] = country_values

# print(ebola_long)

variable_split = ebola_long.variable.str.split('_')
# status_values = variable_split
print((variable_split.str))
