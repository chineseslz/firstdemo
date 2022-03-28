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
time.sleep(1)

music[70].click()  #播放   不在当尺寸可见界面下  点击播放按钮存在报错


#driver.switch_to.default_content()#切换到最外层框架
#driver.switch_to.patent_frame() #切换到上层框架


