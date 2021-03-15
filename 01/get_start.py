# -*- coding: utf-8 -*-
"""
    :author: Martin Wang(martin.wang@thermofisher.com)
    :license: MIT, see LICENSE for more details.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv('../data/gapminder.tsv', sep='\t')

# # print(df.head())    # 获取前5行
# # print(df.loc[1])    # 获取第1行的对象
# # print(df.loc[99])   # 获取第100行的对象
# # print(df.tail(1))   # 获取最后1行

# # print(df.shape[0])

# # qty_of_list = df.shape[0]
# # print(df.loc[qty_of_list - 1])

# # print(df['country'].iloc[0: 5])
# # print(df.loc[1:3, ['country', 'year']])
# # print(df.iloc[:, list(range(3, 7))])

# # print(df.iloc[:, 0:6:2])

# # print(df.iloc[[0, 1, 3], ::])

# print(df.loc[42, 'year'])
