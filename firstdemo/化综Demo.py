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
time.sleep(3)
login_user = driver.find_elements(By.CLASS_NAME,"el-input__inner")[0]
login_user.send_keys("admin")
login_pwd = driver.find_elements(By.CLASS_NAME,"el-input__inner")[1]
login_pwd.send_keys("admin")
login_btn = driver.find_element(By.CLASS_NAME,("el-button.login-btn-submit.el-button--primary.el-button--medium"))
login_btn.click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[text()='企业生产全流程']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[text()='设备设施管理']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[text()='设备设施类型']").click()


time.sleep(5)
driver.quit()