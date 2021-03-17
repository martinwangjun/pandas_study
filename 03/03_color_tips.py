import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

# 带颜色散点图
def record_sex(sex):
    return 0 if(sex == 'Female') else 1


tips['sex_color'] = tips['sex'].apply(record_sex)
tips_male = tips[tips['sex'] == 'Male']
tips_female = tips[tips['sex'] == 'Female']

print(tips_male)
print(tips_female)

scatter_plot = plt.figure()
axes1 = scatter_plot.add_subplot(1, 2, 1)
axes2 = scatter_plot.add_subplot(1, 2, 2)

axes1.scatter(
    x=tips_male['total_bill'],
    y=tips_male['tip'],
    s=tips_male['size'] * 10,
    # c=tips_male['sex_color'],
    label='M',
    alpha=0.5)
axes1.scatter(
    x=tips_female['total_bill'],
    y=tips_female['tip'],
    s=tips_female['size'] * 10,
    # c=tips_female['sex_color'],
    label='F',
    alpha=0.5)
axes1.set_title('Scatterplot of Total Bill vs Tip')
axes1.set_xlabel('Total Bill')
axes1.set_ylabel('Tip')

axes2.scatter(
    x=tips['total_bill'],
    y=tips['tip'],
    s=tips['size'] * 10,
    c=tips['sex_color'],
    alpha=0.5)
axes2.set_title('Scatterplot of Total Bill vs Tip')
axes2.set_xlabel('Total Bill')
axes2.set_ylabel('Tip')

axes1.legend()
plt.show()
