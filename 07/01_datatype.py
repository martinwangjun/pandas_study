import pandas as pd
import seaborn as sns

tips = sns.load_dataset('tips')
tips['sex_str'] = tips['sex'].astype(str)
print(tips.dtypes)
