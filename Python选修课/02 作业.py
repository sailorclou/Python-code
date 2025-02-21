# 01 水仙花数
for i in range(1, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            a = i**3 + j**3 + k**3
            if a == int(f'{i}{j}{k}'):
                print(a)

# 02 两个数公因数
a, b = map(int, input('请输入两个整数，并用空格隔开：').split())
if a < b:
    a, b = b, a
for i in range(1, b + 1):
    if a % i == 0 and b % i == 0:
        print(i)

# 03 身份证最后一位
'''
Id17 = []
for i in range(17):
     a = int(input(f'请输入第{i+1}位：'))
     Id17.append(a)
'''
Id17 = input("身份证前17位：")
Id__ = []
Id18 = 0
a = 0
weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
for p in Id17:
    p = int(p)
    Id__.append(p)
for i, x in enumerate(Id__):
    for j, y in enumerate(Id__):
        if i == j:
            a += (x * y)
b = a % 11
remainder = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Id_18 = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
for k in range(0, 11):
    if b == remainder[k]:
        Id__.append(Id_18[k])
        Id18 = Id__
print('完整的身份证号为：', ''.join(map(str, Id18)))
'''
gpt
Id17 = input("请输入身份证前17位：")
Id__ = []
# 将前17位身份证号码转换成列表
for p in Id17:
    p = int(p)
    Id__.append(p)
# 系数
weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
# 计算加权和
a = sum(x * y for x, y in zip(Id__, weight))
# 计算余数
b = a % 11
# 余数对应的最后一位身份证号码
remainder_mapping = {0: 1, 1: 0, 2: 'X', 3: 9, 4: 8, 5: 7, 6: 6, 7: 5, 8: 4, 9: 3, 10: 2}
last_digit = remainder_mapping[b]
# 输出完整的身份证号码
Id18 = Id__ + [last_digit]
print("完整的身份证号码为:", ''.join(map(str, Id18)))
'''

# 04 计算某年某月某日是星期几
year = int(input("输入年份[为4位数]"))
if year % 4 == 0:
    nday = int(input("输入天数[1~366]"))
    month_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    nday = int(input("输入天数[1~365]"))
    month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
count_days = 0
date = []
for month_number, month_days in enumerate(month_day):
    count_days += month_days
    if count_days >= nday:
        month = month_number + 1
        date = [month, nday - (count_days - month_days)]
        break
day_of_week = nday % 7
day_of_week_mapping = {1: '星期一',
                       2: '星期二',
                       3: '星期三',
                       4: '星期四',
                       5: '星期五',
                       6: '星期六',
                       0: '星期日'}
print(f'{year}的第{nday}天是{date[0]}月{date[1]}日{day_of_week_mapping[day_of_week]}')
