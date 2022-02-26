from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
# driver.implicitly_wait(10) #隐式等待

driver.maximize_window()#最大化浏览器窗口

url = "https://www.baidu.com"
driver.get(url) #连接地址
# print(driver.title)    #输出浏览器标题
time.sleep(1)
kw = driver.find_element(By.ID,"kw")
kw.clear()
kw.send_keys("slz")
su = driver.find_element(By.ID,"su")
# print(su.get_attribute("value"))
su.click()

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"c-icon.icon-title_35rjV")))


if "slz什么意思" in driver.page_source:
    print('搜索成功')
else:
    print("搜索失败")

time.sleep(3)
driver.quit()

