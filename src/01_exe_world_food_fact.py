import pandas as pd
import numpy as np


food_fact = pd.read_csv('../data/en.openfoodfacts.org.products.tsv', sep='\t')
# print(food_fact.head())

# print(food_fact.shape)

# print(food_fact.info())

# for x in food_fact.columns:
#     print(x)

# Data file is too large!
print(food_fact.values[18])
