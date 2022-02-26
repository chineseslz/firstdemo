from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

url = "https://www.baidu.com"
driver.get(url) #连接地址
time.sleep(1)
baidu_handle = driver.current_window_handle #获取当前窗口句柄
hao123 = driver.find_element(By.XPATH,"//*[text()='hao123']")
hao123.click()
handles = driver.window_handles  #获取所有句柄
for i in handles:
    if i != baidu_handle:
        driver.switch_to.window(i)  #切换
        print(driver.title)
driver.close()
driver.switch_to.window(baidu_handle)
print(driver.title)