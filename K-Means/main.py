from K_Means import k_means
import matplotlib.pyplot as plt
import json


# 数据集
dataset_10 = [
    [1, 1],
    [2, 1],
    [3, 1],
    [1, 2],
    [4, 2],
    [5, 2],
    [3, 3],
    [2, 4],
    [3, 4],
    [5, 4]
]

dataset_20 = [
    [1, 1],
    [2, 1],
    [3, 1],
    [1, 2],
    [4, 2],
    [5, 2],
    [3, 3],
    [2, 4],
    [3, 4],
    [5, 4]
]

# print(dataset)

# 使用10个数据，分3类，最多迭代20次
C, labels = k_means(dataset_10, 3, 20)
print(C)
print(labels)

# 绘图代码
############################################################
colValue = ['r', 'y', 'g', 'b', 'c', 'k', 'm']
for i in range(len(C)):
    coo_X = []  # x坐标列表
    coo_Y = []  # y坐标列表
    for j in range(len(C[i])):
        coo_X.append(C[i][j][0])
        coo_Y.append(C[i][j][1])
    plt.scatter(coo_X, coo_Y, marker='o',
                color=colValue[i % len(colValue)], label=i)
############################################################

plt.show()
