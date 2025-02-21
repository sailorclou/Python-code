'''
# 01 质因数分解
def IntegerDecomp2Prime(n: int) -> list:
    prime_factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 1
    return prime_factors


print(IntegerDecomp2Prime(6384))


# 02 验证哥德巴赫猜想
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def Goldbach(n):
    prime_paris = []
    for i in range(2, int(n / 2 + 1)):
        if is_prime(i) and is_prime(n - i):
            prime_paris.append((i, n - i))
    return prime_paris


n = int(input("请输入一个大于2的偶数："))
print(Goldbach(n))


# 03 求最大公约数和最小公倍数
def gcd_lcm(m, n):
    if m == n:
       gcd = m
    else:
       gcd, l = gcd_lcm(n, m - n) if m > n else gcd_lcm(m, n - m)
    lcm = int(m * n / gcd)

    return gcd, lcm


m = int(input("请输入数m："))
n = int(input("请输入数n："))
gcd, lcm = gcd_lcm(m, n)
print('{0}和{1}的最大公约数为{2}，最小公倍数为{3}'.format(m, n, gcd, lcm))


# 04 找出数据的峰值
def peak(time, list1, n = 10):
    timepeak = []
    listpeak = []
    for i in range(1, 999):
        if list1[i] > list1[i - 1] and list1[i] > list1[i + 1]:
            timepeak.append(time[i])
            listpeak.append(list1[i])
    if len(listpeak) > n:
        flag = True
        while (flag):
            p = 0
            for j in range(len(listpeak)-1):
                if listpeak[j] < listpeak[j + 1]:
                    peak = listpeak[j + 1]
                    time = timepeak[j + 1]
                    listpeak[j + 1] = listpeak[j]
                    timepeak[j + 1] = timepeak[j]
                    listpeak[j] = peak
                    timepeak[j] = time
            for k in range(len(listpeak)-1):
                if listpeak[k] < listpeak[k + 1]:
                    flag = True
                    p += 1
                    break
            if p == 0:
                break

        listpeak = listpeak[:10]
        timepeak = timepeak[:10]

    return timepeak, listpeak


#测试1
# 数据准备
import math
time = range(0,1000)
list2 = []
for each in time:
    list2.append(math.sin(0.001*each*2*math.pi*3)*math.sin(5*0.02*each))

timepeak, listpeak = peak(time, list2, 10)
#peak(time,list2,10)

#以下代码是绘图给同学们看看曲线啥样
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.plot(time, list2)
plt.plot(timepeak, listpeak, 'ks')
plt.grid()
plt.show()
'''

# 05 找出所有整数
def FindNumber(s:str)->list:
    s0 = s.split()
    num = []
    for word in s0:
        if word.isdigit():
            num.append(int(word))
    return num

teststr1 = "I love tongji for 100 years. He loves tongji for 99 years."
print(FindNumber(teststr1))

