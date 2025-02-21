from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class tj_web:
    def __init__(self, wait_time=3):
        chrome_driver_path = 'C:\\Users\\22801\\.cache\\selenium\\chromedriver\\win64\\127.0.6533.88\\chromedriver.exe'
        chrome_binary_path = 'D:\\Apps\\Google\\Chrome\\Application\\chrome.exe'  # 替换为你的 Chrome 安装路径

        chrome_options = Options()
        chrome_options.binary_location = chrome_binary_path
        self.tj_browser = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)
        self.First_page = 'https://www.tongji.edu.cn'
        self.wait_time = wait_time

    def auto_click(self, txt_list):
        self.tj_browser.get(self.First_page)

        for txt in txt_list:
            try:
                menu_item = WebDriverWait(self.tj_browser, self.wait_time).until(
                    EC.element_to_be_clickable((By.LINK_TEXT, txt))
                )
                menu_item.click()

                time.sleep(self.wait_time)

                screenshot_filename = f"{txt}.png"
                self.tj_browser.save_screenshot(screenshot_filename)

                page_source_filename = f"{txt}.txt"
                with open(page_source_filename, 'w', encoding='utf-8') as file:
                    file.write(self.tj_browser.page_source)

                # 回到主菜单
                self.tj_browser.get(self.First_page)

            except Exception as e:
                print(f"An error occurred: {e}")

    def close_browser(self):
        self.tj_browser.quit()


# Example usage
if __name__ == '__main__':
    txt_list = ['科学研究', '招生就业', '交流合作']
    tj = tj_web(wait_time=3)
    tj.auto_click(txt_list)
    tj.close_browser()
