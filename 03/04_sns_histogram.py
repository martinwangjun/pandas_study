import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

g = sns.displot(data=tips, x='total_bill', kind='hist')
g.set_axis_labels('Total Bill')
ax = g.ax
ax.set_title('Total Bill Histogram with Density Plot')
plt.show()
