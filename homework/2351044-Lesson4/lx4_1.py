from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

# 设置 ChromeDriver 路径
chrome_driver_path = 'C:\\Users\\22801\\.cache\\selenium\\chromedriver\\win64\\127.0.6533.88\\chromedriver.exe'
chrome_binary_path = 'D:\\Apps\\Google\\Chrome\\Application\\chrome.exe'  # 替换为你的 Chrome 安装路径

service = Service(chrome_driver_path)
chrome_options = Options()
chrome_options.binary_location = chrome_binary_path

# 打开浏览器
browser = webdriver.Chrome(service=service, options=chrome_options)

url = 'https://music.163.com/#/discover/toplist'
browser.get(url)

# 等待页面加载
time.sleep(5)  # 简单的等待，建议使用显式等待

# 切换到 iframe
iframe = browser.find_element(By.ID, 'g_iframe')
browser.switch_to.frame(iframe)

# 寻找大容器
toplist = browser.find_element(By.ID, 'toplist')
# 寻找 tbody 通过标签名
tbody = toplist.find_element(By.TAG_NAME, 'tbody')
# 寻找所有 tr
trs = tbody.find_elements(By.TAG_NAME, 'tr')
print(trs)

data_list = []
for each in trs:
    # 排名
    rank = each.find_element(By.CLASS_NAME, 'num').text
    music_name = each.find_element(By.CLASS_NAME, 'txt').find_element(By.TAG_NAME, 'b').get_attribute('title')
    singer = each.find_element(By.CLASS_NAME, 'text').get_attribute('title')
    data_list.append([rank, music_name, singer])

print(data_list)

# 关闭浏览器
browser.quit()
