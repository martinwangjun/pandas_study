import pandas as pd

person = pd.read_csv('../data/survey_person.csv')
site = pd.read_csv('../data/survey_site.csv')
survey = pd.read_csv('../data/survey_survey.csv')
visited = pd.read_csv('../data/survey_visited.csv')

# print(person)
print(site)
# print(survey)
# print(visited)

visited_subset = visited.loc[[0, 2, 6], ]
print(visited_subset)

# 在左边的site表中取name，右边的visited_subset表中取site，这2个字段mapping
o2o_merge = site.merge(visited_subset, left_on='name', right_on='site')
print(o2o_merge)

# 运行结果：
#     name    lat    long  ident   site       dated
# 0   DR-1 -49.85 -128.57    619   DR-1  1927-02-08
# 1   DR-3 -47.15 -126.72    734   DR-3  1939-01-07
# 2  MSK-4 -48.87 -123.40    837  MSK-4  1932-01-14

# 在左边的site表中取name，右边的visited_subset表中取site，这2个字段mapping
o2o_merge = site.merge(visited, left_on='name', right_on='site')
print(o2o_merge)

# 运行结果：
#     name    lat    long  ident   site       dated
# 0   DR-1 -49.85 -128.57    619   DR-1  1927-02-08
# 1   DR-1 -49.85 -128.57    622   DR-1  1927-02-10
# 2   DR-1 -49.85 -128.57    844   DR-1  1932-03-22
# 3   DR-3 -47.15 -126.72    734   DR-3  1939-01-07
# 4   DR-3 -47.15 -126.72    735   DR-3  1930-01-12
# 5   DR-3 -47.15 -126.72    751   DR-3  1930-02-26
# 6   DR-3 -47.15 -126.72    752   DR-3         NaN
# 7  MSK-4 -48.87 -123.40    837  MSK-4  1932-01-14

ps = person.merge(survey, left_on='ident', right_on='person')
print(ps)

vs = visited.merge(survey, left_on='ident', right_on='taken')
print(vs)

vs_ps = ps.merge(vs, left_on=['ident', 'taken', 'quant', 'reading'], right_on=['person', 'ident', 'quant', 'reading'])
print(vs_ps)
