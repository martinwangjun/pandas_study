import pandas as pd

df1 = pd.read_csv('../data/concat_1.csv')
df2 = pd.read_csv('../data/concat_2.csv')
df3 = pd.read_csv('../data/concat_3.csv')

df1.columns = ['A', 'B', 'C', 'D']
df2.columns = ['E', 'F', 'G', 'H']
df3.columns = ['A', 'C', 'F', 'H']

print(df1)
print(df2)
print(df3)

concat_df = pd.concat([df1, df2, df3])
print(concat_df)

# 运行结果：
#      A    B    C    D    E    F    G    H
# 0   a0   b0   c0   d0  NaN  NaN  NaN  NaN
# 1   a1   b1   c1   d1  NaN  NaN  NaN  NaN
# 2   a2   b2   c2   d2  NaN  NaN  NaN  NaN
# 3   a3   b3   c3   d3  NaN  NaN  NaN  NaN
# 0  NaN  NaN  NaN  NaN   a4   b4   c4   d4
# 1  NaN  NaN  NaN  NaN   a5   b5   c5   d5
# 2  NaN  NaN  NaN  NaN   a6   b6   c6   d6
# 3  NaN  NaN  NaN  NaN   a7   b7   c7   d7
# 0   a8  NaN   b8  NaN  NaN   c8  NaN   d8
# 1   a9  NaN   b9  NaN  NaN   c9  NaN   d9
# 2  a10  NaN  b10  NaN  NaN  c10  NaN  d10
# 3  a11  NaN  b11  NaN  NaN  c11  NaN  d11

concat_df = pd.concat([df1, df3], join='inner')
print(concat_df)

# 运行结果：
#      A    C
# 0   a0   c0
# 1   a1   c1
# 2   a2   c2
# 3   a3   c3
# 0   a8   b8
# 1   a9   b9
# 2  a10  b10
# 3  a11  b11

concat_df = pd.concat([df1, df3], join='outer')
print(concat_df)

# 运行结果：
#      A    B    C    D    F    H
# 0   a0   b0   c0   d0  NaN  NaN
# 1   a1   b1   c1   d1  NaN  NaN
# 2   a2   b2   c2   d2  NaN  NaN
# 3   a3   b3   c3   d3  NaN  NaN
# 0   a8  NaN   b8  NaN   c8   d8
# 1   a9  NaN   b9  NaN   c9   d9
# 2  a10  NaN  b10  NaN  c10  d10
# 3  a11  NaN  b11  NaN  c11  d11
