from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

#options                    返回下拉框的所有选项
#select_by_index()          通过索引选择
#select_by_value()          通过选项的value属性值选择
#select_by_visible_text()   通过选项的文本值选择

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

#获取下拉框
s = driver.find_element(By.CLASS_NAME,"c-select-dropdown-list")
opt = Select(s).options
print(type(opt),len(opt))

Select(s).select_by_index(2)




