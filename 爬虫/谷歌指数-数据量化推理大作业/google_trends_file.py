from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from scipy.signal import savgol_filter

# 设置中文字体
plt.rcParams['font.family'] = ['Microsoft YaHei', 'SimHei', 'sans-serif']

# 初始化 pytrends 对象
pytrends = TrendReq(hl='en-US', tz=360)

# 定义要搜索的关键词
kw_list = ["焦虑", "孤独", "抑郁"]  # 使用中文关键词


# 获取趋势数据
def get_trends_data(keywords, timeframe='today 5-y', geo='', gprop=''):
    pytrends.build_payload(keywords, cat=0, timeframe=timeframe, geo=geo, gprop=gprop)
    data = pytrends.interest_over_time()
    return data


# 按月汇总数据
def resample_monthly_sum(data):
    monthly_data = data.resample('M').sum()
    return monthly_data


# 保存数据到 Excel
def save_to_excel(data, filename):
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        data.to_excel(writer, sheet_name='月度趋势数据')
    print(f"数据已保存到 {filename}")


# 归一化处理
def normalize_data(data):
    scaler = MinMaxScaler()
    normalized_data = pd.DataFrame(scaler.fit_transform(data), columns=data.columns, index=data.index)
    return normalized_data


# 平滑处理并可视化
def visualize_normalized_data(normalized_data, keywords):
    plt.figure(figsize=(14, 7))

    for keyword in keywords:
        y = normalized_data[keyword].values
        y_smooth = savgol_filter(y, window_length=11, polyorder=3)  # 使用 Savitzky-Golay 滤波器

        plt.plot(normalized_data.index, y, label=f'{keyword}（归一化）', alpha=0.3)  # 原始数据点，透明度设为0.3
        plt.plot(normalized_data.index, y_smooth, label=f'{keyword}（平滑）')

    plt.xlabel('日期')
    plt.ylabel('归一化搜索指数')
    plt.title('谷歌趋势数据 - 归一化和平滑处理')
    plt.legend()

    # 格式化横坐标
    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(len(normalized_data.index)))
    plt.gca().xaxis.set_major_formatter(plt.FixedFormatter(normalized_data.index.strftime('%Y-%m')))

    plt.grid(True)
    plt.show()


# 示例使用
if __name__ == "__main__":
    timeframe = "today 5-y"  # 获取最近5年的数据

    # 获取趋势数据
    trends_data = get_trends_data(kw_list, timeframe)

    # 检查数据
    if not trends_data.empty:
        # 删除 isPartial 列，因为它不需要写入 Excel
        trends_data = trends_data.drop(columns=['isPartial'])

        # 按月汇总数据（求和）
        monthly_trends_data = resample_monthly_sum(trends_data)

        # 保存数据到 Excel
        filename = '原始趋势数据_月度.xlsx'
        save_to_excel(monthly_trends_data, filename)

        # 归一化处理
        normalized_trends_data = normalize_data(monthly_trends_data)

        # 可视化
        visualize_normalized_data(normalized_trends_data, kw_list)
    else:
        print("未找到给定关键词和时间范围的数据。")
