from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)  # 隐式等待

driver.maximize_window()  # 最大化浏览器窗口

url = "https://www.gzjkqaq.com/park/#/login"
driver.get(url)  # 连接地址
# print(driver.title)    #输出浏览器标题

ele = driver.find_element(By.XPATH,
                          '/html/body/div/div[1]/div/div/div[10]/div/div[2]/div/form/div[1]/div/div/input').send_keys(
    'admin')
ele = driver.find_element(By.XPATH,
                          '/html/body/div/div[1]/div/div/div[10]/div/div[2]/div/form/div[2]/div/div/input').send_keys(
    'admin')
time.sleep(3)
ele = driver.find_element(By.XPATH,
                          '/html/body/div/div[1]/div/div/div[10]/div/div[2]/div/form/div[3]/div/button/span').click()
time.sleep(1)

ele = driver.find_element(By.XPATH, '//*[@id="theme-color--"]/aside/div/ul/li[3]/div').click()
time.sleep(1)
ele = driver.find_element(By.XPATH, '//*[@id="theme-color--"]/aside/div/ul/li[3]/ul/li[1]').click()
time.sleep(1)

ele = driver.find_element(By.XPATH, '//*[@id="pane-notice/mettingNotice"]/div/div/div/div[1]/button').click()
time.sleep(1)
# 输入会议名称
ele = driver.find_element(By.XPATH,
                          '//*[@id="pane-notice/mettingNotice"]/div/div/div/div[4]/div[2]/div/div[2]/form/table/tr[1]/td[2]/div/div/div[1]/input').send_keys(
    '自动脚本会议')
time.sleep(1)


link = driver.find_element(By.XPATH,
                       '//*[@id="pane-notice/mettingNotice"]/div/div/div/div[4]/div[2]/div/div[2]/form/table/tr[2]/td[2]/div/div/div[1]/div/div').click()
dizhi = driver.find_element(By.XPATH, '//*[@id="tipinput"]')
js = "arguments[0].v-model='江苏中石科技有限公司'；"
link = driver.execute_script(js, dizhi)



time.sleep(5)
driver.quit()
