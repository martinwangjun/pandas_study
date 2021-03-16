# -*- coding: utf-8 -*-
"""
    :author: Martin Wang(martin.wang@thermofisher.com)
    :license: MIT, see LICENSE for more details.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv('../data/gapminder.tsv', sep='\t')

# print(df.head(n=10))
# print(df.groupby('year')['pop'].mean() / 1000000)

# print(df.groupby(['continent', 'year'])[['lifeExp', 'pop']].mean())

print(df.groupby('continent')['country'].value_counts())
