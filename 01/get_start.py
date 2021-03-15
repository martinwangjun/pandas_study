# -*- coding: utf-8 -*-
"""
    :author: Martin Wang(martin.wang@thermofisher.com)
    :license: MIT, see LICENSE for more details.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv('../data/gapminder.tsv', sep='\t')


# print(type(df.columns))

# print(type(df))
# print(df.shape)
# print(df.columns)
# print(df.dtypes)
# print(df.info())

# country_df = df['country']
# print(country_df.head())
# print(country_df.head(10))
# print(country_df.tail())
# print(country_df.tail(10))

# subset = df[['country', 'continent', 'year']]
# print(subset.head())

# subset = df[[1, 2]]
# print(subset.head())

# global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
# # print(global_yearly_life_expectancy)
# global_yearly_life_expectancy.plot()
# plt.show()
# print(pd.show_versions(as_json=True))
