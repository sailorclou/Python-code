import numpy as np
import matplotlib.pyplot as plt

s0 = 5000   # 仿真试验样本标准差
sr = 1343    # 现场试验样本标准差
n = 6  # 观
c = 0.8
nr_list = []
E_list = []
x_n0 = []
y_nr = []
for n0 in range(100, 220):
    nr = ((n0-3)*sr**2)/(s0**2-(n0-3)*np.log(c))+3
    x_n0.append(n0)
    y_nr.append(nr)

    E = nr*s0**2/(6+nr)/(nr-3)
    E_list.append(round(E/200000, 2))
    nr_list.append([n0, round(nr, 2), E])

print(np.array(nr_list))
#print(E_list)
'''
# np.random.seed(0)
# colors = np.random.rand(41)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
plt.scatter(x_n0, y_nr, s=E_list, alpha=0.5)   # 面积表示后验方差相对大小
plt.xlabel('样本量n0')
plt.ylabel('等效样本量nr')
plt.show()

'''