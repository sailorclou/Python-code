# 01 生成斐波那契数列
n = int(input("请输入一个整数："))
num = [0, 1]
num0 = num[0]
num1 = num[1]
for i in range(0, n - 2):
    new = num0 + num1
    num.append(new)
    num0 = num1
    num1 = new
print(num)

# 02 去除质数
import random

all_numbers = []
for i in range(21):
    num = random.randint(2, 10000)
    all_numbers.append(num)
print(all_numbers)
for num in all_numbers:
    for i in range(2, num):
        if num % i == 0:
            all_numbers.remove(num)
            break
print(all_numbers)

# 03 密码检查
import re


def has_numbers(input_string):
    return bool(re.search(r'\d', input_string))


def has_upper(input_string):
    return any(char.isupper() for char in input_string)


def has_lower(input_string):
    return any(char.islower() for char in input_string)


def has_spe(input_string):
    spes = ['~', '@', '#', '%', '!', '&', '$']
    for char in input_string:
        for spe in spes:
            if char == spe:
                return 1
    return 0


code = input("请输入密码：")
# c = code.split()
i = 0
# 1 判断是否包含数字
i += has_numbers(code)
# 2 判断是否包含大写字母
i += has_upper(code)
# 3 判断是否包含小写字母
i += has_lower(code)
# 4 判断是否大于七位
if len(code) > 7:
    i += 1
# 5 判断是否包含特殊字符
i += has_spe(code)

if i >= 3:
    print("密码设置合格")
else:
    print("密码不符合规定，需满足以下至少三条要求：\n包含数字\n包含大写字母\n包含小写字\n大于7位\n"
          "包含特殊字符（~ @ # % ! & $）")

# 04 字典
import random

random_integers = [random.randint(1, 10) for i in range(20)]
count = {}
for integer in random_integers:
    if integer in count:
        count[integer] += 1
    else:
        count[integer] = 1
print(count)
