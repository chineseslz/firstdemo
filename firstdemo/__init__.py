from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.select import Select    #下拉框
from selenium.webdriver.common.action_chains import ActionChains   #鼠标操作
from selenium.webdriver.common.keys import Keys   #键盘操作


driver = webdriver.Chrome()
driver.implicitly_wait(10) #隐式等待


url = "https://www.baidu.com/"
urls = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&ch=2&tn=68018901_28_oem_dg&wd=slz&fenlei=256&oq=skz&rsv_pq=8042745f00058100&rsv_t=25e2Z8yxBfnDlfQXbNeeEqyT498QR7iqxVwIuoEpNKBrOxGvC%2Bn%2BTmLdDaFxgFjp3Fnz1I%2FRtsvR&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_btype=t&inputT=969&rsv_sug3=10&rsv_sug1=9&rsv_sug7=100&rsv_sug2=0&rsv_sug4=1137"

driver.get(url) #连接地址
time.sleep(1)

value = driver.find_element(By.XPATH,"//*[text()='slz']")
print(value)




