import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# from data_load import mat_dataset1
import torch
import scipy.io as scio

#数据分布直方图
# error = pd.read_csv(r"C:\Document\ourdata\PPT\error_ours.csv", header=None)
#
# hist, bin_edges = np.histogram(error)
# width = (bin_edges[1] - bin_edges[0]) * 0.8
# plt.bar(bin_edges[1:], hist/max(hist), width=width, color='#445437')
#
# cdf = np.cumsum(hist/sum(hist))
# plt.plot(bin_edges[1:], cdf, '-*', color='#FFCC00')
#
# plt.grid()
#
# plt.show()

## CDF图
from matplotlib.font_manager import FontProperties

#设置汉字格式
font = FontProperties(fname=r"C:\Windows\Fonts\AdobeHeitiStd-Regular.otf")
data = pd.read_csv(r"C:\Document\ourdata\PPT2\tridata.csv", header=None)
Data = data.iloc[:, 4]
# data = data.T
denominator = len(data)  # 分母数量
# Data = pd.Series(data)  # 将数据转换为Series利用分组频数计算
Fre = Data.value_counts()
Fre_sort = Fre.sort_index(axis=0, ascending=True)
Fre_df = Fre_sort.reset_index()  # 将Series数据转换为DataFrame
Fre_df = Fre_df/denominator  # 转换成概率
Fre_df.columns = ['Rds', 'Fre']
Fre_df['cumsum'] = np.cumsum(Fre_df['Fre'])
plot = plt.figure()
ax1 = plot.subplot(1, 1, 1)
ax1.plot(Fre_df['Rds'], Fre_df['cumsum'])
ax1.set_title("传统算法估计与真值差小于2的样本用神经网络估计误差的CDF", fontproperties=font)
ax1.set_xlabel("Error")
ax1.set_ylabel("Probability")
# ax1.set_xlim(0.1,0.5)
plt.show()

## 数据分布
# from matplotlib.font_manager import FontProperties
#
# font = FontProperties(fname=r"C:\Windows\Fonts\AdobeHeitiStd-Regular.otf")
#
# # dict_labels1 = scio.loadmat(r"C:\Document\ourdata\mat\window401\traininglabel.mat")
# # label1 = dict_labels1['traininglabel']
# # dict_labels2 = scio.loadmat(r"C:\Document\ourdata\mat\window401\testlabel.mat")
# # label2 = dict_labels2['testlabel']
# #
# # label = np.concatenate((label1, label2), axis=0)
# data = pd.read_csv(r"C:\Document\ourdata\PPT2\tridata.csv", header=None)
# Data = data.iloc[:, 7]
# plt.hist(Data, bins=8, color='#FFCC00', edgecolor='white')
# # 设置坐标轴标签和标题
# plt.xlabel("次/分钟", fontproperties=font, size=13)
# plt.ylabel("数量", fontproperties=font, size=13)
# plt.title("呼吸分布直方图", fontproperties=font, size=13)
# plt.show()