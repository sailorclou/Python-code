import numpy as np
from scipy.optimize import minimize
from scipy.stats import invgamma
import matplotlib.pyplot as plt

x_ = 5183.8  # 历史仿真试验求出的标准差数据均值
s = 1472  # 历史数据标准差
alpha = 2 + x_**2 / s**2
beta = x_ * (1 + x_**2 / s**2)

# 给定的参数
epsilon_1 = 5000
epsilon_2 = 4000
a = 0.05
p = 0.5  # 历史仿真试验的可信度

# 目标函数
def objective(params):
    alpha = params[0]
    beta = params[1]
    # 计算逆伽马分布的累积分布函数在指定区间内的概率
    cdf_lower = invgamma.cdf(epsilon_1, alpha, scale=beta)
    cdf_upper = invgamma.cdf(epsilon_2, alpha, scale=beta)
    # 计算与目标概率的差值的平方和
    diff_lower = (cdf_lower - (1 - a)) ** 2
    diff_upper = (cdf_upper - (1 - a)) ** 2
    return diff_lower + diff_upper


# 初始参数值
initial_guess = [alpha, beta]  # 初始的 alpha 和 beta 值

# 最小化目标函数，找到使得目标函数最小化的参数值
result = minimize(objective, np.array(initial_guess))

# 输出结果
alpha_optimal, beta_optimal = result.x
print("最优参数值:")
print("alpha:", alpha_optimal)  # 24.70016690238035
print("beta:", beta_optimal)   # 69471.67592918793

# 生成一组 x 值，用于绘制概率密度函数和累积分布函数图
x_values = np.linspace(0, 8000, 1000)

# 计算概率密度函数值
pdf_values = invgamma.pdf(x_values, alpha_optimal, scale=beta_optimal)

# 计算累积分布函数值
cdf_values = invgamma.cdf(x_values, alpha_optimal, scale=beta_optimal)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
# 绘制概率密度函数图
plt.figure(figsize=(10, 5))
plt.plot(x_values, pdf_values, label='概率密度函数 (PDF)')
plt.fill_between(x_values, pdf_values, color='skyblue', alpha=0.3)
plt.xlabel('方差')
plt.ylabel('概率密度')
plt.title('逆伽马分布的概率密度函数')
plt.legend()
plt.grid(True)
plt.show()

# 绘制累积分布函数图
plt.figure(figsize=(10, 5))
plt.plot(x_values, cdf_values, label='累积分布函数 (CDF)')
plt.xlabel('方差')
plt.ylabel('累积概率')
plt.title('逆伽马分布的累积分布函数')
plt.legend()
plt.grid(True)
plt.show()