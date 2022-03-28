from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.implicitly_wait(10) #隐式等待


url = "https://www.baidu.com/"
driver.get(url) #连接地址
time.sleep(1)
driver.add_cookie({"name":"BDUSS","value":"dOflZLNVVOSFNNamxxNWlQcHhYZTE2WjdJalhSZ0lMc3AxYWVJbnRwbUViZWhoRVFBQUFBJCQAAAAAAAAAAAEAAAC3ZNVQtPS09LXE0KHW7eHMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAITgwGGE4MBhdG"})
driver.add_cookie({"name":"BAIDUID","value":"50C9C8EB4B452E0C70EC21515031C5CF"})
time.sleep(2)
driver.refresh()






