import pandas as pd
import numpy as np
from pandas.core import series

scientists = pd.read_csv('../data/scientists.csv')
ages = scientists['Age']

# # 向量加减
# print(ages + ages)

# # 向量乘标量
# print(ages + 10)

# # 不同长度向量间计算
# print(ages + pd.Series([1, 100]))

# 不同长度的其他数据类型，会报错
# print(ages + np.array([1, 100]))

rev_ages = ages.sort_index(ascending=False)
print(ages)
print(rev_ages)
print(ages + rev_ages)  # 数据还是按照原来的顺序相加了
