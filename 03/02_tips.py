import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
# print(tips)

# # 绘制直方图
# fig = plt.figure()
# axes1 = fig.add_subplot(1, 1, 1)    # 设定图表大小
# axes1.hist(tips['total_bill'], bins=10)
# axes1.set_title('Histogram of Total Bill')
# axes1.set_xlabel('Total Bill')
# axes1.set_ylabel('Frequency')
# plt.show()

# # 绘制散点图
# scatter_plot = plt.figure()
# axes1 = scatter_plot.add_subplot(1, 1, 1)
# axes1.scatter(tips['total_bill'], tips['tip'])
# axes1.set_title('Scatterplot of Total Bill vs Tip')
# axes1.set_xlabel('Total Bill')
# axes1.set_ylabel('Tip')
# plt.show()

# # 箱线图
# box_plot = plt.figure()
# axes1 = box_plot.add_subplot(1, 1, 1)
# axes1.boxplot(
#     [
#         tips[tips['sex'] == 'Female']['tip'],
#         tips[tips['sex'] == 'Male']['tip'],
#     ],
#     labels=['女', '男']
# )
# axes1.set_title('Boxplot of Tips by Sex')
# axes1.set_xlabel('性别')
# axes1.set_ylabel('小费')
# plt.rcParams['font.sans-serif'] = ['SimHei']        # 正常显示中文
# plt.rcParams['axes.unicode_minus'] = False          # 正常显示负号
# plt.show()

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
    # label=[l for c, l in set(zip(tips['sex_color'], tips['sex']))],
    alpha=0.5)
axes2.set_title('Scatterplot of Total Bill vs Tip')
axes2.set_xlabel('Total Bill')
axes2.set_ylabel('Tip')

axes1.legend()
# axes2.legend()
plt.show()

# x_values = [6.2, 3.6, 7.3, 3.2, 2.7]
# y_values = [1.5, 3.2, 5.4, 3.1, 2.8]
# colors = [1, 1, 0, 1, -1]
# labels = ["a", "a", "b", "a", "c"]
# clset = set(zip(colors, labels))

# ax = plt.gca()
# sc = ax.scatter(x_values, y_values, c=colors, cmap="brg")

# handles = [plt.plot([], color=sc.get_cmap()(sc.norm(c)), ls="", marker="o")[0] for c, l in clset]
# labels = [l for d, l in clset]
# ax.legend(handles, labels)

# plt.show()
