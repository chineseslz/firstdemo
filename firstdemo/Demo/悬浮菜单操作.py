from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.implicitly_wait(10) #隐式等待



url = "https://www.baidu.com/"
driver.get(url) #连接地址
time.sleep(1)

shezhi = driver.find_element(By.ID,"s-usersetting-top")
ActionChains(driver).move_to_element(shezhi).perform()  #鼠标悬停设置按钮
time.sleep(1)
gaojisousuo =driver.find_element(By.XPATH,"//*[text()='高级搜索']")
gaojisousuo.click()





