from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

# 指标总体均值数据
mean_data = np.array([
    2.0233, 2.0315, 1.9614, 2.0322, 2.0069, 1.9588, 1.9751, 1.9992, 2.0362, 2.0368,
    1.9642, 2.0374, 2.0361, 1.9937, 2.0220, 1.9628, 1.9880, 2.0324, 2.0213, 2.0364,
    2.0090, 1.9532, 2.0264, 2.0341, 2.0111, 2.0189, 2.0169, 1.9853, 2.0090, 1.9654
])
mean_data = mean_data * 1e+5
# 计算均值的估计值
mean_estimate = np.mean(mean_data)

# 计算方差的估计值
var_estimate = np.var(mean_data, ddof=1)  # 使用样本方差，自由度为 n-1

# print("均值的估计值:", mean_estimate)
#print("标准差差的估计值:", np.sqrt(var_estimate))  # 0.028

# 使用估计的均值和方差构建正态分布对象(代理模型）
proxy_model = norm(loc=mean_estimate, scale=np.sqrt(var_estimate))

alpha = 0.05
epsilon1 = 5000
epsilon2 = 4000
lower_bound = mean_estimate - epsilon1
upper_bound = mean_estimate + epsilon2

# 计算所需的仿真试验样本量，并限制在指定范围内
def calculate_simulation_samples(mean, alpha, epsilon1, epsilon2, proxy_model, min_samples, max_samples):
    # 计算下限和上限

    lower_bound = mean - epsilon1
    upper_bound = mean + epsilon2

    # 计算下限和上限的累积概率
    lower_cdf = proxy_model.cdf(lower_bound)
    upper_cdf = proxy_model.cdf(upper_bound)

    # 计算区间概率
    interval_probability = upper_cdf - lower_cdf

    # 计算仿真样本量
    simulation_samples1 = min_samples * interval_probability
    simulation_samples2 = max_samples * interval_probability

    # 将仿真样本量限制在指定范围内
    simulation_samples = max(simulation_samples1, min(simulation_samples2, max_samples))

    return simulation_samples


# 计算仿真样本量，并限制在指定范围内
simulation_samples = calculate_simulation_samples(mean_estimate, alpha, epsilon1, epsilon2, proxy_model, 128, 211)
print("仿真样本量:", simulation_samples)

# 寻找使仿真样本量最小化的最优指标总体均值
#result = minimize_scalar(lambda x: calculate_simulation_samples(x, alpha, epsilon1, epsilon2, proxy_model,128, 211))
# 重新定义目标函数，确保输入参数的顺序和函数签名一致
def objective_function(mean, alpha, epsilon1, epsilon2, proxy_model, min_samples, max_samples):
    return calculate_simulation_samples(mean, alpha, epsilon1, epsilon2, proxy_model, min_samples, max_samples)

# 使用全局优化方法来寻找最优解
result = minimize_scalar(objective_function, bounds=(lower_bound, upper_bound), args=(alpha, epsilon1, epsilon2, proxy_model, 128, 211), method='bounded')
# 最优指标总体均值
optimal_mean = result.x
print("最优指标总体均值:", optimal_mean)

# 生成一组 x 值，用于绘制概率密度函数和累积分布函数图
x_values = np.linspace(mean_estimate - 4*np.sqrt(var_estimate), mean_estimate + 4*np.sqrt(var_estimate), 1000)

# 计算概率密度函数值
pdf_values = proxy_model.pdf(x_values)

# 计算累积分布函数值
cdf_values = proxy_model.cdf(x_values)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
# 绘制概率密度函数图
plt.figure(figsize=(10, 5))
plt.plot(x_values, pdf_values, label='概率密度函数 (PDF)')
plt.fill_between(x_values, pdf_values, color='skyblue', alpha=0.3)
plt.xlabel('刚度指标总体均值')
plt.ylabel('概率密度')
plt.title('代理模型的概率密度函数')
plt.legend()
plt.grid(True)
plt.show()

# 绘制累积分布函数图
plt.figure(figsize=(10, 5))
plt.plot(x_values, cdf_values, label='累积分布函数 (CDF)')
plt.xlabel('刚度指标总体均值')
plt.ylabel('累积概率')
plt.title('代理模型的累积分布函数')
plt.legend()
plt.grid(True)
plt.show()
