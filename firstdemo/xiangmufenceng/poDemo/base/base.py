'''
    基础的内容
'''
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Base():
    def __init__(self, driver):
        self.driver = driver  # type:  WebDriver

    def byname(self, element):
        return self.driver.find_element(By.NAME, element)

    def byxpath(self, element):
        return self.driver.find_element(By.XPATH, element)

    def open_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def close(self):
        self.driver.quit()
