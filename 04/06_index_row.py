import pandas as pd

df1 = pd.read_csv('../data/concat_1.csv')
df2 = pd.read_csv('../data/concat_2.csv')
df3 = pd.read_csv('../data/concat_3.csv')

df1.index = [0, 1, 2, 3]
df2.index = [4, 5, 6, 7]
df3.index = [0, 2, 5, 7]

col_concat_df = pd.concat([df1, df2, df3], axis=1)
print(col_concat_df)

# 运行结果：
#      A    B    C    D    A    B    C    D    A    B    C    D
# 0   a0   b0   c0   d0  NaN  NaN  NaN  NaN   a8   b8   c8   d8
# 1   a1   b1   c1   d1  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
# 2   a2   b2   c2   d2  NaN  NaN  NaN  NaN   a9   b9   c9   d9
# 3   a3   b3   c3   d3  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
# 4  NaN  NaN  NaN  NaN   a4   b4   c4   d4  NaN  NaN  NaN  NaN
# 5  NaN  NaN  NaN  NaN   a5   b5   c5   d5  a10  b10  c10  d10
# 6  NaN  NaN  NaN  NaN   a6   b6   c6   d6  NaN  NaN  NaN  NaN
# 7  NaN  NaN  NaN  NaN   a7   b7   c7   d7  a11  b11  c11  d11

col_concat_df = pd.concat([df1, df3], axis=1, join='inner')
print(col_concat_df)

# 运行结果：
#     A   B   C   D   A   B   C   D
# 0  a0  b0  c0  d0  a8  b8  c8  d8
# 2  a2  b2  c2  d2  a9  b9  c9  d9
