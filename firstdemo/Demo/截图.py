from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

url = "https://www.baidu.com"
driver.get(url) #连接地址
time.sleep(1)
driver.save_screenshot('./首页_1.png')
driver.get_screenshot_as_file('./首页_1.png')
