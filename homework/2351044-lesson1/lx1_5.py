# 中文显示当天年月日和星期几
from datetime import datetime


def get_weekday_cn(day):
    weekdays = {
        0: '星期一',
        1: '星期二',
        2: '星期三',
        3: '星期四',
        4: '星期五',
        5: '星期六',
        6: '星期日'
    }
    return weekdays.get(day, '未知')


def display_date_in_chinese():
    # 获取当前日期和时间
    now = datetime.now()

    # 提取年月日和星期几
    year = now.year
    month = now.month
    day = now.day
    weekday = now.weekday()

    # 获取星期几的中文名称
    weekday_cn = get_weekday_cn(weekday)

    # 格式化日期字符串
    date_str = f"今天是{year}年{month}月{day}日，{weekday_cn}。"

    # 输出日期字符串
    print(date_str)


# 显示当前日期
display_date_in_chinese()
