import pandas as pd

scientists = pd.read_csv('../data/scientists.csv')

# 获取基本统计量
print(scientists['Age'].describe())

# 获取年龄>60
ages = scientists['Age']
# print(ages[ages > 60])

# 使用Boolean变量
print(ages[[True, True, False, False, False, False, False, False]])
