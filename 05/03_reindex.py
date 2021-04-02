import pandas as pd

gapminder = pd.read_csv('../data/gapminder.tsv', sep='\t')

life_exp = gapminder.groupby(['year'])['lifeExp'].mean()
# print(life_exp.loc[range(2000, 2010), ])

y2000 = life_exp[life_exp.index > 2000]
print(y2000)

print(y2000.reindex(range(2000, 2010)))
