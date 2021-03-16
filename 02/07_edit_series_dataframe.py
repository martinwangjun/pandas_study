import pandas as pd

scientists = pd.read_csv('../data/scientists.csv')

# # 添加列
# born_datetime = pd.to_datetime(scientists['Born'], format='%Y-%m-%d')
# scientists['BornAt'] = born_datetime
# print(scientists)

# # 直接更改列
# scientists['Age'] = scientists['Age'] + 1
# print(scientists)

# 删除列

print(scientists.drop(['Age'], axis=1))
