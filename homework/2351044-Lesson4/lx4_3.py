from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class tj_bbs:
    def __init__(self):
        # 设置 ChromeDriver 路径
        chrome_driver_path = 'C:\\Users\\22801\\.cache\\selenium\\chromedriver\\win64\\127.0.6533.88\\chromedriver.exe'
        chrome_binary_path = 'D:\\Apps\\Google\\Chrome\\Application\\chrome.exe'  # 替换为你的 Chrome 安装路径

        service = Service(chrome_driver_path)
        chrome_options = Options()
        chrome_options.binary_location = chrome_binary_path

        # 初始化 WebDriver
        self.bbs_browser = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)
        self.login_page = 'http://cyr985.net3v.club/bbs/login.asp'
        self.post_page = 'http://cyr985.net3v.club/bbs/topic.asp?id=4891&boardid=6&TB=1'
        self.wait_time = 5

    def auto_login(self, username, password):
        # 打开登录页面
        self.bbs_browser.get(self.login_page)
        time.sleep(self.wait_time)  # 等待页面加载
        # 等待用户名字段可交互
        # WebDriverWait(self.bbs_browser, self.wait_time).until(
        #     EC.visibility_of_element_located((By.NAME, 'name'))
        # )
        # 输入用户名
        username_field = self.bbs_browser.find_element(By.NAME, 'name')
        username_field.send_keys(username)
        # WebDriverWait(self.bbs_browser, self.wait_time).until(
        #     EC.visibility_of_element_located((By.NAME, 'Password'))
        # )
        # 输入密码
        password_field = self.bbs_browser.find_element(By.NAME, 'Password')
        password_field.send_keys(password)

        # # 等待登录按钮可交互
        # WebDriverWait(self.bbs_browser, self.wait_time).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, 'login'))
        # )
        # 提交表单
        button = self.bbs_browser.find_element(By.CLASS_NAME, 'login')
        button.click()
        # password_field.send_keys(Keys.RETURN)

        time.sleep(self.wait_time)  # 等待登录完成

    def auto_post(self, bbs_content):
        # 打开发帖页面
        self.bbs_browser.get(self.post_page)
        time.sleep(self.wait_time)  # 等待页面加载

        button = self.bbs_browser.find_element(By.CSS_SELECTOR, 'img[src="Skins/blue/reply.gif"]')
        button.click()

        # content_field = self.bbs_browser.find_element(By.NAME, 'caption')
        # content_field.send_keys(bbs_content)

        # Wait for the iframe to be present and switch to it
        WebDriverWait(self.bbs_browser, self.wait_time).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, 'edit'))
        )
        # Now interact with the contenteditable element
        content_field = self.bbs_browser.find_element(By.CSS_SELECTOR, 'body[contenteditable="true"]')
        # Clear existing content
        content_field.clear()
        content_field.send_keys(bbs_content)
        # Switch back to the default content after interaction
        self.bbs_browser.switch_to.default_content()

        # 提交帖子
        submit_button = self.bbs_browser.find_element(By.ID, 'sayb')
        submit_button.click()
        time.sleep(self.wait_time)  # 等待发帖完成

    def close_browser(self):
        # 关闭浏览器
        self.bbs_browser.quit()


# 示例使用
if __name__ == '__main__':
    bbs = tj_bbs()
    bbs.auto_login('cyy', '123456')
    bbs.auto_post('2351044 cui yi yang')
    bbs.close_browser()
