from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xlwt

# 设置 ChromeDriver 路径
chrome_driver_path = 'C:\\Users\\22801\\.cache\\selenium\\chromedriver\\win64\\127.0.6533.88\\chromedriver.exe'
chrome_binary_path = 'D:\\Apps\\Google\\Chrome\\Application\\chrome.exe'  # 替换为你的 Chrome 安装路径

service = Service(chrome_driver_path)
chrome_options = Options()
chrome_options.binary_location = chrome_binary_path

# 打开浏览器
browser = webdriver.Chrome(service=service, options=chrome_options)

url = 'https://top.baidu.com/board'
browser.get(url)

# 等待页面加载并获取前十条数据
wait = WebDriverWait(browser, 10)
toplist_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".c-single-text-ellipsis")))

# 提取前十条数据
top10_elements = toplist_elements[:50]

# 提取数据
data_list = []
i = 0
for each in top10_elements:
    if i == 10:
        break
    text = each.text.strip()  # 使用 strip() 去掉多余的空白
    if text:  # 确保非空数据
        data_list.append(text)
        i+=1

# 创建 Excel 文件
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('Hot List')

# 写入表头
worksheet.write(0, 0, '排名')
worksheet.write(0, 1, '内容')

# 写入数据
for idx, data in enumerate(data_list, start=1):
    worksheet.write(idx, 0, idx)  # 写入排名
    worksheet.write(idx, 1, data)  # 写入内容

# 保存 Excel 文件
workbook.save('hot_list.xls')

# 关闭浏览器
browser.quit()
