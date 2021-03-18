import pandas as pd

df1 = pd.read_csv('../data/concat_1.csv')
df2 = pd.read_csv('../data/concat_2.csv')
df3 = pd.read_csv('../data/concat_3.csv')

new_row_series = pd.Series(['n1', 'n2', 'n3', 'n4'])
print(pd.concat([df1, new_row_series]))

# 运行结果如下，并没有和我们期望的那样增加一个新的行
#      A    B    C    D    0
# 0   a0   b0   c0   d0  NaN
# 1   a1   b1   c1   d1  NaN
# 2   a2   b2   c2   d2  NaN
# 3   a3   b3   c3   d3  NaN
# 0  NaN  NaN  NaN  NaN   n1
# 1  NaN  NaN  NaN  NaN   n2
# 2  NaN  NaN  NaN  NaN   n3
# 3  NaN  NaN  NaN  NaN   n4

new_row_series = pd.DataFrame(
    [['n1', 'n2', 'n3', 'n4']],
    columns=['A', 'B', 'C', 'D'])
print(pd.concat([df1, new_row_series]))

# 这结果，如您所愿，不过索引有问题（左下角）
#     A   B   C   D
# 0  a0  b0  c0  d0
# 1  a1  b1  c1  d1
# 2  a2  b2  c2  d2
# 3  a3  b3  c3  d3
# 0  n1  n2  n3  n4

new_row_series = pd.DataFrame(
    [['n1', 'n2', 'n3', 'n4']],
    columns=['A', 'B', 'C', 'D'])
print(pd.concat([df1, new_row_series], ignore_index=True))

# 运行结果：
#     A   B   C   D
# 0  a0  b0  c0  d0
# 1  a1  b1  c1  d1
# 2  a2  b2  c2  d2
# 3  a3  b3  c3  d3
# 4  n1  n2  n3  n4
