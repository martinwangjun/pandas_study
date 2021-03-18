import pandas as pd

df1 = pd.read_csv('../data/concat_1.csv')
df2 = pd.read_csv('../data/concat_2.csv')
df3 = pd.read_csv('../data/concat_3.csv')

# 将3个合并成一个DataFrame
concat_rows = pd.concat([df1, df2, df3])
print(concat_rows.iloc[3, 0:2])
