from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.implicitly_wait(10) #隐式等待



url = "https://music.163.com/#/discover/toplist"
driver.get(url) #连接地址
time.sleep(1)

f = driver.find_element(By.ID,"g_iframe")
driver.switch_to.frame(f)   #切换到指定框架
music = driver.find_elements(By.XPATH,"//div[@class='tt']/span")  #选择框架内的元素
driver.execute_script('arguments[0].scrollIntoView();',music[95])  #让music96在当前页面中可见
time.sleep(1)
music[95].click()  #不在当尺寸界面下 播放存在报错  需要调用js



