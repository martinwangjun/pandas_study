import pandas as pd
import numpy as np


# Load data to chipotle
chipotle = pd.read_csv('../data/chipotle.tsv', sep='\t')

# # Get first 10 rows
# print(chipotle.head(10))

# # Rows and columns in the dataset
# print(chipotle.shape)

# print(chipotle.shape[1])

# print(chipotle.columns)

# print(chipotle.index)

# Which was the most-ordered item?
# print(chipotle.groupby('item_name').sum().sort_values(['quantity'], ascending=False).head(1))

# print(chipotle.groupby('choice_description').sum().sort_values(['quantity'], ascending=False).head(1))

# How many items were ordered in total?
print(chipotle.quantity.sum())
