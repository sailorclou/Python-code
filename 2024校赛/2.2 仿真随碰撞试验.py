import numpy as np
import matplotlib.pyplot as plt

# 给定的挠度数据
x_data = np.array([15.92, 15.84, 15.92, 16.08, 16.16, 16.00])

# 计算刚度 E = cF/x
c = 160  # mm^-1
F = 20000  # N
E_data = c * F / x_data

# 计算 E_data 的标准差 s0
s0 = np.std(E_data, ddof=1)

# 提供的历史仿真试验的标准差数据
sr_data = np.array([5010, 6005, 5050, 6007, 3010, 5007, 4032, 3356, 7354, 6289,
                    5001, 5567, 6322, 5378, 3804, 5739, 6382, 4388, 5282, 3782,
                    4782, 4367, 4892, 6389, 5738, 5322, 6271, 7282, 4285, 3421])

# 计算 sr 的平均值
sr = np.mean(sr_data)

# 设定 n0 和 c 的值来估计 nr 的趋势（示例：n0 从 6 到 30）
n0_values = np.arange(6, 31)  # Adjusting n0 to start from 6 since the formula uses (n0-3)
nr_values = []

for n0 in n0_values:
    nr = ((n0 - 3) * sr**2) / (s0**2 - (n0 - 3) * np.log(c)) + 3
    nr_values.append(nr)

print(nr_values, n0_values, s0, sr)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(10, 6))
plt.plot(n0_values, nr_values, marker='o', linestyle='-')   # 面积表示后验方差相对大小
plt.xlabel('汽车碰撞数据量n0')
plt.ylabel('仿真样本量样本量nr')
plt.title('仿真样本量随汽车碰撞试验量变化曲线')
plt.axis([5,32,30,350])
plt.grid(True)
plt.show()

