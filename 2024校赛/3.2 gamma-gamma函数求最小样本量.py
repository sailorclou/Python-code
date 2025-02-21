import numpy as np
from scipy.stats import gamma
import matplotlib.pyplot as plt

nr = 16.5
s0 = 5000

a = (nr - 1) / 2  # 形状参数
b = s0 ** 2 / 19562 / nr**2  # 尺度参数  # 此处第一问为

# 创建gamma-gamma分布对象
gamma_gamma_dist = gamma(a, scale=b)

# 计算累积分布函数
x_n = []
y_cdf = []
cdf_values = []
for n in range(0, 300):
    x_n.append(n)
    #    x = (n - 1) / 2
    cdf = gamma_gamma_dist.cdf(n)
    y_cdf.append(cdf)
    cdf_values.append([int(n), cdf])
    if cdf >= 0.05:
        print(f"最少试验样本量为{n}")
        break

print(cdf_values)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
plt.scatter(x_n, y_cdf, alpha=0.5)
plt.xlabel('样本量n')
plt.ylabel('函数值')
plt.show()