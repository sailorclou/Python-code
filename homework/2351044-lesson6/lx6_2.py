import numpy as np

# 定义支付矩阵
payoffs = {
    ('H', 'H'): (3, -3),
    ('H', 'T'): (-2, 2),
    ('T', 'H'): (-2, 2),
    ('T', 'T'): (1, -1)
}

# 初始化策略概率
jack_strategy = {'H': 0.5, 'T': 0.5}
rose_strategy = {'H': 0.5, 'T': 0.5}

# 设置学习率
learning_rate = 0.2

# 模拟100万次
num_trials = 1000000
jack_wins = 0
rose_wins = 0
jack_earn = 0

for _ in range(num_trials):
    jack_choice = np.random.choice(['H', 'T'], p=[jack_strategy['H'], jack_strategy['T']])
    rose_choice = np.random.choice(['H', 'T'], p=[rose_strategy['H'], rose_strategy['T']])

    payoff = payoffs[(jack_choice, rose_choice)]
    jack_earn += payoff[0]

    if payoff[0] > 0:
        jack_wins += 1
        # 调整 Rose 的策略（减少出 H 的概率）
        rose_strategy['H'] -= learning_rate * rose_strategy['H']
        rose_strategy['T'] += learning_rate * rose_strategy['T']
    elif payoff[0] < 0:
        rose_wins += 1
        # 调整 Jack 的策略（减少出 H 的概率）
        jack_strategy['H'] -= learning_rate * jack_strategy['H']
        jack_strategy['T'] += learning_rate * jack_strategy['T']

    # 确保策略概率在 [0, 1] 范围内
    jack_strategy['H'] = max(min(jack_strategy['H'], 1), 0)
    jack_strategy['T'] = 1 - jack_strategy['H']
    rose_strategy['H'] = max(min(rose_strategy['H'], 1), 0)
    rose_strategy['T'] = 1 - rose_strategy['H']

# 输出最终结果
print(f"Jack wins: {jack_wins}")
print(f"Rose wins: {rose_wins}")
print(jack_earn)
print(f"Final Jack strategy: H = {jack_strategy['H']}, T = {jack_strategy['T']}")
print(f"Final Rose strategy: H = {rose_strategy['H']}, T = {rose_strategy['T']}")
