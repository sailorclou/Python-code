from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyttsx3


class tj_web(object):
    def __init__(self):
        self.tj_browser = webdriver.Chrome()
        self.First_page = 'https://news.tongji.edu.cn/info/1003/88134.htm'
        self.wait_time = 10

        # Open the first page
        self.tj_browser.get(self.First_page)
        time.sleep(3)  # Wait for the page to load

    def auto_replace(self):
        time.sleep(8)  # Additional waiting time, possibly to ensure page elements are loaded

        # Find all <h3> elements on the page
        h3_elements = self.tj_browser.find_elements(By.TAG_NAME, 'h3')

        # Iterate through the found <h3> elements
        for element in h3_elements:
            original_text = element.text
            new_text = original_text.replace('覃海洋', '崔艺洋')  # Replace 'Your Name' with the actual name

            # Use JavaScript to update the element's text
            self.tj_browser.execute_script("arguments[0].innerText = arguments[1];", element, new_text)

        # Optionally alert to confirm the changes in the browser (can be removed if not needed)
        self.tj_browser.execute_script("alert('Text replacement complete!');")

        # Handle the alert
        alert = self.tj_browser.switch_to.alert
        alert.accept()  # This will close the alert

    def speak_text(self):
        # Find all <h3> elements
        h3_elements = self.tj_browser.find_elements(By.TAG_NAME, 'h3')

        if len(h3_elements) >= 2:
            # Retrieve the second <h3> element
            modified_title = h3_elements[1].text

            # Initialize text-to-speech engine
            engine = pyttsx3.init()

            # Speak the modified title of the second <h3>
            engine.say(modified_title)
            engine.runAndWait()
        else:
            print("There are less than two <h3> elements on the page.")


# Example usage:
if __name__ == "__main__":
    web = tj_web()  # Initialize the web object
    web.auto_replace()  # Replace the text on the page
    web.speak_text()  # Read the modified title of the second <h3> aloud
