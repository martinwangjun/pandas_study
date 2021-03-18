import pandas as pd

df1 = pd.read_csv('../data/concat_1.csv')
df2 = pd.read_csv('../data/concat_2.csv')
df3 = pd.read_csv('../data/concat_3.csv')

# df = df1.append(df2)
# print(df)

# # 运行结果：
# #     A   B   C   D
# # 0  a0  b0  c0  d0
# # 1  a1  b1  c1  d1
# # 2  a2  b2  c2  d2
# # 3  a3  b3  c3  d3
# # 0  a4  b4  c4  d4
# # 1  a5  b5  c5  d5
# # 2  a6  b6  c6  d6
# # 3  a7  b7  c7  d7

# new_row_data = pd.DataFrame(
#     [['n1', 'n2', 'n3', 'n4']],
#     columns=['A', 'B', 'C', 'D'])
# print(df1.append(pd.DataFrame(new_row_data), ignore_index=True))

df = df1.append(df2, ignore_index=True)
print(df)

# 运行结果：
#     A   B   C   D
# 0  a0  b0  c0  d0
# 1  a1  b1  c1  d1
# 2  a2  b2  c2  d2
# 3  a3  b3  c3  d3
# 4  a4  b4  c4  d4
# 5  a5  b5  c5  d5
# 6  a6  b6  c6  d6
# 7  a7  b7  c7  d7