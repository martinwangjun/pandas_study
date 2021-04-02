import pandas as pd
import numpy as np

ebola = pd.read_csv('../data/country_timeseries.csv')

# # # 统计非NaN的总数
# # print(ebola.count())

# # # 统计缺失值是多少
# # missing_rows = ebola.shape[0] - ebola.count()
# # print(missing_rows)

# # print(np.count_nonzero(ebola['Cases_Guinea'].isnull()))

# # 清理缺失数据
# print(ebola.iloc[0:10, 0:5])
# print(ebola.fillna(0).iloc[0:10, 0:5])

# print(ebola.fillna(method='ffill').iloc[0:10, 0:5])
# # 前值插入的话，还是有可能会继续存在NaN
# #          Date  Day  Cases_Guinea  Cases_Liberia  Cases_SierraLeone
# # 0    1/5/2015  289        2776.0            NaN            10030.0
# # 1    1/4/2015  288        2775.0            NaN             9780.0
# # 2    1/3/2015  287        2769.0         8166.0             9722.0
# # 3    1/2/2015  286        2769.0         8157.0             9722.0
# # 4  12/31/2014  284        2730.0         8115.0             9633.0
# # 5  12/28/2014  281        2706.0         8018.0             9446.0
# # 6  12/27/2014  280        2695.0         8018.0             9409.0
# # 7  12/24/2014  277        2630.0         7977.0             9203.0
# # 8  12/21/2014  273        2597.0         7977.0             9004.0
# # 9  12/20/2014  272        2571.0         7862.0             8939.0

# print(ebola.fillna(method='bfill').iloc[:, 0:5].tail(10))
# # 后值插入的话，还是有可能会继续存在NaN
# #           Date  Day  Cases_Guinea  Cases_Liberia  Cases_SierraLeone
# # 112   4/4/2014   13         143.0           18.0                2.0
# # 113   4/1/2014   10         127.0            8.0                2.0
# # 114  3/31/2014    9         122.0            8.0                2.0
# # 115  3/29/2014    7         112.0            7.0                2.0
# # 116  3/28/2014    6         112.0            3.0                2.0
# # 117  3/27/2014    5         103.0            8.0                6.0
# # 118  3/26/2014    4          86.0            NaN                NaN
# # 119  3/25/2014    3          86.0            NaN                NaN
# # 120  3/24/2014    2          86.0            NaN                NaN
# # 121  3/22/2014    0          49.0            NaN                NaN

# print(ebola.interpolate().iloc[0:10, 0:5])
# # 插值法，method参数可选
# #          Date  Day  Cases_Guinea  Cases_Liberia  Cases_SierraLeone
# # 0    1/5/2015  289        2776.0            NaN            10030.0
# # 1    1/4/2015  288        2775.0            NaN             9780.0
# # 2    1/3/2015  287        2769.0         8166.0             9722.0
# # 3    1/2/2015  286        2749.5         8157.0             9677.5
# # 4  12/31/2014  284        2730.0         8115.0             9633.0
# # 5  12/28/2014  281        2706.0         8018.0             9446.0
# # 6  12/27/2014  280        2695.0         7997.5             9409.0
# # 7  12/24/2014  277        2630.0         7977.0             9203.0
# # 8  12/21/2014  273        2597.0         7919.5             9004.0
# # 9  12/20/2014  272        2571.0         7862.0             8939.0

# # 删除NaN
# print(ebola.dropna())
# #           Date  Day  Cases_Guinea  Cases_Liberia  Cases_SierraLeone  Cases_Nigeria  Cases_Senegal  ...  Deaths_Liberia  Deaths_SierraLeone  Deaths_Nigeria  Deaths_Senegal  Deaths_UnitedStates  Deaths_Spain  Deaths_Mali    
# # 19  11/18/2014  241        2047.0         7082.0             6190.0           20.0            1.0  ...          2963.0              1267.0             8.0             0.0                  1.0           0.0          6.0    

# # [1 rows x 18 columns]

# # NaN计算
ebola['total'] = ebola['Cases_Guinea'] + ebola['Cases_Liberia'] + ebola['Cases_SierraLeone']
print(ebola.loc[:, ['Cases_Guinea', 'Cases_Liberia', 'Cases_SierraLeone', 'total']].head(10))
#    Cases_Guinea  Cases_Liberia  Cases_SierraLeone    total
# 0        2776.0            NaN            10030.0      NaN
# 1        2775.0            NaN             9780.0      NaN
# 2        2769.0         8166.0             9722.0  20657.0
# 3           NaN         8157.0                NaN      NaN
# 4        2730.0         8115.0             9633.0  20478.0
# 5        2706.0         8018.0             9446.0  20170.0
# 6        2695.0            NaN             9409.0      NaN
# 7        2630.0         7977.0             9203.0  19810.0
# 8        2597.0            NaN             9004.0      NaN
# 9        2571.0         7862.0             8939.0  19372.0

# NaN计算忽略NaN
print(ebola.Cases_Guinea.sum(skipna=True))      # 84729.0
print(ebola.Cases_Guinea.sum(skipna=False))     # nan
