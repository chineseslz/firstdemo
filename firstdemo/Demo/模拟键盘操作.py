from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys   #键盘操作


driver = webdriver.Chrome()
driver.implicitly_wait(10) #隐式等待


url = "https://www.baidu.com/"
driver.get(url) #连接地址
time.sleep(1)

el = driver.find_element(By.ID,'kw')
el.send_keys('python')
time.sleep(2)
#全选  ctrl+a
el.send_keys(Keys.CONTROL,"a")
time.sleep(2)
#删除
el.send_keys(Keys.BACKSPACE)
time.sleep(1)
el.send_keys("美女")
time.sleep(1)
#全选
el.send_keys(Keys.CONTROL,"a")
time.sleep(1)
#复制
el.send_keys(Keys.CONTROL,"c")
time.sleep(1)
el.send_keys(Keys.BACKSPACE)
time.sleep(1)
#粘贴
el.send_keys(Keys.CONTROL,"v")
time.sleep(1)



