import pandas as pd

scientists = pd.read_csv('../data/scientists.csv')
names = scientists['Name']

# names.to_pickle('../output/scientists_name.txt')
# scientists_name = pd.read_pickle('../output/scientists_name.txt')
# print(scientists_name)

# # 指定'|'为分隔符
# names.to_csv('../output/scientists_name.txt', sep='|', index=False)

# Excel
# 保存 Series 到Excel，不能直接存，要转成 DataFrame
names.to_frame().to_excel('../output/names.xlsx')

# 保存 DataFrame 到 Excel
scientists.to_excel('../output/scientists.xlsx', sheet_name='Scientists', index=False, encoding='utf8')
