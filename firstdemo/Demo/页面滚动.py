from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains   #鼠标操作


driver = webdriver.Chrome()
driver.implicitly_wait(10) #隐式等待

# js="window.scrollTo(0,10000)"
# driver.execute_script(js)
# 绝对滚动window.scrollTo(X,Y)
# 相对滚动window.scrollBy(X,Y)

url = "https://www.douyu.com/directory/all"

driver.get(url) #连接地址
time.sleep(1)

value = driver.find_element(By.XPATH,"//*[text()='下一页']")
value.click()
time.sleep(1)




