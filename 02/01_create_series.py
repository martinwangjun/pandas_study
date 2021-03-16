import pandas as pd

# Series 中的每个元素的数据类型必须相同
# 如果“不同”，则会转换object形式
s = pd.Series(['banana', 2])    # 传入 list
print(s)
s = pd.Series(('banana', 2))    # 传入 tuple
print(s)
s = pd.Series(
    {
        'name': 'Linda',
        'location': 'Wuxi',
    }
)                               # 传入 dictionary
print(s)

# 指定每个元素的名称
s = pd.Series(['Martin', 'Shanghai'], ['name', 'location'])
print(s)
