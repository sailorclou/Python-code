# 01 抢红包
import random

num_person = int(input("红包人数："))
total_money = float(input("红包总额（元）："))

left_person = num_person
left_money = total_money

pocket = 1
for i in range(num_person):
    if left_person == 1:
        print("第%2d个好友抢到%6.2f元" % (i+1, round(pocket, 2)))
        break
    pocket = random.uniform(0.01, left_money - (left_money - 1) * 0.01)
    left_money -= pocket
    print("第%2d个好友抢到%6.2f元" % (i+1, round(pocket, 2)))
    """
    新的表达
    print(f"第{i+1: 2d}个好友抢到{round(pocket, 2): 6.2f}元")
    or
    print(f"第{: 2d}个好友抢到{: 6.2f}元".format(i+1, round(pocket, 2))
    """
    left_person -= 1

# 02 判断三角形种类
import random as r
import math as m
#help(m)

a = r.randint(1, 20)
b = r.randint(1, 20)
c = r.randint(abs(a - b) + 1, a + b - 1)

sides = [a, b, c]
sides.sort()
if m.hypot(sides[0], sides[1]) > sides[2]:
    print(f"以长度为{a}、{b}、{c}的三边组成的三角形为锐角三角形")
else:
    print(f"以长度为{a}、{b}、{c}的三边组成的三角形不是锐角三角形")
'''
sides_square = [side**2 for side in sides]
sides_square.sort()

x = m.pow(a, 2)
y = m.pow(b, 2)
z = m.pow(c, 2)

sides = [x, y, z]
sides.sort()

A = sides[0]
B = sides[1]
C = sides[2]

if sides_square[0] + sides_square[1] == sides_square[2]:
    print(f"以长度为{a}、{b}、{c}的三边组成的三角形为直角三角形")
elif sides_square[0] + sides_square[1] > sides_square[2]:
    print(f"以长度为{a}、{b}、{c}的三边组成的三角形为锐角三角形")
elif sides_square[0] + sides_square[1] < sides_square[2]:
    print(f"以长度为{a}、{b}、{c}的三边组成的三角形为钝角三角形")
'''

# 03 假期表
import zhdate as zh
import calendar as cal
import datetime

CHN = ["一", "二", "三", "四", "五", "六", "日"]
year = int(input("请输入一个年份:"))

lunar_festivals         = ['春节 ', '端午节', '中秋节']
lunar_festival_month    = [1, 5, 8]
lunar_festival_day      = [1, 5,15]
lunar_festival_interval = [7, 2, 2]    #day-1

solar_festivals         = ['元旦 ', '清明节', '劳动节', '国庆节']
solar_festival_month    = [1, 4, 5,10]
solar_festival_day      = [1, 5, 1, 1]
solar_festival_interval = [2, 2, 2, 6]

holiday = []

for i in range(len(lunar_festivals)):
    lu_start = zh.ZhDate(year, lunar_festival_month[i], lunar_festival_day[i])
    lu_end = lu_start + lunar_festival_interval[i]
    #(zh.ZhDate(year, lunar_festival_month[i], lunar_festival_day[i] + lunar_festival_interval[i]))
    so_start = lu_start.to_datetime()
    so_end = lu_end.to_datetime()
    holiday.append(f'{lunar_festivals[i]:>3} {so_start.year}.{so_start.month: 2d}.{so_start.day: 2d}\
     ~ {so_end.year}.{so_end.month: 2d}.{so_end.day: 2d}\
     星期{CHN[so_start.weekday()]} ~ 星期{CHN[so_end.weekday()]}')

for i in range(len(solar_festivals)):
    ca_start = datetime.datetime(year, solar_festival_month[i], solar_festival_day[i])
    #ca_start = ca_start.to_datetime()
    ca_end = ca_start + datetime.timedelta(days=solar_festival_interval[i])
    #ca_end = ca_end.to_datetime()
    holiday.append(f'{solar_festivals[i]:>3} {ca_start.year}.{ca_start.month: 2d}.{ca_start.day: 2d}\
     ~ {ca_end.year}.{ca_end.month: 2d}.{ca_end.day: 2d}\
     星期{CHN[ca_start.weekday()]} ~ 星期{CHN[ca_end.weekday()]}')

holiday.sort(key=lambda x: x[1])

for h in holiday:
    print(h)
'''
spring_festival_zh_start = zh.ZhDate(year, 1, 1)
spring_festival_zh_end = zh.ZhDate(year, 1, 8)
spring_festival_ca_start = spring_festival_zh_start.to_datetime()
spring_festival_ca_end = spring_festival_zh_end.to_datetime()
print(f'春节 {spring_festival_ca_start.year}.{spring_festival_ca_start.month}.{spring_festival_ca_start.day}\
 ~ {spring_festival_ca_end.year}.{spring_festival_ca_end.month}.{spring_festival_ca_end.day}\
 星期{CHN[spring_festival_ca_start.weekday()]} ~ 星期{CHN[spring_festival_ca_end.weekday()]}')
'''

import zhdate as zh
import calendar as cal
import datetime
CHN = ["一", "二", "三", "四", "五", "六", "日"]
year = int(input("请输入一个年份:"))
lunar_festivals = [' 春节 ', '端午节', '中秋节']
lunar_festival_month = [1, 5, 8]
lunar_festival_day = [1, 5, 15]
lunar_festival_interval = [7, 2, 2]  # day-1
solar_festivals = [' 元旦 ', '清明节', '劳动节', '国庆节']
solar_festival_month = [1, 4, 5, 10]
solar_festival_day = [1, 5, 1, 1]
solar_festival_interval = [2, 2, 2, 6]
holiday = []
for i in range(len(lunar_festivals)):
    lu_start = zh.ZhDate(year, lunar_festival_month[i], lunar_festival_day[i])
    lu_end = lu_start + lunar_festival_interval[i]
    so_start = lu_start.to_datetime()
    so_end = lu_end.to_datetime()
    holiday.append((so_start, f'{lunar_festivals[i]} {so_start.year}.{so_start.month:2d}.{so_start.day:2d} '
                              f'~ {so_end.year}.{so_end.month:2d}.{so_end.day:2d} '
                              f'星期{CHN[so_start.weekday()]} ~ 星期{CHN[so_end.weekday()]}'))
for i in range(len(solar_festivals)):
    ca_start = datetime.datetime(year, solar_festival_month[i], solar_festival_day[i])
    ca_end = ca_start + datetime.timedelta(days=solar_festival_interval[i])
    holiday.append((ca_start, f'{solar_festivals[i]} {ca_start.year}.{ca_start.month:2d}.{ca_start.day:2d} '
                               f'~ {ca_end.year}.{ca_end.month:2d}.{ca_end.day:2d} '
                               f'星期{CHN[ca_start.weekday()]} ~ 星期{CHN[ca_end.weekday()]}'))
holiday.sort(key=lambda x: x[0])
for h in holiday:
    print(h[1])

# 04 二维码
import qrcode
import os

# 目标网址
url = "https://www.tongji.edu.cn/"

# 创建二维码对象并添加网址
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(url)
qr.make(fit=True)

# 创建二维码图像
img = qr.make_image(fill_color="black", back_color="white")

# 保存二维码图像
img.save("tongji_university_qr_code.png")

print("二维码已生成，请扫描生成的图片。")
# 指定生成的二维码图片文件路径
qr_code_path = "tongji_university_qr_code.png"

# 检查文件是否存在
if os.path.exists(qr_code_path):
    # 使用默认图像查看器打开二维码图片
    os.system(f"start {qr_code_path}")
else:
    print("未找到生成的二维码图片文件。")