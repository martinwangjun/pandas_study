import pandas as pd

visited_file = '../data/survey_visited.csv'

visited = pd.read_csv(visited_file)
print(visited)

visited = pd.read_csv(
    visited_file,
    keep_default_na=False)
print(visited)

visited = pd.read_csv(
    visited_file,
    na_values=[''],     # 指定那个数是 NaN，通过 List 导入， 本例中，''为NaN
    keep_default_na=False)
print(visited)
