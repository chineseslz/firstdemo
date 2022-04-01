from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.implicitly_wait(10) #隐式等待

driver.maximize_window()#最大化浏览器窗口

url = "http://192.168.0.200:8080/#/login"
driver.get(url) #连接地址
# print(driver.title)    #输出浏览器标题

#登录
time.sleep(2)
login_user = driver.find_elements(By.CLASS_NAME,"el-input__inner")[0]
login_user.send_keys("admin")
login_pwd = driver.find_elements(By.CLASS_NAME,"el-input__inner")[1]
login_pwd.send_keys("admin")
login_btn = driver.find_element(By.CLASS_NAME,("el-button.login-btn-submit.el-button--primary.el-button--medium"))
login_btn.click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[text()='企业生产全流程']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[text()='作业安全']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[text()='特殊作业申请']").click()
time.sleep(1)
datetime1 = driver.find_element(By.XPATH,'//*[@id="pane-pos/private/private-list"]/div/div/div/form/div[3]/div/div/input[1]')
datetime1.click()
datetime1.send_keys("2022-03-31 00:00:00")
datetime2 = driver.find_element(By.XPATH,'//*[@id="pane-pos/private/private-list"]/div/div/div/form/div[3]/div/div/input[2]')
datetime2.click()
datetime2.send_keys("2022-04-21 00:00:00")
button = driver.find_element(By.XPATH,"//*[text()='查询']").click()


#
# time.sleep(5)
# driver.quit()