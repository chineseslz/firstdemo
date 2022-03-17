'''
    基础层代码
'''
from datetime import datetime, date, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By


def date_n(n):
    return str(date.today() + timedelta(days=int(n)))


driver = webdriver.Chrome()


def get_driver():
    return driver


def byname(element):
    return driver.find_element(By.NAME, element)


def byxpath(element):
    return driver.find_element(By.XPATH, element)


def open_url(url):
    driver.get(url)
    driver.maximize_window()


def close():
    driver.quit()
