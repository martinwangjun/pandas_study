import pandas as pd
scientists = pd.read_csv('../data/scientists.csv')

# 获取所有的年龄大于平均年龄的科学家的DataFrame
# print(scientists[scientists['Age'] > scientists['Age'].mean()])

# 《Python数据分析 活用Pandas库》P34页说得不一定对，如果长度不一致，会报错
# print(scientists.loc[[True, False, True, True, True, False, True, True]])

first_half = scientists[:4]
print(first_half)

second_half = scientists[4:]
print(second_half)

print(scientists * 2)
