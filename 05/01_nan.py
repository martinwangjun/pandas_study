import pandas as pd
from numpy import NaN, nan, NAN

# NaN
print(NaN == NaN)       # 与 None 不同，NaN != NaN
print(pd.isnull(NaN))
print(pd.isnull(None))
